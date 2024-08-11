#This file will have pay load data
def create_booking_pay_Load():
    pay_load = {
        "firstname": "Ramesha",
        "lastname": "T S",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-12-31"
        },
        "additionalneeds": "super bowls"
    }
    return pay_load


def create_token_pay_load():
    pay_load = {
        "username": "admin",
        "password": "password123"
    }
    return pay_load


def update_booking_pay_Load():
    pay_load = {
        "firstname": "Ramesha",
        "lastname": "Toremavinalli Siddesh",
        "totalprice": 1000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-06-30"
        },
        "additionalneeds": "super bowls"
    }
    return pay_load


def partial_update_booking_pay_Load():
    pay_load = {
        "firstname": "Bhoomika",
        "lastname": "Ramesh",
        "totalprice": 1000,
    }
    return pay_load