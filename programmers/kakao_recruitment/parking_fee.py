import math


def solution(fees, records):
    answer = []
    time_record = {}
    fee_record = {}
    limit_time, base_fee, unit_time, unit_fee = fees
    for record in records:
        time, car_no, type_in_out = record.split(" ")
        if car_no not in time_record:
            time_record[car_no] = [time]
        else:
            calculate_parking_time(time_record, fee_record, car_no, time)
            time_record.pop(car_no, None)

    for car_no in time_record:
        calculate_parking_time(time_record, fee_record, car_no, "23:59")

    for car_no in sorted(fee_record):
        time = fee_record[car_no]
        if time <= limit_time:
            answer.append(base_fee)
        else:
            answer.append(base_fee + math.ceil((time - limit_time) / unit_time) * unit_fee)
    return answer


def calculate_parking_time(time_record, fee_record, car_no, time):
    before_hour, before_min = time_record[car_no][0].split(":")
    after_hour, after_min = time.split(":")
    parked_min = to_minute(after_hour, after_min) - to_minute(before_hour, before_min)
    fee_record[car_no] = fee_record.get(car_no, 0) + parked_min


def to_minute(hour, minute):
    return int(hour) * 60 + int(minute)


print(
    solution(
        [180, 5000, 10, 600],
        [
            "05:34 5961 IN",
            "06:00 0000 IN",
            "06:34 0000 OUT",
            "07:59 5961 OUT",
            "07:59 0148 IN",
            "18:59 0000 IN",
            "19:09 0148 OUT",
            "22:59 5961 IN",
            "23:00 5961 OUT"
        ]
    ) == [14600, 34400, 5000]
)
