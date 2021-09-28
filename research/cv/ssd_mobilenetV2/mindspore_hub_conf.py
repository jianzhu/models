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
from src.ssd import SSD320, SSDWithLossCell, ssd_mobilenet_v2
from src.config import config
from mindspore.common import dtype as mstype

def ssd_mobilenet_v2_fpn_net(ssd, *args, **kwargs):
    return SSDWithLossCell(ssd, config).to_float(mstype.float16)

def create_network(name, *args, **kwargs):
    if name == "ssd_mobilenetv2":
        backbone = ssd_mobilenet_v2()
        ssd = SSD320(backbone=backbone, config=config)
        return ssd_mobilenet_v2_fpn_net(ssd, *args, **kwargs)
    raise NotImplementedError(f"{name} is not implemented in the repo")
