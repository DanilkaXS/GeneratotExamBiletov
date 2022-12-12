from pprint import pprint

from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'service_account.json'
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials, static_discovery=False)



# name = "TTTTESTFILE"
# specialnost = "lol"
# description = f"exam${specialnost}"
# file_metadata = {
#     'name': name,
#     'mimeType': 'application/vnd.google-apps.folder',
#     'parents': ["1md3FixnbjMBiGtEXKoBVUd1rP8OLZOE2"],
#     'description': description,
# }
# r = service.files().create(body=file_metadata, fields='id').execute()

results = service.files().list(pageSize=10,
                               fields="nextPageToken, files(id,name,description)").execute()




r = service.files().delete(fileId='1NkKUWrpqKQKCs4Rz1v7G604FZDTsww3JQ7roStWdLJw').execute()





pprint(results['files'])