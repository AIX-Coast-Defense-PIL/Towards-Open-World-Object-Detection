## Base paper
- Towards Open World Object Detection [[arXiv](https://arxiv.org/abs/2103.02603) | [video](https://www.youtube.com/watch?v=aB2ZFAR-OZg) | [poster](https://github.com/JosephKJ/OWOD/blob/master/ORE_poster.pdf)]
  - ### Presented at CVPR 2021 as an ORAL paper

## How to start
- python version : 3.6
- install pytorch, torchvision  
예시)
```
pip3 install torch==1.6.0 torchvision==0.7.0 --extra-index-url https://download.pytorch.org/whl/lts/1.8/cu111
```
- install requirements.txt
```
pip install -r requirements.txt
```
  - if there ir error on installing fvcore, use this command
  ```
  pip install -U 'git+https://github.com/facebookresearch/fvcore'
  ```
- install detectorn2
  - linux : https://github.com/facebookresearch/detectron2/releases  
  예시)
  ```
  python -m pip install detectron2==0.6 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu113/torch1.10/index.html
  ```

## Dataset setting

(1) Create folder datasets/VOC2007

(2) Put Annotations and JPEGImages inside datasets/VOC2007
- download data from [google drive 1](https://drive.google.com/drive/folders/1Sr4_q0_m2f2SefoebB25Ix3N1VIAua0w), [google drive 2](https://drive.google.com/file/d/1TdBylqdZ9VjEitW0pondNRqG2AhDirx_/view?usp=sharing)

(3) Create folder datasets/VOC2007/ImageSets/Main

(4) Put the content of datasets/OWOD_imagesets inside datasets/VOC2007/ImageSets/Main