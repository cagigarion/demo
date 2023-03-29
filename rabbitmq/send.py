import pika
import random
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

'''
 before sending we need to make sure the recipient queue exists
 . If we send a message to non-existing location, RabbitMQ will just drop the message

we need to make sure that the queue will survive a RabbitMQ node restart. In order to do so, we need to declare it as durable:

'''
channel.queue_declare(queue='task_queue', durable=True)


'''
 All we need to know now is how to use a default exchange identified by an empty string
This exchange is special ‒ it allows us to specify exactly to which queue the message should go
The queue name needs to be specified in the routing_key parameter

'''

rd = random.random()

message = ' '.join(sys.argv[1:]) or "Hello World!"
print('messaeg', message)



channel.basic_publish(exchange='logs', 
                    routing_key='task_queue', 
                    body= message,
                    properties= pika.BasicProperties(delivery_mode= pika.spec.PERSISTENT_DELIVERY_MODE))

print(f" [x] Sent 'Hello World! {message}'")

connection.close()
