import csv
import pandas as pd
#import binascii
import numpy as nm

from os.path import exists
print("Type the Filename:")

input_data = input('::')

if exists(input_data):
        in_file = open(input_data,"r")
        output_str = in_file.read()
        d = output_str.split("\n")
else:
        print ("No such file found")


# for i in d:
#     print(i)
for i in d:
    with open("Data_baru.csv", "a") as out_file:
       writer = csv.writer(out_file)
       writer.writerow(nm.array(i.split(":")))        
    out_file.close()

print("Selesai Diconvert")
