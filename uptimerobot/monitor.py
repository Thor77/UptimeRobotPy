from .status import MonitorStatus
from .utrobject import UptimeRobotObject


class Monitor(UptimeRobotObject):
    def __init__(self, account, attributes):
        super().__init__(account, attributes)
        self.status = MonitorStatus(self.status)
