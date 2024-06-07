import requests
import json
from typing import List, Union
from brynq_sdk.brynq import BrynQ
from brynq_sdk.factorial.ats import Ats
from brynq_sdk.factorial.core import Core
from brynq_sdk.factorial.finance import Finance
from brynq_sdk.factorial.payroll import Payroll
from brynq_sdk.factorial.time import Time


# Set the base class for Factorial. This class will be used to set the credentials and those will be used in all other classes.
class Factorial(BrynQ):
    def __init__(self, label: Union[str, List], debug: bool = False):
        """"
        For the documentation of Factorial, see: https://apidoc.factorialhr.com/docs/authentication-1
        """
        super().__init__()
        base_url = 'https://api.factorialhr.com/api/v1/'
        headers = self._get_credentials(label, base_url)
        self.ats = Ats(headers, base_url)
        self.core = Core(headers, base_url)
        self.finance = Finance(headers, base_url)
        self.payroll = Payroll(headers, base_url)
        self.time = Time(headers, base_url)

    def _get_credentials(self, label, base_url):
        """
        Sets the credentials for the SuccessFactors API.
        :param label (str): The label for the system credentials.
        :returns: headers (dict): The headers for the API request, including the access token.
        """
        credentials = self.get_system_credential(system='factorial', label=label)
        payload = {
            "client_id": f"{credentials['client_id']}",
            "client_secret": f"{credentials['client_secret']}",
            "grant_type": "client_credentials"
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/x-www-form-urlencoded"
        }
        url = f'{base_url}/auth/token'
        payload = json.dumps(payload)
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()
        access_token = response.json()['access_token']

        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }

        return headers

