class WebNode:

    def __init__(self, url: str, prev: ListNode, next: ListNode):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = WebNode(homepage, None, None)
        self.curr = self.head

    def visit(self, url: str) -> None:
        self.curr.next = WebNode(url, self.curr, None)
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        steps_left = steps
        while self.curr.prev and steps_left > 0:
            self.curr = self.curr.prev
            steps_left -= 1
        return self.curr.url

    def forward(self, steps: int) -> str:
        steps_left = steps
        while self.curr.next and steps_left > 0:
            self.curr = self.curr.next
            steps_left -= 1
        return self.curr.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)