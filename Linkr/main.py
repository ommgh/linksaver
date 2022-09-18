import pyrebase

firebaseConfig={
    'apiKey': "AIzaSyB6dA9F_hC2rh2CptOHdyjW5ILMlleiR9o",
  'authDomain': "linksaver-36a0a.firebaseapp.com",
  'databaseURL': "https://linksaver-36a0a-default-rtdb.asia-southeast1.firebasedatabase.app/",
  'projectId': "linksaver-36a0a",
  'storageBucket': "linksaver-36a0a.appspot.com",
  'messagingSenderId': "305557677509",
  'appId': "1:305557677509:web:09ea47872da613674ed7ac",
  'measurementId': "G-L4530TBBN4"
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
   Exit=input("Type 'e' to EXIT")
else:
    print("Thank You") 
    import time
    time.sleep(5)










