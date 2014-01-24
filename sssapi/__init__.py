import requests
from requests_oauthlib  import OAuth1

class Client(object):
    BASE_URL = "http://beta.snowshoestamp.com/api/v2/"
    app_key = None
    app_secret = None

    def __init__(self, app_key=None, app_secret=None):
        self.app_key = app_key
        self.app_secret = app_secret
    
    def get_api_url(self, method):
        return "%s%s" % (self.BASE_URL, method)

    def get_auth(self):
        return OAuth1(self.app_key, self.app_secret,
                      signature_type='auth_header')
    auth = property(get_auth, )
    
    def call(self, data_dict=None, method="stamp"):
        response = requests.post(self.get_api_url(method=method), 
                                 data=data_dict, auth=self.auth)
        
        if response.status_code >= 500:
            return {"error": "Server error while contacting %s. Data: %s" % (
                self.get_api_url(method=method), str(data_dict)),
                    "code": 20}
        else:
            return response.json()
