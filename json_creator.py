# imports
import json

# create a data with dictionary
data = {
    'name' : 'Mohammad hasan',
    'age' : 22,
    'skills': ['flutter','python','c#','unity','blender','photoshop']
}

# create a name for json file
file_name = 'data.json'


# create and open the file and put the data into the json file
with open(file_name , 'w') as json_file:
    json.dump(data,json_file,indent=4)


print(f'created : {json_file.name}')