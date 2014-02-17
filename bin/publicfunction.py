def error_info(args=''):
    try:
        return '''<span class='error'>Error: '''+str(args)+'''</span>'''
    except:
        return '''<span class='error'>Error Irresolvable</span>'''

def normal_info(args=''):
    try:
        return '''<span class='info'>'''+str(args)+'''</span>'''
    except:
        error_info('normal info resolve failed')
