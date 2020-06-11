#COSC.151.100
#Spring 2020
#James E Fitzgerald III
#March 9,2020

#The user will enter their first name with a capital first letter.

first_name = input('Please enter your first name:'  )
print(first_name.capitalize())

#The user will enter their last name with a capital first letter.

last_name = input('Please enter your last name:'  )
print(last_name.capitalize())

# The user will enter their current age.

current_age = int(input('Please enter your current age:'))

#The user will enter today's date in the month.day.year format.

todays_date = input('Please enter the current date in month.day.year:  ')
#The user will enter their desired hourly salary.

hourly_salary = float(input('Please enter your desired hourly salary:  '))


# The amount of money the user wants to make multiplied by 80 hours;The amount of money the user wants to make multiplied by 80 hours multipled by 26 weeks


print('Thank you:',first_name,last_name,'You are in a great positon for your',current_age,'Lets review your pay starting with',todays_date,'Your pay after 80 hours worked:',hourly_salary * 80,'Based on these numbers you will have an annual salary of',hourly_salary * 80 * 26)



