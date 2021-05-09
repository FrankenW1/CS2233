class Duration:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __add__(self, other):
        if not isinstance(other, Duration):
            return 'oops'
        total_hours = self.hours + other.hours
        total_minutes = self.minutes + other.minutes
        if total_minutes >= 60:
            total_hours += 1
            total_minutes -= 60
        return Duration(total_hours, total_minutes)
  
one_way_time = Duration(3, 46)
round_trip_time = one_way_time + one_way_time

print(one_way_time + 56)
print(round_trip_time.hours, round_trip_time.minutes)
