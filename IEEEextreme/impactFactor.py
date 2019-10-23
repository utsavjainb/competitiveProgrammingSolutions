import json
from collections import defaultdict


num_inputs = int(input())

citations = defaultdict(int)
pubs = defaultdict(int)
mapping = {}
entries = []
output = []

for x in range(num_inputs):
    entries.append(json.loads(input()))

for entry in entries[0]["publications"]:
    mapping[entry["publicationTitle"]] = entry["publicationNumber"]
    for counts in entry["articleCounts"]:
        pubs[entry["publicationNumber"]] += int(counts["articleCount"])

for x in range(1, len(entries)):
    for entry in entries[x]["paperCitations"]["ieee"]:
        if entry["year"] in {"2018", "2017"}:
            citations[entry["publicationNumber"]] += 1

for key, value in mapping.items():
    IF = citations[value]/pubs[value]
    output.append((key, IF))
    
output.sort(key= lambda x : (x[1], x[0]), reverse=True)

for pair in output:
    print(pair[0], format(pair[1], '.2f'), sep=": ")
    
    