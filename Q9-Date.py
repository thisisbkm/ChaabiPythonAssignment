from datetime import datetime, timedelta

def check_date_range(from_date, to_date, difference):
    date_format = "%y-%m-%d"
    try:
        from_date_obj = datetime.strptime(from_date, date_format)
        to_date_obj = datetime.strptime(to_date, date_format)
        delta = to_date_obj - from_date_obj
        if delta < timedelta(days=difference):
            return True
        else:
            return False
    except ValueError:
        return False


if __name__=="__main__":
    result = check_date_range('21-05-01', '21-05-15', 20)
    print(result)

    result = check_date_range('21-05-01', '21-06-01', 30)
    print(result)
