i=1
insert=""
insertion=False
while True:
    if i > 1 and not insertion:
        insert = insert+"再"
        insertion=not insertion
    print(f"你{insert}看看你后面呢")
    i+=1
