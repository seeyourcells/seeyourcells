# Requirements
Python 3.6, CUDA 10.0, cudnn 10.0 and other common packages listed in `requirements.txt`.

# Installation
### 1. Install dependencies 
``` pip install -r requirements.txt```

### 2. Run setup from the repository root directory
``` python setup.py build_ext --inplace ```
``` pip install . ```

### 3. Download yolo.weights
download data from https://drive.google.com/file/d/1Jm8lbFcMMo-RhTBJtrOxCU-Uc1EfmihW 

all model data from https://drive.google.com/drive/folders/1gvT8Oiub-JPbvAztieHM3uS2g4uh7MiZ

### 4. Make directory
Make **/bin** directory from root and put the weights file into the bin.
Please rename **yolov3.weights** to **yolo.weights**.

