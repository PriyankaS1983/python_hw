# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 11:52:09 2023

@author: priya
"""

import os
import csv

budget_data_csv = os.path.join('Resources', 'budget_data.csv')

# Declaring variables and setting few of them to 0
row_count=0
net_total=0
difference = 0
change=[]
date_change = {}
previous_value = 0
greatest_profit_increase=0
greatest_profit_decrease=0

# Read csv
with open(budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    
 # Calculate total months 
    for row in csvreader:
        if row[0]!=0:
            row_count = row_count + 1
            
 # Calculate net profit/loss               
        net_total = net_total + int(row[1])  
        
 # Calculate change in profit or loss
        if previous_value!= 0:
            difference = int(row[1]) - previous_value
            change.append(difference)
        # Reset previous_value to current row[1] value    
        previous_value = int(row[1])
        
    average_change = sum(change) / len(change)
 
 # Calculate graetest increase in profits
greatest_profit_increase = max(change)
 
 # Calculate graetest decrease in profits
greatest_profit_decrease = min(change)
      
        # Print Output
#output_path = os.path.join('Resources', 'budget_data_output.txt')

print("Financial Analysis")
print("...........................")
print(f"Total Months: {row_count}")
print(f"Total: ${net_total}")
print(f"Average change: ${average_change}")
print(f"Greatest increase in profits: ${greatest_profit_increase}")
print(f"Greatest decrease in profits: ${greatest_profit_decrease}")        