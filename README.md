# VBACPrediction
Code for the VBAC Prediction Logistic Regression &amp; GBDT models that achieve cutting-edge AUC without using race.

# Getting started
You can use the already-preprocessed dataset, ```2019_vbac_data.csv```, or you can start from scratch.

To start from scratch:

1. Download & unzip the 2019 birth dataset from https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm.
2. Move the unzipped .txt file to the same repository as ```load_vbac_data.py``` and ```features.py```.
3. Run ```python3 load_vbac_data.py```. This file filters the dataset on TOLACs (in the dataset, TOLAC indicates failure) and VBACs (successes) and extracts just the features we want.
4. Find the outputted dataset in ```2019_vbac_data.csv```.
