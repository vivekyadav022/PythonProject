letter='''Dea Vivek Yadav
you are selected!
Date:01/02/2023
'''
name=input("Enter your name\n")
date=("Enter your date\n")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)
