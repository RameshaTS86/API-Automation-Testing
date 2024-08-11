# this is the file which will be running first when we run pytest
#can be used to create common IDs, tokens etc and can be utilise in the other test files

import pytest
import requests
from src.helpers.api_request_wrapper import *
from src.helpers.pay_load_manager import *
from src.helpers.common_verification import *
from src.utils.utils import  *
from src.constants.api_constants import *



#Token Creations
@pytest.fixture()
def create_token_id():
    response = post_request(url=API_Constants().create_token_url(),
                            header=common_headers_json(),payload=create_token_pay_load(),
                            auth=None,in_json=False)
    response_data = response.json()
    return response_data["token"]



#BookingID Creation
@pytest.fixture()
def test_create_booking_id():

    response = post_request(url=API_Constants().create_booking_url(),
                            header=common_headers_json(),payload=create_booking_pay_Load(),
                            auth=None,in_json=False)
    verify_http_status_code(response,200)
    response_data = response.json()
    return response_data["bookingid"]