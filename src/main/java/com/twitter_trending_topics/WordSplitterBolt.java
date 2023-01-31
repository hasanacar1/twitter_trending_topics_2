package com.twitter_trending_topics;

import org.apache.storm.task.OutputCollector;
import org.apache.storm.task.TopologyContext;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseRichBolt;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Tuple;
import org.apache.storm.tuple.Values;

import java.util.ArrayList;
import java.util.Map;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * Receives tweets and emits its words over a certain length.
 */
public class WordSplitterBolt extends BaseRichBolt {

    private static final Logger logger = LoggerFactory.getLogger(WordSplitterBolt.class);

    private static final long serialVersionUID = 5151173513759399636L;

    private final int minWordLength;

    private OutputCollector collector;

    public WordSplitterBolt(int minWordLength) {
        this.minWordLength = minWordLength;
    }

    @Override
    public void prepare(Map map, TopologyContext topologyContext, OutputCollector collector) {
        this.collector = collector;
    }

    @Override
    public void execute(Tuple input) {
        //logger.info("SPLITTER BOLT INPUT {}", input);
        ArrayList<String> tweets = (ArrayList<String>) input.getValueByField("tweet");

        for (String tweet : tweets){
            String text = tweet.replaceAll("\\p{Punct}", " ").replaceAll("\\r|\\n", "").toLowerCase();
            String[] words = text.split(" ");
            for (String word : words) {
                if (word.length() >= minWordLength) {
                    collector.emit(new Values(word));
                }
            }
        }
    }

    @Override
    public void declareOutputFields(OutputFieldsDeclarer declarer) {
        declarer.declare(new Fields("word"));
    }
}
