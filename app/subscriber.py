from event import Event
import unittest


class Subscriber:
    def is_subscribe(self, event: Event) -> bool:
        subs = self.subscribed()
        if not subs:
            return False
        if not type(subs) is list:
            subs = [subs]
        for sub in subs:
            if isinstance(event, sub):
                return True
        return False

    def subscribe(self, event: Event) -> None:
        pass

    def subscribed(self):
        pass


class TestSubscriber(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.subscriberA = self.SubscriberA()
        self.subscriberB = self.SubscriberB()
        self.subscriberX = self.SubscriberX()

    class EventA(Event):
        pass

    class EventB(Event):
        pass

    class EventC(Event):
        pass

    class SubscriberA(Subscriber):
        def subscribed(self):
            return [TestSubscriber.EventA]

    class SubscriberB(Subscriber):
        def subscribed(self):
            return [TestSubscriber.EventB, TestSubscriber.EventC]

    class SubscriberX(Subscriber):
        def subscribed(self):
            return Event

    def test_購読対象を判別できる(self):
        a = self.EventA()
        b = self.EventB()
        c = self.EventC()
        self.assertTrue(self.subscriberA.is_subscribe(a))
        self.assertFalse(self.subscriberA.is_subscribe(b))
        self.assertFalse(self.subscriberA.is_subscribe(c))
        self.assertFalse(self.subscriberB.is_subscribe(a))
        self.assertTrue(self.subscriberB.is_subscribe(b))
        self.assertTrue(self.subscriberB.is_subscribe(c))
        self.assertTrue(self.subscriberX.is_subscribe(a))
        self.assertTrue(self.subscriberX.is_subscribe(b))
        self.assertTrue(self.subscriberX.is_subscribe(c))


if __name__ == '__main__':
    unittest.main()
