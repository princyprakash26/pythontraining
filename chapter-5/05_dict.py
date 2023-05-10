#dictionaries and set.

oxford = {
    "keys":"are equal to 'value'",
    "mylist":[2,3,5,6],
    "marks":"if you work hard you will pass",
    "youtube":"it is the platform sharing videos."
}
#1.
# # print(oxford["keys"])
# print(oxford.items())

# for a, b in oxford.items():
#          print(a ,"=", b)
#2.dictionary methods:


for key in oxford.keys():
  print(key)
print(oxford.keys())


#3.get

# print(oxford.get("marks"))
# print(oxford.get("smark"))#by using this term the code can't throw any error if has no value.