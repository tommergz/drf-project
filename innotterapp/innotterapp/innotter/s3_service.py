from datetime import datetime
import os
import boto3
from rest_framework.decorators import permission_classes


from innotter.utils import get_object


bucket = os.environ.get('BUCKET_NAME')


def add_file(local_file):
    new_img = f"{bucket}/{datetime.now().microsecond}.jpg"
    print(new_img)
    s3 = boto3.client('s3', aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                      aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
                      region_name='eu-north-1')
    s3.put_object(Bucket=bucket, Key=new_img, Body=local_file)

    presigned_url = get_object(s3, bucket, new_img)
    print(presigned_url)
    return presigned_url