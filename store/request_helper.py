import requests
from django.conf import settings
from decorators import RequestRetrial


@RequestRetrial(settings.RETRIAL_COUNT)
def get_request(url, params={}, headers={}):
    """
    Args:
        url: url to which the get request has to be made
        params: request params to be sent along with the request
    Returns: response of the request made
    """
    return requests.get(url, params=params, headers=headers)


@RequestRetrial(settings.RETRIAL_COUNT)
def post_request(url, params={}, headers={}):
    """
    Args:
        url: url to which the post request has to be made
        params: json to be sent along with the request
    Returns: response of the  request made
    """
    return requests.post(url, json=params, headers=headers)


@RequestRetrial(settings.RETRIAL_COUNT)
def delete_request(url, params={}, headers={}):
    """
    Args:
        url: url to which the request has to be made
        params: data to be sent along the  request
    Returns: response of the request made
    """
    return requests.delete(url, data=params, headers=headers)
