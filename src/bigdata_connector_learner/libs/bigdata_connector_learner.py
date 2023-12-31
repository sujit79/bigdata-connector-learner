import requests
import json
import pandas as pd

headers = {
      'Content-Type': "application/json",
}

def execute(verb, url, body):
  #
  
  res = None
  # Make API request, get response object back, create dataframe from above schema.
  try:
    if verb == "get":
      res = requests.get("{url}".format(url=url), data=body, headers=headers)
    else:
      res = requests.post("{url}".format(url=url), data=body, headers=headers)
  except Exception as e:
    return e
 
  if res != None and res.status_code == 200:
    return json.loads(res.text)
  return None


def get_data_frame(verb, url, body):
    result = execute(verb, url, body)
    df = pd.read_json(result)

    return df

    
  