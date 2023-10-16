def find_country(city_name, countries):
    for country_info in countries:
        if city_name in country_info['cities']:
            return country_info['country']

    return 'Not Found'