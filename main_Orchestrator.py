###################################################################################
#                                                                                 # 
# For direct API calls to the Orchestrator, an API key is used for authentication #
#                                                                                 #
###################################################################################

import api
import os
from dotenv import find_dotenv, load_dotenv

#load Orchestrator URL and API Key from .env file
env_path = '.env'                                                               # Set path to .env file.  Here the .env file is in the same directory.
if not os.path.exists(env_path):                                                # Error Handling if .env cannot be found       
    raise FileNotFoundError(f"The .env file was not found at: {env_path}")
else:
    load_dotenv(dotenv_path=env_path)
    print("\nEnvironment variables loaded successfully.")

# Set Orchestrator FQDN/IP and API Key via from .env file
orch_url = os.environ.get("ORCH_URL")                                           # Reads .env file and sets 'orch_url' variable
orch_api_key = os.environ.get("ORCH_API_KEY")                                   # Reads .env file and sets 'orch_api_key' variable

"""
#Pass Orchestrator url and headers for API Call to desired module/function.
#Full URL for API call will be completed in the module being called in next section.

#Example:

apiCall = api.<desired module/function>(orch_url, headers)

"""
apiCall = api.orchHostname(orch_url, orch_api_key)                              # Passes url and api key to 'OrchHostname function' in 'GET_Orchestrator_Hostname.py' module

