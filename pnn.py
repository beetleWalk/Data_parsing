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

    # Check that the date field is in the format of either M/DD/YY or MM/DD/YY

    import re

    # Matching capital letters

    str = "01/09/02"
    # all = re.findall(r"[1-9]|[[1][0-2]]/[\d]{1,2}/[\d]{2}", str)
    # prog = re.compile(r"[1-9]|[1|2][0-9]/[1-9]|[1|2][0-9]|[3][0|1]/[0-9]{2}")
    prog = re.match(r"[1-9]|[1|2][0-9]/[1-9]|[1|2][0-9]|[3][0|1]/[0-9]{2}", "01/09/02")
    result = prog.match(string)

    # [1-9] this is if the month is between 1 and 9
    # [1][0-2] this is if the month is 10, 11, or 12

    for s in all:
        print(s)

    # try:
    #     datetime.datetime.strptime(date_field, "%m/%d/%y")
    # except ValueError as err:
    #     print(err)

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
    if gender != "male" and gender != "female":
        male_set = ['m', 'a', 'l', 'e']
        # Check for gender containing all characters in string "male"
        if 0 not in [char in gender for char in male_set]:
            if "f" in gender:
                return "Female"
            else:
                return "Male"
        else:
            return "Unknown"

def age_calc(service_field):
    service_date = service_field
    current_date = datetime.datetime.now()
    today = current_date.date()
    service_age = today.year - service_date.year - ((today.month, today.day) < (service_date.month, service_date.day))
    return service_age


def add_age_col(dataframe):
    age_at_service = age_calc()
    deIdentified_data = dataframe.assign(age_at_service)
    return deIdentified_data

def parse_csv(csv_file, date_cols, gender_col):
    df = pd.read_csv(csv_file)
    for col in date_cols:
        df[col] = df[col].apply(correct_date)

    df[gender_col] = df[gender_col].apply(correct_gender)
    # print(df["Subject"])

def zipcode_modif():


def deIdentify_data(dataframe):
    #call add_age_col

    dataframe.drop(columns=['Date of Service', 'Date of Birth'])

    #call zip_code_modif



if __name__ == '__main__':
    csv_file = "AssignmentData.csv"
    date_cols = ["Date of Service", "Date of Birth"]
    gender_col = "gender2"
    parse_csv(csv_file, date_cols, gender_col)
