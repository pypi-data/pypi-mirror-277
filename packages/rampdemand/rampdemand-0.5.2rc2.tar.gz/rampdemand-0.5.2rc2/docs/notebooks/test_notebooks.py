# import nbformat
# from nbconvert.preprocessors import ExecutePreprocessor
#
# notebook_filename="thermal_app.ipynb"
# with open(notebook_filename) as f:
#     nb = nbformat.read(f, as_version=4)
#
# ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
# try:
#     ep.preprocess(nb, {'metadata': {'path': '.'}})
# except:
#     print("some fuckup")
from ramp import User, Appliance, UseCase, get_day_type
import pandas as pd

# loading data

use_case = UseCase()  # creating a new UseCase instance
use_case.load("example_excel_usecase.xlsx")

use_case.date_start = "2020-01-01"
use_case.initialize(num_days=30)
use_case.generate_daily_load_profiles()
