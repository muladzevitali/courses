from random import normalvariate, randint
from itertools import count, groupby, filterfalse, islice
from datetime import datetime

from scipy.stats import normaltest


def read_fake_data():
    for timestamp in count():
        if randint(0, 7 * 60 * 60 * 24 - 1) == 1:
            value = normalvariate(0, 1)
        else:
            value = 100

        yield datetime.fromtimestamp(timestamp), value


def group_by_day(iterable):
    for day, group_data in groupby(iterable, key=lambda row: row[0].day):
        yield list(group_data)


def is_normal(data, threshold=1e-3):
    _, values = zip(*data)
    k2, p_value = normaltest(values)
    if p_value < threshold:
        return False
    return True


def filter_anomalous_groups(data):
    yield from filterfalse(is_normal, data)


def filter_anomalous_data(data):
    group_data = group_by_day(data)
    yield from filter_anomalous_groups(group_data)


if __name__ == '__main__':
    data = read_fake_data()
    anomaly_generator = filter_anomalous_data(data)
    first_five_anomalies = islice(anomaly_generator, 5)

    for data_anomaly in first_five_anomalies:
        start_date = data_anomaly[0][0]
        end_date = data_anomaly[-1][0]
        print(f"Anomaly from {start_date} to {end_date}")
