def function():
    try:
        a=int(input("Enter a number:"))
        b=int(input("Enter the another number:"))
        print(a/b)
        return a/b
    except Exception as e:
        print(f"This problem occurred: {e}")
        return 0
    finally:       
        print("I will always be executed")
    
    
    # print("I will be always executed.")


print(__name__)
if __name__=="__main__":
    function()
    print("Main")