Collection of functions for Silver Peak API calls,
contained in a package called 'api'.  When 'api' package
is imported, it imports all functions from each module
in the package.  To call a function from one of the modules,
preface the function with "api.".

For example, to pass the necessary variables to the function 'OrchHostname'
in the 'GET_Orchestrator_Hostname.py' module, use 'api.OrchHostname(orch_url, orch_api_key)'.

API keys are used for authentication, rather than user names and passwords.
A ".env" file is needed, to pass the Orchestrator URL and API key as 
environmental variables in the 'main.Orchestrator.py' and 'main.Appliance(S).py' scripts.

Steps to run:

    1.) create an .env file that contains the following:
            ORCH_URL = '<Rest API of URL of target Orchestrator>'  ##This can be found under the 'Support--->Rest API' menu of your Orchestrator ##

            ORCH_API_KEY = '<API Key created in Orchestrator>'     ## Create key under the 'Orchestrator--->API Key' menu of your Orchestrator ##
    
    2.) Select module that you want to run, i.e. 'GET_Orchestrator_Hostname.py'

    3.) Get function name from selected module.  In the case of 'GET_Orchestrator_Hostname.py', the function is 'OrchHostname'.

    4.) Select proper 'main' script.  For Orchestrator API calls, use 'main_Orchestrator.py'.  For API calls to appliances, use 'main_Appliance(s).py

    5.) Update 'apiCall' function call (line #21) with the function name obtained in step #3

Additional modules will be added, as they are developed.
