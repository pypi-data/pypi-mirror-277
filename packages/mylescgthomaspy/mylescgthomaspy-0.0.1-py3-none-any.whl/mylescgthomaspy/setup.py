# Assumes that this code file is in directory CODE_03 of the following file structure:
# ├── root directory
# │   ├── 00_INPUT
# │   ├── 01_INTERMEDIATE
# │   ├── 02_OUTPUT
# │   └── 03_CODE
# ├── .gitignore
# ├── requirements.txt
# ├── ...
# └── instructions.md
import os
SCRIPT_DIR = os.getcwd()
PARENT_DIR = os.path.dirname(SCRIPT_DIR)
INPUT_DIR = os.path.join(PARENT_DIR, "00_INPUT/")
INTER_DIR = os.path.join(PARENT_DIR, "01_INTERMEDIATE/")
OUTPUT_DIR = os.path.join(PARENT_DIR, "02_OUTPUT/")

def get_script_directory():
    return SCRIPT_DIR