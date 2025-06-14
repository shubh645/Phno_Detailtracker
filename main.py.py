import phonenumbers # type: ignore
from phonenumbers import geocoder # type: ignore #geocoder module is used to get the location of phone number(like country name)
from phonenumbers import carrier # type: ignore #carrier is used to get the service provider of the number i/e it gives the name of service provider(like airtel,jio etc)
from phonenumbers import timezone # type: ignore #timezone module is used to get the timezone of the number

# Parse the phone number.parse () is used to parse phone number and get the details of the number.parsing is the process of converting a string into a number.
# The parse() function takes a string as input and returns a PhoneNumber object that contains the parsed phone number. 

number = phonenumbers.parse(str(input("ENTER THE PHONE_NUMBER: ")))
timezone_info=timezone.time_zones_for_number(number)
print("Timezone: ",timezone_info)
service_provider=carrier.name_for_number(number,"en")
print("Service provider: ",service_provider)
# Get the region description in English
print(geocoder.description_for_number(number, "en"))
