import requests
import json
import pprint
api_key = "38d71704-704d-4529-9267-5e83bc499891"

def annotate(text):
    base_url = "http://data.bioontology.org"
    annotator_url = base_url + "/annotator"
    params = {
        "apikey": api_key,
        "format": "json",
        "ontologies": "SNOMEDCT,LOINC",

        "text": text, 
    }
    r = requests.get(annotator_url, params=params)
    return r.json()
    
line = "Chest pain is a symptom of Myocardial Infarction."
lst = annotate(line)

a = {}
def output():
    for i in range(len(lst)):
        key = lst[i]["annotations"][0]["text"]
        value = lst[i]["annotatedClass"]["@id"]
        a.setdefault(key,[])
        a[key].append(value)
    return pprint.pprint(a)  
output() 
   

