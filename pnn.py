import pandas as pd
import datetime
import re
import calendar
import logging

logging.basicConfig(filename='edits.log', level=logging.WARNING)
PATTERN = r"([1-9]|[1][0-2])/([1-9]|[1|2][0-9]|[3][0|1])/([0-9]{2})"
REGEX = re.compile(PATTERN)


def date_log(date_field):
    empty = ''
    logging.warning('%s appears to be corrupted and is therefore being overwritten with a empty string', date_field)
    return empty


def conversion(text):
    return text.lower()


def correct_date(date_field):
    current_date = datetime.datetime.now().date()
    curr_year = current_date.strftime("%Y")
    month_31 = [1, 3, 5, 7, 8, 10, 12]

    # Check that the date field is in the format of either M/DD/YY or MM/DD/YY
    match = REGEX.match(date_field)

    if match:
        try:
            result = datetime.datetime.strptime(date_field, "%m/%d/%y")
        except ValueError:
            return date_log(date_field)
    else:
        return date_log(date_field)

    day = result.day
    month = result.month
    year = str(result.year)

    if year > curr_year[-2:]:
        year = "19" + year
    else:
        year = "20" + year

    if year > curr_year or year < "1900":
        logging.warning("Year is invalid")
        return date_log(date_field)

    if day > 30 and month not in month_31:
        logging.warning("Cannot have day greater than 30 in a month with less than 31 days")
        return date_log(date_field)

    if month == 2:
        if calendar.isleap(int(year)) and day > 29:
            logging.warning("Cannot have day greater than 29 in Feb on a leap year")
            return date_log(date_field)
        elif day > 28:
            logging.warning("Cannot have day greater than 28 in Feb on a non-leap year")
            return date_log(date_field)

    return date_field


def correct_gender(gender_field):
    gender = conversion(gender_field)
    if gender != "male" and gender != "female":
        male_set = ['m', 'a', 'l', 'e']
        # Check for gender containing all characters in string "male"
        if 0 not in [char in gender for char in male_set]:
            if "f" in gender:
                logging.warning("Gender field %s appears to be female and is being corrected as such", gender_field)
                return "Female"
            else:
                logging.warning("Gender field  %s appears to be male and is being corrected as such", gender_field)
                return "Male"
        else:
            logging.warning("Unable to decipher potential gender from gender field %s, will be overwritten by Unknown",
                            gender_field)
            return "Unknown"

    return gender_field


def age_calc(service_field, birth_date):
    # get year from service date
    service_year = service_field[-2:]
    birth_year = birth_date[-2:]
    current_date = datetime.datetime.now()
    today_year = current_date.strftime("%Y")

    if service_year > today_year:
        service_year = "19" + service_year

    else:
        service_year = "20" + service_year

    service_age = int(service_year) - int(birth_year)
    return str(service_age)


# def add_age_col(service_field):
#     service_age = []
#     for i in service_field:
#         age_at_service = age_calc(service_field)
#         service_age.append(age_at_service)
#
#     deIdentified_data = assignment_df.assign(service_age=service_age)
#     return deIdentified_data


def zipcode_modif(zipcode_field):
    # keeps the three initial zipcode digits
    zipcode_init = str(zipcode_field)[:3]
    return zipcode_init


def join_df(original_df, extra_df):
    merged_df = pd.merge(original_df, extra_df, on='Race', how='left')
    return merged_df


def parse_csv(csv_file):
    df = pd.read_csv(csv_file)
    return df


def deidentify_data(dataframe):
    # deletes Date of Birth and Date of Service columns
    return dataframe.drop(columns=['Date of Service', 'Date of Birth'])


if __name__ == '__main__':
    assignment_data = "AssignmentData.csv"
    median_income = "income.csv"

    date_cols = ["Date of Service", "Date of Birth"]
    gender_col = "gender2"
    assignment_df = parse_csv(assignment_data)

    # correct gender misspelling
    assignment_df[gender_col] = assignment_df[gender_col].apply(correct_gender)

    # check for date errors
    for col in date_cols:
        assignment_df[col] = assignment_df[col].apply(correct_date)

    # save cleaned dataset to Assignment Data Cleaned.csv without index column
    assignment_df.to_csv("Assignment Data Cleaned.csv", index=False)

    # load income dataset
    income_df = parse_csv(median_income)

    # left join cleaned dataset with income dataset
    joined_df = pd.merge(assignment_df, income_df, left_on='Race', right_on='Race', how='left')
    # joined_df = join_df(assignment_df, income_df)

    joined_df["Age of Service"] = joined_df.apply(lambda x: age_calc(x["Date of Service"], x["Date of Birth"]),
                                                   axis=1)

    joined_df["Zipcode"] = joined_df["Zipcode"].apply(zipcode_modif)

    # joined_df["Date of Service"] = joined_df["Date of Service"].apply(add_age_col)

    deIdentified_df = deidentify_data(joined_df)

    deIdentified_df.to_csv("Deindentified Data Cleaned.csv", index=False)
