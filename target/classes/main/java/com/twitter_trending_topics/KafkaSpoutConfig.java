package com.twitter_trending_topics;


import java.io.Serializable;

public class KafkaSpoutConfig {

  //private static final long serialVersionUID = -6477042435089264571L;

  public Integer maxWaitTime = 100;

  public KafkaConsumerConfiguration kafkaConsumerConfiguration;
}
