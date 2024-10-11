import csv
from collections import namedtuple
from fastavro import parse_schema, writer
import random

first_name = ['ikenna', 'chinyere', 'blaise', 'andre', 'obum', 'Daniel']
Lastname = ['ikenna', 'chinyere', 'blaise', 'andre', 'obum', 'Daniel']


schema = {
            "namespace": "students_data2.avro",
            "type": "record",
            "name": "students_data2",
            "fields": [
                        {"name": "Id", "type": "string"},
                        {"name": "first_name", "type": "string"},
                        {"name": "Last_name", "type": "string"}
                      
                        ]
                    }

parsed_schema = parse_schema(schema)
with open("users.avro", "wb") as fp:
    for i in range(10):
        data = [str(i),random.choice(first_name), random.choice(Lastname)]
        writer(fp, schema, data)
