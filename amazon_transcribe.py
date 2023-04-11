import pandas as pd
import time
import boto3 #boto3 is the aws sdk for python

import csv
with open("amazon-key.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    access_key_id = row[0]
    secret_access_key = row[1]

transcribe = boto3.client('transcribe',
aws_access_key_id = access_key_id,
aws_secret_access_key = secret_access_key,
region_name = "us-east-2"
) 

#data is uploaded to the S3 Bucket
BUCKET_NAME = "livestreamaudiobucket"
FILE_NAME = "SM1_F1_A01.wav"
JOB_NAME = "transcribe_job" # can be anything


def start_transcribe_job(transcribe, job_name, bucket, file):
    # this is the location of your audio file
    file_uri = f'https://s3.amazonaws.com/{bucket}/{file}'
    
    # try launching the job and return any error messages
    try:
        transcribe.start_transcription_job(
            TranscriptionJobName=job_name,
            Media={'MediaFileUri': file_uri},
            MediaFormat='mp3',
            LanguageCode='en-US')
        return True
    except Exception as e:
        return e
    
