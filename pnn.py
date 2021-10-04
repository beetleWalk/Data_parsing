import pandas as pd
import datetime
import re
import calendar

PATTERN = r"([1-9]|[1][0-2])/([1-9]|[1|2][0-9]|[3][0|1])/([0-9]{2})"
REGEX = re.compile(PATTERN)

def conversion(text):
    return text.lower()

def correct_date(date_field):
    current_date = datetime.datetime.now().date()
    curr_year = current_date.strftime("%Y")
    month_31 = [1, 3, 5, 7, 8, 10, 12]
    empty = ''

    # Check that the date field is in the format of either M/DD/YY or MM/DD/YY
    match = REGEX.match(date_field)

    if match:
        try:
            result = datetime.datetime.strptime(date_field, "%m/%d/%y")
        except ValueError:
            return empty
    else:
        return empty

    day = result.day
    month = result.month
    year = str(result.year)

    if year > curr_year[-2:]:
        year = "19" + year
    else:
        year = "20" + year

    if year > curr_year or year < "1900":
        return empty

    if day > 30 and month not in month_31:
        return empty

    if month == 2:
        if calendar.isleap(year) and day > 29:
            return empty
        elif day > 28:
            return empty

    return date_field

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
    call add_age_col

    dataframe.drop(columns=['Date of Service', 'Date of Birth'])

    call zip_code_modif



if __name__ == '__main__':
    csv_file = "AssignmentData.csv"
    date_cols = ["Date of Service", "Date of Birth"]
    gender_col = "gender2"
    parse_csv(csv_file, date_cols, gender_col)