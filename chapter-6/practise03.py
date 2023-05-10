spamwords=['click here','subscribe now','buy now']

mail=input('enter your mail:').lower()
spam=False

if 'click here' in mail:
    spam=True
if 'buynow' in mail:
    spam=True
if 'subscribe now' in mail:
    spam=True
    


print('spam is:',spam)


