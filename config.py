import os

import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

WORKSPACE_PATH = ROOT_DIR
APIMODEL_PATH = WORKSPACE_PATH +'/output/models'
ANNOTATION_PATH = WORKSPACE_PATH + '/output/annotations'
IMAGE_PATH = WORKSPACE_PATH + '/samples'
MODEL_PATH = WORKSPACE_PATH +'/output/models'
PRETRAINED_MODEL_PATH = WORKSPACE_PATH +'/pre-trained-models'
CONFIG_PATH = 'models/sign_recognition_mobnet_pipeline.config'
CHECKPOINT_PATH = MODEL_PATH