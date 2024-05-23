import zeep
import requests
import xml.etree.ElementTree as ET

def soap_request():
    url= "https://www.dataaccess.com/webservicesserver/NumberConversion.wso"

    payload= """ <?xml version="1.0" encoding="utf-8"?>
                    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                    <soap:Body>
                        <NumberToWords xmlns="http://www.dataaccess.com/webservicesserver/">
                            <ubiNum>500</ubiNum>
                        </NumberToWords>
                    </soap:Body>
                </soap:Envelope>"""

    headers={
        'Content-Type: text/xml; charset=utf-8'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    
    print("xml response",response.text)
    print("status response", response)

    root = ET.fromstring(response.text)

soap_request()