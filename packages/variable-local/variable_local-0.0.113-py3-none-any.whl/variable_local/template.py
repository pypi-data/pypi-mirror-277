import random
import re

from language_remote.lang_code import LangCode
from logger_local.MetaLogger import MetaLogger
from smartlink_local.smartlink import SmartlinkLocal
from smartlink_remote_restapi.smartlink_remote import SmartlinkRemote
from url_remote.our_url import OurUrl
from python_sdk_remote.utilities import get_environment_name, get_brand_name, generate_otp, get_current_datetime_string

from .constants import variable_local_logger_init_object
from .variables_local import VariablesLocal

LEFT_BRACKETS = '{'
RIGHT_BRACKETS = '}'


class ReplaceFieldsWithValues(metaclass=MetaLogger, object=variable_local_logger_init_object):
    def __init__(self, message, lang_code: LangCode, variables: VariablesLocal):
        self.message = message
        self.lang_code = lang_code
        self.variables = variables
        self.smartlink_local = None  # For performance reasons

    def get_smartlink_url_by_variable_name_and_kwargs(self, variable_name: str, **kwargs) -> str:
        self.smartlink_local = self.smartlink_local or SmartlinkLocal()
        smartlink_regex = r"smartlinkUrl\(smartlinkType=([0-9]+)\)"
        smartlink_type_id = re.search(smartlink_regex, variable_name).group(1)
        url_redirect_template = self.smartlink_local.get_smartlink_type_dict_by_id(
            smartlink_type_id, select_clause_value="url_redirect_template").get("url_redirect_template")
        if url_redirect_template:
            url_redirect = self.get_formatted_message(message=url_redirect_template)
        else:
            url_redirect = None
        smartlink_details = self.smartlink_local.insert(
            smartlink_type_id=smartlink_type_id, campaign_id=kwargs.get('campaign_id'),
            url_redirect=url_redirect,
            from_recipient_dict=kwargs.get('from_recipient'), to_recipient_dict=kwargs.get('to_recipient'))
        smartlink_url = SmartlinkRemote.get_smartlink_url(identifier=smartlink_details['identifier'])
        return smartlink_url

    # TODO variable_name: VariableNameEnum / SpecialVariableEnum
    def get_variable_value_by_variable_name_and_kwargs(self, variable_name: str, **kwargs) -> str:
        # TODO: use worker actions instead
        """Returns a special variable value by variable name"""
        # TODO: test each case
        smartlink_regex = r"smartlinkUrl\(smartlinkType=([0-9]+)\)"

        if variable_name == 'otp':
            variable_value = generate_otp()
        elif variable_name == 'date_sortable':
            variable_value = get_current_datetime_string()
        elif variable_name == 'environmentName':
            variable_value = get_environment_name()
        elif variable_name == 'brandName':
            variable_value = get_brand_name()
        elif variable_name == 'appUrl':
            variable_value = OurUrl.app_url(environment_name=get_environment_name(), brand_name=get_brand_name())
        elif re.match(smartlink_regex, variable_name):
            variable_value = self.get_smartlink_url_by_variable_name_and_kwargs(variable_name, **kwargs)
        else:  # TODO: add more special variables
            self.logger.warning("Unknown special variable name `" + variable_name + "` in message: " + self.message,
                                object=kwargs)
            return ""

        return str(variable_value)

    def get_variable_values_and_chosen_option(self, profile_id: int = None, **kwargs) -> str:
        self.logger.warning("get_variable_values_and_chosen_option is deprecated. Use get_formatted_message instead.")
        formatted_message = self.get_formatted_message(profile_id, **kwargs)
        return formatted_message

    # Should be used both by Dialog workflow and message-local-python-package Message.py
    def get_formatted_message(self, profile_id: int = None, **kwargs) -> str:
        """Returns:
            1. A list of all variable values by variable names that were inside curly braces of message
            2. A string that's a copy of the message but without the variable names inside curly braces
            and a randomly chosen parameter out of each curly braces options:
            "Hello ${{First Name}}, how are you ${{feeling|doing}}?" --> "Hello {}, how are you doing?"
        """
        old_message = self.message
        kwargs = kwargs.get('kwargs', kwargs)  # in case someone sent the kwargs in a diff way
        self.message = kwargs.get("message", self.message)
        formatted_message = self.message

        pattern = re.compile(r'\${{[^}]*}}')  # ${{vraiable}}
        matches = pattern.findall(formatted_message)
        for exact_match in matches:
            match = exact_match[3:-2].strip()  # remove '${{' and '}}'
            if '|' in match:  # # choose random option from {A|B|C}
                # pick random choice
                options = match.split('|')
                random_option = random.choice(options)
                formatted_message = formatted_message.replace(exact_match, random_option, 1)

            elif match in kwargs:
                formatted_message = formatted_message.replace(
                    exact_match, str(kwargs[match] if match in kwargs else kwargs[match]), 1)

            elif match in self.variables.name2id_dict.keys():
                # replace variable name with variable_value
                variable_id = self.variables.get_variable_id_by_variable_name(match)
                variable_value = self.variables.get_variable_value_by_variable_id(
                    variable_id=variable_id, lang_code=self.lang_code, profile_id=profile_id)
                formatted_message = formatted_message.replace(exact_match, variable_value, 1)

            else:
                formatted_message = formatted_message.replace(
                    exact_match, self.get_variable_value_by_variable_name_and_kwargs(match, **kwargs), 1)

        self.message = old_message
        return formatted_message
