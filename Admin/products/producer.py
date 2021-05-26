import pika
from pika import channel

params = pika.URLParameters('amqps://oljdtgfk:JpYNFVbl7X8IF8o9heuD6XK_ZNvu5cAJ@beaver.rmq.cloudamqp.com/oljdtgfk')

connection  = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='admin', body='hello')