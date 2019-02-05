import subprocess
import time

s1 = subprocess.Popen("python3 ./time.py", shell=True)
s2 = subprocess.Popen("python3 ./time.py", shell=True)
time.sleep(12)

