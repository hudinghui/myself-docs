
##钉钉告警：
[aries]
状态：告警发生中
当前时间: 2026-04-10 23:03:48
告警时间: 2026-04-10 23:03:18

监控对象: 10.0.0.107
对象别名: kafka-cluster-101

服务树: voghion.common.kafka-cluster-101

告警名称: kafka消费者节点数小于2
告警概要: 消费者kf-topic-marketing-api-email-low-priority-new的节点数小于2
故障描述：
消费者kf-topic-marketing-api-email-low-priority-new的节点数小于2，当前数：0

link http://f.aries.open-c3.marshotspot.com/#/ack/oDHi3LXSLTLpzcjKhgW5SVEk

[aries]
状态：告警发生中
当前时间: 2026-04-10 23:03:48
告警时间: 2026-04-10 23:03:18

监控对象: 10.0.0.107
对象别名: kafka-cluster-101

服务树: voghion.common.kafka-cluster-101

告警名称: kafka topic消费者节点数小于2
告警概要: 消费者 kf-topic-marketing-api-email-sc-low-priority-new 的节点数小于2
故障描述：
消费者 kf-topic-marketing-api-email-sc-low-priority-new 的节点数小于2，当前数：0
消费者 kfk-topic-marketing-api-push-low-priority 的节点数小于2，当前数：0
消费者 rmq-topic-marketing-api-push-high-priority 的节点数小于2，当前数：0
消费者 rmq-topic-marketing-api-sms-low-priority 的节点数小于2，当前数：0
消费者 rmq-topic-marketing-api-whatsapp-low-priority 的节点数小于2，当前数：0

link http://f.aries.open-c3.marshotspot.com/#/ack/nxbEjQt5ZR5aUVagHo58ej8n


