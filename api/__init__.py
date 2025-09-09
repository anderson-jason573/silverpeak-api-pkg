"""
***************************************************************

This module initializes the 'api' package, when it is imported.
It imports all of the functions from the modules in the api 
package, so they can be called by using 'api.<function>'.

It also imports the requests, json and sys packages.

***************************************************************
"""
import requests
import json
import sys
from .get_orchestrator_hostname import orchHostname
from .login import ecLogin
#end
