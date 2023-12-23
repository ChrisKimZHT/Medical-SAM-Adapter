#!/bin/sh
echo "Input model weights path: "
read -r weights

python predict.py -net sam -mod sam_adpt -exp_name mydataset -sam_ckpt ./checkpoint/sam/sam_vit_b_01ec64.pth -image_size 1024 -out_size 256 -b 1 -dataset mydataset -data_path ./data -val_freq 1 -vis 1 -weights $weights