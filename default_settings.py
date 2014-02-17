Sql_Host='localhost'
Sql_User='root'
Sql_Password='root'
Sql_Charset='utf8'
Sql_Database='webshell'
Sql_TimeOut=3
# user_id email password reg_time privilege
Sql_Select_User="SELECT user_id,password,privilege FROM users WHERE user_id='%s'"
Sql_Add_User="INSERT INTO users VALUES ('%s','%s','%s','%s',%d)"
Re_User_Name=r'^[-_\w\.]{1,16}$'
Re_User_Password=r'^[\@\w\!\#\$\%\^\&\*\.\~]{6,22}$'
Re_User_Email=r'^[\w]+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$'
#xxxx-xx-xx
Re_User_Date=r'^((?!0000)[0-9]{4}-((0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-8])|(0[13-9]|1[0-2])-(29|30)|(0[13578]|1[02])-31)|([0-9]{2}(0[48]|[2468][048]|[13579][26])|(0[48]|[2468][048]|[13579][26])00)-02-29)$'
#xx:xx:xx
Re_User_Time=r'^((2[0-3])|([0-1][0-9])):([0-5][0-9]):([0-5][0-9])$'