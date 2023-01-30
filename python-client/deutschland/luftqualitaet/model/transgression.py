"""
    Umweltbundesamt Air Data API

    Air data API of Umweltbundesamt  # noqa: E501

    The version of the OpenAPI document: 2.0.1
    Contact: immission@uba.de
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from deutschland.luftqualitaet.exceptions import ApiAttributeError
from deutschland.luftqualitaet.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    OpenApiModel,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)


class Transgression(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {}

    validations = {}

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (
            bool,
            date,
            datetime,
            dict,
            float,
            int,
            list,
            str,
            none_type,
        )  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            "_0": (int,),  # noqa: E501
            "_1": (str,),  # noqa: E501
            "_2": (str,),  # noqa: E501
            "_3": (int,),  # noqa: E501
            "_4": (int,),  # noqa: E501
            "_5": (int,),  # noqa: E501
            "_6": (int,),  # noqa: E501
            "_7": (int,),  # noqa: E501
            "_8": (int,),  # noqa: E501
            "_9": (int,),  # noqa: E501
            "_10": (int,),  # noqa: E501
            "_11": (int,),  # noqa: E501
            "_12": (int,),  # noqa: E501
            "_13": (int,),  # noqa: E501
            "_14": (int,),  # noqa: E501
            "_15": (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        "_0": "0",  # noqa: E501
        "_1": "1",  # noqa: E501
        "_2": "2",  # noqa: E501
        "_3": "3",  # noqa: E501
        "_4": "4",  # noqa: E501
        "_5": "5",  # noqa: E501
        "_6": "6",  # noqa: E501
        "_7": "7",  # noqa: E501
        "_8": "8",  # noqa: E501
        "_9": "9",  # noqa: E501
        "_10": "10",  # noqa: E501
        "_11": "11",  # noqa: E501
        "_12": "12",  # noqa: E501
        "_13": "13",  # noqa: E501
        "_14": "14",  # noqa: E501
        "_15": "15",  # noqa: E501
    }

    read_only_vars = {}

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Transgression - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            _0 (int): Id of station. [optional]  # noqa: E501
            _1 (str): Date of first activity. [optional]  # noqa: E501
            _2 (str): Date of recent activity. [optional]  # noqa: E501
            _3 (int): Sum of values of year. [optional]  # noqa: E501
            _4 (int): Value of January. [optional]  # noqa: E501
            _5 (int): Value of Feburary. [optional]  # noqa: E501
            _6 (int): Value of March. [optional]  # noqa: E501
            _7 (int): Value of April. [optional]  # noqa: E501
            _8 (int): Value of May. [optional]  # noqa: E501
            _9 (int): Value of June. [optional]  # noqa: E501
            _10 (int): Value of July. [optional]  # noqa: E501
            _11 (int): Value of August. [optional]  # noqa: E501
            _12 (int): Value of September. [optional]  # noqa: E501
            _13 (int): Value of October. [optional]  # noqa: E501
            _14 (int): Value of November. [optional]  # noqa: E501
            _15 (int): Value of December. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", False)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set(
        [
            "_data_store",
            "_check_type",
            "_spec_property_naming",
            "_path_to_item",
            "_configuration",
            "_visited_composed_classes",
        ]
    )

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Transgression - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            _0 (int): Id of station. [optional]  # noqa: E501
            _1 (str): Date of first activity. [optional]  # noqa: E501
            _2 (str): Date of recent activity. [optional]  # noqa: E501
            _3 (int): Sum of values of year. [optional]  # noqa: E501
            _4 (int): Value of January. [optional]  # noqa: E501
            _5 (int): Value of Feburary. [optional]  # noqa: E501
            _6 (int): Value of March. [optional]  # noqa: E501
            _7 (int): Value of April. [optional]  # noqa: E501
            _8 (int): Value of May. [optional]  # noqa: E501
            _9 (int): Value of June. [optional]  # noqa: E501
            _10 (int): Value of July. [optional]  # noqa: E501
            _11 (int): Value of August. [optional]  # noqa: E501
            _12 (int): Value of September. [optional]  # noqa: E501
            _13 (int): Value of October. [optional]  # noqa: E501
            _14 (int): Value of November. [optional]  # noqa: E501
            _15 (int): Value of December. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", False)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(
                    f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                    f"class with read only attributes."
                )