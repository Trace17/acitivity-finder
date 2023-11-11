# Activity Finder
This is an application using Django Web Framework to build both the backend and frontend of a web application which finds a random activity or random date idea based on a users location and any additional filters they might have for the activity (Example: Outside activity in Oregon). This app consists of two microservices which communicate with eachother and beautiful soup to parse the web. 

## Why it exists?
The idea for this application came to me while trying to find an activity for my partner and I to do, the only problem was there were too many options. Because of this analysis paralysis, we decided to pick a random number, and based on that number, we would count down on the activities until we reached that one and thats the activity we would do. This wasnt just a problem for us, it became a trend on social media for couples and friends to do the exact same thing. Having options is great, but sometimes you want a little spontaneity to take you out of the routine of things. This application is a rendition of exactly that. 


## This application can be used for
- Finding a random date idea to add a little spontaneity to your life
- To find something to do in a new city
- To be the final decider on which activity to do

## How to use:
Right now this application does not have a domain. To use it simply pull the files and change in two seperate terminal instances change to the following directories in different terminal instances:

- BA_Micorservice and run "python3 activity_generator.py" 
- The main directory (date_finder) and run "python3 manage.py runserver"

Once this is complete go to localhost:8000 in any web browser and have fun! 


https://user-images.githubusercontent.com/91487097/206829279-fdee8e19-fca7-4562-8c8f-7f40e321c8e9.mov

