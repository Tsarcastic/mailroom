"""Test Mail Room Madness."""

import pytest


def variables():
    """Test to make sure the variables are working as intended."""
    from mail_room_madness import DONORS_CT
    assert DONORS_CT


def test_report():
    """Test to make sure the report generates properly."""
    from mail_room_madness import report, DONORS_AMT, DONORS_CT
    report()


def print_letter():
    """To make sure the letter prints properly given the arguments."""
    from mail_room_madness import print_letter
    print_letter('me', '500')
