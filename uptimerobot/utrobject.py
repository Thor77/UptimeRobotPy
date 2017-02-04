class UptimeRobotObject(object):
    def __init__(self, account, attributes):
        self.account = account
        self.attributes = attributes

    def __getattribute__(self, name):
        if name in super().__getattribute__('attributes'):
            return super().__getattribute__('attributes')[name]
        else:
            return super().__getattribute__(name)

    def __repr__(self):
        return '{0.friendly_name} ({0.id}) <{0.status}>'.format(self)
