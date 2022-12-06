#regu

# import re
# txt="hello world"
# x=re.split("\s",txt)
# print(x)
# y=re.sub()



#exception handling

# from logging.config import valid_ident
# from statistics import variance


# try:
#     a=10+"hai"
#     print(a)
# except (ArithmeticError,ZeroDivisionError) :
#     print("this statement is raising an exception")
# except TypeError:
#     print("type error")
# except ValueError:
#     print("value error")
# else:
#     print("welcome")
      
# try:
#     x=10
#     print(X)
# except ArithmeticError:
#     print("an error occured")
# else:
#     ("no error")
# finally:
#     ("done")
    


# from ast import NameConstant


try:
    a=10
    print(a)
    raise NameError("hello")
except NameError as e:
    print("an exception occured")
    print(e)