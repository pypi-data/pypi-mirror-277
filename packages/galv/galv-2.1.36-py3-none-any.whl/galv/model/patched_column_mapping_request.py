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


class PatchedColumnMappingRequest(
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
            
            
            class map(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.AnyTypeSchema
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                ) -> 'map':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
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
                "map": map,
                "team": team,
                "read_access_level": read_access_level,
                "edit_access_level": edit_access_level,
                "delete_access_level": delete_access_level,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["map"]) -> MetaOapg.properties.map: ...
    
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
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "map", "team", "read_access_level", "edit_access_level", "delete_access_level", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["map"]) -> typing.Union[MetaOapg.properties.map, schemas.Unset]: ...
    
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
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "map", "team", "read_access_level", "edit_access_level", "delete_access_level", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        map: typing.Union[MetaOapg.properties.map, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        team: typing.Union[MetaOapg.properties.team, None, str, schemas.Unset] = schemas.unset,
        read_access_level: typing.Union[MetaOapg.properties.read_access_level, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        edit_access_level: typing.Union[MetaOapg.properties.edit_access_level, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        delete_access_level: typing.Union[MetaOapg.properties.delete_access_level, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PatchedColumnMappingRequest':
        return super().__new__(
            cls,
            *_args,
            name=name,
            map=map,
            team=team,
            read_access_level=read_access_level,
            edit_access_level=edit_access_level,
            delete_access_level=delete_access_level,
            _configuration=_configuration,
            **kwargs,
        )
