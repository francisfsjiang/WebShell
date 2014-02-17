import publicfunction as PF
import default_settings as RE
import re
import random


Help_Info='''
<span class='info'>timer xxxx-xx-xx xx:xx:xx</span><br />
<span class='info'>eg. 2013-01-01 03:04:04</span>
'''

def resolve(args):
    if len(args)==1 and args[0]=='help':
        return help_info()
    if len(args)!=2:
        return PF.normal_info("input arguments error, input 'timer help' to get help");
    if re.search(RE.Re_User_Date,args[0])==None:
        return PF.normal_info('date fromat is wrong.')
    if re.search(RE.Re_User_Time,args[1])==None:
        return PF.normal_info('time fromat is wrong.')
    try:
        #y-m-d
        date=args[0].split('-')
        #h-m-s
        time=args[1].split(':')
        #print(date)
        #print(time)
        #8/08/2008 20:00:00
        time_output0=args[0]+' '+args[1]
        time_output1=date[1]+'/'+date[2]+'/'+date[0]+' '+time[0]+':'+time[1]+':'+time[2]
        #output=content1+args[0]+' '+args[1]+content2+time_output+content3
        dom_id0=str(random.randint(0,2147483648))
        dom_id1=str(random.randint(0,2147483648))
        output=content%(time_output0,dom_id0,dom_id1,time_output1,dom_id0,dom_id1)
        #output="""<div align="center" class="STYLE3">距'%s'还有</div>"""%(time_output0)
        return output
    except:
        return PF.error_info('error')

def help_info():
    return Help_Info


content="""
<span class='info'>距%s还有</span>
<br/>
<span id="timeDate%s">0天</span>
<span id="times%s">00:00:00</span>
<script>
var now = new Date();
function createtime(){
    var grt= new Date("%s");
    now.setTime(now.getTime()+1000);
    days = (grt - now) / 1000 / 60 / 60 / 24;
    dnum = Math.floor(days);
    hours = (grt - now) / 1000 / 60 / 60 - (24 * dnum);
    hnum = Math.floor(hours);
    if(String(hnum).length ==1 ){hnum = "0" + hnum;}
    minutes = (grt - now) / 1000 /60 - (24 * 60 * dnum) - (60 * hnum);
    mnum = Math.floor(minutes);
    if(String(mnum).length ==1 ){mnum = "0" + mnum;}
    seconds = (grt - now) / 1000 - (24 * 60 * 60 * dnum) - (60 * 60 * hnum) - (60 * mnum);
    snum = Math.round(seconds);
    if(String(snum).length ==1 ){snum = "0" + snum;}

document.getElementById("timeDate%s").innerHTML = dnum+"天";
document.getElementById("times%s").innerHTML = hnum + ":" + mnum + ":" + snum;
}
setInterval("createtime()",1000);
</script>"""

"""
    <TABLE width=234 height="60" border=0 align=center cellPadding=0 cellSpacing=0>
        <TBODY>
            <TR>
                <TD colSpan=2 height=24>
                    <div align="center" class="STYLE3">距'%s'还有</div>
                </TD>
            </TR>

            <TR>
                <TD align=middle id=timeDate%s>
                    <div align="center" class="STYLE3">660天</div>
                </TD>
                <TD align=middle id=times%s>
                    <div align="center" class="STYLE3">18:09:53</div>
                </TD>
            </TR>
        </TBODY>
    </TABLE>
"""