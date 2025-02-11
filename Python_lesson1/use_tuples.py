filenames = ["data1.py", "data2.xls", "data3.xlsx", "data4.py", "data5.xls", "data6.xlsm"]


xls_filenames = [file for file in filenames if file.lower().endswith((".xls", ".xlsx", ".xlsm"))]
print(xls_filenames)