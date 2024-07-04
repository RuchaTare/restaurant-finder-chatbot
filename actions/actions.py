from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


ZomatoData = pd.read_csv('zomato.csv', header=0, encoding='unicode_escape')
s = set(ZomatoData.City)


def RestaurantSearch(City, Cuisine, Price):

    TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (
        ZomatoData['City'].apply(lambda x: City.lower() in x.lower()))]

    if Price == "<300":
        TEMP = TEMP[TEMP['Average Cost for two'] < 300]

    elif Price == "300-700":
        TEMP = TEMP[(TEMP['Average Cost for two'] > 300) &
                    (TEMP['Average Cost for two'] < 700)]

    else:
        TEMP = TEMP[TEMP['Average Cost for two'] > 700]

    TEMP.sort_values(by='Aggregate rating', inplace=True, ascending=False)

    return TEMP[['Restaurant Name', 'Address',
                 'Average Cost for two', 'Aggregate rating']]


def checkLocation(location):
    if location not in s:
        return "We do not operate in that area yet."
    else:
        return ""


def sendmail(MailID, subject, str_restaurant):
    mail_content = str_restaurant

    sender_address = 'upgradfoodie21@gmail.com'
    sender_pass = 'upgrad123'

    receiver_address = MailID
    message = MIMEMultipart()

    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = subject
    message.attach(MIMEText(mail_content, 'plain'))

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_address, sender_pass)
    text = message.as_string()
    s.sendmail(sender_address, receiver_address, text)
    s.quit()


class ActionLocationExist(Action):
    def name(self):
        return 'action_location_exist'

    def run(self, dispatcher, tracker, domain):
        response = ""
        #config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}

        loc = tracker.get_slot('location').strip()
        response = checkLocation(location=loc)

        if response != "":
            location_match = 'zero'
            #dispatcher.utter_message("We do not operate in that area yet.")
            return [SlotSet('location', None), SlotSet('location_match', location_match)]

        else:
            location_match = 'one'
            return [SlotSet('location', loc), SlotSet('location_match', location_match)]


class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        response = ""
        res_counter = 0

        cuisine = tracker.get_slot('cuisine').strip()
        loc = tracker.get_slot('location').strip()
        price = tracker.get_slot('price').strip()

        results = RestaurantSearch(City=loc, Cuisine=cuisine, Price=price)
        restaurant_num = 'zero'

        if results.shape[0] == 0:
            response = "No results :(. You can try with some other combination of location, cuisine and price range. "
            restaurant_num = 'zero'

        else:
            restaurant_num = 'one'
            for restaurant in RestaurantSearch(
                    loc, cuisine, price).iloc[:5].iterrows():
                res_counter += 1
                restaurant = restaurant[1]
                response = response + \
                    F"{res_counter}. {restaurant['Restaurant Name']} in {restaurant['Address']} has been rated {restaurant['Aggregate rating']}\n\n"

        dispatcher.utter_message(response)

        return [SlotSet('restaurant_num', restaurant_num)]


class ActionSendMail(Action):
    def name(self):
        return 'action_send_mail'

    def run(self, dispatcher, tracker, domain):
        str_restaurant_details = ''
        res_counter = 0

        cuisine = tracker.get_slot('cuisine').strip()
        loc = tracker.get_slot('location').strip()
        price = tracker.get_slot('price').strip()
        email = tracker.get_slot('email').strip()

        for restaurant in RestaurantSearch(
                loc, cuisine, price).iloc[:10].iterrows():
            res_counter += 1
            restaurant = restaurant[1]
            str_restaurant_details = str_restaurant_details + \
                F"{res_counter}.{restaurant['Restaurant Name']} in {restaurant['Address']} with budget for two people of INR {restaurant['Average Cost for two']} has been rated {restaurant['Aggregate rating']}\n\n"

        subject = F"Restaurant details for {cuisine} cuisine in location {loc} "

        sendmail(email, subject, str_restaurant_details)
        return [SlotSet('email', email)]
