import datetime
import pytz

# from pprint import pprint
# _raw = '''
# 2010,28 March 01:00,31 October 02:00
# 2011,27 March 01:00,30 October 02:00
# 2012,25 March 01:00,28 October 02:00
# 2013,31 March 01:00,27 October 02:00
# 2014,30 March 01:00,26 October 02:00
# 2015,29 March 01:00,25 October 02:00
# 2016,27 March 01:00,30 October 02:00
# 2017,26 March 01:00,29 October 02:00
# 2018,25 March 01:00,28 October 02:00
# 2019,31 March 01:00,27 October 02:00
# 2020,29 March 01:00,25 October 02:00
# 2021,28 March 01:00,31 October 02:00
# 2022,27 March 01:00,30 October 02:00
# 2023,26 March 01:00,29 October 02:00
# 2024,31 March 01:00,27 October 02:00
# 2025,30 March 01:00,26 October 02:00
# 2026,29 March 01:00,25 October 02:00
# 2027,28 March 01:00,31 October 02:00
# 2028,26 March 01:00,29 October 02:00
# 2029,25 March 01:00,28 October 02:00
# '''

# t = {int(l[0]): (
#         datetime.datetime.strptime(f'{l[0]} {l[1]}', '%Y %d %B %H:%M'),
#         datetime.datetime.strptime(f'{l[0]} {l[2]}', '%Y %d %B %H:%M'),
#     ) for l in tuple(l.split(',') for l in _raw.strip().split('\n'))}

# pprint(t)


_bstRanges = {
    2010: (datetime.datetime(2010, 3, 28, 1, 0), datetime.datetime(2010, 10, 31, 2, 0)),
    2011: (datetime.datetime(2011, 3, 27, 1, 0), datetime.datetime(2011, 10, 30, 2, 0)),
    2012: (datetime.datetime(2012, 3, 25, 1, 0), datetime.datetime(2012, 10, 28, 2, 0)),
    2013: (datetime.datetime(2013, 3, 31, 1, 0), datetime.datetime(2013, 10, 27, 2, 0)),
    2014: (datetime.datetime(2014, 3, 30, 1, 0), datetime.datetime(2014, 10, 26, 2, 0)),
    2015: (datetime.datetime(2015, 3, 29, 1, 0), datetime.datetime(2015, 10, 25, 2, 0)),
    2016: (datetime.datetime(2016, 3, 27, 1, 0), datetime.datetime(2016, 10, 30, 2, 0)),
    2017: (datetime.datetime(2017, 3, 26, 1, 0), datetime.datetime(2017, 10, 29, 2, 0)),
    2018: (datetime.datetime(2018, 3, 25, 1, 0), datetime.datetime(2018, 10, 28, 2, 0)),
    2019: (datetime.datetime(2019, 3, 31, 1, 0), datetime.datetime(2019, 10, 27, 2, 0)),
    2020: (datetime.datetime(2020, 3, 29, 1, 0), datetime.datetime(2020, 10, 25, 2, 0)),
    2021: (datetime.datetime(2021, 3, 28, 1, 0), datetime.datetime(2021, 10, 31, 2, 0)),
    2022: (datetime.datetime(2022, 3, 27, 1, 0), datetime.datetime(2022, 10, 30, 2, 0)),
    2023: (datetime.datetime(2023, 3, 26, 1, 0), datetime.datetime(2023, 10, 29, 2, 0)),
    2024: (datetime.datetime(2024, 3, 31, 1, 0), datetime.datetime(2024, 10, 27, 2, 0)),
    2025: (datetime.datetime(2025, 3, 30, 1, 0), datetime.datetime(2025, 10, 26, 2, 0)),
    2026: (datetime.datetime(2026, 3, 29, 1, 0), datetime.datetime(2026, 10, 25, 2, 0)),
    2027: (datetime.datetime(2027, 3, 28, 1, 0), datetime.datetime(2027, 10, 31, 2, 0)),
    2028: (datetime.datetime(2028, 3, 26, 1, 0), datetime.datetime(2028, 10, 29, 2, 0)),
    2029: (datetime.datetime(2029, 3, 25, 1, 0), datetime.datetime(2029, 10, 28, 2, 0)),
}


def in_daylight_saving(dt):
    bstStart, bstEnd = _bstRanges[dt.year]
    return bstStart <= dt <= bstEnd


def add_local_timezone(dt, hoursDiff=None):
    if hoursDiff is None:
        try:
            if in_daylight_saving(dt):
                # https://stackoverflow.com/questions/4008960/pytz-and-etc-gmt-5
                tz = pytz.timezone("Etc/GMT-1")
            else:
                tz = pytz.timezone("Etc/GMT")
        except KeyError:
            tz = pytz.timezone("Etc/GMT")
    else:
        tz = pytz.timezone("Etc/GMT{0:+d}".format(hoursDiff))

    return dt.replace(tzinfo=tz)


def add_utc_timezone(dt):
    return dt.replace(tzinfo=datetime.timezone.utc)


def local_to_utc(dt):
    if dt.tzinfo is None:
        dt = add_local_timezone(dt)
    return dt.astimezone(datetime.timezone.utc).replace(tzinfo=None)


def to_local_time(dt):
    try:
        if in_daylight_saving(dt.replace(tzinfo=None)):
            # https://stackoverflow.com/questions/4008960/pytz-and-etc-gmt-5
            tz = pytz.timezone("Etc/GMT-1")
        else:
            tz = pytz.timezone("Etc/GMT")
    except KeyError:
        tz = pytz.timezone("Etc/GMT")

    return dt.astimezone(tz)
