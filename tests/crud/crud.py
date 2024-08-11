import allure
import pytest
import logging
from src.helpers.api_request_wrapper import *
from src.helpers.pay_load_manager import *
from src.helpers.common_verification import *
from src.utils.utils import  *
from src.constants.api_constants import *



class Test_Create_Booking():
    @allure.title("TC_01 : Creating Booking Validation")
    @allure.tag("New Functional Test Case")
    @allure.description("Create Booking with Valid PayLoad")
    def test_create_booking_with_valid_payload(self):
        response = post_request(url=API_Constants().create_booking_url(),
                                header=common_headers_json(),
                                payload=create_booking_pay_Load(),
                                auth=None,in_json=False)
        verify_http_status_code(response,200)
        bookingid = response.json()["bookingid"]
        print("Booking Successful, Booking ID : ",bookingid)
        print("Booking Data : ",response.json())


    @allure.title("TC_02 : Get Booking details Validation")
    @allure.tag("New Functional Test Case")
    @allure.description("Get Booking Details using Booking ID")
    def test_get_booking_details_using_booking_id(self,test_create_booking_id):
        response = get_request(url=API_Constants().get_booking_details_using_bookingid(test_create_booking_id),
                               header=common_headers_json())
        verify_http_status_code(response,200)
        print("Booking Details Found..!,Booking ID is : ", test_create_booking_id)
        print("Booking Details are : ", response.json())


    @allure.title("TC_03 : Full Update Validation")
    @allure.tag("New Functional Test Case")
    @allure.description("Full Update Booking Details Validation")
    def test_full_update_booking_details(self,test_create_booking_id,create_token_id):
        response = put_request(url=API_Constants().update_partialUpdate_delete_booking_url(test_create_booking_id),
                               header=common_header_put_delete_patch_cookie(create_token_id),
                               payload=update_booking_pay_Load(),
                               auth=None,in_json=False)
        verify_http_status_code(response,200)
        print("Update Successful..!,Updated BookingID is : ",test_create_booking_id)
        print("Updated Booking Details : ",response.json())

    @allure.title("TC_04 : Partial Update Validation")
    @allure.tag("New Functional Test Case")
    @allure.description("Partial Update Booking Details Validation")
    def test_parial_booking_update_validation(self,test_create_booking_id,create_token_id):
        response = patch_request(url=API_Constants().update_partialUpdate_delete_booking_url(test_create_booking_id),
                                 header=common_header_put_delete_patch_cookie(create_token_id),
                                 payload=partial_update_booking_pay_Load(),
                                 auth=None,in_json=False)
        verify_http_status_code(response,200)
        print("Partial Update Successful..!, Partial Updated BookingID is : ",test_create_booking_id)
        print("Partial Updated Booking Details : ",response.json())

    @allure.title("TC_05 : Delete Booking Validation")
    @allure.tag("New Functional Test Case")
    @allure.description("Delete Booking Validation")
    def test_delete_booking_validation(self,test_create_booking_id,create_token_id):
        response = delete_requests(url=API_Constants().update_partialUpdate_delete_booking_url(test_create_booking_id),
                                   headers=common_header_put_delete_patch_cookie(create_token_id),
                                   auth=None,in_json=False)
        verify_http_status_code(response,201)
        print("Deletion Successful..!, Deleted BookingID is : ",test_create_booking_id)
