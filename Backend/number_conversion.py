import zeep
import zeep.exceptions
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

wsdl = 'https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL'
#SOAP client
client = zeep.Client(wsdl=wsdl)

#Function for number to words
@app.route('/api/number-to-words', methods=['GET', 'OPTIONS'])
def number_to_words():
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
    number = request.args.get('number')
    if number is None:
        return jsonify({'Please input a number!'})
    try:
        result = client.service.NumberToWords(number)
        return jsonify({'number':number, 'words':result})
    except zeep.exceptions.Fault as fault:
        return jsonify({f"Exception occured!: {fault}"})

# Raw format of the response
# Response XML:
# <?xml version="1.0" encoding="utf-8"?>
# <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
#   <soap:Body>
#     <NumberToWordsResponse xmlns="http://www.dataaccess.com/webservicesserver/">
#       <NumberToWordsResult>five hundred</NumberToWordsResult>
#     </NumberToWordsResponse>
#   </soap:Body>
# </soap:Envelope>
# Parsed Result: 500 -> five hundred

if __name__ == "__main__":
    app.run(debug=True)