# sqlalchemy-challenge

## Description
This repository is constructed in two primary parts. Part One is the Jupyter Notebook titled climate_starter_new.ipynb and contains an exploratory analysis of precipitation levels at various monitoring stations across Hawaii. This Jupytner Notebook also contains an exploratory analysis of the monitoring station themselves, taking a look at which station is the most active and what it's collected data looks like. Part Two is the app.py file which uses flask to incorporate the SQLalchemy queries made in climate_starter_new, and displays specific variations of the queries using JSON files.

## References
### Check same thread
As I was running the code on my app.py file, I kept getting a thread error on the html code. This lead to having to refresh the page twice each time I wanted to run the code for the page. After doing some research, I used the link below and included the check_same_thread function in line 14 to avoid encountering this error.

Link: https://stackoverflow.com/questions/48218065/objects-created-in-a-thread-can-only-be-used-in-that-same-thread

### Accepting URL components as parameters
I again had to conduct research to figure out how to take components of the URL as paramaters for my HTML functions. I learned from the link below that text placed within the brackets of the URL can go into the function as arguments and be accessed that way. I used this principle to create my dynamic start route (lines 74 and 75 of app.py) and dynamic start/end route (lines 90 and 91 of app.py).

Link: https://stackoverflow.com/questions/24892035/how-can-i-get-the-named-parameters-from-a-url-using-flask
