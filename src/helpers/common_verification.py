# we will have functions in this file to validate the common validations
def verify_http_status_code(response_data, expect_data):
    assert response_data.status_code == expect_data, "Failed AR != ER"