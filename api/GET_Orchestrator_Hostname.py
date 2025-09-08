import requests
import json
import sys

def OrchHostname(orch_url, orch_api_key):

# Create URL and Headers for API Call
    url = orch_url + 'gmsHostname'

    headers = {}
    headers['Content-Type'] = 'application/json'
    headers['X-Auth-Token'] = orch_api_key


# Disable ssl inspection
    requests.packages.urllib3.disable_warnings()

# Make API Call
    response = requests.get(url, headers=headers)

# Print error handling and API call results
    if response.status_code == 200:
        print('\n' + 'Information retrieved successfully. Https response code = ' + str(response.status_code))
    else:
        sys.exit('\n' + 'Retrieval of information has failed. Https response code = ' +str(response.status_code))

# Deserialize json from API call to 'json_response' and print
    json_response = json.loads(response.text)
    print('\n' + str(json_response) + '\n')

#end
