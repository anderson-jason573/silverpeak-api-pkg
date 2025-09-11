########################################################################
#                                                                      #
# API keys are not supported for api calls directly to an appliance.   #
# A username and password are required.  Use an .env file to load them #
# as environmental variables.                                          #
#                                                                      #
########################################################################

import api
import os
from dotenv import find_dotenv, load_dotenv

# Load Appliance(s) URL(s), user and password from .env file
env_path = '.env'                                                               # Set path to .env file.  Here the .env file is in the same directory.
if not os.path.exists(env_path):                                                # Error Handling if .env cannot be found       
    raise FileNotFoundError(f"The .env file was not found at: {env_path}")
else:
    load_dotenv(dotenv_path=env_path)
    print("\nEnvironment variables loaded successfully.")

# Set Orchestrator FQDN/IP and API Key via from .env file
ec_url = os.environ.get("EC_URL")                                               # Reads .env file and sets 'ec_url' variable
user = os.environ.get("USER")                                                   # Reads .env file and sets 'user' variable
password = os.environ.get("PASSWORD")                                           # Reads .env file and sets 'password' variable                                  

""" 
Pass appliance url, user and password to 'ecLogin' function of the 'login.py' module,
to login and receive Session cookies to use for remaining api calls.  
"""

sessionCookies = api.ecLogin(ec_url, user, password)

hostname = api.ecHostname(ec_url, sessionCookies)

print('\n')
print(hostname)

#end
