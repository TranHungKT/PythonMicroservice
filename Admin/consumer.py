import pika
from pika import channel

params = pika.URLParameters('amqps://oljdtgfk:JpYNFVbl7X8IF8o9heuD6XK_ZNvu5cAJ@beaver.rmq.cloudamqp.com/oljdtgfk')
print(params)
connection  = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch,method,properties,body):
    print('Received in admin')
    print(body)

channel.basic_consume(queue='admin',on_message_callback=callback)
 
print('Started')

channel.start_consuming()

channel.close()