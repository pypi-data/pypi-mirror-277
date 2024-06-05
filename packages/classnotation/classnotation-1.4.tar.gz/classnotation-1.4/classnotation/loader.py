from typing import Any, Type, TypeVar, List, get_origin, get_args, Union, Literal, Tuple, ForwardRef
from dataclasses import fields, is_dataclass
import logging
import enum
import json
from .json_types import JSONObject
from .typecheck_error import TypeCheckError
import sys


T = TypeVar('T')


class DataclassLoader:
    allow_whole_float_as_int: bool
    strict: bool

    ############################################################################
    # loads
    #
    # Helper function wrapper to load a JSON string directly into a dataclass.
    ############################################################################
    def loads(
        self,
        data_class: Type[T],
        data: str,
        allow_whole_float_as_int: bool = True,
        strict: bool = True,
    ) -> T:
        return self.load_data(
            data_class=data_class,
            data=json.loads(data),
            allow_whole_float_as_int=allow_whole_float_as_int,
            strict=strict,
        )

    ############################################################################
    # load
    #
    # Load pre-parsed json data into a dataclass
    ############################################################################
    def load_data(
        self,
        data_class: Type[T],
        data: JSONObject,
        allow_whole_float_as_int: bool = True,
        strict: bool = True
    ) -> T:
        self.allow_whole_float_as_int = allow_whole_float_as_int
        self.strict = strict
        return self._load_data(data_class, data, _stack=())

    ############################################################################
    # _load_data
    #
    # An internal function call to load arbitrary data objects
    ############################################################################
    def _load_data(
        self,
        data_class: Type[T],
        data: JSONObject,
        _stack: Tuple[str, ...],

    ) -> T:
        if not is_dataclass(data_class):
            raise TypeCheckError("Expected a dataclass type as `data_class`", _stack)

        field_type_lookup = {field.name: field.type for field in fields(data_class)}
        field_renaming = {field.metadata["json"]: field.name for field in fields(data_class) if "json" in field.metadata}
        validated_data = {}

        for json_key, value in data.items():

            if not isinstance(json_key, str):
                raise TypeCheckError(
                    "Expected only string keys when loading dict into dataclass but found `{}` of type {}".format(json_key, type(json_key)),
                    _stack,
                )

            field_name = json_key
            if json_key in field_renaming:
                field_name = field_renaming[json_key]

            if field_name in field_type_lookup:
                field_type = field_type_lookup[field_name]

                validated_data[field_name] = self.validate_field(value, field_type, data_class,_stack=(*_stack, json_key))

            else:

                if not self.strict:
                    error_message = "Warning: Field '{json_key}' found in json at {stack} but it not present in the dataclass {dataclass}.".format(
                        json_key=json_key,
                        stack=".".join(_stack),
                        dataclass=data_class,
                    )
                    logging.warning(error_message)
                else:
                    raise TypeCheckError(
                        "Warning: Field '{json_key}' found but it not present in the dataclass {dataclass}.".format(
                            json_key=json_key,
                            dataclass=data_class,
                        ),
                        _stack,
                    )

        try:
            return data_class(**validated_data)
        except TypeCheckError as e:
            print("Error found at", ".".join(_stack)) # TODO: this should be incorporated into the message somehow
            raise e

    ################################################################################
    #
    ################################################################################
    def validate_field(
        self,
        value: Any,
        field_type: Type[T],
        parent_object: Any,
        _stack: Tuple[str, ...],
    ) -> T:
        field_type = resolve_field_type(field_type, parent_object)
        field_origin = get_origin(field_type)

        # List[]
        if field_origin == list:
            if isinstance(value, list):
                retval = [
                    self.validate_field(
                        value=element,
                        field_type=get_args(field_type)[0],
                        parent_object=parent_object,
                        _stack=(*_stack, "[{}]".format(i))
                    ) for i, element in enumerate(value)
                ]
                return retval

        # Dict[]
        elif field_origin == dict:
            if isinstance(value, dict):
                retval = {
                    self.validate_field(value=k, field_type=get_args(field_type)[0], parent_object=parent_object,_stack=(*_stack, str(k))):
                    self.validate_field(value=v, field_type=get_args(field_type)[1], parent_object=parent_object,_stack=(*_stack, "[{}]".format(k.__repr__())))
                    for k, v in value.items()
                }
                return retval

        # Set[]
        elif field_origin == set:
            if isinstance(value, list) or isinstance(value, set) or isinstance(value, tuple):
                retval = set([
                    self.validate_field(value=element, field_type=get_args(field_type)[0], parent_object=parent_object,_stack=(*_stack, "[{}]".format(i)))
                    for i, element in enumerate(value)
                ])
                return retval

        # Tuple[]
        elif (get_origin(field_type) == tuple):
            if isinstance(value, list) or isinstance(value, tuple):

                args = get_args(field_type)
                # Variable Length Tuples
                if len(args) == 2 and args[1] == Ellipsis:
                    retval = tuple(
                        self.validate_field(value=element, field_type=get_args(field_type)[0], parent_object=parent_object,_stack=(*_stack, "[{}]".format(i)))
                        for i, element in enumerate(value)
                    )
                    return retval

                # Fixed Length Tuples
                else:
                    if len(args) != len(value):
                        raise TypeCheckError(
                            "Different Number of elements found for tuple then expected found {} ({}), expected {}".format(len(value), value, len(args)),
                            _stack,
                        )

                    retval = tuple(
                        self.validate_field(value=value[i], field_type=args[i], parent_object=parent_object,_stack=(*_stack, "[{}]".format(i)))
                        for i in range(len(value))
                    )
                    return retval

        # Union[] and Optional[]
        elif field_origin == Union:
            all_errors: List[TypeCheckError] = []
            for arg in get_args(field_type):
                try:
                    return self.validate_field(value=value, field_type=arg, parent_object=parent_object,_stack=_stack)
                except TypeCheckError as e:
                    all_errors.append(e)

            if len(all_errors) > 0:
                # Build an error message that contains the errors from parsing each of the possible types in the union
                combined_message: List[str] = ["Expected one of union type `{}` at `{}`".format(field_type, ".".join(_stack))]
                for i, error in enumerate(all_errors):
                    prefix: str = "  {}: ".format(i)
                    for line in error.__str__().split("\n"):
                        combined_message.append(prefix + line)
                        prefix = " " * len(prefix)

                raise TypeCheckError("\n".join(combined_message), _stack)

        # Literal[]
        elif field_origin == Literal:
            arg_value = get_args(field_type)[0]
            if type(value) is str and type(arg_value) is bytes:
                value = value.encode("utf-8")

            if value != arg_value:
                raise TypeCheckError("Expected a literal '{}' but got '{}'".format(get_args(field_type)[0], value), _stack)
            return value

        elif field_origin is None:
            # Special case to call out that bool is historically an instance of int
            # and we want to be sure a bool is not trying to be assigned to an int.
            # TODO: we might want to make a custom isinstance function instead.
            if type(value) is bool and field_type in (int, float):
                pass

            # General case of scalar types
            elif isinstance(value, field_type): #TODO, This can bug sometimes if field_type is not a "type" for any reason. We should sanitize it at the very least to produce a useful error
                return value

            # Enums
            elif issubclass(field_type, enum.Enum):
                for element in field_type:
                    if element.value == value:
                        return field_type(value)
                raise TypeCheckError("Invalid Enum value for {}: {}".format(field_type, value), _stack)

            # Sub Dataclass
            elif isinstance(value, dict) and is_dataclass(field_type):
                retval = self._load_data(field_type, value, _stack=_stack)
                return retval

            # Special handling for floats as integers (as JSON numbers are parsed as floats)
            elif self.allow_whole_float_as_int and field_type is int and isinstance(value, float) and value.is_integer():
                return int(value)

            # Special handling for ints as floats, which can have integers implicitly assinged to them in general
            elif field_type is float and isinstance(value, int):
                return float(value)

            # Special handling for strings as bytes
            elif field_type is bytes and isinstance(value, str):
                return value.encode("utf-8")

            # If we get here, nothing above parsed properly
            raise TypeCheckError(
                "Unhandled scalar type `{found_type}`. Expected `{target_type}`.".format(
                    found_type=type(value),
                    target_type=field_type
                ),
                _stack,
            )

        else:
            raise TypeCheckError(
                "Error: Field '{data_key} in dataclass has an unexpected origin type of {data_origin}. This might be a bug in dataclass loader, please report it.".format(
                    data_key=".".join(_stack),
                    data_origin=field_origin,
                ),
                _stack,
            )

        raise TypeCheckError(
            "Error: Field '{data_key}' is {data_type} but dataclass expected {dataclass_type}".format(
                data_key=".".join(_stack),
                data_type=type(value),
                dataclass_type=field_type,
            ),
            _stack,
        )


