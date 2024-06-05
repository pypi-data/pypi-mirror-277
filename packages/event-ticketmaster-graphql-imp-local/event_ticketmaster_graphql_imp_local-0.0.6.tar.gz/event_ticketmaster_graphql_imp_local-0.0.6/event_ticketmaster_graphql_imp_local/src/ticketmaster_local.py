import geohash2
import pycountry  # for converting from country name -> country code
import requests
from event_remote.event_remote import EventRemote
from logger_local.MetaLogger import MetaLogger
from python_sdk_remote.utilities import our_get_env

from .ticketmaster_event_constants import TicketmasterEventLocalConstants
from .util import convert_ticketmaster_dict_to_external_events_list


class TicketmasterLocal(metaclass=MetaLogger,
                        object=TicketmasterEventLocalConstants.TICKETMASTER_EVENT_LOCAL_CODE_LOGGER_OBJECT):
    def __init__(self, is_test_data: bool = False) -> None:
        self.base_url = TicketmasterEventLocalConstants.TICKETMASTER_BASE_URL
        self.api_key = our_get_env("TICKETMASTER_API_KEY")
        self.discover_events = TicketmasterEventLocalConstants.TICKETMASTER_DISCOVER_EVENTS
        self.event_remote = EventRemote(is_test_data=is_test_data)

    def _internal_get_events(self, query_params: dict):
        query_params_string = "&".join(
            [f"{key}={value}" for key, value in query_params.items()])

        url = f"{self.base_url}{self.discover_events}?apikey={
        self.api_key}&{query_params_string}"
        response = requests.get(url, params=None)
        response_dict = response.json()
        external_events_list = convert_ticketmaster_dict_to_external_events_list(response_dict)
        for event_external_dict in external_events_list:
            self.event_remote.create_event_external(event_external_dict=event_external_dict)
        return response_dict

    def get_event_by_keyword(self, keyword: str, num_of_events: int = 1):
        query_params = {"keyword": keyword, "size": num_of_events}
        response_dict = self._internal_get_events(query_params=query_params)
        return response_dict

    def get_events_by_radius(self, lat: float, lng: float, radius: int, unit: str, num_of_events: int = 1) -> dict:
        geopoint = geohash2.encode(lat, lng, precision=9)

        query_params = {
            "geoPoint": geopoint,
            "radius": radius,
            "unit": unit,
            "size": num_of_events}

        response_dict = self._internal_get_events(query_params=query_params)
        return response_dict

    def get_events_by_radius_km(self, lat, lng, radius, num_of_events=1):
        events = self.get_events_by_radius(lat, lng, radius, "km", num_of_events)
        return events

    def get_events_by_radius_miles(self, lat, lng, radius, num_of_events=1):
        events = self.get_events_by_radius(lat, lng, radius, "miles", num_of_events)
        return events

    def get_events_by_country_code(self, country_code: str,
                                   num_of_events: int = 1):
        query_params = {"countryCode": country_code, "size": num_of_events}
        response_dict = self._internal_get_events(query_params=query_params)
        return response_dict

    def get_events_by_country(self, country: str, num_of_events: int = 1):
        country_code = pycountry.countries.get(name=country).alpha_2
        response_dict = self.get_events_by_country_code(country_code, num_of_events)
        return response_dict

    def get_events_by_cities(self, cities: list[str], num_of_events: int = 1):
        query_parameters = {"city": cities, "size": num_of_events}
        response_dict = self._internal_get_events(query_params=query_parameters)
        return response_dict
