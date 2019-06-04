from beebotte import *
import json

_accesskey  = '*********************************'
_secretkey  = '************************************'
_hostname   = 'api.beebotte.com'
bbt = BBT( _accesskey, _secretkey, hostname = _hostname)

### Alternatively you can authenticate using the channel token
_token      = '***********************************'

bbt = BBT(token = _token, hostname = _hostname)


res1 = Resource(bbt,'TestBeebotte','temp') # don't forget to change channel and field
records = res1.read(limit = 1) #can change limit number
print(records)
b=records[0]
print(b['data'])
