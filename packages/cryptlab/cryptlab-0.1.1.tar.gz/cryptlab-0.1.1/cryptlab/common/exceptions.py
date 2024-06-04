class ServerClosedConnection(Exception):
    pass


class InvalidMessageError(Exception):
    pass


class InvalidRecipientError(Exception):
    pass


class PKIEntryAlreadySet(Exception):
    pass
