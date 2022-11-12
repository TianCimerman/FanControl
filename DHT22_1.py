import debugpy
import Adafruit_DHT
from time import sleep
from gpiozero import LED
debugpy.listen(("0.0.0.0", 5678))

#Fan_Output
led = LED(27)

#Outside
DHT_SENSOR_Outside = Adafruit_DHT.DHT22
DHT_PIN_Outside = 4
#Inside
DHT_SENSOR_Inside= Adafruit_DHT.DHT22
DHT_PIN_Inside = 17

while True:
    humidity_Outside=15
    temperature_Outside=20
    #Outside
    #humidity_Outside, temperature_Outside = Adafruit_DHT.read_retry(DHT_SENSOR_Outside, DHT_PIN_Outside)
    #if humidity_Outside is not None and temperature_Outside is not None:
        #print("Temp_Out={0:0.1f}*C   Humidity_Out={1:0.1f}%".format(temperature_Outside, humidity_Outside))
    #else:
        #print("Failed to retrieve data from humidity sensor outside")
   
    #Inside
    humidity_Inside, temperature_Inside = Adafruit_DHT.read_retry(DHT_SENSOR_Inside, DHT_PIN_Inside)
    if humidity_Inside is not None and temperature_Inside is not None:
        print("Temp_In={0:0.1f}*C   Humidity_In={1:0.1f}%".format(temperature_Inside, humidity_Inside))
    else:
        print("Failed to retrieve data from humidity sensor inside")
    
    if temperature_Inside>9.0:
        if temperature_Outside<(temperature_Inside-1.0):
            led.on()
        if temperature_Outside>(temperature_Inside+1.0):
            led.off()
    else:
        led.off()
    sleep(1)