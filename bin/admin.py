import os
import publicfunction as PF
def resolve(args):
    try:

        cmd=''
        for i in args:
            cmd+=str(i)+' '
        result=os.popen(cmd).readlines()
        output=''
        for i in result:
            output+="<span class='info'>"+i[:len(i)-1]+"</span><br />"
        return output
    except:
        return PF.error_info('excute error')