import boto3

s3_resource=boto3.client("s3")
objects = s3_resource.list_objects(Bucket="broly")["Contents"]
print(objects)
print(len(objects))