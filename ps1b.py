## 6.0001 Pset 1: Part b
## Name: Deniz Sert
## Time Spent: 10 minutes
## Collaborators: None

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the portion of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual rause, as a decimal: "))




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
    #every 6 months, annual salary is increased by semi_annual_raise percentage
    if months%6 == 0:
        annual_salary+=semi_annual_raise*annual_salary
    
    
print("Number of months: ", months)