"""Test Mail Room Madness."""

import pytest

#def variables():
    #"""Test to make sure the variables are working as intended."""
    #from mail_room_madness import DONORS_CT
    #assert DONORS_CT


def test_sort_report():
    """Test to make sure the report generates properly."""
    from mail_room_madness import sort_report, DONORS_AMT, DONORS_CT
    assert sort_report() == ['other', 'example', 'more']

def test_add_amount():
    """Test to make sure donation works"""
    from mail_room_madness import DONORS_AMT, DONORS_CT, add_amount
    add_amount('Bob', 500)
    assert DONORS_AMT['Bob'] == 500
    assert DONORS_CT['Bob'] == 1

#def print_letter():
    #"""To make sure the letter prints properly given the arguments."""
    #from mail_room_madness import print_letter
    #print_letter('me', '500')
