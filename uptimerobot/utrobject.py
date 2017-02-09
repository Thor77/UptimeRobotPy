class UptimeRobotObject(object):
    def __init__(self, account, attributes):
        self.account = account
        self.attributes = attributes

    def __getattr__(self, name):
        return self.attributes[name]

    def __repr__(self):
        return '{0.friendly_name} ({0.id}) <{0.status}>'.format(self)
