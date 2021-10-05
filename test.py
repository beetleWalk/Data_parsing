import pandas as pd
import datetime

def correct_date(str):
    # Check that the date field is in the format of either M/DD/YY or MM/DD/YY

    import re
    # all = re.findall(r"[1-9]|[[1][0-2]]/[\d]{1,2}/[\d]{2}", str)
    prog = re.compile(r"([1-9]|[1][0-2])/([1-9]|[1|2][0-9]|[3][0|1])/([0-9]{2})")
    result = prog.match(str)

    if result:
        print("Search successful.")
        print(re.split("\s", str))
    else:
        print("Search unsuccessful.")

if __name__ == '__main__':
    correct_date("10/31/10")
