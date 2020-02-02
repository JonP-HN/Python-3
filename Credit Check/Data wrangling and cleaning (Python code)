# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 15:37:27 2019

@author: herna
"""

f_input	= open("check_credit.txt",'r')
f_output = open("check_credit.txt-clean-data.csv",	'w')
for	line in	f_input:				
    if '?' not	in line:			
        new_output_line	= line.replace(";" , ",")								
        f_output.write(new_output_line)
f_input.close()
f_output.close()
print("End	processing")
