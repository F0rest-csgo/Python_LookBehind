import os
 
stream = os.popen("echo 你看看你后面呢")
print(stream.read())

while True:
    stream = os.popen("echo 你再看看你后面呢")
    print(stream.read())
    
