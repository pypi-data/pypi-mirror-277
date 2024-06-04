# coding: utf-8

"""
    Battery Data API

    A standard API for accessing battery experiment datasets and metadata  # noqa: E501

    The version of the OpenAPI document: 2.1.36
    Contact: martin.robinson@cs.ox.ac.uk
    Generated by: https://openapi-generator.tech
"""

from galv.paths.validation_schemas_.post import ValidationSchemasCreate
from galv.paths.validation_schemas_id_.delete import ValidationSchemasDestroy
from galv.paths.validation_schemas_keys_.get import ValidationSchemasKeysRetrieve
from galv.paths.validation_schemas_.get import ValidationSchemasList
from galv.paths.validation_schemas_id_.patch import ValidationSchemasPartialUpdate
from galv.paths.validation_schemas_id_.get import ValidationSchemasRetrieve
from galv.paths.validation_schemas_id_.put import ValidationSchemasUpdate


class ValidationSchemasApi(
    ValidationSchemasCreate,
    ValidationSchemasDestroy,
    ValidationSchemasKeysRetrieve,
    ValidationSchemasList,
    ValidationSchemasPartialUpdate,
    ValidationSchemasRetrieve,
    ValidationSchemasUpdate,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
