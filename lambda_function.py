import json
import boto3
import pymysql

#def lambda_handler():
c4dbjlksawrr
	rds_host  = "database-1.c4dbjlksawrr.eu-west-2.rds.amazonaws.com"
	name = 'admin'
	password = 'hackjarhackjar'
	db_name = 'db_eb'
	try:
		conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
		print('connected')
	except pymysql.MySQLError as e:
		print("ERROR: Unexpected error: Could not connect to MySQL instance.")
	client = boto3.client('sqs')
	tmpState = 0
	while tmpState ==0:
		try:
			response = client.receive_message(
					QueueUrl='https://sqs.eu-west-2.amazonaws.com/460220960495/db_eb_queue',
					MaxNumberOfMessages=1,
					WaitTimeSeconds=2,
					ReceiveRequestAttemptId='string'
					)
			tmpList = response['Messages']
			tmpResponse = tmpList[0]
			response1 = client.delete_message(
					QueueUrl='https://sqs.eu-west-2.amazonaws.com/460220960495/db_eb_queue',
					ReceiptHandle=tmpResponse['ReceiptHandle']
					)
			messageBody = tmpResponse['Body']
			with conn.cursor() as cur:
				query = "insert into db_eb (`data`) values('"+messageBody+"')"
				#print(query)
				cur.execute(query)	
				conn.commit()
		except:
			#print("falied"+query)
			tmpState=1

	return {
		'statusCode': 200,
		'body': "Successfully Executed"
	}
