from typing import Protocol


class MessageWriter(Protocol):
    def write(self, message: str) -> None:
        ...


class ConsoleMessageWriter(MessageWriter):
    def write(self, message: str) -> None:
        print(message)


class Salutation:
    _writer: MessageWriter

    def __init__(self, writer: MessageWriter):
        if writer is None:
            raise ValueError('Writer can\'t be None')

        self._writer = writer

    def exclaim(self):
        self._writer.write('Hello DI!')


def main():
    writer = ConsoleMessageWriter()
    salutation = Salutation(writer)
    salutation.exclaim()


if __name__ == '__main__':
    main()
