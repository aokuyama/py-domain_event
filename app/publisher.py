from event import Event
from subscriber import Subscriber
import unittest


class Publisher:
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.subscribers = []

    def register(self, subscriber: Subscriber) -> None:
        for s in self.subscribers:
            if s == subscriber:
                raise RuntimeError
        self.subscribers.append(subscriber)

    def publish(self, event: Event) -> None:
        for s in self.subscribers:
            s: Subscriber
            if s.is_subscribe(event):
                s.subscribe(event)


class TestSubscriber(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.publisher = Publisher()
        self.subscriberA = self.SubscriberA()
        self.subscriberB = self.SubscriberB()

    class EventA(Event):
        pass

    class EventB(Event):
        pass

    class EventC(Event):
        pass

    class SubscriberA(Subscriber):
        def __init__(self) -> None:
            self.read = []

        def subscribed(self):
            return [TestSubscriber.EventA]

        def subscribe(self, e):
            self.read.append(e)

    class SubscriberB(Subscriber):
        def __init__(self) -> None:
            self.read = []

        def subscribed(self):
            return [TestSubscriber.EventB, TestSubscriber.EventC]

        def subscribe(self, e):
            self.read.append(e)

    def test_購読対象のみを購読できる(self):
        a = self.EventA()
        b = self.EventB()
        c = self.EventC()
        self.publisher.register(self.subscriberA)
        self.publisher.register(self.subscriberB)
        self.publisher.publish(a)
        self.assertEqual(1, len(self.subscriberA.read))
        self.assertEqual(0, len(self.subscriberB.read))
        self.publisher.publish(b)
        self.assertEqual(1, len(self.subscriberA.read))
        self.assertEqual(1, len(self.subscriberB.read))
        self.publisher.publish(c)
        self.assertEqual(1, len(self.subscriberA.read))
        self.assertEqual(2, len(self.subscriberB.read))

    def test_多重登録できない(self):
        self.publisher.register(self.subscriberA)
        with self.assertRaises(RuntimeError):
            self.publisher.register(self.subscriberA)
        other_a = self.SubscriberA()
        self.publisher.register(other_a)


if __name__ == '__main__':
    unittest.main()
