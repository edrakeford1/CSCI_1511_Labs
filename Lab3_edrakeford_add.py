"""
Program Name: Lab 3 Part 2 - Adding

Name: Elijah Drakeford

Purpose: To add items to a list that was imported from a different program

Date: January 25, 2026
"""

# import
from Lab3_edrakeford_list import camping

# adding five items to the list
camping.append('socks')
camping.append('knife')
camping.append('jacket')
camping.append('bowl')
camping.append('pot')

# reverse alphabetic order
camping.sort(reverse=True)

print(camping)

