class PubSub:
    def __init__(self):
        self.topics = {}

    def subscribe(self, topic, subscriber):
        if topic not in self.topics:
            self.topics[topic] = []
        self.topics[topic].append(subscriber)

    def publish(self, topic, message):
        for subscriber in self.topics.get(topic, []):
            subscriber.notify(message)

class Subscriber:
    def __init__(self, name):
        self.name = name

    def notify(self, message):
        print(f"[Subscriber: {self.name}] Message: {message}")

# Example usage
if __name__ == '__main__':
    ps = PubSub()
    s1 = Subscriber("Alice")
    ps.subscribe("news", s1)
    ps.publish("news", "Today’s update!")
