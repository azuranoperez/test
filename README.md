
Technical test:

- im.py is the main file a it will produce the tables and create the user

- convertocsv.py converts cities (json) to csv. It needs to be called before the load on mysql

- myqlback.py produces a dump of our DB that can be used to upload it to the Google SQL Cloud 

- appsql folder contains the Google API Engine that will query the DB with a city
