## 1- location Pune zero restaurants not found
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_location_exist
    - slot{"location": "Pune"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "<300"}
    - slot{"price": "<300"}
    - action_search_restaurants
    - slot{"restaurant_num":"zero"}
    - utter_goodbye
    - export

## 2- location Hyderabad zero restaurants found
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - action_location_exist
    - slot{"location": "Hyderabad"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "<300"}
    - slot{"price": "<300"}
    - action_search_restaurants
    - slot{"restaurant_num":"zero"}
    - utter_goodbye
    - export

## 3- location Pune restaurants found
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_location_exist
    - slot{"location": "Pune"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "<300"}
    - slot{"price": "<300"}
    - action_search_restaurants
    - slot{"restaurant_num":"one"}
    - utter_ask_top10_restaurant_needed
* affirm
    - utter_ask_email
* restaurant_search{"email": "email"}    
    - slot{"email":"abc@gmail.com"}
    - action_send_mail
    - utter_inform
    - utter_goodbye
    - export

## 4- location Hyderabad restaurants found
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - action_location_exist
    - slot{"location": "Hyderabad"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "<300"}
    - slot{"price": "<300"}
    - action_search_restaurants
    - slot{"restaurant_num":"one"}
    - utter_ask_top10_restaurant_needed
* affirm
    - utter_ask_email
* restaurant_search{"email": "email"}    
    - slot{"email":"abc@gmail.com"}
    - action_send_mail
    - utter_inform
    - utter_goodbye
    - export

## 4- location Hyderabad restaurants found
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - action_location_exist
    - slot{"location": "Hyderabad"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"price": ">700"}
    - slot{"price": ">700"}
    - action_search_restaurants
    - slot{"restaurant_num":"one"}
    - utter_ask_top10_restaurant_needed
* affirm
    - utter_ask_email
* restaurant_search{"email": "email"}    
    - slot{"email":"abc@gmail.com"}
    - action_send_mail
    - utter_inform
    - utter_goodbye
    - export

## 5 - location Pune restaurants found
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_location_exist
    - slot{"location": "Pune"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"price": ">700"}
    - slot{"price": ">700"}
    - action_search_restaurants
    - slot{"restaurant_num":"one"}
    - utter_ask_top10_restaurant_needed
* affirm
    - utter_ask_email
* restaurant_search{"email": "email"}    
    - slot{"email":"abc@gmail.com"}
    - action_send_mail
    - utter_inform
    - utter_goodbye
    - export

## 3- location Bangalore restaurants found
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_location_exist
    - slot{"location": "Bangalore"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "<300"}
    - slot{"price": "<300"}
    - action_search_restaurants
    - slot{"restaurant_num":"one"}
    - utter_ask_top10_restaurant_needed
* affirm
    - utter_ask_email
* restaurant_search{"email": "email"}    
    - slot{"email":"abc@gmail.com"}
    - action_send_mail
    - utter_inform
    - utter_goodbye
    - export

## 3- location Bangalore restaurants found
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_location_exist
    - slot{"location": "Bangalore"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"price": ">700"}
    - slot{"price": ">700"}
    - action_search_restaurants
    - slot{"restaurant_num":"one"}
    - utter_ask_top10_restaurant_needed
* affirm
    - utter_ask_email
* restaurant_search{"email": "email"}    
    - slot{"email":"abc@gmail.com"}
    - action_send_mail
    - utter_inform
    - utter_goodbye
    - export

## Location Pune found , Italian cuisine , email yes
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - action_location_exist
    - slot{"location": "New Delhi"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"price": "<300"}
    - slot{"price": "<300"}
    - action_search_restaurants
    - utter_ask_top10_restaurant_needed
* affirm
    - utter_ask_email
* restaurant_search{"email": "email"}    
    - slot{"email":"abc@gmail.com"}
    - action_send_mail
    - utter_inform
    - utter_goodbye
    - export

## location specified and foodie serves in that area
* greet
   - utter_greet
* restaurant_search{"location":"Jaipur"}
   - slot{"location":"Jaipur"}
   - action_location_exist
   - slot{"location":"Jaipur"}
   - slot{"location_match": "one"}  
   - utter_ask_cuisine
* restaurant_search{"cuisine":"italian"}
   - slot{"cuisine":"italian"}					  
    - utter_ask_budget
* restaurant_search{"price": "<300"}
    - slot{"price": "<300"}
    - action_search_restaurants
    - utter_ask_top10_restaurant_needed
* affirm
    - utter_ask_email
* restaurant_search{"email": "email"}    
    - slot{"email":"abc45333@yahoo.com"}
    - action_send_mail
    - utter_inform
    - utter_goodbye
    - export

## location,cuisine specified, foodie serves in that area and mail to be sent
* greet
   - utter_greet
