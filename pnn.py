import pandas as pd
import datetime

def conversion(text):
    return text.lower()

def correct_date(date_field):
    current_date = datetime.datetime.now()
    date = current_date.date()
    curr_year = date.strftime("%Y")
    month_31 = [1, 3, 5, 7, 8, 10, 12]
    month_30 = [4, 6, 9, 11]

    month, day, year = date_field.split('/')

    if year > curr_year or year < 0:
        date_field = 'None'

    if month < 1 or month > 12:
        date_field = 'None'

    if day < 1 or (day > 31 and month not in month_31):
        date_field = 'None'

    if day < 1 or (day > 30 and month not in month_30):
        date_field = 'None'


def correct_gender(gender_field):
    gender = gender_field.conversion()
    if gender != "male" or gender != "female":
        gender_field = ''


def age_calc(service_field):
    service_date = service_field
    current_date = datetime.datetime.now()
    today = current_date.date()
    service_age = today.year - service_date.year - ((today.month, today.day) < (service_date.month, service_date.day))
    return service_age

def parse_csv(csv_file, date_cols, gender_col):
    df = pd.read_csv(csv_file)
    for col in date_cols:
        df[col] = df[col].apply(correct_date)

    df[gender_col] = df[gender_col].apply(correct_gender)
    # print(df["Subject"])

def deIdentify_data():
    #add column for age at service
    #remove date of birth and service
    #


if __name__ == '__main__':
    csv_file = "AssignmentData.csv"
    date_cols = ["Date of Service", "Date of Birth"]
    gender_col = "gender2"
    parse_csv(csv_file, date_cols, gender_col)
