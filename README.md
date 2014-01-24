
#Python SDK Instructions#

1.These instructions assume you are using Django. Once you’ve downloaded the SDK, unzip it. The unzipped folder will be called snowshoe. Inside snowshoe, open api, then python, then sssapi. Here you will see __init__.py You can drop the sssapi folder containing __init__.py into your codebase as its own app, so go ahead and do that to get started.

2. To get the app running, you will need to register on our site. Go to beta.snowshoestamp.com and click Log In. Now, log in (or sign up for an account), and then, when you are logged in, click “New App” to register an app with us. The only required fields are name and callback url, and this callback url is whatever URL you are using for the view that will recieve data from the stamp screen

3. The address of the stamp screen is:

https://beta.snowshoestamp.com/applications/client/<your app key here>

The first step in making your app work is forwarding the user to that address, replacing <your app key> with the app key you can find on your Application page on our site.

4. In __init__.py, you will see a Client object. You will also note we import requests and requests_oauthlib. You will need these installed on your server:

 pip install requests requests_oauthlib

5. Finally, you will need to create a view that recieves data from the stamp screen (the POSTed coordinates) and passes them to our API using the Client object. This view should be accessible via the URL you registered as the callback for your app on our site:

 
from sssapi import Client
from django.shortcuts import render_to_response

def callback(request):
 client = Client(app_key=”your app key here!”, app_secret=”your app secret here!”)
 response = client.call({“data”: request.POST[‘data’]})

 if response.has_key(‘stamp’):
 if response[‘stamp’][‘serial’] == “DEV-STAMP”:
 return render_to_response(“authorized_page.html”, 
 {},
 RequestContext(request, {}))

