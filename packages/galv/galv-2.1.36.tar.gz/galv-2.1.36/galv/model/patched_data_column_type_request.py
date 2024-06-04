# coding: utf-8

"""
    Battery Data API

    A standard API for accessing battery experiment datasets and metadata  # noqa: E501

    The version of the OpenAPI document: 2.1.36
    Contact: martin.robinson@cs.ox.ac.uk
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from galv import schemas  # noqa: F401


class PatchedDataColumnTypeRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
            
            
            class description(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
            unit = schemas.StrSchema
            
            
            class data_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "int": "INT",
                        "float": "FLOAT",
                        "str": "STR",
                        "bool": "BOOL",
                        "datetime64[ns]": "DATETIME64NS",
                    }
                
                @schemas.classproperty
                def INT(cls):
                    return cls("int")
                
                @schemas.classproperty
                def FLOAT(cls):
                    return cls("float")
                
                @schemas.classproperty
                def STR(cls):
                    return cls("str")
                
                @schemas.classproperty
                def BOOL(cls):
                    return cls("bool")
                
                @schemas.classproperty
                def DATETIME64NS(cls):
                    return cls("datetime64[ns]")
            
            
            class team(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'uri'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'team':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class read_access_level(
                schemas.EnumBase,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        4: "POSITIVE_4",
                        3: "POSITIVE_3",
                        2: "POSITIVE_2",
                        1: "POSITIVE_1",
                        0: "POSITIVE_0",
                        schemas.NoneClass.NONE: "NONE",
                    }
                
                @schemas.classproperty
                def POSITIVE_4(cls):
                    return cls(4)
                
                @schemas.classproperty
                def POSITIVE_3(cls):
                    return cls(3)
                
                @schemas.classproperty
                def POSITIVE_2(cls):
                    return cls(2)
                
                @schemas.classproperty
                def POSITIVE_1(cls):
                    return cls(1)
                
                @schemas.classproperty
                def POSITIVE_0(cls):
                    return cls(0)
                
                @schemas.classproperty
                def NONE(cls):
                    return cls(None)
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'read_access_level':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class edit_access_level(
                schemas.EnumBase,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        4: "POSITIVE_4",
                        3: "POSITIVE_3",
                        2: "POSITIVE_2",
                        1: "POSITIVE_1",
                        schemas.NoneClass.NONE: "NONE",
                    }
                
                @schemas.classproperty
                def POSITIVE_4(cls):
                    return cls(4)
                
                @schemas.classproperty
                def POSITIVE_3(cls):
                    return cls(3)
                
                @schemas.classproperty
                def POSITIVE_2(cls):
                    return cls(2)
                
                @schemas.classproperty
                def POSITIVE_1(cls):
                    return cls(1)
                
                @schemas.classproperty
                def NONE(cls):
                    return cls(None)
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'edit_access_level':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class delete_access_level(
                schemas.EnumBase,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        4: "POSITIVE_4",
                        3: "POSITIVE_3",
                        schemas.NoneClass.NONE: "NONE",
                    }
                
                @schemas.classproperty
                def POSITIVE_4(cls):
                    return cls(4)
                
                @schemas.classproperty
                def POSITIVE_3(cls):
                    return cls(3)
                
                @schemas.classproperty
                def NONE(cls):
                    return cls(None)
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'delete_access_level':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "name": name,
                "description": description,
                "unit": unit,
                "data_type": data_type,
                "team": team,
                "read_access_level": read_access_level,
                "edit_access_level": edit_access_level,
                "delete_access_level": delete_access_level,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unit"]) -> MetaOapg.properties.unit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data_type"]) -> MetaOapg.properties.data_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["team"]) -> MetaOapg.properties.team: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["read_access_level"]) -> MetaOapg.properties.read_access_level: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["edit_access_level"]) -> MetaOapg.properties.edit_access_level: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["delete_access_level"]) -> MetaOapg.properties.delete_access_level: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "description", "unit", "data_type", "team", "read_access_level", "edit_access_level", "delete_access_level", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unit"]) -> typing.Union[MetaOapg.properties.unit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data_type"]) -> typing.Union[MetaOapg.properties.data_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["team"]) -> typing.Union[MetaOapg.properties.team, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["read_access_level"]) -> typing.Union[MetaOapg.properties.read_access_level, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["edit_access_level"]) -> typing.Union[MetaOapg.properties.edit_access_level, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["delete_access_level"]) -> typing.Union[MetaOapg.properties.delete_access_level, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "description", "unit", "data_type", "team", "read_access_level", "edit_access_level", "delete_access_level", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        unit: typing.Union[MetaOapg.properties.unit, str, schemas.Unset] = schemas.unset,
        data_type: typing.Union[MetaOapg.properties.data_type, str, schemas.Unset] = schemas.unset,
        team: typing.Union[MetaOapg.properties.team, None, str, schemas.Unset] = schemas.unset,
        read_access_level: typing.Union[MetaOapg.properties.read_access_level, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        edit_access_level: typing.Union[MetaOapg.properties.edit_access_level, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        delete_access_level: typing.Union[MetaOapg.properties.delete_access_level, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PatchedDataColumnTypeRequest':
        return super().__new__(
            cls,
            *_args,
            name=name,
            description=description,
            unit=unit,
            data_type=data_type,
            team=team,
            read_access_level=read_access_level,
            edit_access_level=edit_access_level,
            delete_access_level=delete_access_level,
            _configuration=_configuration,
            **kwargs,
        )
