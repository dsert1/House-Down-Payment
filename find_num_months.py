## 6.0001 Pset 1: Part a 
## Name: Deniz Sert
## Time Spent: 45 min
## Collaborators: Miles Kaming-Thanassi

##########################################################################
## Get user input for annual_salary, portion_saved and total_cost below ##
##########################################################################
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the portion of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))




#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
months = 0
current_savings = 0
r = .05


###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################

while(current_savings<total_cost*.12):
    #increases current saving by ROI and annual salary portion saved
    current_savings+=current_savings*r/12
    current_savings+=annual_salary*portion_saved/12
    
    #increments number of months
    months+=1
    
    
print("Number of months: ", months)
