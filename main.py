# while 1==1:
#     print("Help I'm stuck in this loop")

# name = ""

# while len(name) == 0:
#     name = input("Enter your name: ")

# print("Hello "+name)

# name = None

# while not name:
#     name = input("Enter your name: ")

# print("Hello "+name)

# for loop a statement that will execute its block of code a limited amount of times

#while loop = unlimited
#for loop = limited


# for i in range(10):
#     print(i+1)

# for i in range(50,100+1,2):
#     print(i)

# for i in "Bro Code":
#     print(i)

# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)
# print("Happy New Year!")

# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# symbol = input("Enter a symbol to use: ")

# for i in range(rows):
#     for j in range(columns):    
#         print(symbol, end="")
#     print()

# 2D lists = a list of lists
# drinks = ["coffee","soda","tea"]
# dinner= ["bacon","rice","hambuger"]
# dessert= ["yogurt","ice cream"]

# food = [drinks,dinner,dessert]

# print(food[1][2])

# utensils = {"fork","spoon","knife"}

# for x in utensils:
#     print(x)

# dictionary 

capitals = {'USA': 'Washington DC',
            'India': 'New Dehli',
            'China':'Beijing',
            'Russia': 'Moscow'}

# print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key,value in capitals.items():
    print(key, value)










