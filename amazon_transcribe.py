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
region_name = "ap-south-1"
) 

#data is uploaded to the S3 Bucket
BUCKET_NAME = "livestreamaudiobucket"
FILE_NAME = "SM1_F1_A01.wav"
JOB_NAME = "transcribe_job2" # can be anything


def start_transcribe_job(transcribe, job_name, bucket, file):
    # this is the location of your audio file
    file_uri = f'https://s3.amazonaws.com/{bucket}/{file}'
    print("Starting Transcription Job")
    # try launching the job and return any error messages
    try:
        transcribe.start_transcription_job(
            TranscriptionJobName=job_name,
            Media={'MediaFileUri': file_uri},
            MediaFormat='wav',
            LanguageCode='en-US')
        return True
    except Exception as e:
        return e
    
    
    
def get_transcription_text(transcribe, job_name):

    import urllib.request
    import json
    import time
    
    # let's obtain the job instance
    job = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    
    # and it's status
    status = job['TranscriptionJob']['TranscriptionJobStatus']
    
    # check the status every 5 seconds and 
    # return the transcribed text if the job is finished
    # otherwise return None if job failed
    while True:
        if status == 'COMPLETED':
            print(f"Job {job_name} completed")
            with urllib.request.urlopen(job['TranscriptionJob']['Transcript']['TranscriptFileUri']) as r:
                data = json.loads(r.read())
            return data['results']['transcripts'][0]['transcript']
        elif status == 'FAILED':
            print(f"Job {job_name} failed")
            return None
        else:
            print(f"Status of job {job_name}: {status}")
            time.sleep(5)
    
# launch the job
job_status = start_transcribe_job(transcribe, JOB_NAME, BUCKET_NAME, FILE_NAME)

print(job_status)
# if job launched successfully `job_status` will be True
if job_status: # and we can start requesting the results from the service
    text = get_transcription_text(transcribe, JOB_NAME)
    print(f'The transcribed text for {FILE_NAME} file:')
    print(text)
else: # or print the error code if somethign went wrong
    print(f'Job {JOB_NAME} failed with the error: {job_status}')
