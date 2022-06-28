from gpiozero import Button
import time
import math

wind_count = 0
radius_cm = 7.2
wind_interval = 5

def spin():
    global wind_count
    wind_count = wind_count + 1
    #print("spin" + str(wind_count))

def calculate_speed(time_sec):
    global wind_count
    circumference_cm = (2 * math.pi) * radius_cm

    # Divide by 2 here if each side of the reed switch is in the magnets path:
    rotations = wind_count / 2.0

    dist_km = (circumference_cm * rotations) / 100000.0

    km_per_sec = dist_km / time_sec
    km_per_hour = km_per_sec * 3600

    return km_per_hour * 1.18


def reset_wind():
    global wind_count
    wind_count = 0

wind_speed_sensor = Button(5)
wind_speed_sensor.when_pressed = spin

while True:
    wind_count = 0
    time.sleep(wind_interval)
    print(calculate_speed(wind_interval), "km/h")