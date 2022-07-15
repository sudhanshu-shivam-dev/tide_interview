from distutils.log import debug
from flask import jsonify
from flask import Flask
import json 
from flask import request
from manager import send_ack_m 
app = Flask(__name__)

@app.route('/submit_req', methods = ['POST'])
def send_ack():
    
    req = request.json
    return jsonify(send_ack_m(req['name'], req['domain']))
    # return 'success'


   
if __name__ == '__main__':
    app.run(debug=True)