def resolve(args):
    return '''test'''


'''
<div>
    <TABLE  border=0 align=center cellPadding=0 cellSpacing=0>
        <TBODY>
            <TR>
                <TD colSpan=2 height=24 id=info>
                    <div align="center" class="STYLE3">距还有</div>
                </TD>
            </TR>

            <TR>
                <TD align=middle class=fb id=timeDate>
                    <div align="center" class="STYLE3">660天</div>
                </TD>
                <TD align=middle class=fb id=times>
                    <div align="center" class="STYLE3">18:09:53</div>
                </TD>
            </TR>
        </TBODY>
    </TABLE>
<SCRIPT>
var now = new Date();
function createtime(){
    var grt= new Date("8/08/2008 20:00:00");
    now.setTime(now.getTime()+250);
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

document.getElementById("timeDate").innerHTML = dnum+"天";
document.getElementById("times").innerHTML = hnum + ":" + mnum + ":" + snum;
document.getElementById("info").innerHTML = grt.getYear()+grt.getMonth();
}
setInterval("createtime()",250);
</SCRIPT>
</div>
'''



'''

<TABLE>


        <TBODY>
            <TR>
                <TD>
<TABLE width=234 height="60" border=0 align=center cellPadding=0 cellSpacing=0>
    <TBODY>
    <TR>
        <TD colSpan=2 height=24>
            <div align="center" class="STYLE3">距08年8月8日 奥运会开幕还有</div>
        </TD>
    </TR>

    <TR>
        <TD align=middle class=fb id=timeDate
            <div align="center" class="STYLE3">660天</div>
        </TD>
        <TD align=middle class=fb id=times>
            <div align="center" class="STYLE3">18:09:53</div>
        </TD>
    </TR>
    <TR>
        <TD colspan="2" align=middle class=fb id=timeDate>
        <div align="center"><span class="STYLE3"><br />
        距08年7月8日</span> 生日还有
        </div>
        </TD>
    </TR>
    <TR>
    <TD width="87" align=middle class=fb id=timeDate2>
        <div align="center" class="STYLE3"></div>
    </TD>
    <TD width="147" align=middle class=fb id=times2>
        <div align="center" class="STYLE3"></div>
    </TD>
    </TR>
    </TBODY>
    </TABLE>

<SCRIPT>
var now = new Date();
function createtime(){

var grt= new Date("8/08/2008 20:00:00");

now.setTime(now.getTime()+250);
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

document.getElementById("timeDate").innerHTML = dnum+"天";
document.getElementById("times").innerHTML = hnum + ":" + mnum + ":" + snum;
}

function createtime2(){

var grt= new Date("10/5/2013 21:40:30");

now.setTime(now.getTime()+250);
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

document.getElementById("timeDate2").innerHTML = dnum+"天";
document.getElementById("times2").innerHTML = hnum + ":" + mnum + ":" + snum;
}

setInterval("createtime()",250);
setInterval("createtime2()",250);
</SCRIPT>


</TD></TR></TBODY></TABLE>'''

#计时器
'''<SPAN id=span_dt_dt></SPAN>
<SCRIPT language=javascript>
<!--
//document.write("");
function show_date_time(){
window.setTimeout("show_date_time()", 1000);
BirthDay=new Date()("1/08/2010 16:00:00");//这个日期是可以修改的
today=new Date()();
timeold=(BirthDay.getTime()-today.getTime());
sectimeold=timeold/1000
secondsold=Math.floor(sectimeold);
msPerDay=24*60*60*1000
e_daysold=timeold/msPerDay
daysold=Math.floor(e_daysold);
e_hrsold=(e_daysold-daysold)*24;
hrsold=Math.floor(e_hrsold);
e_minsold=(e_hrsold-hrsold)*60;
minsold=Math.floor((e_hrsold-hrsold)*60);
seconds=Math.floor((e_minsold-minsold)*60);
span_dt_dt.innerHTML="<align=center><p><font color=#A22900><p><font size=4>"+daysold+"天"+hrsold+"小时"+minsold+"分"+seconds+"秒"+"<br /></font><br /></font>" ; //这里你自己改。就是倒计时的样式，字体大小size=4 颜色是color
}
show_date_time();
//-->
</SCRIPT>'''


'''<audio src="http://neveralso.com/music/HotelCalifornia.mp3" controls="controls">
Your browser does not support the audio element.
</audio>
'''

'''<audio src="http://www.w3school.com.cn/i/horse.ogg" controls="controls">
Your browser does not support the audio element.
</audio>'''


'''<img src="http://www.w3school.com.cn/i/eg_tulip.jpg"
alt="上海鲜花港 - 郁金香" width="400" height="266" />'''


