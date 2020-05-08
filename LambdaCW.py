import boto3
import logging
import json
import sys
from botocore.exceptions import ClientError

#setup simple logging for INFO
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#define the connection
ec2 = boto3.resource('ec2')

client = boto3.client('ec2',region_name='us-west-2') #Add your region

def put_cpu_alarm(instance_id):
    client   = boto3.client('cloudwatch')
    response = client.put_metric_alarm (
        AlarmName          = f'NetworkOut_ALARM_{instance_id}',
        AlarmDescription   = 'Alarm when server NetworkOut bytes does not exceed 40 bytes',
        MetricName         = 'NetworkOut',
        Namespace          = 'AWS/EC2' ,
        Statistic          = 'Average',
        ActionsEnabled     = True,
        AlarmActions       = ['arn:aws:automate:us-west-2:ec2:stop'], #Add your region
        Dimensions         = [{'Name': 'InstanceId', 'Value':instance_id}],
        Period             = 120,
        EvaluationPeriods  = 4,
        Threshold          = 40,
        ComparisonOperator = 'LessThanOrEqualToThreshold',
        TreatMissingData   = 'notBreaching'
    )
    print (instance_id)

def lambda_handler(event, context):
    print("Received event:" + json.dumps(event, indent=2))
    instance_id = event['detail']['instance-id']
    print ("Instance:",instance_id)
    ec2 = boto3.resource('ec2')

    instance = ec2.Instance(instance_id)
    for tags in instance.tags:
        if tags["Key"] == 'AutoStop':
            put_cpu_alarm(instance_id)
            print ("Alarm applied")
        else:
            print ("Alarm not applied")

