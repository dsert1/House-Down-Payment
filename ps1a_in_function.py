def part_a(annual_salary, portion_saved, total_cost):
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
	return months