# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.

import unittest
import os
import json


class RedisTest(unittest.TestCase):

    def test_describe_cache_instances(self):
        cmd = """python ../../main.py redis describe-cache-instances """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_cache_instance(self):
        cmd = """python ../../main.py redis create-cache-instance  --cache-instance '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_cache_instance(self):
        cmd = """python ../../main.py redis describe-cache-instance  --cache-instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_cache_instance_attribute(self):
        cmd = """python ../../main.py redis modify-cache-instance-attribute  --cache-instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_cache_instance(self):
        cmd = """python ../../main.py redis delete-cache-instance  --cache-instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_cache_instance_class(self):
        cmd = """python ../../main.py redis modify-cache-instance-class  --cache-instance-id 'xxx' --cache-instance-class 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_reset_cache_instance_password(self):
        cmd = """python ../../main.py redis reset-cache-instance-password  --cache-instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_instance_class(self):
        cmd = """python ../../main.py redis describe-instance-class """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_user_quota(self):
        cmd = """python ../../main.py redis describe-user-quota """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

