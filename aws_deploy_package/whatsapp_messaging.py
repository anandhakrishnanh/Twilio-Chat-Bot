from twilio.rest import Client
import requests

def message(event=None, context=None):
    # getting the quote of the day
    url = "http://www.forbes.com/forbesapi/thought/uri.json?enrich=true&query=1&relatedlimit=5"
    response = requests.get(url)
    data = response.json()
    quote = data['thought']["quote"]
    message = 'Hello, Good Morning!\n\n\nThis is an automated message sent by Anandha Krishnan H, if you do not want to get these messages please contact him\n\n\nQuote ' \
              'for the day :' + quote

    account_sid = 'AC5cf37d1ff48d4d1325396e4f11dfb3a5'  # <account sid> here
    auth_token = 'a8474727b1785cf161b6752515b2f230'  # <auth_token> here

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body= message,
        to='whatsapp:+918111828059' # <Add the number you want to send it to>
    )

    print(message.sid)
