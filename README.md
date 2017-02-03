UptimerobotPy
=============
A simple, pythonic interface to the [UptimeRobot](https://uptimerobot.com)-API

Installation
============
```
python setup.py install
```

Example
=======
```py
>> from uptimerobot import Acccount
>> a = Account('API_KEY')
>> a
your@mail.com
>> a.monitors
[Monitor 1 (1234) <up>, Monitor 2 (5678) <down>]
>> alert_contacts = a.alert_contacts
>> alert_contacts
[Mail 1 (1234) <active>, Mail 2 (5678) <paused>]
>> alert_contacts[0].value
your@mail.com
>> filter(lambda ac: ac.status, alert_contacts))
[Mail 1 (1234) <active>]
```
