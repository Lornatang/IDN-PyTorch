# Copyright 2022 Dakewe Biotech Corporation. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
import random

import numpy as np
import torch
from torch.backends import cudnn

# Random seed to maintain reproducible results
random.seed(0)
torch.manual_seed(0)
np.random.seed(0)
# Use GPU for training by default
device = torch.device("cuda", 0)
# Turning on when the image size does not change during training can speed up training
cudnn.benchmark = True
# When evaluating the performance of the SR model, whether to verify only the Y channel image data
only_test_y_channel = True
# Image magnification factor
upscale_factor = 2
# Current configuration parameter method
mode = "train"
# Experiment name, easy to save weights and log files
exp_name = "IDN_x2"

if mode == "train":
    # Dataset address
    train_image_dir = "./data/TB291/IDN/train"
    test_lr_image_dir = f"./data/Set5/LRbicx{upscale_factor}"
    test_hr_image_dir = f"./data/Set5/GTmod12"

    image_size = 72
    batch_size = 64
    num_workers = 4

    # Incremental training and migration training
    resume = ""

    # Total num epochs (600,000 iters)
    epochs = 406

    # Optimizer parameter
    model_lr = 1e-4
    model_betas = (0.9, 0.999)
    model_weight_decay = 1e-4

    # Dynamically adjust the learning rate policy (250,000 iters)
    lr_scheduler_milestones = [int(epochs * 0.4), int(epochs * 0.8)]
    lr_scheduler_gamma = 0.1

    # How many iterations to print the training result
    print_frequency = 200

if mode == "test":
    # Test data address
    lr_dir = f"./data/Set5/LRbicx{upscale_factor}"
    sr_dir = f"./results/test/{exp_name}"
    hr_dir = f"./data/Set5/GTmod12"

    model_path = "./results/pretrained_models/IDN_x2-TB291-2096ee7f.pth.tar"
