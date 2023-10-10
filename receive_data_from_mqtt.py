import pika

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    # Consume data from the previous queue
    channel.basic_consume(queue='task_1', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

def callback(ch, method, properties, body):
    print(f"Received {body}")

if __name__ == "__main__":
    main()
