# AWS_S3_Python
Amazon S3 Buckets
An Amazon S3 bucket is a storage location to hold files. S3 files are referred to as objects.

This section describes how to use the AWS SDK for Python to perform common operations on S3 buckets.

#Create an Amazon S3 Bucket
The name of an Amazon S3 bucket must be unique across all regions of the AWS platform. The bucket can be located in a specific region to minimize latency or to address regulatory requirements.

#Uploading Files
The AWS SDK for Python provides a pair of methods to upload a file to an S3 bucket.
The upload_file method accepts a file name, a bucket name, and an object name. The method handles large files by splitting them into smaller chunks and uploading each chunk in parallel.

Details at: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-examples.html
