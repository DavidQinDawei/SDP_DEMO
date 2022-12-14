from __future__ import print_function
import  requests,pprint
payload = {
    "action":"email",
    "data":{
        "body":"test5",
        "to":"79475584@qq.com",
        "from":"dawei.qin@uconn.edu",
        "subject":"test123456",
    }
}
response = requests.post('http://localhost/users/email/', json=payload)
##
pprint.pprint(response.json())
#
#from django.http import JsonResponse
#import json
##from users.models import Users
#def email(request):
#    params = json.loads(request.body)
#    data = params['data']
#    gmail_send_message(data)
#
#

#from __future__ import print_function
#
#import base64
#from email.message import EmailMessage
#import os.path
#import google.auth
#from googleapiclient.discovery import build
#from googleapiclient.errors import HttpError
#from google.oauth2.credentials import Credentials
#from google_auth_oauthlib.flow import InstalledAppFlow
#from google.auth.transport.requests import Request
#def gmail_send_message():
#    """Create and send an email message
#    Print the returned  message id
#    Returns: Message object, including message id
#
#    Load pre-authorized user credentials from the environment.
#    TODO(developer) - See https://developers.google.com/identity
#    for guides on implementing OAuth2 for the application.
#    """
#    SCOPES = 'https://mail.google.com/'
#    creds = None
#    # The file token.json stores the user's access and refresh tokens, and is
#    # created automatically when the authorization flow completes for the first
#    # time.
#    if os.path.exists('token.json'):
#        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
#    if not creds or not creds.valid:
#        if creds and creds.expired and creds.refresh_token:
#            creds.refresh(Request())
#        else:
#            flow = InstalledAppFlow.from_client_secrets_file(
#                'credentials.json', SCOPES)
#            creds = flow.run_local_server(port=0)
#        # Save the credentials for the next run
#        with open('token.json', 'w') as token:
#            token.write(creds.to_json())
#
#    try:
#        service = build('gmail', 'v1', credentials=creds)
#        message = EmailMessage()
#
#        message.set_content('This is automated draft mail')
#
#        message['To'] = '79475584@qq.com'
#        message['From'] = 'dawei.qin@uconn.edu'
#        message['Subject'] = 'Automated draft'
#
#        # encoded message
#        encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
#            .decode()
#
#        create_message = {
#            'raw': encoded_message
#        }
#        # pylint: disable=E1101
#        send_message = (service.users().messages().send
#                        (userId="me", body=create_message).execute())
#        print(F'Message Id: {send_message["id"]}')
#    except HttpError as error:
#        print(F'An error occurred: {error}')
#        send_message = None
#    return send_message
#
#
#if __name__ == '__main__':
#    gmail_send_message()