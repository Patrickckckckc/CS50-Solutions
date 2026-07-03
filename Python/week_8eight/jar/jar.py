class Jar:
    def __init__(self, cookies=0, capacity=12):
        if capacity < 0:
            raise ValueError("No Negative Cookies")
        self._capacity = capacity
        self._cookies = cookies

    def __str__(self):
        return f"{'🍪' * self.cookies}"

    def deposit(self, n):
        if n < 0:
            raise ValueError("Cannot deposit negative cookies")
        if self._cookies + n > self._capacity:
            raise ValueError("Too much cookies")
        self._cookies += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Cannot withdraw negative cookies")
        if self._cookies - n < 0:
            raise ValueError("Negative Cookies")
        self._cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def cookies(self):
        return self._cookies