* restaurant_search{"location":"New Delhi","cuisine":"North Indian"}
   - slot{"location":"New Delhi"}
   - action_location_exist
   - slot{"location":"New Delhi"}
   - slot{"location_match": "one"}
   - slot{"cuisine":"North Indian"}
   - utter_ask_budget
* restaurant_search{"price": "<300"}
    - slot{"price": "<300"}
    - action_search_restaurants
    - utter_ask_top10_restaurant_needed
* affirm
    - utter_ask_email
* restaurant_search{"email": "email"}    
    - slot{"email":"abc@gmail.com"}
    - action_send_mail
    - utter_inform
    - utter_goodbye
    - export

## location not found - Ladakh
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Ladakh"}
    - slot{"location": "Ladakh"}
    - action_location_exist
    - slot{"location": null}
    - slot{"location_match": "zero"}
    - utter_invalid_location
    - utter_goodbye
    - export

## location not found - Ladakh
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "leh"}
    - slot{"location": "leh"}
    - action_location_exist
    - slot{"location": null}
    - slot{"location_match": "zero"}
    - utter_invalid_location
    - utter_goodbye
    - export
## location not found - Nairobi
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Nairobi"}
    - slot{"location": "Nairobi"}
    - action_location_exist
    - slot{"location": null}
    - slot{"location_match": "zero"}
    - utter_invalid_location
    - utter_goodbye
    - export
## location not found - Bijapur
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bijapur"}
    - slot{"location": "Bijapur"}
    - action_location_exist
    - slot{"location": null}
    - slot{"location_match": "zero"}
    - utter_invalid_location
    - utter_goodbye
    - export
## location not found - Jamnagar
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Jamanagar"}
    - slot{"location": "Jamanagar"}
    - action_location_exist
    - slot{"location": null}
    - slot{"location_match": "zero"}
    - utter_invalid_location
    - utter_goodbye
    - export

## location not found - Bokaro
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bokaro"}
    - slot{"location": "Bokaro"}
    - action_location_exist
    - slot{"location": null}
    - slot{"location_match": "zero"}
    - utter_invalid_location
    - utter_goodbye
    - export

## location not found - Sangli
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Sangli"}
    - slot{"location": "Sangli"}
    - action_location_exist
    - slot{"location": null}
    - slot{"location_match": "zero"}
    - utter_invalid_location
    - utter_goodbye
    - export

## location not found - Kanyakumari
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Kanyakumari"}
    - slot{"location": "Kanyakumari"}
    - action_location_exist
    - slot{"location": null}
    - slot{"location_match": "zero"}
    - utter_invalid_location
    - utter_goodbye
    - export

## location not found - Manali
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Manali"}
    - slot{"location": "Manali"}
    - action_location_exist
    - slot{"location": null}
    - slot{"location_match": "zero"}
    - utter_invalid_location
    - utter_goodbye
    - export

## location not found - Parbhani
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Parbhani"}
    - slot{"location": "Parbhani"}
    - action_location_exist
    - slot{"location": null}
    - slot{"location_match": "zero"}
    - utter_invalid_location
    - utter_goodbye
    - export

## location not found - Paris
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Paris"}
    - slot{"location": "Paris"}
    - action_location_exist
    - slot{"location": null}
    - slot{"location_match": "zero"}
    - utter_invalid_location
    - utter_goodbye
    - export
## location not found - zurich
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "zurich"}
    - slot{"location": "zurich"}
    - action_location_exist
    - slot{"location": null}
    - slot{"location_match": "zero"}
    - utter_invalid_location
    - utter_goodbye
    - export

## location,cuisine specified, foodie serves in that area and mail not to be sent
* greet
   - utter_greet
* restaurant_search{"location":"Goa","cuisine":"italian"}
   - slot{"location":"Goa"}
   - action_location_exist
   - slot{"location":"Goa"}
   - slot{"location_match": "one"}
   - slot{"cuisine":"italian"}
   - utter_ask_budget
* restaurant_search{"price": "<300"}
    - slot{"price": "<300"}
    - action_search_restaurants
    - utter_ask_top10_restaurant_needed
* deny
    - utter_goodbye
    - export

## location,cuisine specified, foodie serves in that area and mail not to be sent
* greet
   - utter_greet
* restaurant_search{"location":"Jaipur","cuisine":"American"}
   - slot{"location":"Jaipur"}
   - action_location_exist
   - slot{"location":"Jaipur"}
   - slot{"location_match": "one"}
   - slot{"cuisine":"American"}
   - utter_ask_budget
* restaurant_search{"price": "<300"}
    - slot{"price": "<300"}
    - action_search_restaurants
    - utter_ask_top10_restaurant_needed
* deny
    - utter_goodbye
    - export

