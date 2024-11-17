# Style_Transfer

This project implements Neural Style Transfer (NST) using PyTorch. Neural Style Transfer is a technique for blending two images—a content image and a style image—to generate a new image that maintains the content of the content image while adopting the style of the style image.

## Website URL

Local URL: http://localhost:8501
         or
Network URL: http://10.8.219.62:8501
       

## Key Features
- Implemented using PyTorch for flexibility and efficiency.
- Pre-trained VGG19 model is used for feature extraction.
- Support for multiple style images and content images.
- Adjustable style-content ratio for fine-tuning results.
- Efficient optimization using Adam optimizers.

## Table of Contents

Installation

Argumants

Examples


## Installation

```
pip install pytorch torchvision

pip install streamlit

pip install PIL

```


## Arguments

- --content: Path to the content image.

- --style: Path to the style image.

- --output: Path to save the generated image.

## Examples

![amber](https://github.com/user-attachments/assets/b1d2a439-66b4-4888-b071-793aa283d5d6)

![rain_princess](https://github.com/user-attachments/assets/88f70c12-3cb5-44f0-a072-315f3c8d8c72)

![stylized-amber-rain_princess](https://github.com/user-attachments/assets/78dfc823-f6c1-469f-ace0-1c91de61a449)

## Acknowledgment

- The implementation is inspired by PyTorch NST Tutorial.
  
- Pre-trained VGG19 model is provided by torchvision/kaggle.
