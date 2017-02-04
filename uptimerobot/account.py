from .alert_contact import AlertContact
from .monitor import Monitor
from .tools import request, setattrs


class Account(object):
    def __init__(self, api_key):
        '''
        Initialize interface to an UptimeRobot-Account

        :param api_key: API key used for authentication

        :type api_key: str
        '''
        self.api_key = api_key

        # Fetch details
        details = self._request('getAccountDetails')
        setattrs(self, details['account'])

    def __repr__(self):
        return self.email

    def _request(self, endpoint, params={}):
        return request(self.api_key, endpoint, params)

    @property
    def monitors(self):
        '''
        List monitors attached to this account

        :return: monitors attached to this account
        :rtype: [uptimerobot.Monitor]
        '''
        return [
            Monitor(self, **monitor) for monitor in
            self._request('getMonitors')['monitors']
        ]

    @property
    def alert_contacts(self):
        '''
        List alert contacts attached to this account

        :return: alert contacts attached to this account
        :rtype: [uptimerobot.AlertContact]
        '''
        return [
            AlertContact(self, **alert_contact) for alert_contact in
            self._request('getAlertContacts')['alert_contacts']
        ]
