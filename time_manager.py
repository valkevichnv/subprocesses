import subprocess
import time

s1 = subprocess.Popen(["python3", "./time.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
s2 = subprocess.Popen(["python3", "./time.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
time.sleep(120)
_ = s1.communicate(input=' \n'.encode())
_ = s2.communicate(input=' \n'.encode())
#print(_.decode())
