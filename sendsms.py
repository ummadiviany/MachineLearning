

#account_sid=os.environ["TWILIO_ACCOUNT_SID"]
#auth_token=os.environ["TWILIO_AUTH_TOKEN"]
account_sid='AC167f35105be04139dcdffac84bb41d31'
#account_sid='PN5d1b41f64151695f8101673874d0c934'
while True:
    import os
    from twilio.rest import Client
    import schedule
    import time
    account_sid='AC167f35105be04139dcdffac84bb41d31'
    auth_token='d946954600bc7b9477b893d638a90e23'

    Client=Client(account_sid,auth_token)
    Client.messages.create(
        to='+919490304798',
        from_='+18317041254',
        body="akapak parak"
    )
    time.sleep(30)
