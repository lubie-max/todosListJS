# calculator for squering , cubing, sqrooting

# class calculator:
#     def __init__(self, num):
#         msg=f""" You chose {self.num} \n 
#         1. For squering Number press 1:\n
#         2. For cubing Number press 2:\n
#         3. For sqr rooting Number press 3:\n
#         """
#         print(msg)
#         user=int(input("Enter the choice:"))

#         if user==1:
#             def squr():
#                 return num**2

#         elif user==2:
#             def cude():
#                 return num**3

#         elif user==3:
#             def sqrroot():
#                 return num**0.5

#         else:
#             print("Invalid Input!")
#             exit()
                 
# if __name__ == "main":

#     c1=calculator(3)
    
def calculator():
    while (True):
        num=(int(input("Enter the number:")))
        msg=f""" You chose {num} \n 
        1. For squering Number press 1:\n
        2. For cubing Number press 2:\n
        3. For sqr rooting Number press 3:\n
        """
        print(msg)
        user=int(input("Enter the choice:"))

        if user==1:
            print(num**2)

        elif user==2:
            print(num**3)

        elif user==3:
            print(num**0.5)
        
        else:
            exit()

calculator()