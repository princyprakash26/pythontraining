

with open('mine.txt','r') as f:
    f.read()
    if('twinkle' in f.read()):
       print("Twinkle is  Present")
    else:
        print('twinkle is not present')