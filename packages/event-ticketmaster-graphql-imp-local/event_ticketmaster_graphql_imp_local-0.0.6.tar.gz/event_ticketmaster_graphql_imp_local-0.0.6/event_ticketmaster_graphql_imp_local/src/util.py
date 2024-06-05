from logger_local.Logger import Logger
from python_sdk_remote.utilities import our_get_env

from .ticketmaster_event_constants import TicketmasterEventLocalConstants


class TicketmasterResponseException(Exception):
    pass


logger = Logger.create_logger(object=TicketmasterEventLocalConstants.TICKETMASTER_EVENT_LOCAL_CODE_LOGGER_OBJECT)


def convert_ticketmaster_dict_to_external_events_list(ticketmaster_dict: dict) -> list[dict]:
    logger.start("start convert ticketmaster JSON to external events list",
                 object=ticketmaster_dict)
    try:
        if 'errors' in ticketmaster_dict:
            error_details = ticketmaster_dict.get('errors')
            raise TicketmasterResponseException(error_details[0]['detail'])

        events_data = ticketmaster_dict['_embedded']['events']
        external_events = []

        # Iterate through each event
        for event in events_data:
            url = event['url']
            # subsystem_id = 1  # temp
            system_id = TicketmasterEventLocalConstants.TICKETMASTER_SYSTEM_ID
            external_event_identifier = event['id']
            environment_id = our_get_env("ENVIRONMENT_ID")

            external_events.append({'url': url,
                                    'system_id': system_id,
                                    # 'subsystem_id': subsystem_id,
                                    'external_event_identifier': external_event_identifier,
                                    'environment_id': environment_id})

        logger.end("end convert ticketmaster JSON to external events list",
                   object={'external_events': external_events})
        return external_events

    except TicketmasterResponseException as e:
        logger.exception(f"Ticketmaster response exception: {str(e)}",
                         object=e)
        raise e

    except Exception as e:
        logger.exception(
            f"An unexpected error occurred: {str(e)}", object=e)
