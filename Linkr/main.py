import pyrebase

firebaseConfig={
   'apiKey':config('API_KEY'),
  'authDomain':config('AUTH_DOMAIN'), 
  'databaseURL':config('DATABASE_URL'), 
  'projectId':config('PROJECT_ID'),
  'storageBucket':config('STORAGE_BUCKET'),
  'messagingSenderId':config('MESSAGE_SEND_ID'),
  'appId':config('APP_ID'),
  'measurementId':config('MEASUREMENY_ID')
}
firebase=pyrebase.initialize_app(firebaseConfig)

auth=firebase.auth()
db=firebase.database()
#Login/Signup Module
try:
    email=input("Enter Your Email")
    password=input("Enter Your Password")
    auth.sign_in_with_email_and_password(email,password)
    print("Logged In Sucessfully")
except:
    print("No user exists,Signing you up")
    try:
        auth.create_user_with_email_and_password(email,password)
        print("New User Created Sucessfully")
    except:
            print("User Already Exists,Please Check Your Password")

#Upload Link Module
LinkName=input("Name For Your Link")
LinkAddress=input("Link URL")
data={'Name':LinkName, 'Link':LinkAddress}
db.push(data)
print("Link Saved Sucessfully")

#View Module
print("Do You Want To View Your Links")
response=input("yes/no")
if response=='yes':
   onelink=db.get()
   print(onelink.val())
   Exit=input("Press 'e' to EXIT")
else:
    print("Thank You") 
    import time
    time.sleep(3)










