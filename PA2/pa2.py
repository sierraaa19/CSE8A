#1.1: Implement a grade calculator
def grade_calculator (number_grade):
    if number_grade >= 0 and number_grade < 60:
        return "F"
    elif number_grade >= 60 and number_grade < 70:
        return "D"
    elif number_grade >= 70 and number_grade < 80:
        return "C"
    elif number_grade >= 80 and number_grade < 90:
        return "B"
    elif number_grade >= 90 and number_grade <= 100:
        return "A"
    else:
        return "Input Invalid!"
print (grade_calculator)    


#1.2: Manipulating lists
def fix_list (data):
    if data [0] < data [2]:
        return data
    elif data [0] > data [2]:
        return [data [2], data [1], data [0]]
print (fix_list)


#1.3: Implement a function that tells the number of days in a month
def days_in_month (month):
    if month == "January" or month == "March" or month == "May" or month == "July":
        return 31
    elif month =="August" or month == "October" or month =="December":
        return 31
    elif month == "April" or month == "June" or month == "September" or month == "November":
        return 30
    elif month == "February":
        return 28
print (days_in_month)


#1.4: Manipulating lists 2: sorting strings
def fix_string_list (data):
    if len (data [0]) < len(data [2]):
        return data
    elif len (data [0]) > len (data [2]):
        return [data [2], data [1], data [0]]
print (fix_string_list)
    
    
    
