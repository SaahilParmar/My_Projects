from project import pwd_generator, one_two, mail_validation, mail_setup, data_collection, pwd_handling
from unittest import mock


def test_pwd_generator():  # OUTPUT WILL NEVER BE CONSECUTIVE CHARACTERS IN ANY COMBINATION.
    assert pwd_generator(4) != 'aa11'
    assert pwd_generator(4) != 'AA11'
    assert pwd_generator(4) != 'aa//'
    assert pwd_generator(4) != '//11'
    assert pwd_generator(4) != '1111'
    assert pwd_generator(4) != '////'
    assert pwd_generator(4) != 'AAAA'
    assert pwd_generator(4) != 'aaaa'


def test_one_two():  # OUTPUT WILL EITHER BE 1 OR 2.
    with mock.patch('builtins.input', return_value='1'):
        assert one_two('type') == 1
    with mock.patch('builtins.input', return_value='2'):
        assert one_two('type') == 2


def test_mail_validation():  # ONLY VALID EMAIL ID WILL BE RETURNED, ELSE FALSE WILL BE RETURNED.
    assert mail_validation('a') is False
    assert mail_validation('a@') is False
    assert mail_validation('a@a') is False
    assert mail_validation('@a') is False
    assert mail_validation('a.com') is False
    assert mail_validation('@a.com') is False
    assert mail_validation('saahil.parmar@gmail.com') == 'saahil.parmar@gmail.com'


def test_mail_setup():  # ONLY CORRECT 'EMAIL ID, SUBJECT & BODY' WILL BE A SUCCESS.
    assert mail_setup('saahil.parmar@gmail.com', 'this is subject', 'this is body') is True
    assert mail_setup(1, 1, 1) is False
    assert mail_setup('saahil.parmar@gmail.com', 1, 1) is False
    assert mail_setup('saahil.parmar@gmail.com', 'this is subject', 1) is False
    assert mail_setup('saahil.parmar@gmail.com', 1, 'this is body') is False


def test_data_collection():  # IF NOTHING IS ADDED IN THE LIST, OUTPUT IS AN EMPTY LIST.
    with mock.patch('builtins.input', return_value='2'):
        assert data_collection() == sorted([])


def test_pwd_handling():  # WHEN INCORRECT EMAIL FORMAT IS USED.
    assert pwd_handling('a') == 'INVALID EMAIL ADDRESS.'
    assert pwd_handling('a@') == 'INVALID EMAIL ADDRESS.'
    assert pwd_handling('.com') == 'INVALID EMAIL ADDRESS.'
    assert pwd_handling('@a.com') == 'INVALID EMAIL ADDRESS.'
