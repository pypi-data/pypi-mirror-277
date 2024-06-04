from datetime import date

from freezegun import freeze_time

from ..abstract.time_filter import TimeFilter
from .client import DatabricksClient, _day_hour_to_epoch_ms


def test__day_hour_to_epoch_ms():
    _day_hour_to_epoch_ms(date(2023, 2, 14), 14) == 1644847200000


@freeze_time("2023-7-4")
def test_DatabricksClient__time_filter():
    # default is yesterday
    default_time_filter = None
    default_filter = DatabricksClient._time_filter(default_time_filter)
    expected_default = {
        "filter_by": {
            "query_start_time_range": {
                "end_time_ms": 1688428800000,  # July 4, 2023 12:00:00 AM GMT
                "start_time_ms": 1688342400000,  # July 3, 2023 12:00:00 AM GMT
            }
        }
    }
    assert default_filter == expected_default

    # custom time (from execution_date in DAG for example)
    time_filter = TimeFilter(day=date(2020, 10, 15))
    custom_filter = DatabricksClient._time_filter(time_filter)
    expected_custom = {
        "filter_by": {
            "query_start_time_range": {
                "end_time_ms": 1602806400000,  # October 16, 2020 12:00:00 AM
                "start_time_ms": 1602720000000,  # October 15, 2020 12:00:00 AM
            }
        }
    }
    assert custom_filter == expected_custom

    # hourly extraction: note that hour_min == hour_max
    hourly = TimeFilter(day=date(2023, 4, 14), hour_min=4, hour_max=4)
    hourly_filter = DatabricksClient._time_filter(hourly)
    expected_hourly = {
        "filter_by": {
            "query_start_time_range": {
                "end_time_ms": 1681448400000,  # April 14, 2023 5:00:00 AM
                "start_time_ms": 1681444800000,  # April 14, 2023 4:00:00 AM
            }
        }
    }
    assert hourly_filter == expected_hourly


class MockDatabricksClient(DatabricksClient):
    def __init__(self):
        self._db_allowed = ["prd", "staging"]
        self._db_blocked = ["dev"]


def test_DatabricksClient__keep_catalog():
    client = MockDatabricksClient()
    assert client._keep_catalog("prd")
    assert client._keep_catalog("staging")
    assert not client._keep_catalog("dev")
    assert not client._keep_catalog("something_unknown")


def test_DatabricksClient__get_user_mapping():
    client = MockDatabricksClient()
    users = [
        {"id": "both", "email": "hello@world.com", "user_name": "hello world"},
        {"id": "no_email", "email": "", "user_name": "no email"},
        {"id": "no_name", "email": "no@name.fr", "user_name": ""},
        {"id": "no_both", "email": "", "user_name": ""},
        {"id": "", "email": "no@id.com", "user_name": "no id"},
    ]
    expected = {
        "hello@world.com": "both",
        "hello world": "both",
        "no@name.fr": "no_name",
        "no email": "no_email",
    }
    mapping = client._get_user_mapping(users)
    assert mapping == expected


def test_DatabricksClient__match_table_with_user():
    client = MockDatabricksClient()
    user_mapping = {"bob@castordoc.com": 3}

    table = {"id": 1, "owner_email": "bob@castordoc.com"}
    table_with_owner = client._match_table_with_user(table, user_mapping)

    assert table_with_owner == {**table, "owner_external_id": 3}

    table_without_owner = {"id": 1, "owner_email": None}
    actual = client._match_table_with_user(table_without_owner, user_mapping)
    assert actual == table_without_owner
