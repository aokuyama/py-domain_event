import unittest


class Event:
    def name(self) -> str:
        return self.__class__.__name__

    def body(self) -> str:
        return ""

    def overview(self) -> str:
        return self.name() + " :\n" + self.body()


class TestEvent(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.event = Event()

    class EventA(Event):
        def body(self):
            return 'event a'

    def test_名前や概要が自動で取得できる(self):
        self.assertEqual('Event', self.event.name())
        a = self.EventA()
        self.assertEqual('EventA', a.name())
        self.assertEqual("Event :\n", self.event.overview())
        self.assertEqual("EventA :\nevent a", a.overview())


if __name__ == '__main__':
    unittest.main()
