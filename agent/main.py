import docker
import pika, sys, os
import logging
import json
import base64


logging.basicConfig(format='%(asctime)s %(message)s',level=logging.INFO)

#read file conf/function_jsondata_conf.json
dt_conf_file = 'conf/function_jsondata_conf.json'
try:
    with open(dt_conf_file,"r") as conf_file:
        dt_config =json.load(conf_file)
        #print(dt_config)
    
except:
    logging.error(f'Problem when handling the input file {dt_conf_file}')
    exit(0)



# func_config=dt_config["function_name"]
# print(func_config)

json_string = json.dumps(dt_config)
data_bytes = json_string.encode('ascii')

base64_bytes = base64.b64encode(data_bytes)
base64_string = base64_bytes.decode('ascii')

print("Encoded Data: ", base64_string)

# func_config=dt_config["function_name"]
# print(func_config)
# ops =func_config["ops"]
# print(ops)
client = docker.from_env()
container = client.containers.run(image="etl:latest", command="python3 main.py "+ base64_string, detach=True)
# containers = client.containers.list(all=True)

# print(containers)

# docker_image =msg["docker"]["image"]
# docker_command=msg["docker"]["command"]

# def main():
#     connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
#     channel = connection.channel()

#     channel.queue_declare(queue='hello')

#     def callback(ch, method, properties, body):
#         print(" [x] Received %r" % body.decode())

#     channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

#     print(' [*] Waiting for messages. To exit press CTRL+C')
#     channel.start_consuming()

# if __name__ == '__main__':
#     try:
#         main()
#     except KeyboardInterrupt:
#         print('Interrupted')
#         try:
#             sys.exit(0)
#         except SystemExit:
#             os._exit(0)