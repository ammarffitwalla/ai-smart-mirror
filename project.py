from flask import Flask
from flask import request #JASON structured data
from flask import make_response
import paho.mqtt.client as paho #request publish
import json
import pprint #structured printing
import random
#from apiclient import discovery

app=Flask(__name__)

broker="52.66.197.30"
client= paho.Client("client-001") 
client.connect(broker)

@app.route('/webhook', methods=['POST'])

def webhook():

	req = request.get_json(silent=True, force=True)
	print("Request:")
	pprint.pprint(req)
	res = makeWebhookResult(req)
	res = json.dumps(res, indent=4)
	print(res)
	r = make_response(res)
	r.headers['Content-Type'] = 'application/json'
	return r


def makeWebhookResult(req):

	result = req.get("result")
	action = result.get("action")
	print(action)
	parameters = result.get("parameters")
	print("parameters")
	pprint.pprint(parameters)
	num1=parameters.get("number")
	num2=parameters.get("number1")
	sign=parameters.get("synonyms")
	
	if num1 and num2 and sign:
		if sign=="+":
			a=int(num1)+int(num2)
			l=["The sum of "+ str(num1) + " and "+ str(num2) + " is "+ str(a), "The addition of "+ str(num1) + " and "+ str(num2) + " is "+ str(a),]
			speech=random.choice(l)
			print(speech)
			
		if sign=="-":
			a=int(num1)-int(num2)
			l=["The substraction of "+ str(num1) + " and "+ str(num2) + " is "+ str(a), "The answer is "+ str(a),]
			speech=random.choice(l) 
			print(speech)
		if sign=="*":
			a=int(num1)*int(num2)
			l=["The multiplication of "+ str(num1) + " and "+ str(num2) + " is "+ str(a), "The product for "+ str(num1) + " and "+ str(num2) + " is "+ str(a),]
			speech=random.choice(l) 
			print(speech)
		if sign=="/":
			a=int(num1)/int(num2)
			speech="The division of "+ str(num1) + " and "+ str(num2) + " is "+ str(a) 
			print(speech)

	if  action=="hello":
		message=[
                    {
                    "speech": "how can i help you?", 
                    "type": 0
                     },
                  
                     {
                    "displayText": "how can i help you?" ,
                    "platform": "google",
                    "textToSpeech": "how can i help you?" ,
                    "type": "simple_response"
                    },{
    "buttons": [
      {
        "openUrlAction": {
          "url": "google.com"
        },
        "title": "title working"
      }
    ],
    "formattedText": "formattedText working",
    "image": {
      "url": "https://www.google.co.in/search?q=google&rlz=1C1CHBD_enIN821IN821&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjq7cLSmLXeAhUEFHIKHXrpDbwQ_AUIECgD&biw=1366&bih=657#imgrc=eCL1Y6f9xrPtDM:"
    },
    "platform": "google",
    "subtitle": "Subtitle working",
    "title": "title1 working",
    "type": "basic_card"
  }
                                        ]
	
	return {
    
        # "data": data,
        # "contextOut": [],
        
        "data": {
        "google": {
            "expect_user_response": True,
            "is_ssml": True,
            "permissions_request": None,
           
        }
        },
     "messages": message,
     "source": "aadhar-api",

        }  
'''  
	return{
			"speech": speech,
			"displayText": speech,
            "source": "apiai-weather-webhook-sample"
		}
'''

if __name__=="__main__":
	app.run()