
"""
************************************************************************

This module will return the hostname for an appliance.

************************************************************************
"""

import requests
import json
import sys

def ecHostname(ec_url, sessionCookies):

# Create URL, Headers and Body for API Call
    url = ec_url + '/hostname'

    headers = {}
    headers['Content-Type'] = 'application/json'
    headers['X-XSRF-Token'] = (sessionCookies['edgeosCsrfToken'])

# Disable ssl inspection
    requests.packages.urllib3.disable_warnings()

# Make API Call
    response = requests.get(url, headers=headers, cookies=sessionCookies, verify = False)

# Print error handling and API call results
    if response.status_code != 200:
        sys.exit('\n' + 'Request unsuccessful. Https response code = ' +str(response.status_code))

# Return information

    json_response = json.loads(response.text)
    return(json_response)

#end
