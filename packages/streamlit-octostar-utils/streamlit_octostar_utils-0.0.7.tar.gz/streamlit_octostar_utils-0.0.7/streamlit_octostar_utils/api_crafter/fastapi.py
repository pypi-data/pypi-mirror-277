import asyncio
from fastapi import Request
from fastapi.responses import JSONResponse, StreamingResponse
from pydantic import BaseModel
from typing import Union, List, Optional, Literal
from io import BytesIO
import zipfile
import json
from pydantic import ValidationError
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
import ast
import uuid

class CommonParsers(object):
    async def parse_form_list(form_data: str,
                              format=Literal['csv', 'python']) -> Optional[List[str]]:
        try:
            if not form_data:
                return None
            if format == 'csv':
                return form_data.split(',')
            elif format == 'python':
                return ast.literal_eval(form_data)
        except:
            raise ValidationError("Parsing failed in parse_from_list!")

class Route(object):
    pass

class CommonModels(object):
    class OKResponseModel(BaseModel):
        message: str = "OK"
        status: str = "success"
        
    class DataResponseModel(BaseModel):
        data: Union[list, dict]
        status: str = "success"

    class ZipResponseModel(object):
        class Element(object):
            def __init__(self, file: bytes, path: str, filename: str, json: dict):
                self.file = file
                self.path = path
                self.filename = filename
                self.json = json
            
        def __init__(self, elements: List[Element], paths: Optional[List[str]] = None, filename: Optional[str] = None, status: str = "success"):
            self.elements = elements
            self.paths = paths
            self.status = status
            self.filename = filename
        
        def get(self):
            zip_buffer = BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for element in self.elements: 
                    file_name = f"{element.path}/{element.filename}"
                    zip_file.writestr(file_name, element.file)
                    json_name = f"{element.path}/{element.filename}.dict"
                    zip_file.writestr(json_name, json.dumps(element.json, indent=4))
                for path in self.paths:
                    zip_file.writestr(path + "/", '')
                zip_file.writestr('response.dict', json.dumps({'status': self.status}, indent=4))
            zip_buffer.seek(0)
            headers = {}
            headers['Content-Disposition'] = 'attachment;'
            filename = self.filename or (str(uuid.uuid4()) + ".zip")
            headers['Content-Disposition'] += f' filename="{filename}"'
            return StreamingResponse(zip_buffer, media_type='application/zip', headers=headers)

class DefaultErrorRoute(Route):
    error_responses = {
        500: {
            "description": "Generic Server Error",
            "content": {
                "application/json": {
                    "example": {"message": "Something unexpected went wrong!", "status": "error"}
                }
            }
        },
        501: {
            "description": "Not Implemented",
            "content": {
                "application/json": {
                    "example": {"message": "This method (with these parameters) is not implemented!", "status": "error"}
                }
            }
        },
        400: {
            "description": "Bad Request",
            "content": {
                "application/json": {
                    "example": {"message": "These two lists must have the same length!", "status": "error"}
                }
            }            
        },
        422: {
            "description": "Validation Error",
            "content": {
                "application/json": {
                    "example": {"message": "Validation error on 0 -> filename!", "status": "error"}
                }
            }            
        },        
    }
    
    async def handle_error(request: Request, exc: Exception):
        '''Generic Error Handler'''
        status_code = 500
        if isinstance(exc, StarletteHTTPException):
            status_code = exc.status_code
        elif isinstance(exc, NotImplementedError):
            status_code = 501
        elif isinstance(exc, AssertionError):
            status_code = 400
        elif isinstance(exc, ValidationError) or isinstance(exc, RequestValidationError):
            status_code = 422
        try:
            message = exc.message
        except:
            message = str(exc)
        return JSONResponse(
            status_code=status_code,
            content={"message": message, 'status': 'error'}
        )
    
    def add_default_exceptions_handler(fs_app):
        fs_app.add_exception_handler(RequestValidationError, DefaultErrorRoute.handle_error)
        fs_app.add_exception_handler(StarletteHTTPException, DefaultErrorRoute.handle_error)
        fs_app.add_exception_handler(Exception, DefaultErrorRoute.handle_error)
    
class RequestCancelledMiddleware:
    def __init__(self, app):
        self.app = app
    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return
        queue = asyncio.Queue()
        async def message_poller(sentinel, handler_task):
            nonlocal queue
            while True:
                message = await receive()
                if message["type"] == "http.disconnect":
                    handler_task.cancel()
                    return sentinel
                await queue.put(message)
        sentinel = object()
        handler_task = asyncio.create_task(self.app(scope, queue.get, send))
        asyncio.create_task(message_poller(sentinel, handler_task))
        try:
            return await handler_task
        except asyncio.CancelledError:
            print("Cancelling request due to disconnect")