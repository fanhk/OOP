__author__ = 'fhk'
# coding=gbk

from twilio.rest import TwilioRestClient

account_sid = "ACcb175e27f187cea744f47adcf549623b"
auth_token = "88fae92fa4cff57781d5c84ea5370a0f"
client = TwilioRestClient(account_sid, auth_token)
message = client.sms.messages.create(body="duang~~~duang~~~duang~~~",
                                     to="+8613577047328",
                                     from_="+18452606517")
print message.sid
