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


class MonitoredPath(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "harvester",
            "path",
            "permissions",
            "files",
            "id",
            "team",
            "url",
        }
        
        class properties:
            url = schemas.StrSchema
            id = schemas.UUIDSchema
            path = schemas.StrSchema
            
            
            class files(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'files':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            harvester = schemas.StrSchema
            team = schemas.StrSchema
            
            
            class permissions(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        read = schemas.BoolSchema
                        write = schemas.BoolSchema
                        create = schemas.BoolSchema
                        __annotations__ = {
                            "read": read,
                            "write": write,
                            "create": create,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["read"]) -> MetaOapg.properties.read: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["write"]) -> MetaOapg.properties.write: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["create"]) -> MetaOapg.properties.create: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["read", "write", "create", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["read"]) -> typing.Union[MetaOapg.properties.read, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["write"]) -> typing.Union[MetaOapg.properties.write, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["create"]) -> typing.Union[MetaOapg.properties.create, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["read", "write", "create", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    read: typing.Union[MetaOapg.properties.read, bool, schemas.Unset] = schemas.unset,
                    write: typing.Union[MetaOapg.properties.write, bool, schemas.Unset] = schemas.unset,
                    create: typing.Union[MetaOapg.properties.create, bool, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'permissions':
                    return super().__new__(
                        cls,
                        *_args,
                        read=read,
                        write=write,
                        create=create,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class regex(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'regex':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class stable_time(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 32767
                    inclusive_minimum = 0
            active = schemas.BoolSchema
            
            
            class max_partition_line_count(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 2147483647
                    inclusive_minimum = 0
            
            
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
                "url": url,
                "id": id,
                "path": path,
                "files": files,
                "harvester": harvester,
                "team": team,
                "permissions": permissions,
                "regex": regex,
                "stable_time": stable_time,
                "active": active,
                "max_partition_line_count": max_partition_line_count,
                "read_access_level": read_access_level,
                "edit_access_level": edit_access_level,
                "delete_access_level": delete_access_level,
            }
    
    harvester: MetaOapg.properties.harvester
    path: MetaOapg.properties.path
    permissions: MetaOapg.properties.permissions
    files: MetaOapg.properties.files
    id: MetaOapg.properties.id
    team: MetaOapg.properties.team
    url: MetaOapg.properties.url
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["path"]) -> MetaOapg.properties.path: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["files"]) -> MetaOapg.properties.files: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["harvester"]) -> MetaOapg.properties.harvester: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["team"]) -> MetaOapg.properties.team: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["permissions"]) -> MetaOapg.properties.permissions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["regex"]) -> MetaOapg.properties.regex: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stable_time"]) -> MetaOapg.properties.stable_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max_partition_line_count"]) -> MetaOapg.properties.max_partition_line_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["read_access_level"]) -> MetaOapg.properties.read_access_level: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["edit_access_level"]) -> MetaOapg.properties.edit_access_level: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["delete_access_level"]) -> MetaOapg.properties.delete_access_level: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["url", "id", "path", "files", "harvester", "team", "permissions", "regex", "stable_time", "active", "max_partition_line_count", "read_access_level", "edit_access_level", "delete_access_level", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["path"]) -> MetaOapg.properties.path: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["files"]) -> MetaOapg.properties.files: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["harvester"]) -> MetaOapg.properties.harvester: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["team"]) -> MetaOapg.properties.team: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["permissions"]) -> MetaOapg.properties.permissions: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["regex"]) -> typing.Union[MetaOapg.properties.regex, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stable_time"]) -> typing.Union[MetaOapg.properties.stable_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active"]) -> typing.Union[MetaOapg.properties.active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max_partition_line_count"]) -> typing.Union[MetaOapg.properties.max_partition_line_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["read_access_level"]) -> typing.Union[MetaOapg.properties.read_access_level, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["edit_access_level"]) -> typing.Union[MetaOapg.properties.edit_access_level, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["delete_access_level"]) -> typing.Union[MetaOapg.properties.delete_access_level, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["url", "id", "path", "files", "harvester", "team", "permissions", "regex", "stable_time", "active", "max_partition_line_count", "read_access_level", "edit_access_level", "delete_access_level", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        harvester: typing.Union[MetaOapg.properties.harvester, str, ],
        path: typing.Union[MetaOapg.properties.path, str, ],
        permissions: typing.Union[MetaOapg.properties.permissions, dict, frozendict.frozendict, ],
        files: typing.Union[MetaOapg.properties.files, list, tuple, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, ],
        team: typing.Union[MetaOapg.properties.team, str, ],
        url: typing.Union[MetaOapg.properties.url, str, ],
        regex: typing.Union[MetaOapg.properties.regex, None, str, schemas.Unset] = schemas.unset,
        stable_time: typing.Union[MetaOapg.properties.stable_time, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        active: typing.Union[MetaOapg.properties.active, bool, schemas.Unset] = schemas.unset,
        max_partition_line_count: typing.Union[MetaOapg.properties.max_partition_line_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        read_access_level: typing.Union[MetaOapg.properties.read_access_level, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        edit_access_level: typing.Union[MetaOapg.properties.edit_access_level, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        delete_access_level: typing.Union[MetaOapg.properties.delete_access_level, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MonitoredPath':
        return super().__new__(
            cls,
            *_args,
            harvester=harvester,
            path=path,
            permissions=permissions,
            files=files,
            id=id,
            team=team,
            url=url,
            regex=regex,
            stable_time=stable_time,
            active=active,
            max_partition_line_count=max_partition_line_count,
            read_access_level=read_access_level,
            edit_access_level=edit_access_level,
            delete_access_level=delete_access_level,
            _configuration=_configuration,
            **kwargs,
        )
