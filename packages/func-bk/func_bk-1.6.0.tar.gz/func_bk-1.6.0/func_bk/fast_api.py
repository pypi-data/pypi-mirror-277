from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from fastapi.utils import generate_unique_id
from typing import Any, List, Union
from enum import Enum

from markupsafe import Markup
from pydantic import BaseModel


def path(
        app: FastAPI,
        func: callable,
        type: str,
        path: str,
        response_model: Any = None,
        status_code: int = None,
        tags: List[Union[str, Enum]] = None,
        dependencies = None,
        summary: str = None,
        description: str = None,
        response_description: str = "Successful Response",
        responses = None,
        deprecated: bool = None,
        operation_id = None,
        response_model_include = None,
        response_model_exclude = None,
        response_model_by_alias: bool = True,
        response_model_exclude_unset: bool = False,
        response_model_exclude_defaults: bool = False,
        response_model_exclude_none: bool = False,
        include_in_schema: bool = True,
        response_class: type[Response] = JSONResponse,
        name: str = None,
        callbacks = None,
        openapi_extra = None,
        generate_unique_id_function = generate_unique_id
    ):
    type = type.lower()
    route_function = None
    if type == "get":
        route_function = app.get
    elif type == "post":
        route_function = app.post
    elif type == "put":
        route_function = app.put
    elif type == "delete":
        route_function = app.delete
    elif type == "patch":
        route_function = app.patch

    if route_function:
        route_function(
            path=path,
            response_model=response_model,
            status_code=status_code,
            tags=tags,
            dependencies=dependencies,
            summary=summary,
            description=description,
            response_description=response_description,
            responses=responses,
            deprecated=deprecated,
            operation_id=operation_id,
            response_model_include=response_model_include,
            response_model_exclude=response_model_exclude,
            response_model_by_alias=response_model_by_alias,
            response_model_exclude_unset=response_model_exclude_unset,
            response_model_exclude_defaults=response_model_exclude_defaults,
            response_model_exclude_none=response_model_exclude_none,
            include_in_schema=include_in_schema,
            response_class=response_class,
            name=name,
            callbacks=callbacks,
            openapi_extra=openapi_extra,
            generate_unique_id_function=generate_unique_id_function
        )(func)

class Label():
    type: str
    id: str
    placeholder: str
    help_text: str
    style_input:str
    label: str
    none:bool
    def __init__(self, type:str, id:str, place:str = "", help:str = "", style:str = None,label:str = '', none:bool = False):
        self.type=type
        self.id=id
        self.placeholder=place
        self.help_text=help
        self.style_input=style
        self.label = label
        self.none=none

class BForm():
    def labels(self) -> List[Label]:
        a=[]
        cls=type(self)
        for i in cls.__dict__:
            if isinstance(cls.__dict__[i], Label):
                a.append(cls.__dict__[i])   
        return a

    def as_p(self):
        a=''
        all=self.labels()

        for i in all:
            a+=f'<label for="{i.id}">{i.label}</label>'
            if not(i.style_input):
                a += f"<input type='{i.type}' id='{i.id}' name='{i.id}' placeholder='{i.placeholder}' "
            else:
                a += f"<input class='{i.style_input}' type='{i.type}' id='{i.id}' name='{i.id}' placeholder='{i.placeholder}' "
            
            if not(i.none):
                a += 'required'

            a += f"> {i.help_text} \n"
        return Markup(a)
    # def upgrade_value(self):
    #         a=''
    #         a+="""
    #         <script>
    #         function handleFormSubmit(event) { 
    #             event.preventDefault(); // Предотвратить отправку формы 
    #             var formData = new FormData(event.target); // Получить данные формы 
    #             var formIndex = Array.from(document.forms).indexOf(event.target); // Получить индекс текущей формы 
    #             // Найти соответствующий объект BForm по индексу формы 
    #             var form = forms[formIndex]; 
    #             if (form) { 
    #                 for (var pair of formData.entries()) { 
    #                     // Найти соответствующий объект Label в метках формы 
    #                     var label = form.labels.find(function(item) { 
    #                         return item.id === pair[0]; 
    #                     }); 
    #                     if (label) { 
    #                         // Обновить атрибуты объекта Label 
    #                         label.value = pair[1]; 
    #                     } 
    #                 } 
    #             } 
    #         } 
    #         Array.from(document.forms).forEach(function(form) { 
    #             form.addEventListener('submit', handleFormSubmit); 
    #         }); 
    #         </script>
    #         """
    #         return Markup(a)
    # def is_valid(self):
    #     errors = {}
    #     all=self.Dlabels()
    #     for field_name, field_data in all:
    #         field_value = field_data['value']
    #         required = field_data['required']
            
    #         if required and not field_value:
    #             errors[field_name] = "Это обязательное поле"
        
    #     if errors:
    #         return False, errors
    #     else:
    #         return True,True


