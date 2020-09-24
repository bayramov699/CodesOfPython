import json
from os import replace

def change_info():
    changed = []
    changingItems = ['domain_length', 'pronouncement', 'brandable']
    numberToString = {
        "1": 'bad',
        "2": 'poor',
        "3": 'fair',
        "4": 'good',
        "5": 'excellent',
    }

    with open('./d.json', 'r') as f:
        info = json.loads(f.read())
        for item in info:
            item['fields'].update(
                {key: numberToString.get(value, "good") for (key, value) in item['fields'].items() if key in changingItems})
            changed.append(item)
    with  open('./changed_base.json', 'w') as f:
        f.write(json.dumps(changed))

change_info()

"""new_file = open("d.json", "r")
json_object = json.load(new_file)
new_file.close()
print(json_object)

for item in json_object:
    if('domain_length', 'pronouncement', 'brandable')==1:
        replace("bad")
    elif('domain_length', 'pronouncement', 'brandable')==2:
        replace("poor")
    elif('domain_length', 'pronouncement', 'brandable')==3:
        replace("fair")
    elif('domain_length', 'pronouncement', 'brandable')==4:
        replace("good")
    elif('domain_length', 'pronouncement', 'brandable')==5:
        replace("excellent")

json_object['domain_length', "1"] = 'bad'
json_object["2"] = 'poor'
json_object["3"] = 'fair'
json_object["4"] = 'good'
json_object["5"] = 'excellent'


new_file = open("d.json", "w")
json.dump(json_object, new_file)
new_file.close()"""