# Copyright 2021 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""hub config"""
from src.resnet import se_resnet50 as resnet
from src.config import config2 as config


def se_resnet50_net(*args, **kwargs):
    return resnet(class_num=config.class_num)


def create_network(name, *args, **kwargs):
    if name == "se-net":
        return se_resnet50_net()
    raise NotImplementedError(f"{name} is not implemented in the repo")