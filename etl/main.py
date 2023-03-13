'''
python3 main.py -metadata eyJmdW5jdGlvbl9uYW1lIjogeyJicm9rZXJzIjogInB1bHNhcjovL2xvY2FsaG9zdDo2NjUwIiwgIndpbmRvdyI6IHt9LCAiaW5wdXRfdG9waWNzIjogeyJsaXN0X29mX3RvcGljcyI6IFsibm9uLXBlcnNpc3RlbnQ6Ly9wdWJsaWMvZGVmYXVsdC90b3BpYzEwMDEiLCAibm9uLXBlcnNpc3RlbnQ6Ly9wdWJsaWMvZGVmYXVsdC90b3BpYzExMDEiXSwgInN1YnNjcmlwdGlvbl9pZCI6ICJzdWJzY3JpcHRpb25faWQxIn0sICJzaW5rIjogeyJuYW1lIjogInN0ZG91dCJ9LCAiaW5wdXRfc2NoZW1hIjogeyJuYW1lIjogIkNvbXBhbnlSZWNvcmQuIiwgImRldGFpX3NjaGVtYSI6IHsiY29tcGFueXJlY29yZCI6IHsiY29tcGFueV9uYW1lIjogInN0cmluZyIsICJwbGFjZSI6ICJzdHJpbmciLCAidGF4X251bWJlciI6ICJzdHJpbmciLCAicmV2ZW51ZSI6ICJpbnQifX19LCAib3BzIjogeyJtYXRjaCI6IHsiX19jb21tZW50IjogInNwZWNpZmljYXRpb24gb2YgYW4gb3AsIHNwZWNpZmljIHRvIG9wIiwgImF0IjogIiQiLCAid2hlcmUiOiB7ImZpZWxkIjogInBsYWNlIiwgIm9wZXJhdG9yIjogIj0iLCAidmFsdWUiOiAiU2FpR29uIn19LCAicm9sbHVwIjogeyJfX2NvbW1lbnQiOiAidGhpcyBvcGVyYXRvciBpcyBiYXNlZCBvbiBhIHdpbmRvdyBvZiBkYXRhIn0sICJhZ2dyZWdyYXRlIjogeyJfX2NvbW1lbnQiOiAidGhpcyBvcGVyYXRvciBjYW4gYmUgYXBwbGllZCBmb3IgYSBzaW5nbGUgbWVzc2FnZSBvciBhIHdpbmRvdyBvZiBkYXRhIn0sICJlbnJpY2giOiB7Il9fY29tbWVudCI6ICJmb3IgYSBzaW5nbGUgZGF0YSJ9fX19
'''
import pulsar
import json
import argparse
import base64

parser = argparse.ArgumentParser()

parser.add_argument('-metadata', '--metadata', help='base64 ascii metadata configuration file')
args = parser.parse_args()       
print(args.metadata)

base64_string = args.metadata 
base64_bytes = base64_string.encode('ascii')

data_bytes = base64.b64decode(base64_bytes)
data = data_bytes.decode('ascii')

print("Decoded Data:", data)



# args = parser.parse_args()


# PULSAR_CONNECTION = 'pulsar://pulsar:6650'

# client = pulsar.Client(PULSAR_CONNECTION)

# consumer = client.subscribe('my-topic', 'my-subscription')

# while True:
#     msg = consumer.receive()
#     try:
#         print("Received message '{}' id='{}'".format(msg.data(), msg.message_id()))
#         # Acknowledge successful processing of the message
#         consumer.acknowledge(msg)
#     except Exception:
#         # Message failed to be processed
#         consumer.negative_acknowledge(msg)

# client.close()