import api
import os
from dotenv import find_dotenv, load_dotenv

#load Orchestrator URL and API Key from .env file
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# Set Orchestrator FQDN/IP and API Key via from .env file
orch_url = os.getenv("ORCH_URL")
orch_api_key = os.getenv("ORCH_API_KEY")

"""
#Pass Orchestrator url and headers for API Call to desired module/function.
#Full URL for API call will be completed in the module being called in next section.

#Example:

apiCall = api.<desired module/function>(orch_url, headers)
"""
apiCall = api.OrchHostname(orch_url, orch_api_key)

