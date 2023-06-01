from confluent_kafka import Producer

# Konfigurasi producer
producer_config = {
    'bootstrap.servers': 'localhost:9092',  # Sesuaikan dengan host dan port Kafka Anda
    'client.id': 'my_producer'
}

# Membuat producer
producer = Producer(producer_config)

# Mengirim pesan ke topik 'my_topic'
topic = 'my_topic'
message = 'Hello, Kafka!'

producer.produce(topic, value=message)
producer.flush()

print('Pesan berhasil dikirim')
