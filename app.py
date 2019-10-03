from flask import Flask
from flask import Flask, request, jsonify, send_from_directory
from jwt_token import ValidateApiToken
import service
import service
import json
import logging
import os
app = Flask(__name__)


logging.basicConfig(filename='log/app.log', filemode='a',format='%(asctime)s- %(message)s',datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route('/bank_details',methods=['GET'])
def bank_details_api():

	para_data={}

	logger.info(request.headers)
	logger.info(request.args)

	if "Authorization" in request.headers.keys():
		headers=request.headers['Authorization']
		conf=ValidateApiToken(headers)
		verify=conf.verify_token()
	

		if verify['Access']=="Access Granted":
			logger.info(verify)
			try:
				para_data["ifsc"]=request.args['ifsc']
				para_data["limit"]=request.args['limit'] 
				para_data["offset"]=request.args['offset']
			except Exception:
				para_data["limit"]= 1
				para_data["offset"]= 0
			
			db_connect=service.connect(para_data)
			return json.dumps({'success':True,"Bank_Details":db_connect},default=str)

		elif verify['success']=="False" and verify['Access']=='Access Denied':
			logger.error(verify['Access'])
			return jsonify({'Error': "Invalid credentials"}),400

		else:
			logger.error(verify['Access'])
			return jsonify({'Error': "Oops Token Expired"}),400

	else:
		logger.error("Invalid Access_token or parameters")
		return jsonify({'Error': "Invalid request or parameters"}),400






@app.route('/branches_details',methods=['GET'])
def details_of_branches_api():

	para_data={}

	logger.info(request.headers)
	logger.info(request.args)

	
	if "Authorization" in request.headers.keys():
		headers=request.headers['Authorization']
		conf=ValidateApiToken(headers)
		verify=conf.verify_token()

		if verify['Access']=="Access Granted":
			logger.info(verify)
			try:
				para_data["bank_name"]=request.args['bank_name']
				para_data["city"]=request.args['city']
				para_data["limit"]=request.args['limit'] 
				para_data["offset"]=request.args['offset']
			except Exception:
				para_data["limit"]= 10
				para_data["offset"]= 0
				
			db_connect=service.connect(para_data)
			return json.dumps({'success':True,"Details_of_Branches":db_connect},default=str)

		elif verify['success']==False and verify['Access']=='Access Denied':
			logger.error(verify['Access'])
			return jsonify({'Error': "Invalid credentials"}),400

		else:
			logger.error(verify['Access'])
			return jsonify({'Error': "Oops Token Expired"}),400
	else:
		logger.error("Invalid Access_token")
		return jsonify({'Error': "Invalid request"}),400

	
	


	
	

if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	os.environ["API_USER"]="NARUTO"
	os.environ["API_PASSWORD"]="1234@"
	os.environ["HOST"]="localhost"
	os.environ["DATABASE"]="bank"
	os.environ["DB_USER"]="postgres"
	os.environ["DB_PASSWORD"]="myPassword"
	app.run(host='0.0.0.0', port=port ,debug=True)
	

