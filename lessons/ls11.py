def chars(msg: str) -> str:
    index: int = 0
    copy: str = msg
    while index <= len(msg):
        print(msg[index])
        index += 1
    return copy


a: str = "Hey"
b: str = "Hi"
chars(msg=a)
