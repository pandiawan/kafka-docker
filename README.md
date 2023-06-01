
# Kafka Server using Docker Compose  
  
This repository provides a simple setup to run Apache Kafka server using Docker Compose.  
  
## Prerequisites  
  
- Docker: Ensure that Docker is installed on your system. You can download and install Docker from the official Docker website: [https://www.docker.com](https://www.docker.com)  
  
## Getting Started  
  
1. Clone this repository to your local machine:  
    ```shell  
    git clone https://github.com/pandiawan/kafka-docker.git
    ```  
2. Navigate to the cloned repository:
    ```shell  
    cd kafka-docker
    ```  
    Start Kafka server using Docker Compose:  
    ```shell  
    docker-compose up -d
    ```  
   This command will download the necessary Docker images and start the Kafka server in the background. The Kafka server will be accessible at `localhost:9092`.  

3. Running the Kafka Producer and Consumer using Python  
To run the Kafka producer and consumer using Python, make sure you have Python and the `confluent-kafka` library installed. You can install the library using `pip`:  
    ```shell  
    pip install confluent-kafka
   ```
   **Run the Kafka producer:**
   ```shell
   python example/kafka_producer.py
   ```
   This will start the Kafka producer and send messages to the specified topic.
   
   **Run the Kafka consumer:**
   ```shell
   python example/kafka_consumer.py
   ```
   This will start the Kafka consumer and receive messages from the specified topic.
   
   Press `Ctrl+C` to stop the producer and consumer when you're done.

4. Clean up:
To stop and remove the Docker containers, run the following command:
    ```shell
    docker-compose down
   ```

## Configuration
The `docker-compose.yml` file provides default configuration for running the Kafka server. You can modify the following parameters as per your requirements:
-  `KAFKA_BROKER_ID`: The unique identifier for the Kafka broker. Each broker in the cluster should have a unique ID. 
-  `KAFKA_ZOOKEEPER_CONNECT`: The connection string for the ZooKeeper server. Modify this if you are running ZooKeeper on a different hostname or port.
-  `KAFKA_LISTENER_SECURITY_PROTOCOL_MAP`: The listener security protocol mapping configuration. Modify this if you want to enable encryption and authentication for Kafka listeners. 
- `KAFKA_ADVERTISED_LISTENERS`: The advertised listeners configuration for Kafka. Modify this if you want to expose Kafka on a different hostname or port. 
- `KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR`: The replication factor for the internal Kafka offsets topic. Modify this if you want to adjust the replication factor.
- `KAFKA_TRANSACTION_STATE_LOG_MIN_ISR`: The minimum in-sync replicas (ISR) for the transaction state log topic. Modify this if you want to set a specific minimum ISR value.
- `KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR`: The replication factor for the transaction state log topic. Modify this if you want to adjust the replication factor.

## Contributing
Contributions are welcome! If you find any issues or want to add new features, please open an issue or submit a pull request.