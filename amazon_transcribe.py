import pandas as pd
import time
import boto3 #boto3 is the aws sdk for python

import csv
with open("amazon-key.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    aws_access_key_idprint = row[0]
    aws_secret_access_key = row[1]

# transcribe = boto3.client('transcribe',
# aws_access_key_id = #insert your access key ID here,
# aws_secret_access_key = # insert your secret access key here
# region_name = # region: usually, I put "us-east-2"
# ) 