from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
# note you need to import to the sib_api_v3_sdk to install this exeute the cmd pip install sib_api_v3_sdk or pip3 install sib_api_v3_sdk

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = 'your_api_here'

api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
subject = "My Subject"
html_content = "<html><body><h1>kaiso ho  </h1></body></html>"
sender = {"name":"Prince","email":"Example.com"}
to = [{"email":"example.com","name":"Jane Doe"}]
cc = [{"email":"example2@example2.com","name":"Janice Doe"}]
bcc = [{"name":"John Doe","email":"example@example.com"}]
reply_to = {"email":"replyto@domain.com","name":"John Doe"}
headers = {"Some-Custom-Name":"unique-id-1234"}
params = {"parameter":"My param value","subject":"HI there"}
send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, bcc=bcc, cc=cc, reply_to=reply_to, headers=headers, html_content=html_content, sender=sender, subject=subject)

try:
    api_response = api_instance.send_transac_email(send_smtp_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
