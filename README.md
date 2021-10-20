# Python Way : To Retrieve Instance meta data
## Method 1
- Get VM metadata from Google Cloud
## Usage
Does the discovery for test project and finds the metdata for all the instances in JSON format
```python 
>>>python get_instance_metadata_googlecloud.py
```


## Method 2
- Get VM metadata from AWS using its IMDS
### Usage
```python
>>>python get_instance_metadata_aws.py
>>>ami-id
```
### Arguments
```diff
+ ami-id
+ ami-launch-index
+ ami-manifest-path
+ block-device-mapping
+ events
+ hostname
+ iam
+ instance-action
+ instance-id
+ instance-life-cycle
+ instance-type
+ local-hostname
+ local-ipv4
+ mac
+ metrics
+ network
+ placement
+ profile
+ public-hostname
+ public-ipv4
+ public-keys
+ reservation-id
+ security-groups
+ services
```



