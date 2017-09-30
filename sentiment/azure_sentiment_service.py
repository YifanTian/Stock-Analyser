# -*- coding: utf-8 -*-

import httplib, urllib
import json

# **********************************************
# *** Update or verify the following values. ***
# **********************************************

# Replace the accessKey string value with your valid access key.
accessKey = '5011f466eab04d7fabe0a3afae93d3ff'

# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your access keys.
# For example, if you obtained your access keys from the westus region, replace 
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial access keys are generated in the westcentralus region, so if you are using
# a free trial access key, you should not need to change this region.
uri = 'westus.api.cognitive.microsoft.com'
path = '/text/analytics/v2.0/sentiment'

def GetSentiment (text):
    "Gets the sentiments for a set of documents and returns the information."
    documents = { 'documents': [
        { 'id': '1', 'language': 'en', 'text': text },
    ]}
    headers = {'Ocp-Apim-Subscription-Key': accessKey}
    conn = httplib.HTTPSConnection (uri)
    body = json.dumps (documents)
    conn.request ("POST", path, body, headers)
    response = conn.getresponse ()
    # return response.read ()
    print(json.loads(response.read()).keys())
    # return json.loads(response.read())["documents"][0]["score"]

# documents = { 'documents': [
#     { 'id': '1', 'language': 'en', 'text': 'I really enjoy the new XBox One S. It has a clean look, it has 4K/HDR resolution and it is affordable.' },
#     { 'id': '2', 'language': 'es', 'text': 'Este ha sido un dia terrible, llegué tarde al trabajo debido a un accidente automobilistico.' }
# ]}

if __name__ == "__main__":
    print 'Please wait a moment for the results to appear.\n'

    result = GetSentiment('I do it!')
    print(result)
    # print(json.loads(result)["documents"][0]["score"])
    # print (json.dumps(json.loads(result), indent=4))