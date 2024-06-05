"""
Class to construct a query filter.
"""
from dataclasses import dataclass
from datetime import datetime
from itertools import filterfalse
from typing import Any


@dataclass
class Query:
    prop_name: str
    operator: str
    value: Any
    available_operators = {
        'lt': 'lower than',
        'le': 'lower than or equal',
        'eq': 'equal',
        'gt': 'greater than',
        'ge': 'greater or equal',
        'in': 'in a list of values',
        'between': 'between two values'
    }

    def valid_operator(self, model_props: dict):
        """
        Verify that the logical operator is correct.

        :param model_props: The dictionary of available properties for the query.
        :return: Nothing.
        """
        if self.operator not in self.available_operators.keys():
            error_message = 'The available operators are:'
            for oper, desc in self.available_operators.items():
                error_message += f' "{oper}" ({desc})'
            raise ValueError(f'The operator {self.operator} is not valid. {error_message}')

        if type(self.value) == str and self.operator != 'eq':
            raise ValueError(f'You can not use the operator {self.operator} '
                             f'with a string attribute {self.prop_name}')
        if self.operator == 'in':
            self.correct_list_operators(model_props)
        if self.operator == 'between':
            self.correct_between_operator(model_props)

    def valid_prop_name(self, model_props: dict):
        """
        Control that the model attribute provided is available.

        :param model_props: The dictionary of available properties for the query.
        :return: Nothing.
        """
        # Name is correct
        if self.prop_name not in model_props.keys():
            raise ValueError(f'The attribute {self.prop_name} is not valid')

        if self.operator in ('in', 'between'):
            return
        # Type is correct
        if not isinstance(self.value, model_props[self.prop_name]):
            raise TypeError(f'The value {self.value} can not be parsed to the correct type')

    def correct_list_operators(self, model_props: dict):
        """
        Control if all values in the list of values have a correct type.

        :param model_props: The dictionary of available properties for the query.
        """
        if not isinstance(self.value, list):
            raise ValueError('The value must be a list.')

        if any(filterfalse(lambda x: isinstance(x, model_props[self.prop_name]), self.value)):
            raise ValueError(f'One or several values in the list has not a correct data type '
                             f'for "{self.prop_name}"')

    def correct_between_operator(self, model_props: dict):
        """
        Control if the provided value is consistent to use with the between operator.

        :param model_props: the dictionary of available properties for the query
        """
        if not isinstance(self.value, list):
            raise ValueError('You have to apply this filter on a list of two elements')
        self.correct_list_operators(model_props)
        if len(self.value) != 2:
            raise ValueError('The "between" operator need two values')

    def to_tuple(self) -> tuple:
        """
        Return the query object into a tuple format.
        """
        if isinstance(self.value, list):
            value = self.control_list_values(self.value)
        else:
            value = self.datetime_to_iso(self.value)
        return self.prop_name, self.operator, value

    @staticmethod
    def datetime_to_iso(input_value: object) -> object:
        """
        If the value is a datetime object, try to convert it into string iso format.

        :param input_value: The value to check and convert.
        :return: The initial value or the value converted to the iso format.
        """
        if isinstance(input_value, datetime):
            value = input_value.isoformat()
        else:
            value = input_value
        return value

    def control_list_values(self, values: list) -> list:
        """
        Apply the datetime to iso conversion to all values in the list of values.

        :param values: The list of values.
        """
        final_values = []
        for value in values:
            v = self.datetime_to_iso(value)
            final_values.append(v)
        return final_values
