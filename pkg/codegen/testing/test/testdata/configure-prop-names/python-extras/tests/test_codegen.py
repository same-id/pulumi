# Copyright 2016-2023, Pulumi Corporation.
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

import pulumi
import pytest

from pulumi_gcp import compute

@pytest.fixture
def my_mocks():
    old_settings = pulumi.runtime.settings.SETTINGS
    try:
        mocks = MyMocks()
        pulumi.runtime.mocks.set_mocks(mocks)
        yield mocks
    finally:
        pulumi.runtime.settings.configure(old_settings)


class MyMocks(pulumi.runtime.Mocks):
    def call(self, args):
        return {}
    def new_resource(self, args):
        """
        new_resource mocks resource construction calls. This function should return the physical identifier and the output properties
        for the resource being constructed.

        :param MockResourceArgs args.
        """
        assert args.inputs['bootDisk']['initializeParams']['image'] == "debian-cloud/debian-11"
        return 'foo', args.inputs

@pulumi.runtime.test
def test_func_with_default_value(my_mocks):
    compute.instance.Instance(
        "instance-old",
        boot_disk={
            "initializeParams": {
                "image": "debian-cloud/debian-11",
            },
        },
    )

