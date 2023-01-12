#logging file exceptions

import logging

logging.basicConfig(filename='mylog.log',level=logging.DEBUG)

try:
    f=open('filelog1.text','w')
    a,b=[int(x) for x in input("enter two values:").split()]
    logging.info("Division is in progress")
    c=a/b
    f.write("writing %d into file"%c)
except ZeroDivisionError:
    print("Division by zero is not allowed")
    print("please enter non zero value ")
    logging.error("Zero division error")   

finally:
    f.close()
    print('file closed')     