def user_check(user_name):
  if '@' in user_name:
    user_name = user_name.split('@')
    if user_name[0]:
      for i in user_name[0]:
        if (ord(i) >= 0 and ord(i) <= 45) or (ord(i) == 47)  or (ord(i) == 127) or (ord(i) >= 58 and ord(i) <= 64) or (ord(i) >= 91 and ord(i) <= 96) or (ord(i) >= 123 and ord(i) <= 126) : #to check there are no special characters except for '.'
          print('The user name is not valid')
          return
        else:
          if user_name[1][0] != '.' :
            count = 0
            for i in user_name[1]:
              if (ord(i) >= 0 and ord(i) <= 45) or (ord(i) == 47)  or (ord(i) == 127) or (ord(i) >= 58 and ord(i) <= 64) or (ord(i) >= 91 and ord(i) <= 96) or (ord(i) >= 123 and ord(i) <= 126) : #to check there are no special characters except for '.'
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
    print('there is no @ in username')

def password_check(password):
  if (len(password) < 6) or (len(password) > 16) :
    print('password is too long or too short')
    return
  count = 0 #to check the count of special charactger in the password
  for i in password:
    if (ord(i) >= 0 and ord(i) <= 47)  or (ord(i) == 127) or (ord(i) >= 58 and ord(i) <= 64) or (ord(i) >= 91 and ord(i) <= 96) or (ord(i) >= 123 and ord(i) <= 126) :
      count = count + 1
  if count > 0 :
    count = 0 #to check the count of numbers in the password
    for i in password:
      if (ord(i) >= 48 and ord(i) <= 57 ):
        count = count + 1
    if count > 0:
      count = 0 # to check if there are any character with caps
      for i in password:
        if (ord(i) >= 65 and ord(i) <= 90) :
          count = count + 1
      if count > 0:
        count = 0 # to check if there are any characters with small caps
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

def main():  
  reason = input('Do you want to register or login to the site: ')
  if reason.lower() == 'register':
    username = input('please enter your user mail id: ')
    usercheck_return = user_check(username)
    print(usercheck_return)
    if usercheck_return == 1:
      passcode = input('please enter the password: ' )
      passwordcheck_return = password_check(passcode)
      if passwordcheck_return == 1:
        with open('creds.txt','a') as obj:
          obj.write("#Credential file:\nUsername={}\tPassword={}".format(username,passcode))
  elif reason.lower() == 'login' :
    username = input('enter your login user mail: ')
    passcode = input('enter your password: ')
    cred_string = 'Username={}\tPassword={}'.format(username,passcode)
    with open('creds.txt','r') as obj :
      credentials = obj.readlines()
      if cred_string in credentials:
        print('Login successful')
      else:
        print("we don't find the account, please try to register")

if __name__ == "__main__":
    main()
