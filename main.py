import os
from dotenv import find_dotenv, load_dotenv

#load Orchestrator URL and API Key from .env file
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# Set Orchestrator FQDN/IP and API Key via from .env file
orch_url = os.getenv("ORCH_URL")
orch_api_key = os.getenv("ORCH_API_KEY")

# Create URL and Headers for API Call
url = orch_url + 'gmsHostname'

headers = {}
headers['Content-Type'] = 'application/json'
headers['X-Auth-Token'] = orch_api_key

#Pass url and headers for API Call to desired module/function
"""
apiCall = api.<desired module/function>(url, headers)

