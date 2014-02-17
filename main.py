import tornado.web
import tornado.ioloop
import tornado.websocket
import json
import sys
import datetime
sys.path.append('bin')

#自定义error 模块
import publicfunction as PF

#监听端口
PORT=8001

#START
# 子模块
import login
import register
import timeanddate
import logout
import tester
import hash
import admin
import timer
import HotelCalifornia
import videoplayer
import audioplayer
import imageviewer
import eval
# 权限   admin vip normal
#         7    3     1
User_Privilege={
    0:'visitor',
    1:'user',
    3:'vip',
    7:'administrator'
}

# 函数库名:[权限，函数库]s
Function_Dict={
    'time':[0,timeanddate],
    'register':[0,register],
    'login':[0,login],
    'logout':[1,logout],
    'test':[0,tester],
    'hash':[0,hash],
    'admin':[4,admin],
    'timer':[0,timer],
    'HotelCalifornia':[4,HotelCalifornia],
    'videoplayer':[1,videoplayer],
    'audioplayer':[1,audioplayer],
    'imageviewer':[1,imageviewer],
    'eval':[4,eval]
}

#END


Shell_Help_Info="""
<h2>Welcome to WebShell</h2>
<h3>order list:</h3>
"""

class SocketHandler(tornado.websocket.WebSocketHandler):
    """
    on_message(message) 接受消息
    write_messate(message) 发送消息
    """
    clients=set()
    user_state=0
    user_name=''
    user_email=''
    def open(self):
        time_now=datetime.datetime.now()
        time_now=time_now.strftime('%Y-%m-%d %H:%M:%S')
        #temp=self.
        #print(temp)
        ##print(str(id(self)) + " joined "+time_now)
        #self.write_message(json.dumps({
        #'type': 'sys',
        #'message': 'Welcome to WebSocket',
        #}))
        SocketHandler.clients.add(self)

    def on_close(self):
        time_now=datetime.datetime.now()
        time_now=time_now.strftime('%Y-%m-%d %H:%M:%S')
        ##print(str(id(self)) + " left "+time_now)
        SocketHandler.clients.remove(self)

    def on_message(self, message):
        time_now=datetime.datetime.now()
        time_now=time_now.strftime('%Y-%m-%d %H:%M:%S')
        ##print(str(id(self)) + " sent " +message +"  "+ time_now)
        try:
            medict=json.loads(message)
            #output=str(medict['cmd'])+str(medict['args'])
            medict['cmd']=medict['args'][0]
            medict['args']=medict['args'][1:]
            print(medict)
            output=order_resolve(medict['cmd'],medict['args'],self)
        except Exception:
            output=PF.error_info('error @ receive')
        if not output:
            output=PF.normal_info('No out put')
        #print(output)
        self.write_message(output)
        #self.write_message(json.dumps({
        #    'type': 'user',
        #    'id': id(self),
        #    'message': output,
        #}))
        #SocketHandler.send_to_all({
        #    'type': 'user',
        #    'id': id(self),
        #    'message': output,
        #})

    @staticmethod
    def send_to_all(message):
        for i in SocketHandler.clients:
            i.write_message(json.dumps(message))

def order_resolve(cmd,args,sockethandler):
    """

    """
    try:
        if cmd =='help':
            return  shell_help()
        if cmd == 'login' :
            temp=Function_Dict[cmd][1].resolve(args)
            sockethandler.user_state=temp[0]
            return temp[1]
        if cmd == 'logout':
            sockethandler.user_state=0
            return Function_Dict[cmd][1].resolve(args)
        if cmd =='registr':
            return Function_Dict[cmd][1].resolve(args)
        if cmd not in Function_Dict:
            return PF.normal_info('Sorry , command '+cmd+' is not found. Input help to see more. Or contact neveralso@gmail.com')

        if Function_Dict[cmd][0]==0 or (Function_Dict[cmd][0] & sockethandler.user_state):
            return Function_Dict[cmd][1].resolve(args)
        else:
            return 'Sorry , '+User_Privilege[sockethandler.user_state]+' , your permission level is not high enough to use this command'
    except all:
        return PF.error_info('resolve')

def shell_help():
    temp=''
    for i in Function_Dict:
        temp+=PF.normal_info(i)+'<br />'
    return Shell_Help_Info+temp


def callback():
    print('end')


if __name__ == '__main__':
    app = tornado.web.Application([
        ('/socket', SocketHandler),
    ])
    app.listen(PORT)
    print("listening at:"+str(PORT))
    #cb=tornado.ioloop.IOLoop.add_callback(callback)
    ioloop=tornado.ioloop.IOLoop.instance()
    #timeout=ioloop.add_timeout(100,cb)
    #ioloop.remove_timeout(timeout)
    ioloop.start()

