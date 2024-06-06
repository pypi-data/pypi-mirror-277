# Copyright 2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Modifications made by Cloudera are:
#     Copyright (c) 2016 Cloudera, Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

from cdpcli import CDP_ACCESS_KEY_ID_KEY_NAME, \
                   CDP_PRIVATE_KEY_KEY_NAME, \
                   CDP_REGION_KEY_NAME
from cdpcli.compat import six
from cdpcli.extensions.configure.list import ConfigureListCommand
import mock
from tests import unittest
from tests.unit import FakeContext


class TestConfigureListCommand(unittest.TestCase):

    def test_configure_list_command_nothing_set(self):
        # Test the case where the user only wants to change a single_value.
        context = FakeContext(
            all_variables={'config_file': '/config/location'})
        context.full_config = {
            'profiles': {'default': {}}}
        stream = six.StringIO()
        self.configure_list = ConfigureListCommand(stream)
        self.configure_list(context, args=[], parsed_globals=None)
        rendered = stream.getvalue()
        self.assertRegexpMatches(rendered, 'profile\\s+<not set>')
        self.assertRegexpMatches(rendered, 'cdp_region\\s+<not set>')
        self.assertRegexpMatches(rendered, 'cdp_access_key_id\\s+<not set>')
        self.assertRegexpMatches(rendered, 'cdp_private_key\\s+<not set>')

    def test_configure_from_env(self):
        env_vars = {
            'profile': 'myprofilename'
        }
        context = FakeContext(
            all_variables={'config_file': '/config/location'},
            environment_vars=env_vars)
        context.context_var_map = {'profile': (None, "PROFILE_ENV_VAR")}
        context.full_config = {
            'profiles': {'default': {}}}
        stream = six.StringIO()
        self.configure_list = ConfigureListCommand(stream)
        self.configure_list(context, args=[], parsed_globals=None)
        rendered = stream.getvalue()
        self.assertRegexpMatches(
            rendered, 'profile\\s+myprofilename\\s+env\\s+PROFILE_ENV_VAR')

    def test_configure_from_config_file(self):
        config_file_vars = {
            # this is not a known configuration so this is ignored.
            'foo': 'bar',
            CDP_REGION_KEY_NAME: 'eu-1',
            CDP_ACCESS_KEY_ID_KEY_NAME: 'key_id',
            CDP_PRIVATE_KEY_KEY_NAME: 'mysecretkey'
        }
        context = FakeContext(
            all_variables={'config_file': '/config/location'},
            config_file_vars=config_file_vars)
        context.context_var_map = {'region': ()}
        context.full_config = {
            'profiles': {'default': {}}}
        stream = six.StringIO()
        self.configure_list = ConfigureListCommand(stream)
        self.configure_list(context, args=[], parsed_globals=None)
        rendered = stream.getvalue()
        self.assertRegexpMatches(
            rendered, 'profile\\s+<not set>\\s+None\\s+None')
        self.assertRegexpMatches(
            rendered, 'cdp_region\\s+eu-1\\s+config-file')
        self.assertRegexpMatches(
            rendered, 'cdp_access_key_id\\s+\\*+y_id\\s+config-file')
        self.assertRegexpMatches(
            rendered, 'cdp_private_key\\s+\\*+tkey\\s+config-file')

    def test_configure_from_multiple_sources(self):
        # Here the profile is from an env var, the
        # region is from the config file, and the credentials
        # are from an iam-role.
        env_vars = {
            'profile': 'myprofilename'
        }
        config_file_vars = {
            CDP_REGION_KEY_NAME: 'eu-1'
        }
        credentials = mock.Mock()
        credentials.access_key_id = 'access_key'
        credentials.private_key = 'private_key'
        credentials.access_token = None
        credentials.method = 'foobar'
        context = FakeContext(
            all_variables={'config_file': '/config/location'},
            environment_vars=env_vars,
            config_file_vars=config_file_vars,
            credentials=credentials)
        context.context_var_map = {
            'profile': ('profile', 'CDP_DEFAULT_PROFILE')}
        context.full_config = {
            'profiles': {'default': {}}}
        stream = six.StringIO()
        self.configure_list = ConfigureListCommand(stream)
        self.configure_list(context, args=[], parsed_globals=None)
        rendered = stream.getvalue()
        # The profile came from an env var.
        self.assertRegexpMatches(
            rendered, 'profile\\s+myprofilename\\s+env\\s+CDP_DEFAULT_PROFILE')
        # The cdp_region came from config file.
        self.assertRegexpMatches(
            rendered, 'cdp_region\\s+eu-1\\s+config-file')
        # The credentials came from 'foobar'.  Note how we're
        # also checking that the access_key/private_key are masked
        # with '*' chars except for the last 4 chars.
        self.assertRegexpMatches(
            rendered, r'cdp_access_key_id\s+\*+_key\s+foobar')
        self.assertRegexpMatches(
            rendered, r'cdp_private_key\s+\*+_key\s+foobar')

    def test_profile_set_in_context(self):
        config_file_vars = {
            # this is not a known configuration so this is ignored.
            'foo': 'bar',
            CDP_REGION_KEY_NAME: 'eu-1',
            CDP_ACCESS_KEY_ID_KEY_NAME: 'key_id',
            CDP_PRIVATE_KEY_KEY_NAME: 'mysecretkey'
        }
        context = FakeContext(
            all_variables={'config_file': '/config/location'},
            config_file_vars=config_file_vars)
        context.profile = 'dev'
        context.context_var_map = {}
        context.full_config = {
            'profiles': {'dev': {}}}
        stream = six.StringIO()
        self.configure_list = ConfigureListCommand(stream)
        self.configure_list(context, args=[], parsed_globals=None)
        rendered = stream.getvalue()
        self.assertRegexpMatches(
            rendered, 'profile\\s+dev\\s+manual\\s+--profile')
        self.assertRegexpMatches(
            rendered, 'cdp_region\\s+eu-1\\s+config-file')
        self.assertRegexpMatches(
            rendered, r'cdp_access_key_id\s+\*+y_id\s+config-file')
        self.assertRegexpMatches(
            rendered, r'cdp_private_key\s+\*+tkey\s+config-file')
