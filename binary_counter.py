from gpiozero import LED
from time import sleep
import time

led1 = LED(17)
led2 = LED(27)
led3 = LED(23)
led4 = LED(24)

count = 0
start = time.time()
while True:
    sleep(0.1)
    if (count % 100 == 0):
        print(count)
    count = count + 1
    if (count % 2) > 0:
        led4.on()
    else:
        led4.off()
    if (count % 4) > 1:
        led3.on()
    else:
        led3.off()
    if (count % 8) > 3:
        led2.on()
    else:
        led2.off()
    if (count % 16) > 7:
        led1.on()
    else:
        led1.off()
    sleep(0.5)
    if count == 1500:
        break
end = time.time()
print("time taken:", end - start)
