# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 23:14:50 2024

@author: GOKHUN
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.drawing.image import Image




parameters = pd.read_excel("parameters.xlsx")

dist = input("which distribution: ")

"""
1 ->Normal
2 ->Exp.
3 ->Poisson
4 ->Uniform
"""

if dist == "1":
    # create an array of (n) values normal distributed
    data = np.random.normal(size=parameters.iloc[1, 1], loc=parameters.iloc[3, 1], scale=parameters.iloc[4, 1])
elif dist == "2":
    # create an array of (n) values exponential distributed
    data = np.random.exponential(size=parameters.iloc[1, 1], scale=parameters.iloc[0, 1])
elif dist == "3":
    # create an array of (n) values poisson distributed
    data = np.random.poisson(lam=parameters.iloc[0, 1], size=parameters.iloc[1, 1])
elif dist == "4":
    # create an array of (n) values uniform distributed
    data = np.random.uniform(low=parameters.iloc[5, 1], high=parameters.iloc[6, 1], size=parameters.iloc[1, 1])




# create a histogram
plt.hist(data, bins=10)

# Save the plot as an image
plt.savefig("histogram.png")

# Close the plot to avoid displaying it
plt.close()




# Create a DataFrame with the generated data
df = pd.DataFrame(data, columns=["VALUES"])

# Create a workbook and add a worksheet
wb = Workbook()
ws = wb.active

# Write the DataFrame to the Excel file
for r in dataframe_to_rows(df, index=False, header=True):
    ws.append(r)

# Add the image to the worksheet
img = Image('histogram.png')
ws.add_image(img, 'D1')  # Adjust the cell reference as needed

# Save the workbook
wb.save('output.xlsx')
