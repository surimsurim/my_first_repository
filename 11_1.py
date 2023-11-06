"""#입력 암호화
import getpass
pw = input("Pass :")
print(pw)"""

"""#sha256
import hashlib
hl = hashlib.sha256()
target = "hello"

hl.update(target.encode("utf-8"))
print(hl.hexdigest())"""

"""#keccak256
import Crypto.Hash.keccak as kek
target = "to be or not to be, That is a question!"
kksh = kek.new(digest_bits=256)
kksh.update(target.encode("utf-8"))
print((kksh.hexdigest()))"""

"""#입력키 변환
import getpass
import hashlib

pw = getpass.getpass("Pass : ")
print(pw)
hl = hashlib.sha256()

hl.update(pw.encode("utf-8"))
print(hl.digest())
print(hl.hexdigest())"""

"""#암호 파일 
import hashlib
import os

def pwInsert():
    if os.path.exists('pw.text'):
        pw = hashlib.sha256()
        hs.update(pw.encode("utf-8"))
        with open('pw.txt', 'r') as fp:
            return hs.hexdigest() == fp.read()
    else:
        return True
    
if pwInsert():
    pw = input('new pass :')
    with open('pw.txt', 'w') as fp:
        hs = hashlib.sha256()
        hs.update(pw.encode("utf-8"))
        fp.write(hs.hexdigest())
else:
    print("not allow password")
"""
"""#시스템 정보 확인
import platform as pf
pn = pf.uname()
print(pn)

pm = pf.machine()
print(pm)

pp = pf.processor()
print(pp)

ps = pf.system()
print(ps)"""

"""#웹페이지
import urllib.request as ur
url = 'https://www.google.com'

res = ur.urlopen(url)
web = res.read()

with open("ul.html", "wb") as fp:
    fp.write(web)
print(web)"""

"""#웹정보 읽기2
import http.client as hc
url = "www.google.com"
conn = http.client.HTTPSConection(url)
conn.request("GET", "/")
r = conn.getresponse()

with open("ulrp.html", "wb") as fp:
    fp.write(r.read())
conn.close()
print(r)
"""

"""#멀티스레드
import threading
def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")

for i in range(3) :
    counter(f"num{i}")
print("single end")"""

"""#싱글스레드
def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")
start = time.time()
for i in range(3):
    counter(f"num{i}")
end = time.time()
print("single end", end = start)"""


"""import threeading as td
import time
def counter(str_name):
    for i in range(5000):
        print(f"Countdown {i}, name : {str_name}\n")
thread1 = td.Thread(target=counter, args=("1num",))
thread2 = td.Thread(target=counter, args=("2num", ))
thread3 = td.Thread(target=counter, args=("3num", ))

thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()

print("multi end")"""

"""#병렬 처리
import multiprocessing as mp
def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")
process1 = mp.Process(target=counter, args=("1num",))
process2 = mp.Process(target=counter, args=("2num",))
process3 = mp.Process(target=counter, args=("3num",))

start = time.time()
process1.start()
process2.start()
process3.start()

process1.join()
process2.join()
process3.join()

end = time.time()
print("proc-end", end-start)"""

"""#main 실행
def main() :
    print("hello world")

def run() :
    print("hello python")

if __name__ == "__main__":
    run()"""