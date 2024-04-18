# ***** To run this project, plz make sure the following packages are installed:
# pip install opencv-python
# pip install tensorflow
# pip install keras
# pip install pathlib
# pip install split-folders
import numpy as np
import pandas as pd
import os

for dirname, _, filenames in os.walk('Rice_Image_Dataset'):
    for filename in filenames:
        print(os.path.join(dirname, filename))