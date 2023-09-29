# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 11:52:09 2023

@author: priya
"""

import os
import csv

election_data_csv = os.path.join('Resources', 'election_data.csv')

# Declaring variables and setting few of them to 0
row_count=0
candidate_list = []
candidate_dict = {}
count = 0
candidate_name = 0

# Read csv
with open(election_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    
 # Calculate total votes and votes per candidate
    for row in csvreader:
        if row[0]!=0:
            row_count = row_count + 1
                 
        candidate_name = row[2]       
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_dict[candidate_name] = 0
            
        candidate_dict[candidate_name] = candidate_dict[candidate_name] + 1     
            
                     
         # Print Output


print("Election Results")
print("...........................")
print(f"Total Votes: {row_count}")
print (f"{candidate_dict}")
   