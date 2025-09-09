
"""
************************************************************************

This module logs in to the appliance and returns the session 
cookie, for future API calls.

************************************************************************
"""

import requests
import json
import sys

def ecLogin(ec_url, user, password):

# Create URL, Headers and Body for API Call
    url = ec_url + '/login'

    headers = {}
    headers['Content-Type'] = 'application/json'
    
    body = {
        'password': password,
        'user': user
    }

# Disable ssl inspection
    requests.packages.urllib3.disable_warnings()

# Make API Call
    response = requests.post(url, headers=headers, json=body, verify=False)

# Print error handling and API call results
    if response.status_code == 200:
        print('\n' + 'Login successful. Https response code = ' + str(response.status_code))
    else:
        sys.exit('\n' + 'Login unsuccessful. Https response code = ' +str(response.status_code))


# store login cookie, from API call, in "orchCookie" and return for future API calls

    sessionID = response.cookies
    return(sessionID)

#end
