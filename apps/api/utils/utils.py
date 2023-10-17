import re
import datetime


def replace_isodate(match: str) -> str:
    """
    Finds the ISODate string and converts it to datetime object
    :param match: Match object
    :return: str
    """
    pattern = r'ISODate\("([^"]+)"\)'
    matched_text = match.group(0)
    iso_str = re.findall(pattern, matched_text)

    return '"' + iso_str[0] + '"'


def replace_with_datetime(obj_list: list[dict]) -> list[dict]:
    """
    Finds the datestrings in a Dict and converts it to datetime object
    :param obj: dictionary to be converted
    :return: Dict
    """
    pattern = r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}'
    for obj in obj_list:
        for key, value in obj.items():
            if isinstance(value, dict):
                for key2, value2 in value.items():
                    if isinstance(value2, dict):
                        for key3, value3 in value2.items():
                            if len(re.findall(pattern, str(value3))) > 0:
                                value2[key3] = datetime.datetime.fromisoformat(value3)
                    elif re.match(pattern, str(value2)):
                        value[key2] = datetime.datetime.fromisoformat(value2)
            elif isinstance(value, str):
                print('str', value)
                if re.match(pattern, str(value)):
                    obj[key] = datetime.datetime.fromisoformat(value)
                else:
                    obj[key] = value
    return obj_list
