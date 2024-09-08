import math

name = "Josef Corbin"
age = 24
height = 6.17
favorite_color = "Purple"

print(name)
print(age)
print(height)
print(favorite_color)

print(name, age, height, favorite_color)

print("Hello, my name is {name}, and I am {age} years old. My favorite color is {favorite_color}, and I am {height} feet tall!")

print(f"""
Name: {name}
Age: {age}
Height: {height}
Favorite Color: {favorite_color}
""")

print(f"""      
      Name: {name}
Age: {age}
Height: {height}
Favorite Color: {favorite_color}
""")

circle_area = math.pi*5**2
print(round(circle_area, 1))

root_age = math.sqrt(age)
print(round(root_age, 3))

sin_height = math.sin(height)
cos_height = math.cos(height)
print(round(sin_height , 3) , round(cos_height , 3))

age_sum = age + 5
height_difference = height - 4
age_height_product = age * height
height_quotient = height/2
age_remainder = age % 3
age_squared = age**2
print(f"""
My age plus 5 equals: {age_sum}
My height minus 4 equals: {height_difference}
My age multiplied by my height equals: {age_height_product}
One half my height equals: {height_quotient}
My age mod 3 equals: {age_remainder}
My age squared equals: {age_squared}
""")

user_temperature = float(input("Please enter a temperature in Fahrenheit: "))
degree_sign = u'\N{DEGREE SIGN}'
converted_temperature = round((user_temperature-32)*(5/9), 0)
print(f"{user_temperature} in Celcius = {converted_temperature}{degree_sign}")