import boto3
ec2_client=boto3.client("ec2")

ec2_client.create_volume(AvailabilityZone='us-east-1a',
      Encrypted=True,
      Size=12,
      SnapshotId='snap-0834d7afbcb68efb7',
      VolumeType='gp2')