from __future__ import unicode_literals

import onedrivesdk
from onedrivesdk.helpers import GetAuthCodeServer
import os

input = getattr(__builtins__, 'raw_input', input)


def main():
    redirect_uri = "http://localhost:8080/"
    client_secret = "tzUNLG6DdGydHriTGawVVg4"

    client = onedrivesdk.get_default_client(
        client_id='5d866328-ad7e-4414-9bc9-df1e47004d41',
        scopes=['wl.signin',
                'wl.offline_access',
                'onedrive.readwrite'])
    auth_url = client.auth_provider.get_auth_url(redirect_uri)

    code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)

    client.auth_provider.authenticate(code, redirect_uri, client_secret)
