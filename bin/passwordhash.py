import  hashlib

def hash(arg):
    temp=arg.encode('utf8')
    temp=hashlib.sha512(temp).hexdigest().encode('utf8')
    #print(temp)
    temp=hashlib.md5(temp).hexdigest()
    #print(temp)
    return temp


#if __name__=='__main__':
#    hash('zxcvbn125369')