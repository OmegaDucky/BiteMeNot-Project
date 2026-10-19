# BiteMeNot-Project
A computer vision project built to detect aggressive dog expressions to prevent unaware biting incidents.

# Credits
This model was trained on data originally sourced from Soumali Mukherjee27 on Kaggle (https://www.kaggle.com/datasets/soumalimukherjee27/dogs-emotion-dataset), which was later labeled and modified by OmegaDucky (GitHub) using Roboflow.

# Configurations
Please refer to file 'data.yaml'. Please change directory path accordingly for the code to function properly, or when training the model with other data.

# Prerequisites
This model was originally trained on Google Colab, running on Python 3, T4 GPU during training. The model was trained on Yolov8n from Ultralytics.

# Library
The libraries are listed as below:
 - ultralytics
 - YOLO

# Usage
Prepare training data of 3 files (Google Colab):
 - /content/bmn_training/train
 - /content/bmn_validation/valid
 - /content/data.yaml
...using the following lines:
 - '!unzip /content/train.zip -d /content/bmn_training'
 - '!unzip /content/valid.zip -d /content/bmn_validation'

# License
Distributed under the MIT License.
