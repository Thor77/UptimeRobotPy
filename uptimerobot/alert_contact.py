from .status import AlertContactStatus
from .utrobject import UptimeRobotObject


class AlertContact(UptimeRobotObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.status = AlertContactStatus(self.status)
