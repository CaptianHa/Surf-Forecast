from email import header
import pandas as pd
from twilio.rest import Client
import keys

client = Client(keys.account_sid, keys.auth_tocken)

df = pd.read_html('https://www.surf-forecast.com/breaks/Talofofo/forecasts/latest')



column1a = str(df[0].iat[0,0])
column1b = str(df[0].iat[1,0])
column1c = str(df[0].iat[2,0])

column2a = str(df[0].iat[0,1])
column2b = str(df[0].iat[1,1])
column2c = str(df[0].iat[2,1])

column3a = str(df[0].iat[0,2])
column3b = str(df[0].iat[1,2])
column3c = str(df[0].iat[2,2])


header1 = "Time                      Height              P.\n"
message1 = column1a + "    " + column2a + "    " + column3a + "\n"
message2 = column1b + "    " + column2b + "    " + column3b + "\n"
message3 = column1c + "    " + column2c + "    " + column3c + "\n"


messageFinal= header1+message1+message2+message3

message = client.messages.create(
    
    body = messageFinal,
    from_ = keys.twilio_number,
    to = keys.target_number

)

