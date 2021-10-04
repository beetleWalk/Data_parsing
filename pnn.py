import pandas as pd


def conversion(text):
    return text.lower()

def correct_date(date_field):


def correct_gender(gender_field):


def parse_csv(csv_file, date_cols, gender_col):
    df = pd.read_csv(csv_file)
    for col in date_cols:
        df[col] = df[col].apply(correct_date)

    df[gender_col] = df[gender_col].apply(correct_gender)
    # print(df["Subject"])

if __name__ == '__main__':
    csv_file = "AssignmentData.csv"
    date_cols = ["Date of Service", "Date of Birth"]
    gender_col = "gender2"
    parse_csv(csv_file, date_cols, gender_col)
