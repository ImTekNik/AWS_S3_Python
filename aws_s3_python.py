import boto3

s3_resource = boto3.resource('s3')
s3_client = boto3.client('s3')


def creat_bucket_to_aws_s3(new_bucket_name):
        s3_resource.create_bucket(Bucket=new_bucket_name,
                          CreateBucketConfiguration={
                              'LocationConstraint': 'eu-eest-1'})
        print(f"you bucket {new_bucket_name} create successfully")


def upload_file_to_aws_s3(bucket_name,file_name):
    s3_client.upload_file(file_name, bucket_name, file_name)
    print("file upload successfull")



def read_single_file_from_aws_s3(bucket_name,file_name):
        obj = s3_resource.Object(bucket_name, file_name)
        body = obj.get()['Body'].read()
        print(body)



def read_multiple_files_from_aws_s3(bucket_name):
        bucket = s3_resource.Bucket(bucket_name)
        for obj in bucket.objects.all():
                body_byte = obj.get()['Body'].read()
                print(body_byte + "\n")


def copy_to_bucket_aws_s3(bucket_from_name, bucket_to_name, file_name):
    copy_source = {
        'Bucket': bucket_from_name,
        'Key': file_name
                        }
    s3_resource.Object(bucket_to_name, file_name).copy(copy_source)





def delet_file_from_aws_s3(bucket_name,file_key):
    s3_resource.Object(bucket_name, file_key).delete()
    print(f"{file_key} successfully delet from {bucket_name}")



#call all function in main function......
creat_bucket_to_aws_s3("hello-bd")
upload_file_to_aws_s3("test.txt","inneed-bucket-1")
read_single_file_from_aws_s3("inneed-bucket-1","test.txt")
read_multiple_files_from_aws_s3("inneed-bucket-1")
copy_to_bucket_aws_s3("inneed-bucket-1","hello-rayhan","test.txt")
delet_file_from_aws_s3("inneed-bucket-1","test.txt")