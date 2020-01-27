import os
from flask import Flask, jsonify, request
import urllib
import urllib.request
import json



app = Flask(__name__)

@app.route('/')
def Welcome():
    return app.send_static_file('index.html')

#enter your API information obtained previously
url = 'https://ussouthcentral.services.azureml.net/workspaces/bead0e202b29437d9283b3c06d52819a/services/c730aba8ba3945c3a9da2703930989a4/execute?api-version=2.0&details=true'
api_key = 'WKCn+LV/Pt6soadGoOyRjnxavS6hLdcIObCnRSRZ7bAvn89YJ9OItk15u+N07w+k2ZeAfl5lcSCkyGCpAFXJMg==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

#method starts on form submit
@app.route('/analyze', methods=['GET', 'POST'])
def Analyze():
    #gets text from form element in index.html
    comment_text = request.form['text']
      
    #if comment is not empty
    if comment_text != "":
        data =  {
        "Inputs": {
                "input1":
                {
                    "ColumnNames": ["text_column"],
                    "Values": [ [ comment_text ], ]
                },        },
            "GlobalParameters": {
            }
        }
        
        #encodes our data object as a json object as a string
        body = str.encode(json.dumps(data))
        #submits request to AzureML in correct format
        req = urllib.request.Request(url, body, headers)
        #opens our req object in parsable format
        response = urllib.request.urlopen(req)
        
        result = response.read()

    return result

   
#This sets that we want to use local host 5000 for this call
port = os.getenv('PORT', '5003')

#This starts the web server if we are on the correct webpage
#If true, this starts the app with debugging at the correct port
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port), debug=True)

