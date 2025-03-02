from gpiozero import LED, Button
from gpiozero import LEDCharDisplay
from time import sleep
from signal import pause

red = LED(2)
yellow = LED(6)
green = LED(26)

button = Button(10)

#display = LEDCharDisplay(17,27,22,23,24,25,16) #map a,b,c,d,e,f,g to respective pins

#display.off() #initialize 7 segment display off

red.off() #initialize LEDs off
yellow.off()
green.on()

def cross_time(seconds):
    count_sequence = list(range(seconds-1, -1, -1))  # countdown to zero
    sleep (5)

    for x in count_sequence:
        #display.value = str(x)
        sleep(1)
    #display.off()

def pedestrian():
    sleep(10)
    print("yes")
    #wait 10 seconds then light turns from green to yellow
    green.off()
    yellow.on()
    sleep(5)
    #wait 10 seconds then light goes from yellow to red
    yellow.off()
    red.on()
    #cross_time(10)
    sleep(2)
    #wait 15 seconds for pedestrian to cross
    red.off()
    green.on()

# Added for debugging
def p2():
    print("p2")
    red.off()
    yellow.off()
    green.off()
    sleep(2)
    red.on()
    yellow.on()
    green.on()

while True:
    #button.when_pressed = pedestrian
    if button.is_pressed:
        print("button is pressed")
    else:
        print("button is not pressed")
    #p2()
    pedestrian()
    sleep(1)
