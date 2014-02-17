import publicfunction as PF

Default_Src='http://localhost/music/horse.ogg'
Audioplayer_Tag='<audio src="%s" controls="controls">Your browser does not support the audio element.</audio>'
Help_Info="""
<span class='info'>audioplayer source_url</span>
"""

def resolve(args):
    if len(args)==1 and args[0]=='help':
        return help_info()
    if len(args)==0:
        return Audioplayer_Tag%(Default_Src)
    if len(args)==1:
        return Audioplayer_Tag%(args[0])
    else:
        return PF.normalinfo('input arguments error, input "audioplayer help" to get help')


def help_info():
    return Help_Info;