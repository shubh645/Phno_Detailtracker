# Phone number detail tracker
Python phonenumbers library is used for tracking the details of person via phone number. This library gets the data from the Google's libphonenumber library.
It can't provide the accurate location of the person because of user privacy. It provides the location (based on the country code), carrier name, time zone.

- Parse is the function which is most important used to parse the string into the readable number.

## Installation:
(using pip command)      
pip install phonenumbers

It supports Python 2.5-2.7 and Python 3.x 

## MODULES:
- Geocoder: Used for tracking the location based on the provided country code
- Carrier: Used for the getting the carrier’s name (service provider) of a number
- Timezone: Provides the timezone according to the country 
