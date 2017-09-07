#env /usr/bin/python

import time;

i = 0;
a = 0;

while(True) :
    a += 10;
    print("tick %d: %d" % (i, a));
    time.sleep(1);
