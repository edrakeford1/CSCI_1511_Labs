"""
Program Name: Restaurant Tip Calculator

Name: Elijah Drakeford

Purpose: This program prompts the user to enter the total amount of a dinner bill. It then calculates both a 15% and a 20% tip based on the entered amount.
Finally, the program displays the total amounts including each of the suggested tips.

Date: January 25, 2026
"""

dinner_bill = float(input("\nEnter the amount of the dinner bill ($): "))
tip_15 = 0.15 * dinner_bill
tip_20 = 0.20 * dinner_bill
dinner_tip15 = dinner_bill + tip_15
dinner_tip20 = dinner_bill + tip_20
suggested_tips = f"\nSuggested tips: \n15%: ${tip_15:.2f} \n20%: ${tip_20:.2f}"
plus_tip = f"\nTotal Amount: \nIncluding 15% tip: ${dinner_tip15:.2f} \nIncluding 20% tip: ${dinner_tip20:.2f}\n"
print(suggested_tips)
print(plus_tip)
