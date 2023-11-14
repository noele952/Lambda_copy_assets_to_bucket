import boto3
import os

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    try:
        source_bucket = os.environ['SourceBucketName']
        destination_bucket = os.environ['DestinationBucketName']
        folder = os.environ['Folder']

        # List objects in the source bucket
        response = s3_client.list_objects_v2(Bucket=source_bucket)
        objects = response.get('Contents', [])

        # Copy each object to the destination bucket with the specified folders
        for obj in objects:
            source_key = obj['Key']
            destination_key = f'{folder}{os.path.basename(source_key)}'

            s3_client.copy_object(
                Bucket=destination_bucket,
                CopySource={'Bucket': source_bucket, 'Key': source_key},
                Key=destination_key
            )


        return {'statusCode': 200, 'body': 'Files copied successfully.'}

    except Exception as e:
        print(f"Error: {str(e)}")
        return {'statusCode': 500, 'body': 'Error copying files.'}

