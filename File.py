import boto3
s3 = boto3.resource("s3")
s3.Bucket('broly').upload_file(r'/home/ec2-user/environment/Python/Broly.jpg', 'Broly.jpg')
    
    