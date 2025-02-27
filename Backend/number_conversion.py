import zeep
import zeep.exceptions

wsdl = 'https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL'

#SOAP client
client = zeep.Client(wsdl=wsdl)

#Function for number to words
def number_to_words(number):
    try:
        result = client.service.NumberToWords(number)
        print(f"Number to words: {number} ==> {result}" )
    except zeep.exceptions.Fault as fault:
        print(f"Exception occured!: {fault}")

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
    number_to_words(1500005414)