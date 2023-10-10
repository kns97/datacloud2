import pika

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    # Publish sample data to a queue
    channel.basic_publish(exchange='', routing_key='task_1', body='Sample data')
    connection.close()

if __name__ == "__main__":
    main()
