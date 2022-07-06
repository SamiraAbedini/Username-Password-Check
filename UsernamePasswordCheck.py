#===================================================================
#--------------------------------E9---------------------------------
#===================================================================
yourusername=input('Enter your username: ')
yourpassword=input('Enter your password: ')

print('login-->')
username=input('username: ')
password=input('password: ')

while username!=yourusername or password!=yourpassword:
    print('Username or Password is not correct!')
    print('login-->')
    username=input('username: ')
    password=input('password: ')

