## 6.0001 Pset 1: Part c
## Name: Deniz Sert
## Time Spent: 1 hr
## Collaborators: Miles Thaming-Thanassi

#r, steps!!

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter your initial deposit: "))
number_of_months = 0
#epsilon = 100


total_cost = 750000
down_payment_percentage = .3





#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################


#if r>=max:
#    max = r
#    min = 0
#else:
#    min = r
#    max = 1.0
current_savings = initial_deposit
########################################################################################################
## Determine the lowest return on investment needed to get the down payment for your dream home below ## 
########################################################################################################

#initializes variables
r = 0.0
high = 1.0
low = r
steps = 0

#BISECTION SEARCH
while abs(current_savings-750000*.3) >= 100:
    
    if (current_savings>750000*.3):
        high = r
    else:
        low = r
    #r is assigned to midpoint
    r = (high+low)/2.0    
    current_savings = initial_deposit * (1+r/12)**36
    steps+=1
    
    #if it is not possible to save within $100 of down payment
    #r is assigned None
    if (steps>100):
        r = None
        break

    
    
print("Best savings rate: ", r)
print("Steps in bisection search: ", steps)