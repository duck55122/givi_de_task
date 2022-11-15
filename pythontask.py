import os

def user_check(user_name):
  '''To chech the user name is valid or not'''
  email_pattern = r"[A-Za-z]{1}[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}"
  if re.match(email_pattern,user_name):
    print('email is valid')
    return 1
  else:
    print('email is invalid')
    return 0

def password_check(password):
  '''to check password is valid or not'''
  #checking the length of password which is not less than 5 and not greater than 16
  password_pattern = r"(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,16}"
  if re.match(password_pattern,password):
    print('password is valid')
    return 1
  else:
    print('password is invalid')
    return 0

def register():
  username = input('please enter your user mail id: ')
  usercheck_return = user_check(username)
  if usercheck_return == 1:
    passcode = input('please enter the password: ' )
    passwordcheck_return = password_check(passcode)
    if passwordcheck_return == 1:
      with open('creds.txt','a') as obj:
        obj.write("Username={}\tPassword={}\n".format(username,passcode))

def login():
  '''to check if there is a creds file.'''
  ''' so that if user tried to login directly even before registering 
    when this piece of code runs for first time. instead of throwing and error it creates a empty file'''
  if not (os.path.exists('creds.txt')):
    obj = open('creds.txt','w')
    obj.close()

  username = input('enter your login user mail: ')
  passcode = input('enter your password: ')
  cred_string = 'Username={}\tPassword={}'.format(username,passcode)
  with open('creds.txt','r') as obj :
    credentials = obj.readlines()
    for cred in credentials:
      #print(cred)
      if cred_string == cred.rstrip():
        print('login success')
        return 1
      

def forgotPassword():
  user = input('enter the user mail id: ')
  with open('creds.txt','r') as obj:
    creds = obj.readlines()
    for cred in creds:
      cred = cred.split()
      if user == cred[0][9:]:
        print('your password is {}'.format(cred[1][9:]))
        return 1


def main():
  reason = input('choose between register, login or forgot password to the site: ')#given user choice to choose between login and reister
  if reason.lower() == 'register':
    register()
  elif reason.lower() == 'login' :
    login_return = login()
    if login_return != 1:
      choice = input('choose between register or forgot password: ')
      if choice.lower() == 'register':
        register()
      elif choice.lower() == 'forgot password':
        return_val = forgotPassword()
        if return_val == None:
          print('your user id is not present, please register')
      else:
        print('you choose wrong option')
  elif reason.lower() == 'forgot password':
    return_val = forgotPassword()
    if return_val == None:
      print('your user id is not present, please register')
  else:
    print('You choose wrong option')


if __name__ == "__main__":
    main()
