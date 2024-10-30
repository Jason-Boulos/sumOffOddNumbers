selected_number = int(input("Please enter an integer: "))
sum = 0

for i in range(selected_number):
    if(i % 2 != 0):
         sum += i
         print(f"{i} is an ODD number ")
    
print(f"some of these ODD numbers is equal to {sum}")

      
       
