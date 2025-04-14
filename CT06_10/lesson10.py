# #recap 1

# # import random
# # somenumber = random.randint(1,15)
# # answer = input("guess a number from 1 to 15: ")
# # answer = int(answer) # convert to number from string
# # if answer == somenumber:
# #     print("thats it!")



# answer = int(input("write a number:"))
# if answer > -1:
#     print(str(answer) + "is a positive number")
# else:
#     print( str(answer) + "is a negative number")



import random
somenumber = random.randint(1,15)
answer = input("guess a number from 1 to 2: ")
answer = int(answer) # convert to number from string
if answer == somenumber:
    print("Congratulations! You did it!")
else:
    print("Oops, better luck next time!")




















