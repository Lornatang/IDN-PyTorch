# IDN-PyTorch

## Overview

This repository contains an op-for-op PyTorch reimplementation
of [Fast and Accurate Single Image Super-Resolution via Information Distillation Network](https://arxiv.org/abs/1803.09454v1)
.

## Table of contents

- [IDN-PyTorch](#idn-pytorch)
    - [Overview](#overview)
    - [Table of contents](#table-of-contents)
    - [Download weights](#download-weights)
    - [Download datasets](#download-datasets)
    - [How Test and Train](#how-test-and-train)
        - [Test](#test)
        - [Train model](#train-model)
        - [Resume train model](#resume-train-model)
    - [Result](#result)
    - [Contributing](#contributing)
    - [Credit](#credit)
        - [Fast and Accurate Single Image Super-Resolution via Information Distillation Network](#fast-and-accurate-single-image-super-resolution-via-information-distillation-network)

## Download weights

- [Google Driver](https://drive.google.com/drive/folders/17ju2HN7Y6pyPK2CC_AqnAfTOe9_3hCQ8?usp=sharing)
- [Baidu Driver](https://pan.baidu.com/s/1yNs4rqIb004-NKEdKBJtYg?pwd=llot)

## Download datasets

Contains DIV2K, DIV8K, Flickr2K, OST, T91, Set5, Set14, BSDS100 and BSDS200, etc.

- [Google Driver](https://drive.google.com/drive/folders/1A6lzGeQrFMxPqJehK9s37ce-tPDj20mD?usp=sharing)
- [Baidu Driver](https://pan.baidu.com/s/1o-8Ty_7q6DiS3ykLU09IVg?pwd=llot)

Please refer to `README.md` in the `data` directory for the method of making a dataset.

## How Test and Train

Both training and testing only need to modify the `config.py` file.

### Test

- line 31: `upscale_factor` change to `2`.
- line 33: `mode` change to `test`.
- line 70: `model_path` change to `results/pretrained_models/IDN_x2-TB291-2096ee7f.pth.tar`.

### Train model

- line 31: `upscale_factor` change to `2`.
- line 33: `mode` change to `train`.
- line 35: `exp_name` change to `IDN_x2`.

### Resume train model

- line 31: `upscale_factor` change to `2`.
- line 33: `mode` change to `train`.
- line 35: `exp_name` change to `IDN_x2`.
- line 48: `resume` change to `samples/IDN_x2/epoch_xxx.pth.tar`.

## Result

Source of original paper results: [https://arxiv.org/pdf/1803.09454v1.pdf](https://arxiv.org/pdf/1803.09454v1.pdf)

In the following table, the psnr value in `()` indicates the result of the project, and `-` indicates no test.

| Method  | Scale |      Set5 (PSNR/SSIM)      |     Set14 (PSNR/SSIM)      |     BSD100 (PSNR/SSIM)     |    Urban100 (PSNR/SSIM)    |
|:-------:|:-----:|:--------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|
|   IDN   |   2   | 37.83(**-**)/0.9600(**-**) | 33.30(**-**)/0.9148(**-**) | 32.08(**-**)/0.8985(**-**) | 31.27(**-**)/0.9196(**-**) |
|   IDN   |   3   | 34.11(**-**)/0.9253(**-**) | 29.99(**-**)/0.8354(**-**) | 28.95(**-**)/0.8013(**-**) | 27.42(**-**)/0.8359(**-**) |
|   IDN   |   4   | 31.82(**-**)/0.8903(**-**) | 28.25(**-**)/0.7730(**-**) | 27.41(**-**)/0.7297(**-**) | 25.41(**-**)/0.7632(**-**) |

```bash
# Download `IDN_x2-TB291-2096ee7f.pth.tar` weights to `./results/pretrained_models`
# More detail see `README.md<Download weights>`
python ./inference.py --inputs_path ./figure/comic_lr.png --output_path ./figure/comic_sr.png --weights_path ./results/pretrained_models/IDN_x2-TB291-2096ee7f.pth.tar
```

Input:

<span align="center"><img width="240" height="360" src="figure/comic_lr.png"/></span>

Output:

<span align="center"><img width="240" height="360" src="figure/comic_sr.png"/></span>

```text
Build IDN model successfully.
Load IDN model weights `./results/pretrained_models/IDN_x2-TB291-c71a4860.pth.tar` successfully.
SR image save to `./figure/comic_sr.png`
```

## Contributing

If you find a bug, create a GitHub issue, or even better, submit a pull request. Similarly, if you have questions,
simply post them as GitHub issues.

I look forward to seeing what the community does with these models!

## Credit

### Fast and Accurate Single Image Super-Resolution via Information Distillation Network

_Zheng Hui, Xiumei Wang, Xinbo Gao_ <br>

**Abstract** <br>
Recently, deep convolutional neural networks (CNNs) have been demonstrated remarkable progress on single 
image super-resolution. However, as the depth and width of the networks increase, CNN-based super-resolution 
methods have been faced with the challenges of computational complexity and memory consumption in practice. 
In order to solve the above questions, we propose a deep but compact convolutional network to directly reconstruct
the high resolution image from the original low resolution image. In general, the proposed model consists 
of three parts, which are feature extraction block, stacked information distillation blocks and reconstruction 
block respectively. By combining an enhancement unit with a compression unit into a distillation block, 
the local long and short-path features can be effectively extracted. Specifically, the proposed enhancement 
unit mixes together two different types of features and the compression unit distills more useful information 
for the sequential blocks. In addition, the proposed network has the advantage of fast execution due to the 
comparatively few numbers of filters per layer and the use of group convolution. Experimental results demonstrate 
that the proposed method is superior to the state-of-the-art methods, especially in terms of time performance.

[[Paper]](https://arxiv.org/pdf/1803.09454v1.pdf)

```bibtex
@inproceedings{Hui-IDN-2018,
  title={Fast and Accurate Single Image Super-Resolution via Information Distillation Network},
  author={Hui, Zheng and Wang, Xiumei and Gao, Xinbo},
  booktitle={CVPR},
  pages = {723--731},
  year={2018}
}
```
