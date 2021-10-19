from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()

service = discovery.build('compute', 'v1', credentials=credentials)
# Project ID for this request.
project = ['test'] # Update placeholder value with your project id


def retrieve_instance_data(service, project_list):
    # Get list & details of all instances for all projects in the project list
    output = []
    for project_id in project_list:
        # First get the list of zones
        zone_list = []
        zone_result = service.zones().list(project=project_id).execute()
        for zone_rows in zone_result['items']:
            zone_list.append(zone_rows['name'])
        for zone_name in zone_list:
            # For every zone for each project, get the instance details
            instances_result = service.instances().list(project=project_id, zone=zone_name).execute()
            if 'items' in instances_result:
                for instance_row in instances_result["items"]:
                    output_row = []
                    metadata_dict = {}
                    # Project id will the first element
                    output_row.append(project_id)
                    output_row.extend([instance_row["name"],instance_row["labels"]["app-name"],instance_row["labels"]["biz-unit"],instance_row["labels"]["env-name"]])
                    # Get metadata key-value entries
                    for metadata_entry in instance_row["metadata"]["items"]:
                        metadata_dict[metadata_entry['key']] = metadata_entry['value']
                    output_row.extend([metadata_dict['server-role'], metadata_dict['server-type'], metadata_dict['os-image']])
                    output.append(output_row)
    return output
output = retrieve_instance_data(service,project)
print (output)
