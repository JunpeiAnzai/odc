from __future__ import unicode_literals

import onedrivesdk
from onedrivesdk.helpers import GetAuthCodeServer
import os

input = getattr(__builtins__, 'raw_input', input)

def main():
    redirect_uri = "http://localhost:8080/"
    client_secret = ""
