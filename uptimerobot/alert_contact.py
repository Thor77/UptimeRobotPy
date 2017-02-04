from .status import AlertContactStatus
from .utrobject import UptimeRobotObject


class AlertContact(UptimeRobotObject):
    def __init__(self, account, attributes):
        super().__init__(account, attributes)
        self.status = AlertContactStatus(self.status)
