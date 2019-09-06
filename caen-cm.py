# stats velo @ Caen

import pprint
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import matplotlib.pyplot as plt

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Copy of CompteursCaen").sheet1

pp = pprint.PrettyPrinter()

def main():

    result = sheet.get_all_records()
    pp.pprint(result)

