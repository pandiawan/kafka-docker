from confluent_kafka import Consumer

# Konfigurasi consumer
consumer_config = {
    'bootstrap.servers': 'localhost:9092',  # Sesuaikan dengan host dan port Kafka Anda
    'group.id': 'my_consumer',
    'auto.offset.reset': 'earliest'
}

# Membuat consumer
consumer = Consumer(consumer_config)

# Subscribe ke topik 'my_topic'
topic = 'my_topic'
consumer.subscribe([topic])

# Menerima dan menampilkan pesan
while True:
    message = consumer.poll(1.0)

    if message is None:
        continue
    if message.error():
        print(f"Error: {message.error()}")
        continue

    print(f'Menerima pesan: {message.value().decode("utf-8")}')

consumer.close()
