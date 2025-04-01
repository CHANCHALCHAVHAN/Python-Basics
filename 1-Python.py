# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 08:26:22 2025

@author: sakuc
"""
def main():
    try:
        name=input("Enter employee name:")
        exprience=int(input("Enter the Exprience of the emplooyee: "))
        role=input("Enter the Role: ")
        
        #validate inputs
        exprience=validate_exprience(exprience)
        role=validate_role(role)
        
        #calculate salary
        salary=calculate_salary(exprience,role)
        
        #display results
        Display_salary(name,exprience,role,salary)
        
        
        
        