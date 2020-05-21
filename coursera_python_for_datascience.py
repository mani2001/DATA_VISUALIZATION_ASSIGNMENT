# -*- coding: utf-8 -*-
"""
Created on Wed May 20 22:54:52 2020

@author: manikantan
"""
#this program runs frequency distributions on the variables MORPHOLOGY_EJECTA_1\2\3 and the number of layers so that it can further be analysed with the other variables to see if there is a connection

#import necessary libraries
import numpy as np
import pandas as pd
print("reading the mars_crater csv file...")
data = pd.read_csv("D:\mars_craters.csv")
print("removing rows which do not have a value for Morphology ejecta 1 (i.e. NA)...")
dataset = data[data.MORPHOLOGY_EJECTA_1!=" "]
print("value counts for the different types of ejecta 1 data for the existing cases")
ME_1 = dataset["MORPHOLOGY_EJECTA_1"].value_counts(sort=False)
print(ME_1.head())

print("\n\npercentage values of different types of ejecta")
percentage_ME_1 = ME_1*100/len(dataset["MORPHOLOGY_EJECTA_1"])
with pd.option_context('display.max_rows',None):
    print(percentage_ME_1)
    
print("\n\nvalue counts for ejecta 2")
print("\nremoving NA\empty values of the dataset for morphology ejecta 2")
dataset_2 = data[data.MORPHOLOGY_EJECTA_2!=" "]
ME_2 = dataset_2["MORPHOLOGY_EJECTA_2"].value_counts(sort=False)
print(len(ME_2))
print(ME_2)

print("\n\npercentage values of different types of ejecta '2' classification")

percentage_ME_2 = ME_2*100/len(dataset["MORPHOLOGY_EJECTA_2"])
with pd.option_context('display.max_rows',None):
    print(percentage_ME_2)
    
print("\n\nvalue counts for ejecta 3")
print("\nremoving NA\empty values of the dataset for morphology ejecta 3")
dataset_3 = data[data.MORPHOLOGY_EJECTA_3!=" "]
ME_3 = dataset_3["MORPHOLOGY_EJECTA_3"].value_counts(sort=False)
print(len(ME_3))
print(ME_3)

print("\n\npercentage values of different types of ejecta '3' classification")

percentage_ME_3 = ME_3*100/len(dataset_3["MORPHOLOGY_EJECTA_3"])
with pd.option_context('display.max_rows',None):
    print(percentage_ME_3)
    
