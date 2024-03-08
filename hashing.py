from passlib.context import CryptContext
pwd_cxt=CryptContext(schemes=['bcrypt'],deprecated="auto")

class Hash():
    #function to Hash the password
    def bcrypt(password:str):
        return pwd_cxt.hash(password)
    #function to verify the password
    def verify(hashed_password,plain_password):
        return pwd_cxt.verify(plain_password,hashed_password)