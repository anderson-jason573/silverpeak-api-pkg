"""
************************************************************
This module is the API call directly to appliances via the
Orchestrator.  It will retrieve a summary of the active
alarms for each appliance.
************************************************************
"""

import json
import requests
from api_methods import ApiMethods



class ApplianceActiveAlarms:
    """ This class ..........."""

    @classmethod
    def active_alarms(cls, obj):
        """ This method ........ """

        try:
            r = ApiMethods.get_appl("/appliance/rest/{0}//alarm"
                .format(obj.id), obj)
            if r.status_code == 200:
                alarm_summary = r.json()
            return alarm_summary

        else:
            print("Unable to get alarm summary for: {0} {1} {2}"
                  .format(obj.hostName, obj.id, r.text))

# end