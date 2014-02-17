import hashlib
import publicfunction as PF

Help_Info="""
<span class='info'>hash method string</span><br />
<span class='info'>method : md5 sha1 sha224 sha256 sha384 sha512</span>
"""

Hash_Method={
    'md5':hashlib.md5,
    'sha1':hashlib.sha1,
    'sha224':hashlib.sha224,
    'sha256':hashlib.sha256,
    'sha384':hashlib.sha384,
    'sha512':hashlib.sha512
}

def resolve(args):
    if len(args)==1 and args[0]=='help':
        return help_info()
    if len(args)!=2 or (args[0] not in Hash_Method):
        return PF.normal_info("input arguments error, input 'hash help' to get help")
    try:
        return PF.normal_info(Hash_Method[args[0]](args[1].encode('utf8')).hexdigest())
    except:
        return PF.error_info('hash error')


def help_info():
    return Help_Info

