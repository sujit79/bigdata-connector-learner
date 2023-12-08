# Big Data Connector Learner
Helps in connecting with Big Data (Not Hadoop, but the actual data source) Using REST (currently only supported).

# Design
Connect to Data  and then query and convert to Pandas Data Frame

# Usage
python bigdata_connector_learner\main.py get $verb $url $body

$verb is get or post (capital does matter)
$url is the url which gives response
$body is the body of the request

# Requirements

python -m pip install -r requirements.txt 



