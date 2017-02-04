from .status import AlertContactStatus
from .utrobject import UptimeRobotObject


class AlertContact(UptimeRobotObject):
    def __init__(self, account, **kwargs):
        super().__init__(account, **kwargs)
        self.status = AlertContactStatus(self.status)
