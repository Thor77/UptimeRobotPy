MONITOR_STATUS_CODES = {
    0: 'paused',
    1: 'not checked yet',
    2: 'up',
    8: 'seems down',
    9: 'down'
}

ALERT_CONTACT_STATUS_CODES = {
    0: 'not activated',
    1: 'paused',
    2: 'active'
}


class Status(object):
    def __init__(self, code):
        self.code = int(code)
        self.status_message = None

    def __repr__(self):
        return self.status_message

    def __bool__(self):
        return self.code == 2


class MonitorStatus(Status):
    def __init__(self, code):
        super().__init__(code)
        self.status_message = MONITOR_STATUS_CODES[int(self.code)]


class AlertContactStatus(Status):
    def __init__(self, code):
        super().__init__(code)
        self.status_message = ALERT_CONTACT_STATUS_CODES[int(self.code)]
