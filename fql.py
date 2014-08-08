import urllib
import json

def get_json(query, access_token):
  params = urllib.urlencode({'q':query, 'access_token':access_token});
  url = "https://graph.facebook.com/fql?"+params;
  data = urllib.urlopen(url).read();
  rjson = json.loads(data);
  return rjson;

