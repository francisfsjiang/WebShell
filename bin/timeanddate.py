# coding: utf-8
import pytz
import datetime
import publicfunction as PF

Help_Info="""
<span class='info'>time [option]</span><br />
<span class='info'>-timezone show the time of one timezone</span><br />
<span class='info'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;continent/city</span><br />
<span class='info'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eg.</span><br />
<span class='info'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sia/Shanghai</span><br />
<span class='info'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;America/New_York</span><br />
"""

OutPatternHead='%Y-%m-%d %A %H:%M:%S timezone '
OutPatternTail='%z .'



def resolve(args):

    default_args={
        '-timezone':'Asia/Shanghai',
        }
    default_info=[]


    try:
        for i in args:
            if i[0]=='-':
                [option,value]=i.split('=')
                #return error_info(str(option)+str(value))
                if option in default_args:
                    default_args[option]=value
                else:
                    return PF.normal_info("input arguments error, input 'help' to help")
            else:
                default_info.append(i)

        return time(default_info,default_args)
    except :
        return PF.error_info('exception')

def time(info,args):
    try:
        if len(info)!=0 and info[0]=='help':
            return help_info()
        nowzone=pytz.timezone(args['-timezone'])
        dt=datetime.datetime.now(nowzone)
        output=dt.strftime(OutPatternHead)+str(args['-timezone'])+' '+dt.strftime(OutPatternTail)[:3]
        return PF.normal_info(output)
    except :
        return PF.error_info('inside '+str(args))

def help_info():
    return Help_Info

