from unittest import TestCase
import pytest
import sys
from pathlib import Path 
d = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(d))
import run

test_data_legal_dictionaries  = [
    ({'2020-01-01':4,'2020-01-02':4,'2020-01-03':6,'2020-01-04':8,'2020-01-05':2,
    '2020-01-06':-6,'2020-01-07':2,'2020-01-08':-2}),

    ({'2020-01-01':6,'2020-01-04':12,'2020-01-05':14,'2020-01-06':2,'2020-01-07':4}),
    
    ({'1970-01-02':4,'1982-05-29':4,'2020-09-07':8,'2020-09-06':9})
]

@pytest.fixture(params=test_data_legal_dictionaries)
def legal_dict_fixture(request):
    t = request.param
    return run.get_weekdays_count(t)


def test_returned_dictionary_count(legal_dict_fixture):
    """check that returned dictionary count is 7 for all legal dictionaries"""
    t = legal_dict_fixture
    print(t)
    assert len(t) == 7


def test_data_legal_dictionary():
    """check that returned dictionary count is valid"""
    d = {'2020-01-01':4,'2020-01-02':4,'2020-01-03':6,'2020-01-04':8,'2020-01-05':2,
    '2020-01-06':-6,'2020-01-07':2,'2020-01-08':-2}

    expected = {'Mon':-6,'Tue':2,'Wed':2,'Thu':4,'Fri':6,'Sat':8,'Sun':2}
    returned = run.get_weekdays_count(d)

    assert expected == returned

def test_exception_is_raised_for_incorrect_date_format():
    """check that error message is received for incorrect date format"""
    d = {'02-29-2020':6,'2020-01-04':12,'2020-01-05':14,'2020-01-06':2,'1970-01-07':4}
    assert run.get_weekdays_count(d) == 'date not supplied in YYYY-MM-DD format'

def test_exception_is_raised_for_year():
    """check that expection is raised for year that is out of range"""
    d = {'2101-01-01':6,'2020-01-04':12,'2020-01-05':14,'2020-01-06':2,'1969-01-07':4}
    with pytest.raises(Exception):
        assert run.get_weekdays_count(d)

def test_exception_is_raised_for_month_out_of_range():
    """check that error message is received for month that is out of range"""
    d = {'2020-13-01':6,'2020-01-04':12,'2020-01-05':14,'2020-01-06':2,'1970-01-07':4}
    assert run.get_weekdays_count(d) == 'date not supplied in YYYY-MM-DD format'


def test_exception_is_raised_for_leap_year():
    """check that error message is received for leap year which has date out of range"""
    d = {'2019-02-29':6,'2020-01-04':12,'2020-01-05':14,'2020-01-06':2,'1970-01-07':4}
    assert run.get_weekdays_count(d) == 'date not supplied in YYYY-MM-DD format'

def test_if_sunday_monday_are_present():
    """check that error message is received if sunday and monday are not present in dictionary"""
    d = {'2020-10-09':4,'2020-10-08':3,'2020-10-10':5,'2020-06-01':4}
    assert run.get_weekdays_count(d) == 'Date dictionary must contain dates of Sunday and Monday'

def test_empty_dictionary():
    """check that empty dictionary receives an error message"""
    d = {}
    assert run.get_weekdays_count(d) == 'date dictionary cannot be empty'


def test_subsitute_for_occurence_of_zero():
    """check that substitute function perform as expected"""
    d = {'2020-09-07':8,'2020-09-06':9}
    expected = {'Mon':8,'Tue':4,'Wed':2,'Thu':1,'Fri':0,'Sat':4,'Sun':9}
    assert run.get_weekdays_count(d) == expected


@pytest.mark.parametrize(
    "d",
    [
        pytest.param(
            {'1970-01-02':-1000001,'1982-05-29':4,'2020-09-07':8,'2020-09-06':9}
        ),
        pytest.param(
            {'1970-01-02':1000001,'1982-05-29':4,'2020-09-07':8,'2020-09-06':9}
        )
    ]
)
def test_value_range_exception(d):
    """check that exception is raised for out of range values"""
    with pytest.raises(Exception):
        assert run.get_weekdays_count(d)
