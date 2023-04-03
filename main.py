import os
from datetime import datetime
import time
import pandas as pd

df = pd.read_excel(r"C:/Users/naren/Downloads/scratch/SSMS/SQL_Challenge_E0101.xlsx")

for i in range(1,6):
    t=[datetime.now().strftime("%y:%m:%d:%H:%M:%S") for i in df.index]
    if os.path.exists(r"C:/Users/naren/Downloads/scratch/SSMS/output.xlsx"):
        df['currenttime'+str(i)]=t
        df.to_excel(r'C:/Users/naren/Downloads/scratch/SSMS/output.xlsx')
    else:
        df['currenttime' + str(i)] = t
        df.to_excel(r'C:/Users/naren/Downloads/scratch/SSMS/output.xlsx')
    time.sleep(5)








