This repository is meant to be an introduction to using Silver Peak/EdgeConnect APIs.  The 'main' scripts are meant
to demonstrate the three different types of API calls:

    1.) API calls directly to the Orchestrator - 'main_Orchestrator.py'
    2.) API calls directly to an appliance - 'main_Appliance.py'
    3.) API calls to an appliance via the Orchestrator - 'main_Appliance_via_Orchestrtor.py'

API keys are used for authentication, rather than user names and passwords.  These are created in the Orchestrator
under the "Orchestrator ---> API Keys" menu.  See '.env.example' file for reference.  Place the .env file in 
the same directory where the '.env.example' file currently resides.

A ".env" file is needed, to pass the Orchestrator URL and API key as 
environmental variables in the 'main.Orchestrator.py' and 'main.Appliance(S).py' scripts.

The functions for api calls arecontained in a package called 'api'.  When the 'api' package
is imported, it imports all functions from each module in the package.  To call a function from one of the modules,
preface the function with "api.".  For example, to pass the necessary variables to the function 'OrchHostname'
in the 'GET_Orchestrator_Hostname.py' module, use 'api.OrchHostname(orch_url, orch_api_key)'.

Steps to run:

    1.) create an .env file that contains the following:
            ORCH_URL = '<Rest API of URL of target Orchestrator>'  ##This can be found under the 'Support--->Rest API' menu of your Orchestrator ##

            ORCH_API_KEY = '<API Key created in Orchestrator>'     ## Create key under the 'Orchestrator--->API Key' menu of your Orchestrator ##

            ## See '.env.example' file for details ##
    
    2.) Select module that you want to run, i.e. 'GET_Orchestrator_Hostname.py'

    3.) Get function name from selected module.  In the case of 'GET_Orchestrator_Hostname.py', the function is 'OrchHostname'.

    4.) Select proper 'main' script.  For Orchestrator API calls, use 'main_Orchestrator.py'.  For API calls to appliances, use 'main_Appliance(s).py

    5.) Update 'apiCall' function call (line #21) with the function name obtained in step #3

