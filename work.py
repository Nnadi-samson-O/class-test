from audioop import avg
from tabnanny import check
from tkinter import Y


# x = 2 + 3

# y = 8

# z = x * y

#name = "onyebuchi"
#print(z)
#print(name)
#print(type(name))
#print(type(x))
 
#print(type([5, 6]))

#print(type({'a':'john', 'b':20}))

#def square(x):
    #x = 5
    #print(x * x)
#square(x)

#def exponet(x, y):
   
    #print(x ** y) 
#exponet(2, 3)
#print(name[:])
#print(len(name))

#scors = [1, 2, 3, 4, 5, 6, 7]
#print(scors[::1])

# #x = 1
# while x <= 10:
#     print(x)
#     x = x + 1

# for x in range(8):
#     print(x)

# def my_sum(x, y):
#     print(x+y)
# my_sum(1012, 10012)

# def my_sum(x, y):
#     return x+y
# x = my_sum(3, 5)
# print(x)

# def is_even(x):
#     if x % 2 == 0:
#         return True

#     else:
#         return False
# print(is_even(9))

# def is_old(y):
#     if y % 2 == 1:
#         return True
#     else:
#         return False
# print(is_old(9))

# def is_prime(x):
#     if x / 2 == 0:


# def add_list(x): 
#     ans = 0

#     for i in x:
#         ans = ans + i

#     return ans

    
# print(add_list([11, 12, 30, 44]))

# def avg(x):
#     return add_list(x) / len(x)
# print(avg([11, 12, 30, 44]))

file_name = input("Enter name for the file.\n")
if file_name: # means same thing as 'if file_name != "" '
    new_text = input(f"Enter text to be stored in {file_name} and press enter when done:\n")

    file_open = open(file_name, "a")
    file_open.write(new_text)
    file_open.close()

    with open(file_name) as new_file:
        text = new_file.read()
        
        print(f"\nThe text in {file_name} has {len(text)} \
            characters in it.\nHere is the text itself:\n{text}\n")
else:
    print("Come, Oga! Just enter a valid file name next time. Mtschew!!!")