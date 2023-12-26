#!/bin/sh
python train.py -net sam -mod sam_adpt -exp_name mydataset -sam_ckpt ./checkpoint/sam/sam_vit_b_01ec64.pth -image_size 1024 -out_size 256 -b 1 -dataset mydataset -data_path ./data -val_freq 5 -vis 100
