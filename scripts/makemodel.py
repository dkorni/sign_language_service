import tensorflow as tf
from object_detection.utils import config_util
from object_detection.builders import model_builder
from config import *

# Load pipeline config and build a detection model
configs = config_util.get_configs_from_pipeline_file(CONFIG_PATH)
detection_model = model_builder.build(model_config=configs['model'], is_training=False)

# Restore checkpoint
ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
ckpt.restore(os.path.join(CHECKPOINT_PATH, 'ckpt-101')).expect_partial()

detection_model.save(MODEL_PATH + "/model.h5")