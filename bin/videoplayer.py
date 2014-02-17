import publicfunction as PF

Default_Src='http://localhost/music/movie.ogg'
Video_Tag='<video src="%s" controls="controls">your browser does not support the video tag</video>'
Help_Info="""
<span class='info'>videoplayer source_url</span>
"""

def resolve(args):
    if len(args)==1 and args[0]=='help':
        return help_info()
    if len(args)==0:
        return Video_Tag%(Default_Src)
    if len(args)==1:
        return Video_Tag%(args[0])
    else:
        return PF.normalinfo('input arguments error, input "videoplayer help" to get help')


def help_info():
    return Help_Info;