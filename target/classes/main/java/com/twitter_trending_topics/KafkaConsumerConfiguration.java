/*
 * Copyright (c) 2014 Hewlett-Packard Development Company, L.P.
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

import java.io.Serializable;


public class KafkaConsumerConfiguration {

    //private static final long serialVersionUID = -1666706655354785832L;
    String topic =  "test4";
    Integer numThreads = 1;
    String groupId = "data_consumer_3";
    String zookeeperConnect= "10.8.128.121:2181";
    String consumerId= "1";
    Integer socketTimeoutMs= 30000;
    Integer socketReceiveBufferBytes = 65536;
    Integer fetchMessageMaxBytes = 1048576;
    Boolean autoCommitEnable = true;
    Integer autoCommitIntervalMs = 60000;
    Integer queuedMaxMessageChunks = 10;
    Integer rebalanceMaxRetries = 4;
    Integer fetchMinBytes = 1;
    Integer fetchWaitMaxMs = 100;
    Integer rebalanceBackoffMs =2000;
    Integer refreshLeaderBackoffMs = 200;
    String autoOffsetReset = "largest";
    Integer consumerTimeoutMs = -1;
    String clientId = "1";
    Integer zookeeperSessionTimeoutMs = 6000;
    Integer zookeeperConnectionTimeoutMs = 6000;
    Integer zookeeperSyncTimeMs = 2000;

    public String getTopic() {
        return topic;
    }

    public Integer getNumThreads() {
        return numThreads;
    }

    public String getGroupId() {
        return groupId;
    }

    public String getZookeeperConnect() {
        return zookeeperConnect;
    }

    public String getConsumerId() {
        return consumerId;
    }

    public Integer getSocketTimeoutMs() {
        return socketTimeoutMs;
    }

    public Integer getSocketReceiveBufferBytes() {
        return socketReceiveBufferBytes;
    }

    public Integer getFetchMessageMaxBytes() {
        return fetchMessageMaxBytes;
    }

    public Boolean getAutoCommitEnable() {
        return autoCommitEnable;
    }

    public Integer getAutoCommitIntervalMs() {
        return autoCommitIntervalMs;
    }

    public Integer getQueuedMaxMessageChunks() {
        return queuedMaxMessageChunks;
    }

    public Integer getRebalanceMaxRetries() {
        return rebalanceMaxRetries;
    }

    public Integer getFetchMinBytes() {
        return fetchMinBytes;
    }

    public Integer getFetchWaitMaxMs() {
        return fetchWaitMaxMs;
    }

    public Integer getRebalanceBackoffMs() {
        return rebalanceBackoffMs;
    }

    public Integer getRefreshLeaderBackoffMs() {
        return refreshLeaderBackoffMs;
    }

    public String getAutoOffsetReset() {
        return autoOffsetReset;
    }

    public Integer getConsumerTimeoutMs() {
        return consumerTimeoutMs;
    }

    public String getClientId() {
        return clientId;
    }

    public Integer getZookeeperSessionTimeoutMs() {
        return zookeeperSessionTimeoutMs;
    }

    public Integer getZookeeperConnectionTimeoutMs() {
        return zookeeperConnectionTimeoutMs;
    }

    public Integer getZookeeperSyncTimeMs() {
        return zookeeperSyncTimeMs;
    }

}
