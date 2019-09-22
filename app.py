from flask import Flask
from flask import Flask, request, jsonify, send_from_directory
from jwt_token import ValidateApiToken
import service
import service
import json
import logging


app = Flask(__name__)


logging.basicConfig(filename='log/app.log', filemode='a',format='%(asctime)s- %(message)s',datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route('/bank_details',methods=['POST'])
def bank_details_api():
	
	rqst_data=request.get_json()
	

	if "Asccess_token" in rqst_data.keys() and "ifsc" in rqst_data.keys():
		
		headers=rqst_data["Access_token"]
		conf=ValidateApiToken(headers)
		verify=conf.verify_token()

		if  verify['Access']=="Access Granted":
			logger.info(verify['Access'])
			db_connect=service.connect(rqst_data)
			return json.dumps({'success':True,"Bank_Details":db_connect},default=str)

		elif verify['success']=="False" and verify['Access']=='Access Denied':
			logger.error(verify['Access'])
			return jsonify({'Error': "Invalid credentials"}),400

		else:
			logger.info(verify['Access'])
			return jsonify({'Error': "Token Expired"}),400

	else:
		logger.info("Invalid request")
		return jsonify({'Error': "Invalid request"}),400






@app.route('/branches_details',methods=['POST'])
def details_of_branches_api():
	
	rqst_data=request.get_json()
	
	
	if "Access_token" in rqst_data.keys() and "bank_name" in rqst_data.keys():
	
		headers=rqst_data["Access_token"]
		conf=ValidateApiToken(headers)
		verify=conf.verify_token()

		if verify['Access']=="Access Granted":
			logger.info(verify)
			db_connect=service.connect(rqst_data)
			return json.dumps({'success':True,"Details_of_Branches":db_connect},default=str)

		elif verify['success']==False and verify['Access']=='Access Denied':
			logger.error(verify['Access'])
			return jsonify({'Error': "Invalid credentials"}),400

		else:
			logger.info(verify['Access'])
			return jsonify({'Error': "Token Expired"}),400
	else:
		logger.info("Invalid request access_token not found")
		return jsonify({'Error': "Invalid request"}),400

	
	


	
	

	

if __name__ == '__main__':
	app.run(debug=True,port=5001)