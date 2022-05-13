from typing import Any, List


class Stack:

    # variable declarions
    _list: List[Any]


    # methods
    def __init__(self) -> None:
        self._list = []

    def push(self, item: Any):
        self._list.append(item)
    
    def pop(self) -> Any:
        return self._list.pop()

    def __getitem__(self, offset: int) -> Any:
        return self._list[offset]

    def __len__(self) -> int:
        return len(self._list)


# ad-hoc testing
if __name__== '__main__':
    stack = Stack()

    for i in range(10):
        stack.push(i)
        print(f'pushed: {i}')

    for i in range(10):
        print(f'access: {stack[i]}')

    for i in range(len(stack)):
        print(f'popped: {stack.pop()}')
    
    print(f'items left: {len(stack)}')
