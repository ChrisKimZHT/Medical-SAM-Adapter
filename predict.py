# train.py
#!/usr/bin/env	python3

""" valuate network using pytorch
    Junde Wu
"""

import os
import sys
import argparse
from datetime import datetime
from collections import OrderedDict
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.metrics import roc_auc_score, accuracy_score,confusion_matrix
import torchvision
import torchvision.transforms as transforms
from skimage import io
from torch.utils.data import DataLoader
#from dataset import *
from torch.autograd import Variable
from PIL import Image
from tensorboardX import SummaryWriter
#from models.discriminatorlayer import discriminator
from dataset import *
from conf import settings
import time
import cfg
from tqdm import tqdm
from torch.utils.data import DataLoader, random_split
from utils import *
import function


args = cfg.parse_args()
if args.dataset == 'refuge' or args.dataset == 'refuge2':
    args.data_path = '../dataset'

GPUdevice = torch.device('cuda', args.gpu_device)

net = get_network(args, args.net, use_gpu=args.gpu, gpu_device=GPUdevice, distribution = args.distributed)

'''load pretrained model'''
assert args.weights != 0
print(f'=> resuming from {args.weights}')
assert os.path.exists(args.weights)
checkpoint_file = os.path.join(args.weights)
assert os.path.exists(checkpoint_file)
loc = 'cuda:{}'.format(args.gpu_device)
checkpoint = torch.load(checkpoint_file, map_location=loc)
start_epoch = checkpoint['epoch']
best_tol = checkpoint['best_tol']

state_dict = checkpoint['state_dict']
if args.distributed != 'none':
    from collections import OrderedDict
    new_state_dict = OrderedDict()
    for k, v in state_dict.items():
        # name = k[7:] # remove `module.`
        name = 'module.' + k
        new_state_dict[name] = v
    # load params
else:
    new_state_dict = state_dict

net.load_state_dict(new_state_dict)

# args.path_helper = checkpoint['path_helper']
# logger = create_logger(args.path_helper['log_path'])
# print(f'=> loaded checkpoint {checkpoint_file} (epoch {start_epoch})')

# args.path_helper = set_log_dir('logs', args.exp_name)
# logger = create_logger(args.path_helper['log_path'])
# logger.info(args)

args.path_helper = set_log_dir('logs', args.exp_name)
logger = create_logger(args.path_helper['log_path'])
logger.info(args)

'''segmentation data'''
transform_train = transforms.Compose([
    transforms.Resize((args.image_size,args.image_size)),
    transforms.ToTensor(),
])

transform_train_seg = transforms.Compose([
    transforms.ToTensor(),
    transforms.Resize((args.image_size,args.image_size)),
])

transform_test = transforms.Compose([
    transforms.Resize((args.image_size, args.image_size)),
    transforms.ToTensor(),
])

transform_test_seg = transforms.Compose([
    transforms.ToTensor(),
    transforms.Resize((args.image_size, args.image_size)),
    
])
'''data end'''
if args.dataset == 'isic':
    print("not implemented")
    exit()
    '''isic data'''
    isic_train_dataset = ISIC2016(args, args.data_path, transform = transform_train, transform_msk= transform_train_seg, mode = 'Training')
    isic_test_dataset = ISIC2016(args, args.data_path, transform = transform_test, transform_msk= transform_test_seg, mode = 'Test')

    nice_train_loader = DataLoader(isic_train_dataset, batch_size=args.b, shuffle=True, num_workers=8, pin_memory=True)
    nice_test_loader = DataLoader(isic_test_dataset, batch_size=args.b, shuffle=False, num_workers=8, pin_memory=True)
    '''end'''

elif args.dataset == 'decathlon':
    print("not implemented")
    exit()
    nice_train_loader, nice_test_loader, transform_train, transform_val, train_list, val_list =get_decath_loader(args)


elif args.dataset == 'mydataset':
    '''mydataset'''
    mydata_predict_dataset = MyDataset(args, args.data_path, transform = transform_test, transform_msk= transform_test_seg, mode = 'predict')

    nice_predict_loader = DataLoader(mydata_predict_dataset, batch_size=args.b, shuffle=False, num_workers=8, pin_memory=True)
    '''end'''

'''begain valuation'''
best_acc = 0.0
best_tol = 1e4

if args.mod == 'sam_adpt':
    net.eval()
    function.predict_sam(args, nice_predict_loader, start_epoch, net)


