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
	rqst_data=request.get_json()
	para_data["ifsc"]=request.args['ifsc']
	if "limit" and  "offset" in para_data.keys():
		para_data["limit"]=request.args['limit']
		para_data["offset"]=request.args['offset']
	else:
		pass
	

	

	if "Access_token" in rqst_data.keys():
		headers=rqst_data["Access_token"]
		conf=ValidateApiToken(headers)
		verify=conf.verify_token()

		if verify['Access']=="Access Granted":
			logger.info(verify)
			db_connect=service.connect(para_data)
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






@app.route('/branches_details',methods=['GET'])
def details_of_branches_api():

	para_data={}
	rqst_data=request.get_json()
	para_data["bank_name"]=request.args['bank_name']
	para_data["city"]=request.args['city']
	
	para_data["limit"]=request.args['limit']
	para_data["offset"]=request.args['offset']

	
	if "Access_token" in rqst_data.keys():
		rqst_data=request.get_json()
		headers=rqst_data["Access_token"]
		conf=ValidateApiToken(headers)
		verify=conf.verify_token()

		if verify['Access']=="Access Granted":
			logger.info(verify)
			db_connect=service.connect(para_data)
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
	# Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    os.environ["API_USER"]="NARUTO"
    os.environ["API_PASSWORD"]="1234@"
    os.environ["HOST"]="localhost"
    os.environ["DATABASE"]="bank"
    os.environ["DB_USER"]="postgres"
    os.environ["DB_PASSWORD"]="myPassword"
    app.run(host='0.0.0.0', port=port ,debug=True)
    

 #    export API_USER="NARUTO"
	# export API_PASSWORD="1234@"
	# export HOST="localhost"
	# export DATABASE="bank"
	# export DB_USER="postgres"
	# export DB_PASSWORD="myPassword"