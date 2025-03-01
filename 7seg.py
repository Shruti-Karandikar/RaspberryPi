from gpiozero import LED
from time import sleep

# Define the GPIO pins for each segment
segments = {
    'a': LED(15),
    'b': LED(14),
    'c': LED(3),
    'd': LED(25),
    'e': LED(24),
    'f': LED(18),
    'g': LED(23)
}

# Segment configurations for numbers 0-9
numbers = {
    0: ['a', 'b', 'c', 'd', 'e', 'f'],
    1: ['b', 'c'],
    2: ['a', 'b', 'g', 'e', 'd'],
    3: ['a', 'b', 'g', 'c', 'd'],
    4: ['f', 'g', 'b', 'c'],
    5: ['a', 'f', 'g', 'c', 'd'],
    6: ['a', 'f', 'g', 'c', 'd', 'e'],
    7: ['a', 'b', 'c'],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    9: ['a', 'b', 'c', 'd', 'f', 'g']
}

def display_number(num):
    # Turn off all segments
    for segment in segments.values():
        segment.off()

    # Turn on the required segments for the given number
    for segment in numbers[num]:
        segments[segment].on()

try:
    while True:
        for i in range(10):
            print("displaying ", i)
            display_number(i)
            sleep(1)

except KeyboardInterrupt:
    print("Program stopped by user.")
    # Turn off all segments before exiting
    for segment in segments.values():
        segment.off()
