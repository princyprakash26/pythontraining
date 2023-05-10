#rename the flle name:
import os

oldname=input('enter your old filename: ')
newname=input('enter your new filename: ')

os.replace(oldname,newname)
