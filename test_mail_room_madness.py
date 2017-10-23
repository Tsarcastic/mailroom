import pytest


def test_sort_report():
    """Test to make sure the report generates properly."""
    from mail_room_madness import sort_report, DONORS_AMT, DONORS_CT
    assert sort_report() == ['other', 'example', 'more']


def test_add_amount01():
    """Test to make sure donation works with new donor."""
    from mail_room_madness import DONORS_AMT, DONORS_CT, add_amount
    add_amount('Bob', 500)
    assert DONORS_AMT['Bob'] == 500
    assert DONORS_CT['Bob'] == 1


def test_add_amount2():
    """Test to make sure donation works with new donor."""
    from mail_room_madness import DONORS_AMT, DONORS_CT, add_amount
    add_amount('example', 200)
    assert DONORS_AMT['example'] == 300
    assert DONORS_CT['example'] == 2


def test_create_letter():
    """Test that the letter prints properly."""
    from mail_room_madness import write_letter
    assert len(write_letter('no one', '200')) >= 100
