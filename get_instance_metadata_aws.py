import requests
URI="http://169.254.169.254/latest/"
METADATA_URI="http://169.254.169.254/latest/metadata"
TOKEN_HEADER_TTL = "X-aws-ec2-metadata-token-ttl-seconds"
TOKEN_TTL = 21600
TOKEN_HEADER = "X-aws-ec2-metadata-token"
def meta_data(resourcetype):
    token_response = requests.put(
        URI + "api/token",
        headers={TOKEN_HEADER_TTL: str(TOKEN_TTL)},
        timeout=5.0,
    )
    token = token_response.text
    requests.headers.update({TOKEN_HEADER: token})
   
    metadataURL=METADATA_URI+'/'+resourcetype
    response = requests.get(metadataURL).text
    if response.status_code == '200':
            return response
    else:
        response.raise_for_status()

def main():
    choice=input("Enter your resource type to be retrieved from metadata server. eg. ami-id")
    meta_data(choice)

if __name__ == '__main__':main()



