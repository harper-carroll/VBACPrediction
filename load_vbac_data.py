
import pandas as pd
import numpy as np
import os
import torch

from features import FEATURES_TO_USE, REPORTING_FLAGS

# Load data 
# Download 2019 dataset from https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm 
data = open("2019_birth_data.txt", "r")
parsed_data = open("2019_birth_data_parsed.csv", "w")

lines = data.readlines()

for line in lines:
	feats = ""
	skip = False
	for feature, index_list in FEATURES_TO_USE.items():
		if skip: 
			continue
		empty = False # Is this feature empty / null?
		for index in index_list:
			if empty or skip:
				continue 
			value = line[index-1]
			if feature == "MARITAL_STATUS" and value == ' ':
				empty = True
				continue
			if feature in REPORTING_FLAGS:
				reporting_flag = REPORTING_FLAGS[feature]
				if reporting_flag == 0 or reporting_flag == ' ' or reporting_flag == '':
					empty = True
					continue
			if feature == "PREVIOUS_CESAREAN" and value == 'N':
				skip = True
			elif feature == "DELIVERY_METHOD_1" and value != -1 and int(value) != 2 and int(value) != 4:
				skip = True
			else:
				feats = feats + str(value)
		if empty: 
			feats = feats + '-1'
		feats = feats + ','

	if not skip:
		parsed_data.write(feats[:-1])
		parsed_data.write('\n')

data.close()
parsed_data.close()


count_no, count_yes = 0, 0
parsed_data = open("2019_birth_data_parsed.csv", "r")
vbac_only_data = open("2019_vbac_data.csv", "w")
data_lines = parsed_data.readlines()
for d_line in data_lines:
	d_line_list = d_line.strip().split(',')
	TOL_ATTEMPTED, DELIVERY_METHOD_1, DELIVERY_METHOD_2 = d_line_list[-3:]
	if int(DELIVERY_METHOD_1) == 2 or int(DELIVERY_METHOD_2) == 1:  
		d_line_list.append('1')
		count_yes += 1
	elif (int(DELIVERY_METHOD_1) == 4 or int(DELIVERY_METHOD_2) == 2) and TOL_ATTEMPTED == 'Y':
		count_no += 1
		d_line_list.append('0')
	else:
		continue
	if len(d_line_list) != 43: continue
	for i, item in enumerate(d_line_list):
		if item == ' ': 
			print("error")   # error here?
			item = 0
		if item == 'N' or item == 'M':
			item = 0
		if item == 'Y' or item == 'F':
			item = 1
		if item == "U" or item == "X":
			item = -1
		d_line_list[i] = str(float(item))

	vbac_only_data.write(','.join(d_line_list))
	vbac_only_data.write('\n')

print(count_no, count_yes)
