import requests

from .exceptions import raise_type

BASE_URL = 'https://api.uptimerobot.com/v2/'


def request(api_key, endpoint, params):
    '''
    Request `endpoint` with `params` from the UptimeRobot-API
    authenticated by `api_key`

    :param api_key: API key used to authenticate for the request
    :param endpoint: API-Endpoint for the request
    :param params: Additional params for the request

    :type api_key: str
    :type endpoint: str
    :type params: dict
    '''
    params['format'] = 'json'
    params['api_key'] = api_key
    r = requests.post(BASE_URL + endpoint, data=params)
    if r:
        data = r.json()
        if data['stat'] != 'ok':
            exception_type = data['error'].pop('type')
            raise_type(exception_type, data['error'])
        return data
    else:
        r.raise_for_status()


def setattrs(cls, attrs):
    '''
    Shorthand for applying setattr to `cls` for every attr in `attrs`

    :param cls: Target class
    :param attrs: Attributes to be set

    :type cls: object
    :type attrs: dict
    '''
    for attr, value in attrs.items():
        setattr(cls, attr, value)
