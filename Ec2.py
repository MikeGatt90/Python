import boto3
ec2 = boto3.resource('ec2')

instances = ec2.create_instances(
        ImageId="ami-026b57f3c383c2eec",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="Python",
        SubnetId="subnet-072c908573b68f831")
    
    