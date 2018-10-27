import time
size = 0.1
while(True):
    f = open("size.txt", "w")
    l = str(size)
    f.writelines(l)
    size = (size + 0.1) % 1
    f.close()
    time.sleep(0.01)
