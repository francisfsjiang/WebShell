import publicfunction as PF

Default_Src='http://localhost/music/eg_tulip.jpg'
Imageviewer_Tag='<img src="%s"/>'
Help_Info="""
<span class='info'>imageviewer source_url</span>
"""

def resolve(args):
    if len(args)==1 and args[0]=='help':
        return help_info()
    if len(args)==0:
        return Imageviewer_Tag%(Default_Src)
    if len(args)==1:
        return Imageviewer_Tag%(args[0])
    else:
        return PF.normalinfo('input arguments error, input "imageviewer help" to get help')


def help_info():
    return Help_Info;
