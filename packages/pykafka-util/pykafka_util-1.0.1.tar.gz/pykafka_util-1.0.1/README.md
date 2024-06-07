<h1 align="center">pykafka_util</h1>

- pykafka_util.py

```python
from pykafka_util.pykafka_util import KafkaManager
kafka_host = f'127.0.0.1:9094'
topic = 'py_kafka'
consumer = 'test'
message = {
    "send_type": "sync_send",
    "name": "lady_killer",
    "age": 18
}

manager = KafkaManager(kafka_host)

v = bytes('{}'.format(json.dumps(message)), 'utf-8')

# 生产消息
manager.produce(topic=topic, value=v)

# 消费消息
    consumed_messages = manager.consume(topic=topic, group_id=consumer, num_messages=10)
    for data in consumed_messages:
        logging.info(f"消费数据：{data}")
```