"""
***************************************************************

This module initializes the 'api' package, when it is imported.
It imports all of the functions from the modules in the api 
package, so they can be called by using 'api.<function>'.

***************************************************************
"""
import requests
import json
import sys
from .login import OrchLogin
from .yamlConversion import readYAML
from .preconfigOrch import preconfigUpload
from .spcustomFile import spcustomCreate
from .applianceInfo import applianceINFO
from .GET_Orchestrator_Hostname import OrchHostname
#end
