"""Conexão e publicação com RabbitMQ"""

import pika
import json

def publish_message(queue_name: str, message: dict):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    
    channel.queue_declare(queue=queue_name, durable=True)
    channel.basic_publish(
        exchange='',
        routing_key=queue_name,
        body=json.dumps(message),
        properties=pika.BasicProperties(delivery_mode=2)  # Tornando as mensagens persistentes
    )
    connection.close()
