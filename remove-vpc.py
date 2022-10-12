import boto3
client=boto3.client("ec2")
response = client.delete_vpc(
    VpcId='You_VPC_ID',)
response
