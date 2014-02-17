import pymysql
import default_settings as SQL
import passwordhash as Hash
import publicfunction as PF

Help_Info="""
<span class='info'>login username password</span>
"""

def resolve(args):
    if len(args)==1 and args[0]=='help':
        return (0,help_info())
    if len(args)!=2:
        return (0,PF.normal_info("input arguments error, input 'login help' to get help"));
    try:
        sql_connect=pymysql.connect(
            host=SQL.Sql_Host,
            user=SQL.Sql_User,
            passwd=SQL.Sql_Password,
            database=SQL.Sql_Database,
            charset=SQL.Sql_Charset,
            connect_timeout=SQL.Sql_TimeOut
        )
    except Exception:
        return (0,PF.error_info('sql connect error'))
    event_handler=sql_connect.cursor()
    query_string=SQL.Sql_Select_User%(args[0])
    #print(query_string)
    if not event_handler.execute(query_string):
        return (0,PF.normal_info('user '+args[0]+' dose not exist'))
    try:
        user_info=event_handler.fetchall()[0];
        #print(user_info[1])
        #print(Hash.hash(args[1]))
        if user_info[1]==Hash.hash(args[1]):
            return (user_info[2],PF.normal_info('login successfully'))
        else:
            return (0,PF.normal_info('wrong password'))
    except:
        return  PF.error_info('unexpect')



def help_info():
    return Help_Info


