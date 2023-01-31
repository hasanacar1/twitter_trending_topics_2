/*
 * (C) Copyright 2014,2016 Hewlett Packard Enterprise Development Company LP.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
 * implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.twitter_trending_topics;

import org.apache.storm.spout.SpoutOutputCollector;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Values;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.lang.Thread;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Map;
import java.util.concurrent.ThreadLocalRandom;

public class TwitterSampleSpout extends KafkaSpout {

  protected TwitterSampleSpout(KafkaSpoutConfig kafkaSpoutConfig) {
            super(kafkaSpoutConfig);
            //logger.info("Created");
            //TODO Auto-generated constructor stub
      }

@SuppressWarnings("unchecked")

  private static final Logger logger = LoggerFactory.getLogger(TwitterSampleSpout.class);

  //private static final long serialVersionUID = 744004533863562119L;

  //public TwitterSampleSpout() {
  //  logger.info("Created");
 // }

  @Override
  protected void processMessage(byte[] message, SpoutOutputCollector collector) {
    //logger.info("MESSAGE INFO : {}", message);
    String s = new String(message, StandardCharsets.UTF_8);
    //logger.info("MESSAGE INFO : {}", s);
    logger.info("method : processMessage");
    ArrayList arr = new ArrayList();
    arr.add(s);
    
    collector.emit(new Values(arr));
  }

  @Override
  public void declareOutputFields(OutputFieldsDeclarer declarer) {
    logger.info("method : declareOutputFields");
    declarer.declare(new Fields("tweet"));
  }
}
