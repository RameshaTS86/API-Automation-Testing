def common_headers_json():
    headers = {
        "Content-Type":"application/json"
    }
    return headers


def common_headers_xml():
    headers = {
        "Content-Type": "application/xml",
    }
    return headers


def common_header_put_patch_delete_basic_auth(basic_auth_value):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic " + str(basic_auth_value),
    }
    return headers


def common_header_put_delete_patch_cookie(token):
    headers = {
        "Content-Type": "application/json",
        "Cookie": "token=" + str(token),
    }
    return headers


def read_csv_file():
    pass


def read_env_file():
    pass


def read_database():
    pass
