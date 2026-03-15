import random

INDIAN_AIRPORTS = ["BLR","DEL","BOM","GOI","MAA","HYD","CCU"]

def search_flights(origin, destination, date, cabin_class):

    domestic_flights = [
        {"airline":"IndiGo","price":"₹5200","class":cabin_class},
        {"airline":"Air India","price":"₹6100","class":cabin_class},
        {"airline":"Vistara","price":"₹7700","class":cabin_class},
        {"airline":"SpiceJet","price":"₹10000","class":cabin_class}
    ]

    international_flights = [
        {"airline":"Emirates","price":"$750","class":cabin_class},
        {"airline":"Lufthansa","price":"$720","class":cabin_class},
        {"airline":"British Airways","price":"$740","class":cabin_class},
        {"airline":"Singapore Airlines","price":"$780","class":cabin_class}
    ]

    if origin in INDIAN_AIRPORTS and destination in INDIAN_AIRPORTS:
        flights = domestic_flights
        route_type = "Domestic"
    else:
        flights = international_flights
        route_type = "International"

    result = f"\n✈️ {route_type} Flights from {origin} -> {destination} on {date} ({cabin_class})\n\n"

    for i,flight in enumerate(flights,start=1):
        seats = random.randint(2,20)
        result += f"{i}. {flight['airline']} - {flight['price']} | Seats left: {seats}\n"

    return result


def search_hotels(city,country,nights):

    INDIAN_CITIES = ["BLR","DEL","BOM","GOI","MAA","HYD","CCU"]

    domestic_hotels = [
        {"hotel":"Taj Hotel","price":"₹12200/night"},
        {"hotel":"Oberoi","price":"₹7100/night"},
        {"hotel":"ITC Hotels","price":"₹17700/night"},
        {"hotel":"Lemon Tree","price":"₹20000/night"}
    ]

    international_hotels = [
        {"hotel":"Hilton","price":"$180/night"},
        {"hotel":"Marriott","price":"$210/night"},
        {"hotel":"Hyatt","price":"$195/night"},
        {"hotel":"Radisson","price":"$175/night"}
    ]

    if city in INDIAN_CITIES:
        hotels = domestic_hotels
        hotel_type = "Domestic"
    else:
        hotels = international_hotels
        hotel_type = "International"

    result = f"\n🏨 {hotel_type} Hotels in {city}, {country} for {nights} nights\n\n"

    for i,hotel in enumerate(hotels,start=1):
        rooms = random.randint(1,10)
        result += f"{i}. {hotel['hotel']} - {hotel['price']} | Rooms left: {rooms}\n"

    return result


available_tools = {
    "search_flights":search_flights,
    "search_hotels":search_hotels
}