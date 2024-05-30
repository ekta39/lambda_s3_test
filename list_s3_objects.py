import boto3

def lambda_handler(event, context):

    # Extract bucket name from the event
    bucket_name = event['bucketname']

    # Initialize the S3 client
    s3 = boto3.client('s3')

    # List objects in the specified bucket
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)

        # Check if objects were found
        if 'Contents' in response:
            files = [obj['Key'] for obj in response['Contents']]
            return files
        else:
            return []
    except Exception as e:
        print(f"Error: {e}")
        return []
