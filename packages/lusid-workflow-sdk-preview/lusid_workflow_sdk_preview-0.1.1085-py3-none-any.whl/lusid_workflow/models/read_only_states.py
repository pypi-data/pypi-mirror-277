# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.1085
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid_workflow.configuration import Configuration


class ReadOnlyStates(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'state_type': 'str',
        'selected_states': 'list[str]'
    }

    attribute_map = {
        'state_type': 'stateType',
        'selected_states': 'selectedStates'
    }

    required_map = {
        'state_type': 'required',
        'selected_states': 'optional'
    }

    def __init__(self, state_type=None, selected_states=None, local_vars_configuration=None):  # noqa: E501
        """ReadOnlyStates - a model defined in OpenAPI"
        
        :param state_type:  The State Type (e.g. InitialState, AllStates, TerminalState, SelectedStates) (required)
        :type state_type: str
        :param selected_states:  Named states for which the field will be readonly - This field can only be populated if StateType = SelectedStates
        :type selected_states: list[str]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._state_type = None
        self._selected_states = None
        self.discriminator = None

        self.state_type = state_type
        self.selected_states = selected_states

    @property
    def state_type(self):
        """Gets the state_type of this ReadOnlyStates.  # noqa: E501

        The State Type (e.g. InitialState, AllStates, TerminalState, SelectedStates)  # noqa: E501

        :return: The state_type of this ReadOnlyStates.  # noqa: E501
        :rtype: str
        """
        return self._state_type

    @state_type.setter
    def state_type(self, state_type):
        """Sets the state_type of this ReadOnlyStates.

        The State Type (e.g. InitialState, AllStates, TerminalState, SelectedStates)  # noqa: E501

        :param state_type: The state_type of this ReadOnlyStates.  # noqa: E501
        :type state_type: str
        """
        if self.local_vars_configuration.client_side_validation and state_type is None:  # noqa: E501
            raise ValueError("Invalid value for `state_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                state_type is not None and len(state_type) < 1):
            raise ValueError("Invalid value for `state_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._state_type = state_type

    @property
    def selected_states(self):
        """Gets the selected_states of this ReadOnlyStates.  # noqa: E501

        Named states for which the field will be readonly - This field can only be populated if StateType = SelectedStates  # noqa: E501

        :return: The selected_states of this ReadOnlyStates.  # noqa: E501
        :rtype: list[str]
        """
        return self._selected_states

    @selected_states.setter
    def selected_states(self, selected_states):
        """Sets the selected_states of this ReadOnlyStates.

        Named states for which the field will be readonly - This field can only be populated if StateType = SelectedStates  # noqa: E501

        :param selected_states: The selected_states of this ReadOnlyStates.  # noqa: E501
        :type selected_states: list[str]
        """

        self._selected_states = selected_states

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReadOnlyStates):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReadOnlyStates):
            return True

        return self.to_dict() != other.to_dict()
