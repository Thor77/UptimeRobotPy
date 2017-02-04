from .status import MonitorStatus
from .utrobject import UptimeRobotObject


class Monitor(UptimeRobotObject):
    def __init__(self, account, **kwargs):
        super().__init__(account, **kwargs)
        self.status = MonitorStatus(self.status)
