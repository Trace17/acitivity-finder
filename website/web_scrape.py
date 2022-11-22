from .get_random_num import get_random_num
import requests
import bs4 


def get_random_result(url):
    """Function that returns a random activity """
    request_result = requests.get(url)
    soup = bs4.BeautifulSoup(request_result.text, "html.parser")
    #find all major headings 
    heading_object = soup.find_all("h3")
    for info in heading_object:
        print(info.getText())
        print("------")
    rand_number = get_random_num(len(heading_object))
    if rand_number == 0:
        return "No Activities Available :( Try some new selections or a different place!"
    activity = heading_object[int(rand_number)-1]
    #create a function which gets rid of the number in front of this activity 
    return activity

def get_link_to_result(activity):
    for link in activity.find_all('a'):
        yelp_link = link['href']
    return_link = "https://www.yelp.com" + yelp_link
    return return_link

def get_return_activity(activity):
    return_activity = activity.getText()
    return return_activity


def get_image_of_result(link):
    request_result = requests.get(link)
    soup = bs4.BeautifulSoup(request_result.text, "html.parser")
    image = soup.find_all("img")
    image_summary = image[0]
    image_link = image_summary['src']
    return image_link

