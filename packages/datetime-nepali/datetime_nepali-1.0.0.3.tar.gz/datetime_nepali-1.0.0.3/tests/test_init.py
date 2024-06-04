import datetime_nepali


class TestInit:
    """Test attributes initialized when a instance of the class is created."""

    def test_max_date_gt_min_date(self):
        assert datetime_nepali.MAXYEAR > datetime_nepali.MINYEAR
