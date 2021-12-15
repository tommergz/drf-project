# import boto3

# s3 = boto3.resource('s3')


# for bucket in s3.buckets.all():
#     print(bucket.name)

# data = open('test.jpg', 'rb')
# s3.Bucket('my-bucket').put_object(Key='test.jpg', Body=data)
# def add_file(self, request):
#     id = request.user.id

#     page = self.get_object()

#     if page.is_private:
#         page.follow_requests.add(id)
    
#     else:
#         page.followers.add(id)   

#     return id