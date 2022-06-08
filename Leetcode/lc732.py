from sortedcontainers import SortedDict

class MyCalendarThree:
    def __init__(self):
        self.d = SortedDict()

    def book(self, start: int, end: int) -> int:
        print(self.d)
        self.d[start] = self.d.setdefault(start, 0) + 1
        self.d[end] = self.d.setdefault(end, 0) - 1
        print(self.d)

        ans = maxBook = 0
        for freq in self.d.values():
            maxBook += freq
            ans = max(ans, maxBook)
        print(ans)

if __name__ == '__main__':
    run = MyCalendarThree()
    print(11)
    run.book(10, 40)

# couldnt understand how the input works@220606
