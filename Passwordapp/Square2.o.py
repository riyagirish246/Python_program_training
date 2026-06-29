numbers = [1, 2, 3, 4, 5]
square = lambda x: x * x

squared_numbers = [square(num) for num in numbers]
print(squared_numbers)  
