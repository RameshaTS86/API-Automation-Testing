#This File will have Common API Constant Values like url,etc

class API_Constants(object):

    def get_all_booking_details_url(self):
        return "https://restful-booker.herokuapp.com/booking/"

    def get_booking_details_using_bookingid(self,bookingid):
        return "https://restful-booker.herokuapp.com/booking/" + str(bookingid)


    def create_booking_url(self):
        return "https://restful-booker.herokuapp.com/booking"

    def update_partialUpdate_delete_booking_url(self,bookingid):
        return "https://restful-booker.herokuapp.com/booking/"+str(bookingid)


    def create_token_url(self):
        return "https://restful-booker.herokuapp.com/auth"

