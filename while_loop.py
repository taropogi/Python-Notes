# while loop in Python  
# A while loop repeatedly executes a block of code as long as a specified condition is true.

# Basic while loop
count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1  # Increment count to avoid infinite loop
print("Finished counting!")

#break, continue and pass
#break statement, this exits the loop
num = 0 
while True:
    if num == 3:
        print("Breaking the loop at num =", num)
        break  # Exit the loop when num is 3
    print(f"Num is: {num}")
    num += 1

# pass statement, this does nothing, it's just a placeholder
i = 0
while i < 5:
    if i == 2:
        pass  # Do nothing when i is 2
    else:
        print(f"i is: {i}")
    i += 1

# continue statement, this skips the current iteration and moves to the next one
j = 0
while j < 5:    
    j += 1
    if j == 3:
        print("Skipping number 3")
        continue  # Skip the rest of the loop when j is 3
    print(f"j is: {j}")