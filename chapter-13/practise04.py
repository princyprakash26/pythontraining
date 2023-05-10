#filter a list of numbers which are divisible by 5
def list_of_numbers(n):
    if n%5==0:
        return True
    return False

a=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(list_of_numbers,a)))