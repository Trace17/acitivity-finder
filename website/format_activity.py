def format_activity(category, city, state, specifics):
    category_url = "+".join( category.split() )
    city_url = "+".join( city.split() )
    state_url = "+".join( state.split() )
    specifics_url = "+".join( specifics.split() )
    specifics_url.replace(", ", "+")
    url = f"https://www.yelp.com/search?find_desc={category_url}+{specifics_url}&find_loc={city_url}%2C+{state_url}"
    return url