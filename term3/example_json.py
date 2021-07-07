import json

file = open('C:\\Users\\G.V Shop\\PycharmProjects\\Luna_Lovegood\\term3\\json_file.json')
json_data = json.load(file)

print(json_data[1]["10"])