##其中某个消费线程的关键日志：
2026-04-10 14:36:44.302 [] [kafka consumer thread kf-topic-marketing-api-email-sc-low-priority-new:kf-consumer-marketing-email-sc-low-property-0] INFO o.a.k.clients.FetchSessionHandler [handleError,442] [] - [Consumer instanceId=kf-consumer-marketing-email-sc-low-property-10.1.0.9-0, clientId=consumer-41, groupId=kf-consumer-marketing-email-sc-low-property] Error sending fetch request (sessionId=1810833176, epoch=20791) to node 1: org.apache.kafka.common.errors.DisconnectException. 2026-04-10 14:36:44.302 [] [kafka-coordinator-heartbeat-thread | kf-consumer-marketing-email-sc-low-property] INFO o.a.k.clients.FetchSessionHandler [handleError,442] [] - [Consumer instanceId=kf-consumer-marketing-email-sc-low-property-10.1.0.9-0, clientId=consumer-41, groupId=kf-consumer-marketing-email-sc-low-property] Error sending fetch request (sessionId=920626443, epoch=20888) to node 3: org.apache.kafka.common.errors.DisconnectException. 2026-04-10 14:36:59.291 [] [kafka-coordinator-heartbeat-thread | kf-consumer-marketing-email-sc-low-property] INFO o.a.k.c.c.i.AbstractCoordinator [markCoordinatorUnknown,780] [] - [Consumer instanceId=kf-consumer-marketing-email-sc-low-property-10.1.0.9-0, clientId=consumer-41, groupId=kf-consumer-marketing-email-sc-low-property] Group coordinator 10.0.0.108:9092 (id: 2147483645 rack: null) is unavailable or invalid, will attempt rediscovery 2026-04-10 14:37:15.822 [] [kafka-coordinator-heartbeat-thread | kf-consumer-marketing-email-sc-low-property] INFO o.a.k.c.c.i.AbstractCoordinator [onSuccess,728] [] - [Consumer instanceId=kf-consumer-marketing-email-sc-low-property-10.1.0.9-0, clientId=consumer-41, groupId=kf-consumer-marketing-email-sc-low-property] Discovered group coordinator 10.0.0.108:9092 (id: 2147483645 rack: null) 2026-04-10 14:51:29.286 [] [kafka-coordinator-heartbeat-thread | kf-consumer-marketing-email-sc-low-property] WARN o.a.k.c.c.i.AbstractCoordinator [run,1119] [] - [Consumer instanceId=kf-consumer-marketing-email-sc-low-property-10.1.0.9-0, clientId=consumer-41, groupId=kf-consumer-marketing-email-sc-low-property] This member will leave the group because consumer poll timeout has expired. This means the time between subsequent calls to poll() was longer than the configured max.poll.interval.ms, which typically implies that the poll loop is spending too much time processing messages. You can address this either by increasing max.poll.interval.ms or by reducing the maximum size of batches returned in poll() with max.poll.records. 2026-04-10 15:11:29.967 [] [main] INFO o.a.k.clients.consumer.KafkaConsumer [subscribe,964] [] - [Consumer instanceId=kf-consumer-marketing-email-sc-low-property-10.1.0.9-0, clientId=consumer-41, groupId=kf-consumer-marketing-email-sc-low-property] Subscribed to topic(s): kf-topic-marketing-api-email-sc-low-priority-new 2026-04-10 15:11:30.779 [] [kafka consumer thread kf-topic-marketing-api-email-sc-low-priority-new:kf-consumer-marketing-email-sc-low-property-0] INFO o.a.k.c.c.i.AbstractCoordinator [onSuccess,728] [] - [Consumer instanceId=kf-consumer-marketing-email-sc-low-property-10.1.0.9-0, clientId=consumer-41, groupId=kf-consumer-marketing-email-sc-low-property] Discovered group coordinator 10.0.0.108:9092 (id: 2147483645 rack: null) 2026-04-10 15:11:30.780 [] [kafka consumer thread kf-topic-marketing-api-email-sc-low-priority-new:kf-consumer-marketing-email-sc-low-property-0] INFO o.a.k.c.c.i.ConsumerCoordinator [onJoinPrepare,476] [] - [Consumer instanceId=kf-consumer-marketing-email-sc-low-property-10.1.0.9-0, clientId=consumer-41, groupId=kf-consumer-marketing-email-sc-low-property] Revoking previously assigned partitions [] 2026-04-10 15:11:30.780 [] [kafka consumer thread kf-topic-marketing-api-email-sc-low-priority-new:kf-consumer-marketing-email-sc-low-property-0] INFO o.a.k.c.c.i.AbstractCoordinator [sendJoinGroupRequest,505] [] - [Consumer instanceId=kf-consumer-marketing-email-sc-low-property-10.1.0.9-0, clientId=consumer-41, groupId=kf-consumer-marketing-email-sc-low-property] (Re-)joining group 2026-04-10 15:11:33.712 [] [kafka consumer thread kf-topic-marketing-api-email-sc-low-priority-new:kf-consumer-marketing-email-sc-low-property-0] INFO o.a.k.c.c.i.AbstractCoordinator [onSuccess,469] [] - [Consumer instanceId=kf-consumer-marketing-email-sc-low-property-10.1.0.9-0, clientId=consumer-41, groupId=kf-consumer-marketing-email-sc-low-property] Successfully joined group with generation 48 2026-04-10 15:11:33.712 [] [kafka consumer thread kf-topic-marketing-api-email-sc-low-priority-new:kf-consumer-marketing-email-sc-low-property-0] INFO o.a.k.c.c.i.ConsumerCoordinator [onJoinComplete,283] [] - [Consumer instanceId=kf-consumer-marketing-email-sc-low-property-10.1.0.9-0, clientId=consumer-41, groupId=kf-consumer-marketing-email-sc-low-property] Setting newly assigned partitions: kf-topic-marketing-api-email-sc-low-priority-new-17, kf-topic-marketing-api-email-sc-low-priority-new-16 2026-04-10 15:11:33.995 [] [kafka consumer thread kf-topic-marketing-api-email-sc-low-priority-new:kf-consumer-marketing-email-sc-low-property-0] INFO o.a.k.c.c.i.ConsumerCoordinator [refreshCommittedOffsetsIfNeeded,525] [] - [Consumer instanceId=kf-consumer-marketing-email-sc-low-property-10.1.0.9-0, clientId=consumer-41, groupId=kf-consumer-marketing-email-sc-low-property] Setting offset for partition kf-topic-marketing-api-email-sc-low-priority-new-17 to the committed offset FetchPosition{offset=928124, offsetEpoch=Optional[0], currentLeader=LeaderAndEpoch{leader=10.0.0.107:9092 (id: 1 rack: null), epoch=0}} 2026-04-10 15:11:33.996 [] [kafka consumer thread kf-topic-marketing-api-email-sc-low-priority-new:kf-consumer-marketing-email-sc-low-property-0] INFO o.a.k.c.c.i.ConsumerCoordinator [refreshCommittedOffsetsIfNeeded,525] [] - [Consumer instanceId=kf-consumer-marketing-email-sc-low-property-10.1.0.9-0, clientId=consumer-41, groupId=kf-consumer-marketing-email-sc-low-property] Setting offset for partition kf-topic-marketing-api-email-sc-low-priority-new-16 to the committed offset FetchPosition{offset=1027023, offsetEpoch=Optional[0], currentLeader=LeaderAndEpoch{leader=10.0.0.109:9092 (id: 3 rack: null), epoch=0}}





