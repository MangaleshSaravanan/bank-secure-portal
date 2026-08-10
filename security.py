import bcrypt
def encryptPwd(pwd):
        pwd_byte = pwd.encode("utf-8")
        salt = bcrypt.gensalt()
        hashByte =  bcrypt.hashpw(pwd_byte,salt)
        return hashByte

def retrivePwd(userinput, stored_hash):
        ui = userinput.encode("utf-8")
        hash_bytes = stored_hash.encode("utf-8")
        return bcrypt.checkpw(ui, hash_bytes)
