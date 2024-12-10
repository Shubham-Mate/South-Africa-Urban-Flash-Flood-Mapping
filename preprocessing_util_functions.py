import re


# Extract event id and event day from the id_eventid_X_day format
def extract_event_id(row):
    match = re.match('id_[a-zA-Z0-9]+_', row)
    return match.group()[3:-1]

def extract_event_day(row):
    match = re.search('_X_[0-9]+', row)
    return int(match.group()[3:])