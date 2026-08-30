a = 8

b = input("Enter the number\n")
try:

    c = a/int(b)

    print(c)
except ZeroDivisionError:
    print("You can not divide the number by zero")
except ValueError:
    print("You can not divide the number by string")
except Exception as e:
    print(e)
except:
    print("Something went wrong")

