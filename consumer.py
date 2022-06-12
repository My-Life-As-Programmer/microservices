import pika

params = pika.URLParameters('amqps://nemryoif:cTWU0YINrNQjvu4Ha94x7rLQm66_n4xO@armadillo.rmq.cloudamqp.com/nemryoif')

connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)


channel.basic_consume(queue='admin', on_message_callback=callback)

print('Started Consuming')
channel.start_consuming()

channel.close()
