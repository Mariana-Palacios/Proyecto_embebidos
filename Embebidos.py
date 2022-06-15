from flask import Flask, request
from flask_restful import Api
from db_actions import get_all_data, save_data

app = Flask(__name__)
api = Api(app)

@app.route('/data')
def get_data():
    response = get_all_data()
    return({'data': response})

@app.route('/save', methods=['POST'])
def put_data():
    resp = save_data(request.json)
    return({'data': 'ok'})

if __name__ == '__main__':
    app.run(debug=True)