## location,cuisine specified, foodie serves in that area and mail not to be sent
* greet
   - utter_greet
* restaurant_search{"location":"Aurangabad","cuisine":"Italian"}
   - slot{"location":"Aurangabad"}
   - action_location_exist
   - slot{"location":"Aurangabad"}
   - slot{"location_match": "one"}
   - slot{"cuisine":"Italian"}
   - utter_ask_budget
* restaurant_search{"price": ">700"}
    - slot{"price": ">700"}
    - action_search_restaurants
    - utter_ask_top10_restaurant_needed
* deny
    - utter_goodbye
    - export

## location,cuisine specified, foodie serves in that area and mail not to be sent
* greet
   - utter_greet
* restaurant_search{"location":"Agra","cuisine":"Chinese"}
   - slot{"location":"Bangalore"}
   - action_location_exist
   - slot{"location":"Bangalore"}
   - slot{"location_match": "one"}
   - slot{"cuisine":"Chinese"}
   - utter_ask_budget
* restaurant_search{"price": ">700"}
    - slot{"price": ">700"}
    - action_search_restaurants
    - utter_ask_top10_restaurant_needed
* deny
    - utter_goodbye
    - export

## location,cuisine specified, foodie serves in that area and mail not to be sent
* greet
   - utter_greet
* restaurant_search{"location":"Mysore","cuisine":"Chinese"}
   - slot{"location":"Mysore"}
   - action_location_exist
   - slot{"location":"Mysore"}
   - slot{"location_match": "one"}
   - slot{"cuisine":"Chinese"}
   - utter_ask_budget
* restaurant_search{"price": "<300"}
    - slot{"price": "<300"}
    - action_search_restaurants
    - utter_ask_top10_restaurant_needed
* deny
    - utter_goodbye
    - export

## location,cuisine specified, foodie serves in that area and mail not to be sent
* greet
   - utter_greet
* restaurant_search{"location":"Mysore","cuisine":"North Indian"}
   - slot{"location":"Mysore"}
   - action_location_exist
   - slot{"location":"Mysore"}
   - slot{"location_match": "one"}
   - slot{"cuisine":"North Indian"}
   - utter_ask_budget
* restaurant_search{"price": ">700"}
    - slot{"price": ">700"}
    - action_search_restaurants
    - utter_ask_top10_restaurant_needed
* deny
    - utter_goodbye
    - export

## location,cuisine specified, foodie serves in that area and mail not to be sent
* greet
   - utter_greet
* restaurant_search{"location":"Ahemadabad","cuisine":"North Indian"}
   - slot{"location":"Ahemadabad"}
   - action_location_exist
   - slot{"location":"Ahemadabad"}
   - slot{"location_match": "one"}
   - slot{"cuisine":"North Indian"}
   - utter_ask_budget
* restaurant_search{"price": ">700"}
    - slot{"price": ">700"}
    - action_search_restaurants
    - utter_ask_top10_restaurant_needed
* deny
    - utter_goodbye
    - export

## location,cuisine specified, foodie serves in that area and mail not to be sent
* greet
   - utter_greet
* restaurant_search{"location":"Goa","cuisine":"Italian"}
   - slot{"location":"Goa"}
   - action_location_exist
   - slot{"location":"Goa"}
   - slot{"location_match": "one"}
   - slot{"cuisine":"Italian"}
   - utter_ask_budget
* restaurant_search{"price": ">700"}
    - slot{"price": ">700"}
    - action_search_restaurants
    - utter_ask_top10_restaurant_needed
* deny
    - utter_goodbye
    - export

## location,cuisine, budget specified, foodie serves in that area and mail to be sent
* greet
   - utter_greet
* restaurant_search{"location":"New Delhi","cuisine":"italian","price":">700"}
   - slot{"location":"New Delhi"}
   - action_location_exist
   - slot{"location":"New Delhi"}
   - slot{"location_match": "one"}							  
   - slot{"cuisine":"North Indian"}
   - slot{"price":">700"}
   - action_search_restaurants
   - utter_ask_top10_restaurant_needed
* affirm
    - utter_ask_email
* restaurant_search{"email": "email"}    
    - slot{"email":"abc@gmail.com"}
    - action_send_mail
    - utter_inform
    - utter_goodbye
    - export

## location,cuisine, budget specified, foodie serves in that area and mail not to be sent
* greet
   - utter_greet
* restaurant_search{"location":"Goa","cuisine":"italian","price":">700"}
   - slot{"location":"Goa"}
   - slot{"location_match": "one"}
   - slot{"location":"Goa"}
   - action_location_exist 
   - slot{"cuisine":"italian"}
   - slot{"price":">700"}
   - action_search_restaurants
   - utter_ask_top10_restaurant_needed
* deny
    - utter_goodbye
    - export
