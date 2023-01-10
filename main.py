from email import header
import pandas as pd
from twilio.rest import Client
import keys

client = Client(keys.account_sid, keys.auth_tocken)

df = pd.read_html('https://www.surf-forecast.com/breaks/Talofofo/forecasts/latest', skiprows=[0])

headers = ["Time", "Height", "Period"] 
# df.columns = headers
message_int = header


message_int = str(df)


message = client.messages.create(
    
    body = message_int,
    from_ = keys.twilio_number,
    to = keys.target_number

)

print(message_int)