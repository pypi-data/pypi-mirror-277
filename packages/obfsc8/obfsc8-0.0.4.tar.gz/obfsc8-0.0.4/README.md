# obfsc8
The **obfsc8** package provides a simple way to obfuscate Personally Identifiable Information (PII) found within CSV, Parquet and JSON files that are stored in the Amazon S3 service.
Designed to be used within Amazon Lambda, EC2 and ECS services, **obfsc8** returns a bytes object of the obfuscated file data that can be easily processed, for example by the boto3 S3.Client.put_object function.  
  


## Setup
Install the latest version of obfsc8 with:
```
pip install obfsc8
```  
  

## obfsc8 methods
The obfsc8 package has one associated function:  

**obfsc8.obfuscate**(  
    ***input_json***: str,  
    ***restricted_fields***: list = [],  
    ***replacement_string***: str = "***"  
)  


### Parameters 

**input_json**
JSON string with the following format:  

    {
        "file_to_obfuscate": "s3://...",
        "pii_fields": ["...", ...]
    }
      

For example, the following requests that the "name" and "email_address" fields be obfuscated in the S3 file found at s3://my_ingestion_bucket/new_data/file1.csv: 
        
    
    {
        "file_to_obfuscate": "s3://my_ingestion_bucket/new_data/file1.csv",
        "pii_fields": ["name", "email_address"]
    }


**restricted_fields**
List of protected fields that will not be obfuscated, even if they appear in the 
"pii_fields" key of the input_json parameter.  Defaults to an empty list.

**replacement_string**
    String used to obfuscate all row values for the fields identified in the "pii_fields" key of the input_json parameter, barring inclusion of each field in the restricted_fields parameter list.  Defaults to the string "***".  

### Returns
BytesIO object containing obfuscated file data in the same file format as the input file defined in input_json (CSV, Parquet or JSON).  

  

## Amazon Lambda Usage
### Amazon Lambda Layer creation
If using this package within an Amazon Lambda instance, first create a Lambda Layer containing it:
```
mkdir obfsc8
cd obfsc8
mkdir python
cd python
pip install obfsc8 -t .
cd ..
zip -r obfsc8_layer.zip .
```
The resulting obfsc8_layer.zip file should be uploaded to the Amazon Lambda instance as a Lambda Layer.

Note that due to the current size of the obfsc8 package, it is not possible for an Amazon Lambda to have an obfsc8 Layer and an AWS SDK Layer loaded at the same time.
It is however possible to have an obfsc8 Layer and a boto3 Layer loaded at the same time.
If you wish to use boto3 within an Amazon Lambda, create an additional boto3 Lambda Layer by repeating the steps above, but replacing "obfsc8" with "boto3", and uploading the resulting .zip to the Lambda as a Lambda Layer.  


### Amazon Lambda lambda_handler example code
The following is an example of possible usage of obfsc8 within an Amazon Lambda, with boto3 handling the writing of the obfuscated file data to an S3 bucket: 
```
import json
import boto3
import obfsc8 as ob


def lambda_handler(event, context)
    try:
        obfuscation_instructions = json.dumps(event["detail"])
        buffer = ob.obfuscate(obfuscation_instructions)
        
        source_filepath_elements = event["detail"]["file_to_obfuscate"].split("/")
        source_filepath_elements[-1] = "obfs_" + source_filepath_elements[-1]
        obfuscated_file_key = ("/").join(source_filepath_elements[3:])
        
        s3 = boto3.client("s3", region_name="eu-west-2")
        put_response = (s3.put_object(
            Bucket="test-bucket",
            Key=obfuscated_file_key, Body=buffer))
            
        return {
            'statusCode': 200,
            'body': json.dumps(f"Successfully obfuscated: {obfuscation_instructions}")
        }
    
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps(f"Failed to obfuscate file: {e}")
        }
```

A test event similar to the following can be used to check the above code functions correctly:
```
{
  "detail-type": "File obfuscation event",
  "source": "aws.eventbridge",
  "detail": {
    "file_to_obfuscate": "s3://source-bucket/2024/test_data.csv",
    "pii_fields": [
      "name",
      "email_address"
    ]
  }
}
```