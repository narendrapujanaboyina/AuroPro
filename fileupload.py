import os
from datetime import datetime
import pandas as pd
from tkinter import *
from tkinter import filedialog

# def open_file():
#     global inputfile
#     # filetypes = [("Excel files", "*.xlsx")]
#     # inputfile=(r"C:/Users/naren/Downloads/scratch/SSMS/SQL_Challenge_E0101.xlsx")
#     win.destroy()
#
#
# # win=Tk()
#
# # button=Button(win,text='open file',command=open_file)
# # button.pack(padx=10,pady=10)
#
# win.mainloop()
#reading input and outpu files
inputfile=(r"C:/Users/naren/Downloads/scratch/SSMS/SQL_Challenge_E0101.xlsx")
inputfile1=pd.read_excel(rf"{inputfile}")

output=r"C:/Users/naren/Downloads/scratch/SSMS/output.xlsx"

# date time in YYYYMMDDHHMMSS format
inputfile1["DataUpdatedAsOn1"] = datetime.now().strftime("%Y%m%d%H%M%S")
# date time in YYYY-MM-DD format
inputfile1["DataUpdatedAsOn2"] = datetime.now().strftime("%Y-%m-%d")
print(inputfile1.head(10))

if (os.path.exists(output)!=True):
    print("the file is created")
    inputfile1.to_excel(output,index=False,sheet_name="DailyTracker")
else:
    print("contents are being written to this file")
    with pd.ExcelWriter(output,mode="a",engine="openpyxl",if_sheet_exists="overlay") as writer:
        inputfile1.to_excel(writer, sheet_name="DailyTracker",header=None, startrow=writer.sheets["DailyTracker"].max_row,index=False)
