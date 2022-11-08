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
  - 이때 detectron2를 인식하지 못하는 문제가 발생하면, 아래 명령어를 입력해준다.
  ```
  pip install fvcore==0.1.1.dev200512
  ```
## Dataset setting

(1) Create folder datasets/VOC2007

(2) Put Annotations and JPEGImages inside datasets/VOC2007
- download data from [google drive 1](https://drive.google.com/drive/folders/1Sr4_q0_m2f2SefoebB25Ix3N1VIAua0w)
- 위 링크 파일을 wget으로 바로 받고 싶을 경우 아래 명령어를 사용할 수 있다.
명령어로 다운 후, 다운로드된 파일명을 .zip으로 바꾸고, unzip해 준다.
```
wget --load-cookies ~/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies ~/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=16lqUlDR8WwByV0CUOaJ0o-_zNuUAmyjY' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=16lqUlDR8WwByV0CUOaJ0o-_zNuUAmyjY" -O Annotations && rm -rf ~/cookies.txt
```
```
wget --load-cookies ~/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies ~/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1I2Nx4S6XELRpYqHqqEA-R7mt3OK5DMJH' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1I2Nx4S6XELRpYqHqqEA-R7mt3OK5DMJH" -O JPEGImages.zip && rm -rf ~/cookies.txt
```

(3) Create folder datasets/VOC2007/ImageSets/Main

(4) Put the content of datasets/OWOD_imagesets inside datasets/VOC2007/ImageSets/Main


## basic command
- train
```
python tools/train_net.py --num-gpus 1 --config-file configs/OWOD/t1/t1_train.yaml SOLVER.IMS_PER_BATCH 2 SOLVER.BASE_LR 0.005
```
- evaluate
```
python tools/train_net.py --num-gpus 1 --config-file ./configs/OWOD/t1/t1_val.yaml SOLVER.IMS_PER_BATCH 2 SOLVER.BASE_LR 0.01 OWOD.TEMPERATURE 1.5 MODEL.WEIGHTS "./output/pascalVOCnSeaShips/basic01/model_final.pth"
``` 
<!-- - test
```
python tools/train_net.py --config-file configs/OWOD/t1/t1_val.yaml --eval-only MODEL.WEIGHTS output/pascalVOC/basic01/model_final.pth
``` -->

## Reference

- Base paper : Towards Open World Object Detection [[arXiv](https://arxiv.org/abs/2103.02603) | [video](https://www.youtube.com/watch?v=aB2ZFAR-OZg) | [poster](https://github.com/JosephKJ/OWOD/blob/master/ORE_poster.pdf)]
  - ### Presented at CVPR 2021 as an ORAL paper
- Base code : [github](https://github.com/JosephKJ/OWOD)
