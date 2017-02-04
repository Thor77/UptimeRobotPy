from .tools import setattrs


class UptimeRobotObject(object):
    def __init__(self, **kwargs):
        setattrs(self, kwargs)

    def __repr__(self):
        return '{0.friendly_name} ({0.id}) <{0.status}>'.format(self)