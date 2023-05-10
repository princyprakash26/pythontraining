

try:
    print("Hello world")
    a=int(input("Enter a number:"))
    b=int(input("Enter the another number:"))
    c=(a/b)
   
except ValueError:
    print("Value error occurred")
except ZeroDivisionError:
    c='infinite'
except Exception as e:
    print(f"This print occurred:{e}")

print(c)