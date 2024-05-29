# a = "hi parth dont worry you will get a girlfriend don,t stress too much"
# # for i in a:
# #     print(i)
# print(len(a))


# a = int(input("enter a no: "))
# if (a>0):
#     print("no is positive")
# elif (a==0):
#     print("no is zero")
# else:
#     print("no is negative")

# import time
# name= input("enter your name: ")
# timestamp = int(time.strftime('%H'))
# if (timestamp<12):
#     print("good morning",name)
# elif (timestamp>12):
#     print("good evening",name)
# else:
#     print("good afternoon sir",name)

# input ("what can i do for you today  ")

# x = int(input("enter your age: "))
# match x:
#     case _ if x>18:
#         print("you can vote")
#     case _ if x<18:
#         print("you can't vote")
#     case _ if x==18:
#         print("you can vote")

# a = int(input("enter a no:  "))

# reversed_num=0

# while a>0:
#     d=a%10
#     reversed_num=reversed_num*10 + d
#     a=a//10
# print(reversed_num)

a = int(input("enter a no:  "))
product = 1
while a>0:
    d=a%10
    product = product * d
    a=a//10
print(product)