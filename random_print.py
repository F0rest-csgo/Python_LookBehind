import random
textlist=["你看看你后面呢"]
for i in range(random.randint(1,100)):
    textlist.append("你再看看你后面呢")
print(textlist[random.randint(0,0)])
while random.randint(1,100) != 0:
    print(textlist[random.randint(1,len(textlist)-1)])
