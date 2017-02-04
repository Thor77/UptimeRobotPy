from .status import MonitorStatus
from .utrobject import UptimeRobotObject


class Monitor(UptimeRobotObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.status = MonitorStatus(self.status)
