import sys
import json

class BoardReader(object):
    ifiles = []
    def __init__(self, ifiles):
        self.ifiles = ifiles

    @staticmethod
    def from_fnames(fnames):
        ifiles = []
        for fname in fnames:
            ifiles.append(open(fname, 'r'))
        return BoardReader(ifiles)

    @staticmethod
    def from_fd(fd):
        return BoardReader([fd])

    def list_squares(self):
        boards = []
        for ifile in self.ifiles:
            squares = []
            for row in ifile.readlines():
                values = []
                for square_value in filter(lambda e: (e.strip()), map(lambda c: c.strip(), row.split(" "))):
                        values.append(self.smart_value(square_value))
                if values:
                    squares.append(values)

            if squares:
                boards.append(squares)
        return boards

    def smart_value(self, value):
        if value in ("X", "_", "None"):
            return None
        if value.isdigit():
            return int(value)

        raise Exception("Unknown value " + value)


if __name__ == "__main__":
    # print squares
    reader = None
    if len(sys.argv) == 1:
        reader = BoardReader.from_fd(sys.stdin)
    else:
        reader = BoardReader.from_fnames(sys.argv[1:])
    print json.dumps(reader.list_squares(), indent=4)
