#Phone Number Tracker Using Python Phonenumbers Module
#importing modules
import phonenumbers
from phonenumbers import carrier,geocoder,timezone

mobileNo = input("Enter Mobile Number With Country Code: ")
mobileNo = phonenumbers.parse(mobileNo)

#get the time zone of the phonenumbers
print(timezone.time_zones_for_number(mobileNo))

#Getting Carrier Of The Phone Number
print(carrier.name_for_number(mobileNo, "en"))

#Getting Region Information
print(geocoder.description_for_number(mobileNo,"en"))
#Valdiatig A Phone Number
print("Valid Mobile Number: ",phonenumbers.is_valid_number(mobileNo))

#Checking posssibilty of a number
print("Checking Possibilty Of Number: ",phonenumbers.is_possible_number(mobileNo))