# Initially copied from https://developers.google.com/calendar/quickstart/python

import datetime
import pickle
import os.path
from pprint import pprint

from pathlib import Path

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

credentials_file = Path("~/Downloads/credentials.json").expanduser()

# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
token_file = Path("~/.token.pickle").expanduser()

# If modifying these scopes, delete the token_file.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    if token_file.exists():
        with open(token_file, 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                str(credentials_file), SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_file, 'wb') as token:
            pickle.dump(creds, token)

    # Construct a Resource object with methods for interacting with the service.
    service = build('calendar', 'v3', credentials=creds)
    # https://developers.google.com/resources/api-libraries/documentation/calendar/v3/python/latest/

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events for all your subscribed calendars')

    calendars = service.calendarList().list().execute()
    # pprint(calendars)
    for cal in calendars['items']:
        print("{id} {summary} {kind} {accessRole}".format(**cal))
        print("="*50)
        events = service.events().list(
            calendarId=cal['id'], timeMin=now,
            maxResults=10, singleEvents=True,
            orderBy='startTime').execute()
        for event in events['items']:
            start_date = event['start'].get('date')
            start_time = event['start'].get('dateTime')
            summary = event.get('summary')
            recurringEventId = event.get('recurringEventId')
            # print(start, event['summary'], event['start'])
            # pprint(event)
            print("{start_date} {start_time} {summary} {recurringEventId}".format(**locals()))
        print()

if __name__ == '__main__':
    main()
