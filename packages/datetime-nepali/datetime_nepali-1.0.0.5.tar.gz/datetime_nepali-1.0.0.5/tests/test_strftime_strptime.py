import datetime_nepali


class TestStrftime:

    def test_strftime_date(self):
        dt = datetime_nepali.date(2077, 6, 4)
        assert dt.strftime("%m/%d/%Y") == "06/04/2077"
        assert dt.strftime("%A of %B %d %y") == "Sunday of Aswin 04 77"
        assert dt.strftime("%a %b") == "Sun Asw"

        dt = datetime_nepali.date(2077, 2, 32)
        assert dt.strftime("%d-%m-%Y") == "32-02-2077"

    def test_strftime_datetime(self):
        dt = datetime_nepali.datetime(2052, 10, 29, 15, 22, 50, 2222)
        assert dt.strftime("%m/%d/%Y %I:%M:%S.%f %p %a %A %U") == "10/29/2052 03:22:50.002222 PM Mon Monday 44"


class TestStrptime:

    def test_strptime_date(self):
        assert datetime_nepali.datetime.strptime("2011-10-11", "%Y-%m-%d").date() == datetime_nepali.date(2011, 10, 11)
        assert datetime_nepali.datetime.strptime("2077-02-32", "%Y-%m-%d").date() == datetime_nepali.date(2077, 2, 32)

    def test_strptime_datetime(self):
        assert datetime_nepali.datetime.strptime("Asar 23 2025 10:00:00",
                                                 "%B %d %Y %H:%M:%S") == datetime_nepali.datetime(2025, 3, 23, 10, 0, 0)

    def test_strptime_year_special_case(self):
        assert datetime_nepali.datetime.strptime("89", "%y") == datetime_nepali.datetime(2089, 1, 1)
        assert datetime_nepali.datetime.strptime("90", "%y") == datetime_nepali.datetime(1990, 1, 1)
        assert datetime_nepali.datetime.strptime("00", "%y") == datetime_nepali.datetime(2000, 1, 1)
