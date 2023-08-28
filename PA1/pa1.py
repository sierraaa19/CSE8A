def fahrenheit_to_celsius (temp_in_fahren):
	celcius = (temp_in_fahren - 32) * 5/9
	return celcius

def celsius_to_fahrenheit (temp_in_c):
        fahrenheit = (temp_in_c * 9/5) + 32
        return fahrenheit

temp_in_f_str = "Enter temperature in fahrenheit:"
temp_in_f = float(input("Enter temperature in fahrenheit:"))
temp_in_c = fahrenheit_to_celsius (temp_in_f)
print ('Temprature in celcius =', temp_in_c)

temp_back = temp_in_c
temp_return = celsius_to_fahrenheit (temp_back)
print ('Temperature converted back to Fahrenheit =', temp_return)
