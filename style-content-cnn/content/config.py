import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '../dataset/')

CLASS_LIST = ["all_ills", "beach", "building_facade", "forest", "formal_garden", "highway", "lake",
              "ruin", "ski_slope", "street", "valley"]

CLASS_COUNT = len(CLASS_LIST)

''' TRAIN '''
BATCH_SIZE = 64
EPOCH_COUNT = 100
SAVE_PERIOD_IN_EPOCHS = 2
LOG_STEP = 1
LEARNING_RATE = 1e-4
NUM_WORKERS = 16

USE_PATCH = 1
PATCH_SIZE = 100

# model save dir
PYTORCH_MODELS = "./models/Content/"

LOAD_TRAINED_MODEL = 0  # continue train from a ckpt

# train dataset
train_dir_path = './dataset_content/train'
train_path = train_dir_path + "/"

# test data
test_dir_path = './dataset_content/test/'
test_path = test_dir_path + 'makato/' # you may need to change this illustrator

# test model name
MODEL_NAME = "content_model-99.pkl"
