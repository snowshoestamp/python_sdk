import requests

class Client(object):
    BASE_URL = "https://ss-dev-api-stamp.azurewebsites.net/v3/"
    api_key = None

    def __init__(self, api_key=None):
        self.api_key = api_key
    
    def get_api_url(self, method):
        return "%s%s" % (self.BASE_URL, method)
    
    def call(self, data_dict=None, method="stamp"):
        response = requests.post(self.get_api_url(method=method), 
                                 data=data_dict, headers={"SnowShoe-Api-Key":self.api_key, "Accept-Encoding":"identity"})
        
        if response.status_code >= 500:
            return {"error": "Server error while contacting %s. Data: %s" % (
                self.get_api_url(method=method), str(data_dict)),
                    "code": 20}
        else:
            return response.json()
