## How to start
- This instruction is based on python 3.9, cuda 11.3
- install pytorch, torchvision  
예시)
```
pip3 install torch==1.8.2 torchvision==0.9.2 torchaudio==0.8.2 --extra-index-url https://download.pytorch.org/whl/lts/1.8/cu111\
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
  - https://github.com/facebookresearch/detectron2/releases  
  예시)
  ```
  python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'
  python -m pip install -e ./
  ```

## Dataset setting

(1) Create folder datasets/VOC2007

(2) Put Annotations and JPEGImages inside datasets/VOC2007
- download data from [google drive 1](https://drive.google.com/drive/folders/1Sr4_q0_m2f2SefoebB25Ix3N1VIAua0w), [google drive 2](https://drive.google.com/file/d/1TdBylqdZ9VjEitW0pondNRqG2AhDirx_/view?usp=sharing)

(3) Create folder datasets/VOC2007/ImageSets/Main

(4) Put the content of datasets/OWOD_imagesets inside datasets/VOC2007/ImageSets/Main

## Reference

- Base paper : Towards Open World Object Detection [[arXiv](https://arxiv.org/abs/2103.02603) | [video](https://www.youtube.com/watch?v=aB2ZFAR-OZg) | [poster](https://github.com/JosephKJ/OWOD/blob/master/ORE_poster.pdf)]
  - ### Presented at CVPR 2021 as an ORAL paper
- Base code : [github](https://github.com/JosephKJ/OWOD)
