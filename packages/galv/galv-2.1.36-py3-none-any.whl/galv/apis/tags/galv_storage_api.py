# coding: utf-8

"""
    Battery Data API

    A standard API for accessing battery experiment datasets and metadata  # noqa: E501

    The version of the OpenAPI document: 2.1.36
    Contact: martin.robinson@cs.ox.ac.uk
    Generated by: https://openapi-generator.tech
"""

from galv.paths.galv_storage_.get import GalvStorageList
from galv.paths.galv_storage_id_.patch import GalvStoragePartialUpdate
from galv.paths.galv_storage_id_.get import GalvStorageRetrieve


class GalvStorageApi(
    GalvStorageList,
    GalvStoragePartialUpdate,
    GalvStorageRetrieve,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
