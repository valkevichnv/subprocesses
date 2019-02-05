import subprocess
import time

s1 = subprocess.Popen(["python3", "./time.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
s2 = subprocess.Popen(["python3", "./time.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
time.sleep(120)
out,err = s1.communicate(input=' \n'.encode())
out,err = s2.communicate(input=' \n'.encode())
