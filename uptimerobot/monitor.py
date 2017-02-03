from .tools import setattrs
from .status import MonitorStatus


class Monitor(object):
    def __init__(self, **kwargs):
        setattrs(self, kwargs)
        self.status = MonitorStatus(self.status)

    def __repr__(self):
        return '{0.friendly_name} ({0.id}) <{0.status}>'.format(self)
