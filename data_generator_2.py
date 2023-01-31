import socket
from confluent_kafka import Producer
from essential_generators import DocumentGenerator
import time

conf = {'bootstrap.servers' : 'localhost:9092',
'client.id' : socket.gethostname()}

producer = Producer(conf)


gen = DocumentGenerator()

def result(err, msg):
      if err is not None:
            print("Hatalı Gonderme : {}".format(str(err)))
      else:
            print("Sent successfully {}".format(str(msg)))

while True :
      #print(gen.sentence())
      producer.produce("raw_data", key = "tweet", value = gen.sentence(), callback=result)
      producer.poll(1)
      time.sleep(1)