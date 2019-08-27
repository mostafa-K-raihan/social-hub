# social-hub
A place to gather all major social media and interact with them

# Installation Back End
1. go to appropriate directory and open up cmd / terminal
2. `git clone https://github.com/mostafa-K-raihan/social-hub.git`
3. cd social-hub
4. cd app
5. create a python file called configuration.py
6. Add this following lines:
  
    `GET_TOTAL_TWEET_COUNT = 1000`
    
    `TWEETS_PER_PAGE = 10`

    `CONSUMER_KEY = <your twitter consumer key>`
    
    `CONSUMER_SECRET = <your twitter consumer secret>`
    
    `ACCESS_TOKEN = <your twitter access token>
    
    `ACCESS_TOKEN_SECRET = <your twitter access token secret>`
    
    `API_RATE_LIMIT_TIME_MINUTES = 15`
7. Change your Database settings inside vue_cli3_webpack_django/settings.py
8. python manage.py makemigrations
9. python manage.py migrate
10. `pip install django`
11. `python -m venv env`
12. `cd venv`
13. `cd Scripts`
14. `sh ./activate.bat` or `source activate` 
15. `cd ../../`
16. `pip install django-webpack-loader mysqlclient djangorestframework django-cors-headers`

# Installation front end 
1. go to social-hub folder
2. check the readme file
  `npm install`

# Runnning
1. go to social-hub/frontend
2. `npm run serve`
3. `cd ..`
4. `python manage.py runserver`




  
