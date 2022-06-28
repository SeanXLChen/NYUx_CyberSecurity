import os
import hashlib


def salted_password(pwd, salt):
    # concate string
    apwd = pwd + salt
    
    # perform sha256 hashing
    sha256 = hashlib.sha256()
    sha256.update(apwd.encode('utf-8'))
    hashv = sha256.hexdigest()

    return hashv
    

def main():
    # input pwd
    pwd = input("Please Type Your Password:")

    # generate salt
    salt = os.urandom(32).hex()

    # generate hash value for salted password
    result = salted_password(pwd, salt)
    print(result)


if __name__ == '__main__':
    main()
