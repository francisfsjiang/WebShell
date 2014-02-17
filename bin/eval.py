import publicfunction as PF

Help_Info="""
<span class='info'>eval expression</span><br />
"""

def resolve(args):
    if len(args)==1 and args[0]=='help':
        return help_info()
    if len(args)!=1:
        return PF.normal_info("input arguments error, input 'eval help' to get help")
    try:
        return PF.normal_info(eval(args[0]))
    except Exception:
        return PF.error_info('wrong expression')


def help_info():
    return Help_Info
