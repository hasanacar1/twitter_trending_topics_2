from socket import timeout
from confluent_kafka import Consumer
import json
from influx import InfluxClient

running = True

conf = {'bootstrap.servers' : 'localhost:9092',
            'group.id' : 'group_1'}

consumer1 = Consumer(conf)

def basic_loop(consumer, topics):
      try:
            consumer.subscribe(topics)

            while running :
                  msg = consumer.poll(timeout=0.1)
                  if msg is None :
                        continue
                  if msg.error():
                        print("Hatalı Gonderme : {}".format(str(msg.error)))
                  else:
                        #print("Sent successfully {}".format(str(msg.value().decode('utf-8'))))
                        test_str = str(msg.value().decode('utf-8'))
                        #print(test_str.split())
                        test_str = test_str.replace('[', '')
                        test_str = test_str.replace(']', ',')
                        test_str = test_str.replace('\'', '"')
                        test_list = test_str.split()
                        item_list = []
                        for item in test_list:
                              item = item[:-1]
                              print(item)
                              item_dict = dict(json.loads(item))
                              item_list.append(item_dict)
                        
                        conn = InfluxClient()
                        conn.append_point(item_list)

                        # for item_2 in item_list:
                        #       conn = InfluxClient()
                        #       conn.append_point(item_list)
                        #       print(item_2['word'])
                        #       print(item_2['wordcount'])

                        #print(type(res))
                        a = ['Tests run: 1', ' Failures: 0', ' Errors: 0']

      finally:
            consumer.close()


basic_loop(consumer=consumer1, topics=["processed_data"])
