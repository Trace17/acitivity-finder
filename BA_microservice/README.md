# Communication Contract Microservice
This microservice accepts an integer value based on the number of results returned from a web scrape. It generates a random value from 1 to the number of results returned and returns that random value via a .txt file.

## Request
This microservice receives a request by monitoring a text file called result_receiver. When that file contains a single integer digit, it automatically begins processing a response for the main server.

## Response
Once a request is received, this microservice saves the received value and generatesa random value within the range of 1 to said value. It then writes this random value to a .txt file named random_activity.txt. This file can then be read by the main program and used to choose a random activity from the filtered search.

## UML Sequence Diagram
![UML Image](BArsenault_UML.jpg)
