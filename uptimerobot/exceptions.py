def raise_type(exception_type, data):
    '''
    Raise an exception for a specific type

    :param exception_type: Type of the exception
    :param data: Additional data given for this exception

    :type exception_type: str
    :type data: dict
    '''
    if exception_type == 'missing_parameter':
        raise MissingParameter(data['parameter_name'])
    else:
        raise Exception(
            'No specific Exception found for "{}"{}'.format(
                exception_type, 'with data "{}"'.format(data) if data else ''
            )
        )


class MissingParameter(Exception):
    pass
