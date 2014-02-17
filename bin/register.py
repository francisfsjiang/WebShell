import pymysql
import default_settings as SQL
import default_settings as RE
import passwordhash as Hash
import re
import datetime
import publicfunction as PF

Help_Info="""
<span class='info'>regist username password email</span>
"""


Time_Date_Format='%Y-%m-%d %H:%M:%S'


def resolve(args):
    if len(args)==1 and args[0]=='help':
        return help_info()
    if len(args)!=3:
        return PF.normal_info("input arguments error, input 'registr help' to get help");

#    if re.search(RE.Re_User_Name,args[0])==None:
#        return PF.normal_info('username fromat is wrong.')
#    if re.search(RE.Re_User_Password,args[1])==None:
#        return PF.normal_info('password fromat is wrong.')
#    if re.search(RE.Re_User_Email,args[2])==None:
#        return PF.normal_info('email fromat is wrong.')
    try:
        sql_connect=pymysql.connect(
            host=SQL.Sql_Host,
            user=SQL.Sql_User,
            passwd=SQL.Sql_Password,
            database=SQL.Sql_Database,
            charset=SQL.Sql_Charset,
            connect_timeout=SQL.Sql_TimeOut
        )
    except:
        return PF.error_info('sql connect error')
    event_handler=sql_connect.cursor()
    query_string=SQL.Sql_Select_User%(args[0])
    #print(query_string)
    if event_handler.execute(query_string):
        return PF.normal_info('user name '+args[0]+' has existed.')
    try:
        time_now=datetime.datetime.now()
        time_now=time_now.strftime('%Y-%m-%d %H:%M:%S')
        # user_id email password reg_time privilege
        query_string=SQL.Sql_Add_User%(args[0],args[2],Hash.hash(args[1]),time_now,1)
        print(query_string)
        event_handler.execute(query_string)
        return PF.normal_info('regist sucessfuly. Pleaee login')
    except:
        return  PF.error_info('unexpect')


def help_info():
    return Help_Info;



