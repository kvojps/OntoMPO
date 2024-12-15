from typing import List, Optional, Dict
from pydantic import BaseModel


class ClassResponse(BaseModel):
    class_name: str
    translated_class_name: Optional[str]
    description: Optional[str]
    object_properties: List["ObjectPropertyResponse"]
    subclasses: List["ClassResponse"]

    class Config:
        arbitrary_types_allowed = True


class ObjectPropertyResponse(BaseModel):
    prop_name: str
    range: List[str]
