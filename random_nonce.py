#generate random number with 30 sec interval for client and server side
#store the random nince in "random.txt" file
import random
import time

n = 100

while n > 0:
    integer = random.randint(100000000000,999999999999)
    #print("Random Nonce")
    print(integer)
    f = open("random.txt", "w")
    f.write(str(integer))
    f.close()
    time.sleep(30) # Delay for 1 minute (60 seconds)
    n -= 1
