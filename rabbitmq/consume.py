import pika
import random
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

channel.queue_declare(queue='task_queue', durable=True)

channel.queue_bind(queue='task_queue', exchange='logs')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

'''
 This uses the basic.qos protocol method to tell RabbitMQ not to give more than one message to a worker at a time.
'''

channel.basic_qos(prefetch_count=1)

'''
 remove auto_ack and send a proper acknowledgment from the worker, once we're done with a task.
'''

channel.basic_consume(queue="task_queue", 
                    on_message_callback = callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)