from datetime import datetime, timedelta

def beforeDay(date, days):
    date_format = "%y-%m-%d"
    try:
        date = datetime.strptime(date, date_format)
        back = date - timedelta(days=days)
        return back.strftime(date_format)
    except ValueError:
        return False

if __name__=="__main__":
    result = beforeDay('21-05-01', 20)
    print(result)