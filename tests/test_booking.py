import pytest

from model.booking import BookingData


def test_create_booking(auth_client) -> None:
    booking_data = BookingData().random()
    response = auth_client.create_booking(booking_data)
    response.status_code == 200


def test_create_booking_additional_needs(auth_client) -> None:
    booking_data = BookingData().random()
    booking_data.additionalneeds = "Added information about needs"
    response = auth_client.create_booking(booking_data)
    response.status_code == 200


@pytest.mark.xfail(reason="бага на стороне сервера")
def test_wrong_type_in_price(auth_client) -> None:
    booking_data = BookingData.random()
    booking_data.totalprice = "two"
    response = auth_client.create_booking(booking_data)
    assert response.status_code != 200


@pytest.mark.xfail(reason="бага на стороне сервера, не работает валидация")
@pytest.mark.parametrize(
    "firstname", [("!@#$%^&*()"), ("1992-08-09"), ("1408")]
)
def test_wrong_type_in_price(auth_client, firstname) -> None:
    booking_data = BookingData.random()
    booking_data.firstname = firstname
    response = auth_client.create_booking(booking_data)
    assert response.status_code != 200


@pytest.mark.xfail(reason="бага на стороне сервера, не работает валидация")
@pytest.mark.parametrize(
    "checkin, checkout",
    [
        ("2020-08-06", "2019-08-06"),
        ("2022-11-10", "2019-03-31"),
        ("2018-02-28", "2000-01-01"),
    ],
)
def test_messed_dates(auth_client, checkin, checkout) -> None:
    booking_data = BookingData.random()
    booking_data.bookingdates.checkin = checkin
    booking_data.bookingdates.checkout = checkout
    response = auth_client.create_booking(booking_data)
    assert response.status_code != 200
