import time

x = 1000
while x > 0:
    print(str(x) + "-7" + str(x - 7))
    x -= 7
    time.sleep(0.05)
