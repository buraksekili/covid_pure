import os
from pathlib import Path

BASE_DIR = os.getcwd()
TRAINING_DATA_DIR =  os.path.join(os.path.dirname(BASE_DIR) + '\\COVID_PURE_DATA\\training')
EVALUATION_DATA_DIR =  os.path.join(os.path.dirname(BASE_DIR) + '\\COVID_PURE_DATA\\evaluation')