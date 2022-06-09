def myfunc(principle,rate,time):
	amount=principle*(pow((1+rate/100),time))
	compound_interest=amount-principle
	return compound_interest
principle=int(input("enter the principal amount:"))
rate=int(input("enter the rate of interest:"))
time=int(input("enter the number of years:"))
compound_interest=myfunc(principle,rate,time)
print("compound interest is :{}".format(compound_interest))

