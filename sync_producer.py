# -*- coding: utf-8 -*-
"""
simple producer

The example above would produce to kafka synchronously - 
the call only returns after we have confirmation that the message made it to the cluster.

"""
import pykafka

def main():
    client = pykafka.KafkaClient(hosts = '10.250.100.19:9092, \
                                        10.250.100.20:9092'
    )
    topic = client.topics['flume_test'] 
    '''producer = topic.get_sync_producer() 
    
    n = 0
    while True:
        producer.produce('simple producer %s' % n)
        n += 1
    '''
    with topic.get_sync_producer() as producer:
        for i in range(4):
            producer.produce('test message ' + str(i ** 2))
            
if __name__ == '__main__':
    main()
