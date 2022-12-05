import sys
from pyspark import SparkConf, SparkContext
from pyspark.streaming  import StreamingContext
#from pyspark.streaming.kafka import KafkaUtils

#processing each micro batch
def process_events(event):
    return (event[0], Counter(event[1].split(" ")).most_common(3))

#push the processed event to Kafka
def push_back_to_kafka(processed_events):
    list_of_processed_events = processed_events.collect()
    producer.send('output_event', value = str(list_of_processed_events))

#create SC with the specified configuration
def spark_context_creator():
    conf = SparkConf()
    #The master URL to connect and set name for our app
    conf.setMaster("spark:34.70.113.82:7077").setAppName("ConnectingDotsSparkKafkaStreaming")
    sc = None
    try:
        sc.stop()
        sc = SparkContext(conf=conf)
    except:
        sc = SparkContext(conf=conf)
    return sc


if __name__ == "__main__":
    sc = spark_context_creator()
    ssc = StreamingContext(sc, 1)

    kafkaStream = KafkaUtils.createStream(ssc, 'localhost:2181', 'test-consumer-group', {'input_event':1})
    lines = kafkaStream.map(lambda x : process_events(x))

    producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=str.encode, key_serializer=str.encode)

    lines.foreachRDD(push_back_to_kafka)
