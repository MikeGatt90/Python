#Delete and EBS Volume from Snapshot

import boto3

ec2_client=boto3.client("ec2")

ec2_client.delete_snapshot(SnapshotId='snap-0834d7afbcb68efb7')