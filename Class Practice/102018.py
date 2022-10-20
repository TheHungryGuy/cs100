msg = "hello World!"

print(msg[1:7])     #outputs only 1-7 not including 7
print(msg.capitalize()) #outputs strings with first letter capitalized
print(msg.startswith("he")) #checks if the message starts with given str
print(msg.startswith("HE")) #capitalization matters
print(msg.count("l"))   #counts how many times string appears
print(msg.count("ello"))   
print(msg.split())  #splits string into list (default delimter at whitespace)
print(msg.split(',')) #changes delimeter from default to set value

print("732-710-2170".split("-"))
print("732-710-2170".strip("-")) 

import string
print(string.punctuation)   #lists all punctation 
print("732-710-2170".split(string.punctuation))

print("732-710-2170".replace("-""",""))

print(1,2,3)
print(1,2,3,sep='-')
print(1,2,3,sep='-',end='xX')

