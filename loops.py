    #FOR LOOPS  

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
    
    
    
numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    print(number)
    
    
    
    #WHILE LOOPS
    
count = 2

while count <= 5:
    print(count)
    count += 1      #Increases the count by 1 
    
    
    
    
    
    #LOOP CONTROL STATEMENTS
    
fruits = ["apple", "pineapple", "avocado", "naartjie"]

for fruit in fruits:
    if fruit == "pineapple":
        break  #Exits the loop if pineapple is found
    print(fruit)
    
    
print()
for fruit in fruits:
    if fruit == "pineapple":
        continue  #Skips pineapple and moves to the next fruit
    print(fruit)

print()
for fruit in fruits:
    if fruit == "pineapple":
        pass  #is a placeholder, no action is needed for pineapple
    print(fruit)
    

count = 0
while count < 5:
    print(count)
    count +=1
    if count == 3:
        break  #Exits the loop when the count is reached - 3