完整问题链路分析
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                           问题根因分析                                                   │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                         │
│  1. DisconnectException 发生后                                                          │
│     │                                                                                   │
│     ▼                                                                                   │
│  2. poll() 在网络恢复前可能阻塞或返回空结果                                              │
│     │                                                                                   │
│     ▼                                                                                   │
│  3. 14分钟后，心跳线程检测到 poll timeout，消费者离开消费组                              │
│     │                                                                                   │
│     ▼                                                                                   │
│  4. 🔴 关键问题：消费者离开组后，主线程的行为                                            │
│     │                                                                                   │
│     │  ┌─────────────────────────────────────────────────────────────────────────────┐  │
│     │  │  while (!shutdownFlag) {                                                    │  │
│     │  │      poll() → 返回空结果（因为已不在消费组，没有分配分区）                    │  │
│     │  │      doConsume(空结果) → 直接返回                                            │  │
│     │  │      commitSync() → 失败或阻塞                                              │  │
│     │  │      // 继续循环...                                                         │  │
│     │  │      // 🔴 永远不会主动重新加入消费组！                                      │  │
│     │  │  }                                                                           │  │
│     │  └─────────────────────────────────────────────────────────────────────────────┘  │
│     │                                                                                   │
│     ▼                                                                                   │
│  5. Kafka Consumer 客户端的限制：                                                        │
│     - 消费者主动离开组后，必须显式调用 unsubscribe() + subscribe() 才能重新加入          │
│     - 或者调用 KafkaConsumer#enforceRebalance() (Kafka 2.6+)                            │
│     - 或者关闭并重建 Consumer                                                            │
│     - 单纯的 poll() 循环不会自动重新加入                                                 │
│                                                                                         │
└─────────────────────────────────────────────────────────────────────────────────────────┘


🔴 根本原因：为什么被踢出后无法自动重连？
结合代码分析，问题出在 AbstractKafkaConsumer.run() 方法：
```
@Override
public void run() {
    while (!shutdownFlag) {
        try {
            ConsumerRecords<K, V> records = consumer.poll(pollTimeout);  // ← 问题点
            summaryOfMessagePollCount += records.count();
            doConsume(records);
        } catch (Exception e) {
            log.warn("kafka consume exception ", e);  // ← 异常被吞掉
        }
        if(!shutdownFlag){
            consumer.commitSync(commitSyncTimeout);  // ← 可能阻塞或失败
        }
    }
}
```

问题链路：

┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                           问题根因分析                                                   │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                         │
│  1. DisconnectException 发生后                                                          │
│     │                                                                                   │
│     ▼                                                                                   │
│  2. poll() 在网络恢复前可能阻塞或返回空结果                                              │
│     │                                                                                   │
│     ▼                                                                                   │
│  3. 14分钟后，心跳线程检测到 poll timeout，消费者离开消费组                              │
│     │                                                                                   │
│     ▼                                                                                   │
│  4. 🔴 关键问题：消费者离开组后，主线程的行为                                            │
│     │                                                                                   │
│     │  ┌─────────────────────────────────────────────────────────────────────────────┐  │
│     │  │  while (!shutdownFlag) {                                                    │  │
│     │  │      poll() → 返回空结果（因为已不在消费组，没有分配分区）                    │  │
│     │  │      doConsume(空结果) → 直接返回                                            │  │
│     │  │      commitSync() → 失败或阻塞                                              │  │
│     │  │      // 继续循环...                                                         │  │
│     │  │      // 🔴 永远不会主动重新加入消费组！                                      │  │
│     │  │  }                                                                           │  │
│     │  └─────────────────────────────────────────────────────────────────────────────┘  │
│     │                                                                                   │
│     ▼                                                                                   │
│  5. Kafka Consumer 客户端的限制：                                                        │
│     - 消费者主动离开组后，必须显式调用 unsubscribe() + subscribe() 才能重新加入          │
│     - 或者调用 KafkaConsumer#enforceRebalance() (Kafka 2.6+)                            │
│     - 或者关闭并重建 Consumer                                                            │
│     - 单纯的 poll() 循环不会自动重新加入                                                 │
│                                                                                         │
└─────────────────────────────────────────────────────────────────────────────────────────┘
