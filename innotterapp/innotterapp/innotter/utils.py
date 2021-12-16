import logging
from botocore.exceptions import ClientError


def get_object(s3, bucket, new_img):
    try:
        response = s3.generate_presigned_url('get_object', Params={'Bucket': bucket, 'Key': new_img}, ExpiresIn=100)
    except ClientError as e:
        logging.error(e)
        return None

    return response
