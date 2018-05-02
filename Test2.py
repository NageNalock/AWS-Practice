import boto3

s3 = boto3.resource('s3')
file_name = '11hello.txt'
s3.Object('start.demo', file_name).put(Body=open(file_name, 'rb'))
print(s3.Object('start.demo', '11hello.txt'))
print('https://s3.us-east-2.amazonaws.com/start.demo/'+file_name)

# for bucket in s3.buckets.all():
#     for key in bucket.objects.all():
#         print(key.key)