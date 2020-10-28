from flask import Flask, jsonify, request, json
import psycopg2
# conn = psycopg2.connect("dbname=tinkle_tracker_test user=jakestucky")


app = Flask(__name__)

companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]


@app.route('/companies', methods=['GET'])
def get_companies():
  return json.dumps(companies)


@app.route('/')
def index():
    return jsonify(data="hello world from jake")

if __name__ == "__main__":
    app.run()

# cur = conn.cursor()
# cur.execute("SELECT * FROM user")
# records = cur.fetchone()

