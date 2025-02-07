'''JavaScript Object Notation'''
import json

with open('sample_states.json') as f:
    data = json.load(f)

for state in data['states']:
    del state['area_codes']

with open('new_states_1.json','w') as f:
    json.dump(data, f, indent=2)