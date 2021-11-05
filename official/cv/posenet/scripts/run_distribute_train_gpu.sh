#!/bin/bash
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

echo "=============================================================================================================="
echo "Please run the script as: "
echo "bash run_distribute_train.sh [RANK_SIZE] [DATASET]"
echo "DATASET including ['KingsCollege', 'StMarysChurch']"
echo "For example: bash run_distribute_train.sh 8 KingsCollege"
echo "It is better to use the absolute path."
echo "=============================================================================================================="
set -e

export DEVICE_NUM=$1
export RANK_SIZE=$1
export DATASET_NAME=$2
export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

BASEPATH=$(cd "`dirname $0`" || exit; pwd)
cd $BASEPATH
rm -rf ./train_parallel
mkdir ./train_parallel
cd ./train_parallel
cp $BASEPATH/../*.py .
cp -r $BASEPATH/../src/ .

env > env.log
echo "start training"
mpirun --allow-run-as-root -n $1 --output-filename log_output --merge-stderr-to-stdout \
nohup python train.py --device_num $1 \
                      --dataset $2 \
                      --is_modelarts False \
                      --run_distribute True \
                      --device_target "GPU" > train.log 2>&1 &

