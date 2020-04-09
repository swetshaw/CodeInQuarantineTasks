# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 22:40:29 2020

@author: Sweta Shaw
"""

import pandas as pd

df_marks = pd.read_csv("marksheet.csv")
marks_list = list(df_marks['Marks'])
marks_set = set(marks_list)
sorted_marks = sorted(marks_set, reverse=True)

while True:
    tie = 0
    print("Enter your Roll No.")
    input_roll = input()
    
    if(input_roll=="stop"):
        break
    else:

        data = df_marks.loc[df_marks['Roll No'] == int(input_roll)]
    
        marks = list(data['Marks'])
        print("Marks: {}".format(marks[0]))

    #Rank
    for i in range(len(sorted_marks)):
        if sorted_marks[i] == marks[0]:
            rank = i+1
            print("Rank:{}".format(rank))        

    #tie
    for item in marks_list:
        if item == marks[0]:
            tie += 1
    print("Tied between: {}\n\n".format(tie))



        
