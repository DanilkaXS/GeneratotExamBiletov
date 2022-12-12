from google.oauth2 import service_account
from googleapiclient.discovery import build
import requests
from flask import Flask, render_template, url_for, request
import json

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/help')
def help_page():
    return render_template('help.html')


@app.route('/postrequest', methods=['POST'])
def post_req():
    data = json.loads(request.data)
    SCOPES = ['https://www.googleapis.com/auth/drive']
    SERVICE_ACCOUNT_FILE = 'service_account.json'
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=credentials, static_discovery=False)

    file_metadata = {
        'name': data['document']['nameDocument'],
        'mimeType': 'application/vnd.google-apps.document',
        'parents': ["1md3FixnbjMBiGtEXKoBVUd1rP8OLZOE2"],
    }
    r = service.files().create(body=file_metadata, fields='id').execute()
    results = service.files().list(pageSize=10,
                                   fields="nextPageToken, files(id,name,description)").execute()
    for i in results['files']:
        print(i)
        try:
            if i['name'] == data['document']['nameDocument']:
                data['id'] = i['id']
                print(i['name'])
        except:
            continue
    requests.post(
        "https://script.google.com/macros/s/AKfycbx4f_AUSt1lmP57xmSi4fOJt3zDeFAwSJ0bX1b09-3uDxbmlEyVjtv9GksdRgdjZCsFrA/exec",
        json=data)

    return data['id']


if __name__ == '__main__':
    app.run()
