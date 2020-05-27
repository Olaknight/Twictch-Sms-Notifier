import requests
from twilio.rest import Client

client = Client(<Account SID>, <Auth Token>)

endpoint = 'https://api.twitch.tv/helix/streams?'
headers = {'Client=ID': "<Client-ID>"}
params = {'user_login': 'Solary'}
response = requests.get(endpoint=endpoint, params=params, headers=header)
json_response = response.json()
streams = json_response.get('data', [])
is_active = lambda streams: streams.get('type') == 'live'
streams_active = filter(is_active, streams)
at_least_one_stream_active = any(streams_active)
last_messages_sent = client.messages.list(limit=1)

if last_messages_sent:
    last_messages_id = last_messages_sent[0].sid
    last_messages_data = client.messages(last_messages_id).fetch()
    last_messages_content = last_messages_data.body
    online_notified = "Live" in last_messages_content
    offline_notified = not online_notified

else:
    online_notified, offline_notified = False, False

if at_least_one_stream_active and not online_notified:
    client.messages.create(body='LIVE!!', from_ < Trial number >, to = < Real phone Number > )
if not at_least_one_stream_active and offline_notified:
    client.messages.create(body='Offline!!', from_ < Trial number >, to = < Real phone Number > )
