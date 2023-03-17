import datetime

class MarsTime:
    def __init__(self, utc_time):
        self.utc_time = utc_time
        self.julian_date = self._calculate_julian_date()
        self.mars_sol_date = self._calculate_mars_sol_date()
        self.mars_coordinated_time = self._calculate_mars_coordinated_time()

    def _calculate_julian_date(self):
        a = (14 - self.utc_time.month) // 12
        y = self.utc_time.year + 4800 - a
        m = self.utc_time.month + 12 * a - 3
        jdn = self.utc_time.day + ((153 * m + 2) // 5) + 365 * y + (y // 4) - (y // 100) + (y // 400) - 32045
        return jdn + (self.utc_time.hour - 12) / 24 + self.utc_time.minute / 1440 + self.utc_time.second / 86400

    def _calculate_mars_sol_date(self):
        return (self.julian_date - 2451549.5) / 1.027491252 + 44796.0 - 0.00096

    def _calculate_mars_coordinated_time(self):
        mct_hours = (self.mars_sol_date % 1) * 24
        mct_minutes = (mct_hours % 1) * 60
        mct_seconds = (mct_minutes % 1) * 60
        return datetime.time(int(mct_hours), int(mct_minutes), int(mct_seconds))

    def __str__(self):
        return f"{self.utc_time} is {self.mars_sol_date:.2f} MTC"

class MarsTimeZone:
    def __init__(self, offset):
        self.offset = offset

    def from_utc(self, utc_time):
        return MarsTime(utc_time + datetime.timedelta(hours=self.offset))

if __name__ == "__main__":
    # Create a MarsTimeZone object for the standard Mars time zone
    mars_time_zone = MarsTimeZone(offset=24)

    # Get the current UTC time
    utc_now = datetime.datetime.utcnow()

    # Convert the UTC time to Mars time
    mars_time = mars_time_zone.from_utc(utc_now)

    # Print the Mars time
    print(mars_time)

    # Create a MarsTimeZone object for the second Mars time zone
    mars_time_zone_2 = MarsTimeZone(offset=12)

    # Convert the UTC time to the second Mars time zone
    mars_time_2 = mars_time_zone_2.from_utc(utc_now)

    # Print the Mars time in the second time zone
    print(mars_time_2)