################################################################################
# resolve_field_type
#
# This function takes a type annotation and resolves it into an actual type if
# it is defined as a string. This is necessary because many functions will be
# expecting a real type value and not a string representation of the type. One
# function is the commonly used `isinstance()`.
################################################################################
def resolve_field_type(
    field_type: Any,
    defined_in_object: Any
) -> Type:
    if isinstance(field_type, str):
        field_type = ForwardRef(field_type, is_argument=False, is_class=True)

    if isinstance(field_type, ForwardRef):
        for base in reversed(defined_in_object.__mro__):
            base_globals = getattr(sys.modules.get(base.__module__, None), '__dict__', {})
            base_locals = dict(vars(base))
            try:
                return field_type._evaluate(base_globals, base_locals, set())
            except NameError as e:
                pass

        raise NameError(
            "Could not find forward reference type \"{field_type}\". This forward reference is either not defined, or it is being used within an imported TypeAlias. Imported TypeAliases dont keep their module information making resolving their forward refs impossible at runtime.".format(
                field_type=field_type.__forward_arg__,
            )
        )

    # Handle most types
    elif isinstance(field_type, type):
        return field_type

    # Special case for the "None" type
    elif field_type is None:
        return type(None)

    # Handle typing generic types, for example List[int]
    elif get_origin(field_type) is not None:
        return field_type

    raise TypeError("Invalid type found on field {} (of type {})".format(field_type, type(field_type)))



################################################################################
# load_data
#
# Top level helper function to load a json string into a dataclass without
# worrying about creating or managing the DataclassLoader object.
################################################################################
def loads(
    data_class: Type[T],
    data: str,
    allow_whole_float_as_int: bool = True,
    strict: bool = True
) -> T:
    loader = DataclassLoader()
    return loader.loads(data_class, data, allow_whole_float_as_int=allow_whole_float_as_int, strict=strict)


################################################################################
# load_data
#
# Top level helper function to load data into a dataclass without worrying
# about creating or managing the DataclassLoader object.
################################################################################
def load_data(
    data_class: Type[T],
    data: JSONObject,
    allow_whole_float_as_int: bool = True,
    strict: bool = True
) -> T:
    loader = DataclassLoader()
    return loader.load_data(data_class, data, allow_whole_float_as_int=allow_whole_float_as_int, strict=strict)
