oxford ={
    "puthagam":"Notebook",
    "jannal":"window",
    "kathavu":"door",
    "narkali":"chair"
}

key=input("Enter the key:")
if (oxford.get(key)==None):
  print ("Value is not found")
else:
 print("the value of corresponding key:",oxford.get(key)) 