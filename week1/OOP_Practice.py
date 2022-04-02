import re
import hashlib



class Account:
    def __init__(self, username, password, phone_number, email):
        self.username = Account.valid_name(username)
        self.password = Account.valid_password(password)
        self.phone_number = Account.valid_phone(phone_number)
        self.email = Account.valid_mail(email)

#username should be in this format: firstname_lastname
    @staticmethod
    def valid_name(username): 
        input_name = re.search(r"\A[a-zA-Z]_[a-zA-Z]\Z", username)
        if input_name:
            return username
        else:
            raise Exception("invalid username")

#password should have at least one capital and one small letter and numbers with 8 characters
    @staticmethod
    def valid_password(password): 
        input_password = re.fullmatch(r"\A(?=+[A-Z])(?=+[a-z])(?=+[0-9]){8}\Z", password)
        if input_password:
            return password
        else:
            raise Exception("invalid password")

#phone numbers should have 11 numbers and start with 09 or 989
    @staticmethod
    def valid_phone(phone_number):
        input_number = re.search(r"\A(989|09)\d{9}\Z", phone_number)
        if input_number:
            return phone_number
        else:
            raise Exception("Invalid phone number")

#email can have number/capital and small letter/./-/_ and the last part can have 2 to 5 character 
    @staticmethod
    def valid_mail(email):
        input_email = re.fullmatch(r"[a-zA-Z0-9._-]+@[a-zA-Z0-9]+.[a-zA-z]{2,5}", email)
        if input_email:
            return email
        else:
            raise Exception("Invalid Email")




class Site:
    def __init__(self, url, register_users, active_users):
        self.url = url
        self.register_users = []
        self.active_users = []


    def register(self, user):
        for i in self.register_users:
            if i.username == user.username:
                raise Exception("user already registered")
            else:
                self. register_users.append(i)
                print("register successful")


    def login(self, username, password, email):
        for user in self.register_users:
            if user.email == email and user.password == hashlib.sha256(password.encode('utf-8')).hexdigest(): #if user login with email and password
                self.active_users.append(user)
                print("login successful")
            elif user.username == username and user.password == hashlib.sha256(password.encode('utf-8')).hexdigest(): #if user login with username and password
                self.active_users.append(user)
                print("login successful")
            elif user.email == email and user.username == username and user.password == hashlib.sha256(password.encode('utf-8')).hexdigest(): #if user login with email, username and password
                self.active_users.append(user)
                print("login successful")
            else:
                print("invalid login")
            
            for user in self.active_users:
                if user.email == email and user.password == hashlib.sha256(password.encode('utf-8')).hexdigest():
                    print("user already logged in")
                elif user.username == username and user.password == hashlib.sha256(password.encode('utf-8')).hexdigest():
                    print("user already logged in")
                elif user.email == email and user.username == username and user.password == hashlib.sha256(password.encode('utf-8')).hexdigest():
                    print("user already logged in")
                

    def logout(self, user):
        if user in self.active_users:
            self.active_users.remove(user)
            print("logout successful")
        else:
            print("user is not logged in")


















