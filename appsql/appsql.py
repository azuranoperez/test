
# This script is incomplete

import cgi
import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app

import MySQLdb
import os
import jinja2

# Configure the Jinja2 environment.
JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  autoescape=True,
  extensions=['jinja2.ext.autoescape'])

# Define your production Cloud SQL instance information.
_INSTANCE_NAME = 'rare-basis-686:antonio'

class MainPage(webapp2.RequestHandler):
    def get(self):
        # Display existing guestbook entries and a form to add new entries.
        if (os.getenv('SERVER_SOFTWARE') and
            os.getenv('SERVER_SOFTWARE').startswith('Google App Engine/')):
            db = MySQLdb.connect(unix_socket='/cloudsql/' + _INSTANCE_NAME, db='im', user='root', passwd='Fudge')
        else:
            db = MySQLdb.connect(host='127.0.0.1', port=3306, db='im', user='root', passwd='')
            # Alternatively, connect to a Google Cloud SQL instance using:
            # db = MySQLdb.connect(host='ip-address-of-google-cloud-sql-instance', port=3306, user='root')

        cursor = db.cursor()
        cursor.execute('SELECT guestName, content, entryID FROM entries')

        # Create a list of guestbook entries to render with the HTML.
        guestlist = [];
        for row in cursor.fetchall():
          guestlist.append(dict([('name',cgi.escape(row[0])),
                                 ('message',cgi.escape(row[1])),
                                 ('ID',row[2])
                                 ]))

        variables = {'guestlist': guestlist}
        template = JINJA_ENVIRONMENT.get_template('main.html')
        self.response.write(template.render(variables))
        db.close()

class Query(webapp2.RequestHandler):
    def post(self):
        # Handle the post to create a new user and grant permissions.
        name = self.request.get('cityname')

        if (os.getenv('SERVER_SOFTWARE') and
            os.getenv('SERVER_SOFTWARE').startswith('Google App Engine/')):
            db = MySQLdb.connect(unix_socket='/cloudsql/' + _INSTANCE_NAME, db='im', user='root', passwd='')
        else:
            db = MySQLdb.connect(host='127.0.0.1', port=3306, db='im', user='root', passwd='password')
            # Alternatively, connect to a Google Cloud SQL instance using:
            # db = MySQLdb.connect(host='ip-address-of-google-cloud-sql-instance', port=3306, db='guestbook', user='root')

        cursor = db.cursor()


statement = """SELECT country_id, region_id FROM cities WHERE name = %s """
command = cursor.execute(statement,value)
results = cursor.fetchall()

for record in results:
    country_code = record[0]
    region_code = record[1]

statement = """SELECT *  FROM countries WHERE id = %s """
command = cursor.execute(statement,country_code)
results = cursor.fetchall()
print results
for record in results[0]:
    print record


statement = """SELECT *  FROM regions WHERE id = %s """
command = cursor.execute(statement,region_code)
results = cursor.fetchall()
print results
for record in results[0]:
    print record

        db.commit()
        db.close()

        self.redirect("/")

application = webapp2.WSGIApplication([('/', MainPage),
                               ('/sign', Guestbook)],
                              debug=True)

def main():
    application = webapp2.WSGIApplication([('/', MainPage),
                                           ('/sign', Query)],
                                          debug=True)
    run_wsgi_app(application)

if __name__ == "__main__":
    main()

