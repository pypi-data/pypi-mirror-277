from typing import Any, NoReturn, TypedDict, Dict
from abc import ABC, abstractmethod

import datetime

type ArgsOrder = Tuple[str]
type ArgsMapping = Tuple[Tuple[str, str]]
type ArgsData = Dict[str, Any]
type TypeMapping = Tuple[Any, str] | NoReturn
type ArgMapping = Tuple[str, TypeMapping]
type Row: Tuple[ArgMapping] | Tuple[Any]
type TypesAllowed = Tuple[str]
type Data = Tuple[Any]
type Options = Tuple[str]
type Results = Tuple[Row]

type TaskIdentifier = int
type Query = str
type Time = int | float

# Fix based on SQLite, Polars, mmap, and PostgreSQL
## Double check dict
## Optional serializer to date formats, etc.
orm_types = {int: 'int', str: 'str', bool: 'bool', float: 'float', datetime.Date: 'basic_date') # Need to fix dict to represent Json... TypedDict with nested optional TypedDicts will do, dict)

# Double check
def get_type(arg: Any, architecture: str) -> tuple[str, Any]:
    for _type, value in orm_types.items():
        if isinstance(arg, _type):
            return value, arg
    try:
        serializaed_arg, optional_format = arg.serialize_to(architecture)
        # Deal with the optional_format for dates, etc. later
        caught_type = str(serializaed_arg).split("'")[1]
        return caught_type, serializaed_arg

class UserDefinedType(ABC):
    @abstractmethod
    def serialize_to(self, architecture: str):
        pass
        
    @abstractmethod
    def deserialize_to(self, architecture: str):
        pass
