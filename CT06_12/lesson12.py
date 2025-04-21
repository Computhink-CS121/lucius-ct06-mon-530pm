from tkinter import Variable


# print("Hello from lesson 12")
# recap 
# ask this word must contain at least 1 "0"




# e.g




# word = "something"
# for letter in word:
#     print(letter)

# word = input("give me a 5 letter word")
# contains_o = False
# contains_i = False
# for letter in word:
#     print(letter)
#     if letter == "o":
#         contains_o = True
#     elif letter == "e":
#         contains_e = True


# if not(contains_e or contains_o):
#     print("invalid word")
# else:
#     print("good word: " + word)


# counter = 0
# while counter < 50:
#     increase 

# order = ""
# answer = input("what is your order? ")
# while not answer == "":
# #inside the loop
#     order = order + answer + ", "
#     answer = input("what is your order?")


# print("you have ordered these items:")
# print(order)


# import random
# for count in range(5):
#     number1 = random.randint(1,10)
#     number2 = random.randint(1,10)
#     answer = input("what is 5+3?")
#     question = "what is " + str(number1) + "+" + str(number2) + "?"
#     answer = input(question)
#     answer = int(answer)
#     hidden_answer = number1 + number2
#     while not answer == hidden_answer:
#         print("wrong! Try again")
#         answer = input(question)
#         answer = int(answer)#convert to a number
#     else:
#         print("you are correct!")


import random
num = 0
while not num == 4:
    num = random.randint(1, 6)
    if num == 4: 
        print("Number is 4")
        break
else:
    print("end of loop bcos of number 4")
















































































































































































































































































































