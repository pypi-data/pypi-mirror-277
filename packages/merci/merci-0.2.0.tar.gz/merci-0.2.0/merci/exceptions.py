class MerciException(Exception):
    pass


class InvalidDataset(MerciException):
    pass


class SensitiveAttributeException(MerciException):
    pass


class InvalidFairnessMeasure(MerciException):
    pass
