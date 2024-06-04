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


class ScheduleFamily(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A ModelSerializer that maps unrecognised properties in the input to an 'custom_properties' JSONField,
and unpacks the 'custom_properties' JSONField into the output.

The Meta.model must have a custom_properties JSONField.
    """


    class MetaOapg:
        required = {
            "identifier",
            "permissions",
            "schedules",
            "description",
            "in_use",
            "id",
            "team",
            "url",
        }
        
        class properties:
            url = schemas.StrSchema
            id = schemas.UUIDSchema
            identifier = schemas.StrSchema
            description = schemas.StrSchema
            in_use = schemas.BoolSchema
            
            
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
            
            
            class schedules(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'schedules':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
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
            
            
            class ambient_temperature(
                schemas.Float64Base,
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'double'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ambient_temperature':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class pybamm_template(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'pybamm_template':
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
            
            
            class custom_properties(
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
                ) -> 'custom_properties':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "url": url,
                "id": id,
                "identifier": identifier,
                "description": description,
                "in_use": in_use,
                "team": team,
                "schedules": schedules,
                "permissions": permissions,
                "ambient_temperature": ambient_temperature,
                "pybamm_template": pybamm_template,
                "read_access_level": read_access_level,
                "edit_access_level": edit_access_level,
                "delete_access_level": delete_access_level,
                "custom_properties": custom_properties,
            }
    
    identifier: MetaOapg.properties.identifier
    permissions: MetaOapg.properties.permissions
    schedules: MetaOapg.properties.schedules
    description: MetaOapg.properties.description
    in_use: MetaOapg.properties.in_use
    id: MetaOapg.properties.id
    team: MetaOapg.properties.team
    url: MetaOapg.properties.url
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["identifier"]) -> MetaOapg.properties.identifier: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["in_use"]) -> MetaOapg.properties.in_use: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["team"]) -> MetaOapg.properties.team: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schedules"]) -> MetaOapg.properties.schedules: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["permissions"]) -> MetaOapg.properties.permissions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ambient_temperature"]) -> MetaOapg.properties.ambient_temperature: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pybamm_template"]) -> MetaOapg.properties.pybamm_template: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["read_access_level"]) -> MetaOapg.properties.read_access_level: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["edit_access_level"]) -> MetaOapg.properties.edit_access_level: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["delete_access_level"]) -> MetaOapg.properties.delete_access_level: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_properties"]) -> MetaOapg.properties.custom_properties: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["url", "id", "identifier", "description", "in_use", "team", "schedules", "permissions", "ambient_temperature", "pybamm_template", "read_access_level", "edit_access_level", "delete_access_level", "custom_properties", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["identifier"]) -> MetaOapg.properties.identifier: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["in_use"]) -> MetaOapg.properties.in_use: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["team"]) -> MetaOapg.properties.team: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schedules"]) -> MetaOapg.properties.schedules: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["permissions"]) -> MetaOapg.properties.permissions: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ambient_temperature"]) -> typing.Union[MetaOapg.properties.ambient_temperature, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pybamm_template"]) -> typing.Union[MetaOapg.properties.pybamm_template, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["read_access_level"]) -> typing.Union[MetaOapg.properties.read_access_level, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["edit_access_level"]) -> typing.Union[MetaOapg.properties.edit_access_level, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["delete_access_level"]) -> typing.Union[MetaOapg.properties.delete_access_level, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_properties"]) -> typing.Union[MetaOapg.properties.custom_properties, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["url", "id", "identifier", "description", "in_use", "team", "schedules", "permissions", "ambient_temperature", "pybamm_template", "read_access_level", "edit_access_level", "delete_access_level", "custom_properties", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        identifier: typing.Union[MetaOapg.properties.identifier, str, ],
        permissions: typing.Union[MetaOapg.properties.permissions, dict, frozendict.frozendict, ],
        schedules: typing.Union[MetaOapg.properties.schedules, list, tuple, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        in_use: typing.Union[MetaOapg.properties.in_use, bool, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, ],
        team: typing.Union[MetaOapg.properties.team, None, str, ],
        url: typing.Union[MetaOapg.properties.url, str, ],
        ambient_temperature: typing.Union[MetaOapg.properties.ambient_temperature, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        pybamm_template: typing.Union[MetaOapg.properties.pybamm_template, list, tuple, None, schemas.Unset] = schemas.unset,
        read_access_level: typing.Union[MetaOapg.properties.read_access_level, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        edit_access_level: typing.Union[MetaOapg.properties.edit_access_level, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        delete_access_level: typing.Union[MetaOapg.properties.delete_access_level, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        custom_properties: typing.Union[MetaOapg.properties.custom_properties, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ScheduleFamily':
        return super().__new__(
            cls,
            *_args,
            identifier=identifier,
            permissions=permissions,
            schedules=schedules,
            description=description,
            in_use=in_use,
            id=id,
            team=team,
            url=url,
            ambient_temperature=ambient_temperature,
            pybamm_template=pybamm_template,
            read_access_level=read_access_level,
            edit_access_level=edit_access_level,
            delete_access_level=delete_access_level,
            custom_properties=custom_properties,
            _configuration=_configuration,
            **kwargs,
        )
