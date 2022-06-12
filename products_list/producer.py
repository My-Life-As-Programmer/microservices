import pika

params = pika.URLParameters('amqps://nemryoif:cTWU0YINrNQjvu4Ha94x7rLQm66_n4xO@armadillo.rmq.cloudamqp.com/nemryoif')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='admin', body='hello')
