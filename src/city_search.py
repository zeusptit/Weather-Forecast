import re
def find_country(city_name, countries):
    for country_info in countries:
        if city_name in country_info['cities']:
            matches = re.findall(r'\b\w', country_info['country'])
            res = ''.join(matches).upper()
            if len(country_info['country']) > 15:
                return res
            return country_info['country']

    return 'Not Found'