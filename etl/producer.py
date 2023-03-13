import pulsar
 
client = pulsar.Client('pulsar://localhost:6650')
 
producer = client.create_producer(
   'persistent://public/default/my-topic',
   block_if_queue_full=True,
   batching_enabled=True,
   batching_max_publish_delay_ms=10)
 
for i in range(10):
    print(('Hello-%d' % i).encode('utf-8'))
    producer.send(('Hello-%d' % i).encode('utf-8'),
       properties=None)
 
client.close()