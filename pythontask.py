import os

def user_check(user_name):
  '''To chech the user name is valid or not'''
  if ('@' in user_name) and (user_name.count('@') == 1) :#to check there is only one @
    user_name = user_name.split('@') #seaparating the username and domain id in to two values
    if user_name[0]:
      for i in user_name[0]:
        if (ord(i) >= 0 and ord(i) <= 45) or (ord(i) == 47)  or (ord(i) == 127) or \
         (ord(i) >= 58 and ord(i) <= 64) or (ord(i) >= 91 and ord(i) <= 96) or \
         (ord(i) >= 123 and ord(i) <= 126) : #to check there are no special characters except for '.'
          print('The user name is not valid')
          return
        else:
          if '.' in user_name[1]:
            if (user_name[1][0] != '.') :#checking if there is a '.' right after '@'
              count = 0
              for i in user_name[1]:
                if (ord(i) >= 0 and ord(i) <= 45) or (ord(i) == 47)  or (ord(i) == 127) or \
                 (ord(i) >= 58 and ord(i) <= 64) or (ord(i) >= 91 and ord(i) <= 96) or \
                  (ord(i) >= 123 and ord(i) <= 126) :#to check there are no special characters except for '.'
                  print('domain has special characters')
                  count = count + 1
                  return
                if count == 0:
                  print('mail is valid')
                  return 1
            else:
              print('domain started with ".", which is not valid')
              return
          else:
            print('This is not valid user mail id')
            return
  else:
    print('This is not valid user mail id')

def password_check(password):
  '''to check password is valid or not'''
  #checking the length of password which is not less than 5 and not greater than 16
  if (len(password) < 6) or (len(password) > 16) :
    print('password is too long or too short')
    return
  count = 0 #code to check the count of special charactger in the password
  for i in password:
    if (ord(i) >= 0 and ord(i) <= 47)  or (ord(i) == 127) or (ord(i) >= 58 and ord(i) <= 64) \
    or (ord(i) >= 91 and ord(i) <= 96) or (ord(i) >= 123 and ord(i) <= 126) :
      count = count + 1
  if count > 0 :
    count = 0 #code to check the count of numbers in the password
    for i in password:
      if (ord(i) >= 48 and ord(i) <= 57 ):
        count = count + 1
    if count > 0:
      count = 0 # code to check if there are any character with caps
      for i in password:
        if (ord(i) >= 65 and ord(i) <= 90) :
          count = count + 1
      if count > 0:
        count = 0 # code to check if there are any characters with small caps
        for i in password:
          if (ord(i) >= 97 and ord(i) <= 122):
            count = count + 1
        if count > 0:
          print('PASSWORD VALID')
          return 1
        else:
          print('password must have atleast one small letter')
          return
      else:
        print('password must have atleast one capital letter')
        return
    else:
      print('password must have atleast one number')
      return
  else:
    print('password must have atleast one special character')
    return

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
  elif reason.lower() == 'forgot password':
    return_val = forgotPassword()
    if return_val == None:
      print('your user id is not present, please register')


if __name__ == "__main__":
    main()
