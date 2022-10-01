from calendar import month
from datetime import date




def get_dob():
	  
    y = int(input("please enter your birth year: "))
    m = int(input("please enter your birth month: "))
    d = int(input("please enter your birth day: "))
    dob = date(y, m, d)
    return dob
    
    # # write code here

	# global dob

	# yr,mont,dy= map(int,input("Enter year ,month ,day separated by spaces = ").split())
	# dob=date(yr,mont,dy)
	# print(dob)
	
	
    # da=datetime.(y,m,day)

def get_age(dob):

	curentdate=date.today()
	age= (curentdate - dob)

	# print(age)
	return age
    # write code here
	
	
    
    # return age_in_days 

def main():
	
    dob = get_dob()
    t = date.today()
    age = int((t - dob).days / 365)
    if dob < t:
        print(f"Your age is:,{age}")
    else:
        print("error")


if __name__ == '__main__':
    main()
