import flask
import json
import mariadb

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# configuration used to connect to MariaDB
config = {
    'host': '127.0.0.1',
    'port': 3307,
    'user': 'root',
    'password': 'Password123!',
    'database': 'company'
}

# route to return all people
@app.route('/api/employees', methods=['GET'])
def index():
   # connection for MariaDB
   conn = mariadb.connect(**config)
   # create a connection cursor
   cur = conn.cursor()
   # execute a SQL statement
   cur.execute("select * from employees")

   # serialize results into JSON
   row_headers=[x[0] for x in cur.description]
   rv = cur.fetchall()
   json_data=[]
   for result in rv:
        json_data.append(dict(zip(row_headers,result)))

   # return the results!
   return json.dumps(json_data)

app.run()
