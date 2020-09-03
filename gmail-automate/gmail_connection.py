import os
import pickle

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class GMAIL_CONNECTION:

    def __init__(self):
        self.__SCOPES = [
            'https://www.googleapis.com/auth/gmail.readonly',
            'https://www.googleapis.com/auth/gmail.labels',
            'https://www.googleapis.com/auth/gmail.modify'
        ]
        self.__TOKEN = 'token.pickle'
        self.__USER_ID = 'me'
        self.__creds = None

    def get_creds(self):

        if os.path.exists(self.__TOKEN):

            with open(self.__TOKEN, 'rb') as token:
                return pickle.load(token)

        if not self.__creds or not self.__creds.valid:

            if self.__creds and self.__creds.expired and self.__creds.refresh_token:
                self.__creds.refresh(Request())

            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.__SCOPES)
                self.__creds = flow.run_local_server(port=0)

            with open(self.__TOKEN, 'wb') as token:
                pickle.dump(self.__creds, token)

        return self.__creds

    def get_service(self):
        return build('gmail', 'v1', credentials=self.get_creds()).users()

    def get_messages_or_threads(view='', mail_id="", attach_id="") -> str:
        mail_string = "get_service().{0}()".format(view)
        exe_string = ".execute()"

        if mail_id:

            if attach_id:

                attach_string = ".attachments().get(userId='{0}', messageId='{1}', id='{2}')".format(
                    USER_ID, mail_id, attach_id)
                return mail_string + attach_string + exe_string

            item_String = ".get(userId='{0}', id='{1}')".format(
                USER_ID, mail_id)
            return mail_string + item_String + exe_string

        list_string = ".list(userId='{1}'){2}.get('{0}', [])".format(
            view, USER_ID, exe_string)
        return mail_string + list_string
