import sys
import json
import yaml
import os

filename, file_extension = os.path.splitext(sys.argv[1])
with open(sys.argv[1], "r") as file:
  metadata_to_add = { 'Deployer': '{}'.format(sys.argv[2]) }
  if file_extension.lower() == ".yaml" or file_extension == ".yml":
    data = yaml.load(file, Loader=yaml.BaseLoader)
    if 'Metadata' in data:
      data['Metadata'].update(metadata_to_add)
    else:
      data.update({'Metadata': { }})
      data['Metadata'].update(metadata_to_add)
  else:
    data = json.load(file)
    if 'Metadata' in data:
      data['Metadata'].update(metadata_to_add)
    else:
      data.update({'Metadata': { }})
      data['Metadata'].update(metadata_to_add)

with open(sys.argv[1], "w") as file:
  if file_extension.lower() == ".yaml" or file_extension == ".yml":
    data = yaml.safe_dump(data, file)
  else:
    data = json.dump(data, file, indent=2)