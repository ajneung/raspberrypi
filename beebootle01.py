import sys

import Adafruit_DHT
from beebotte import *
import bh1750

sensor = Adafruit_DHT.DHT22
pin = 4

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)



_accesskey  = '************************'
_secretkey  = '*****************************'
_hostname   = 'api.beebotte.com'
bbt = BBT( _accesskey, _secretkey, hostname = _hostname)

### Alternatively you can authenticate using the channel token
_token      = '**********************************'

bbt = BBT(token = _token, hostname = _hostname)



while True:
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
        print("Light "+ str(bh1750.readLight())  )
        bbt.writeBulk("TestBeebotte", [
            {"resource": "temp", "data": temperature},
            {"resource": "humid", "data": humidity},
            {"resource": "light", "data": bh1750.readLight()}
])

    else:
        print('Failed to get reading. Try again!')
        sys.exit(1)