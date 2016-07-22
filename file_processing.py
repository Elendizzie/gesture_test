__author__ = "Shuran Zhou @ Mobvoi"

import numpy as np
import json
import os

#Import and preprocess all the .dat files


dir_path = '/home/mobvoi/sensor_raw_data'
file_name = 'flip_up.dat'
PATH = os.path.join(dir_path, file_name)


data = []
with open(PATH) as f:
    for line in f:
        data.append(json.loads(line))
        jtopy = json.loads(line)
        print type(jtopy['data'])

print len(data)