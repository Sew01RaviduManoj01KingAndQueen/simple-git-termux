import os,sys,time,random
print("")
print("")
color = ["\033[1;31m","\033[1;32m"]
m = random.choice(color)+"OWNER: THBD \n"
for msg in m:
    sys.stdout.write(msg)
    sys.stdout.flush()
    time.sleep(0.06)
print("")
