# !usr/bin/env python
# -*- coding:utf-8 -*-

'''
 Description  : 
 Version      : 1.0
 Author       : MrYXJ
 Mail         : yxj2017@gmail.com
 Github       : https://github.com/MrYxJ
 Date         : 2023-09-03 11:21:30
 LastEditTime : 2023-09-05 23:17:59
 Copyright (C) 2023 mryxj. All rights reserved.
'''

from calflops import calculate_flops_hf

batch_size = 1
max_seq_length = 128
model_name = "baichuan-inc/Baichuan-13B-Chat"
flops, macs, params = calculate_flops_hf(model_name=model_name,
                                         input_shape=(batch_size, max_seq_length))

print("%s FLOPs:%s  MACs:%s  Params:%s \n" %(model_name, flops, macs, params))


