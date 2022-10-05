userName= input('What is your name?')
age = input("What is your age?")

print('Hi {}, you\'re {} years old.'.format(userName,age))

if(int(age) >= 18):
    print('Hi {}! you\'re eligible to vote.'.format(userName))
else:
    print('Sorry {}! You\'re underage and can\'t vote.'.format(userName))