# stats velo @ Caen

import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import matplotlib.pyplot as plt

# Preps google
scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]
creds = ServiceAccountCredentials.from_json_keyfile_name(
    'client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Copy of CompteursCaen").sheet1

# Date
date_du_jour = datetime.datetime.today().strftime('%d-%m-%Y')
sheet.update_cell(3, 2, date_du_jour)

# Values
dates = sheet.col_values(1)
dates = dates[5:]
values = sheet.col_values(2)
values = values[5:]

# Graph
plt.plot(dates, values)
plt.xlabel('date')
plt.ylabel('Nombres de cyclistes')
plt.title('Evolution du nombre de cyclistes @ Caen depuis avril 2018')


def main():
    plt.show()


if __name__ == "__main__":
    main()
