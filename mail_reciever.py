from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.


def get_mails(last_num=10):
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    results = service.users().messages().list(userId='me', labelIds=["INBOX"]).execute()
    messages = results.get('messages', [])
    # Mail container list
    mails = list()
    if not messages:
        print('No mails have found.')
    else:
        print('Getting mails...')
        for message in messages[:last_num]:
            msg = service.users().messages().get(userId="me", id=message["id"]).execute()
            msg["snippet"] = str(msg["snippet"])
            mails.append(msg["snippet"])
            
    return mails

if __name__ == "_main__":
    get_mails(5)