###################################################################################
#                                                                                 # 
# For direct API calls to the Orchestrator, an API key is used for authentication #
# This module uses a .env file, to load the api key.                              #
#                                                                                 #
###################################################################################

import api
import os
import sys
from dotenv import find_dotenv, load_dotenv

#load Orchestrator URL and API Key from .env file
env_path = '.env'                                                               # Set path to .env file.  Here the .env file is in the same directory.
if not os.path.exists(env_path):                                                # Error Handling if .env cannot be found       
    raise FileNotFoundError(f"The .env file was not found at: {env_path}")
else:
    load_dotenv(dotenv_path=env_path)
    

# Set Orchestrator FQDN/IP and API Key via from .env file
orch_url = os.environ.get("ORCH_URL")                                           # Reads .env file and sets 'orch_url' variable
if orch_url is None:
    sys.exit('\n' + '"ORCH_URL" is not set in .env file')
else:
    print('"orch_url" loaded successfully')
    
orch_api_key = os.environ.get("ORCH_API_KEY")                                   # Reads .env file and sets 'orch_api_key' variable
if orch_api_key is None:
    sys.exit('\n' + '"ORCH_API_KEY" is not set in .env file')
else:
    print('"orch_api_key" loaded successfully')

"""
Pass Orchestrator url and API key for API Call to desired module/function.

Example:
apiCall = api.<desired module/function>(orch_url, headers)

"""
apiCall = api.orchHostname(orch_url, orch_api_key)                              # Passes url and api key to 'OrchHostname function' in 'GET_Orchestrator_Hostname.py' module

