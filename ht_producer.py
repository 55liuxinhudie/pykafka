# -*- coding: utf-8 -*-
"""
 higher throughput producer

  
  do() is similar to do1. 
"""

import pykafka
import traceback

def do1():
    client = pykafka.KafkaClient(hosts = '10.250.100.19:9092, \
                                        10.250.100.20:9092'
    )
    topic = client.topics['flume_test']
    producer = topic.get_producer() 
    i = 0
    while True:
	print i
	producer.produce('simple producer %s' % i)
	i += 1
    producer.stop()

def do2():
    client = pykafka.KafkaClient(hosts = '10.250.100.19:9092, \
                                        10.250.100.20:9092'
    )
    topic = client.topics['flume_test']
    with topic.get_producer() as producer: 
	i = 0
	while True:
	    print i
	    producer.produce('simple producer %s' % i)
	    i += 1
 
def main():
    do1()
    
if __name__ == '__main__':
    main()