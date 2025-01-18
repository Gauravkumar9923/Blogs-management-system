class APIException(Exception):
    """
       Base class for API exceptions.
       Subclasses should provide `.status_code` and `.default_detail` properties.
       """

    # default - for unhandled exceptions - should ideally never happen, since
    # these will be mostly raised by devs themselves while handling requests.
    status_code = 500
    default_detail = "A server error occurred."

    def __init__(self, detail=None, errors=None, code=None, r_code=None):

        if detail is None:
            self.detail = self.default_detail
        else:
            self.detail = detail

        self.errors = errors

        if code is None:
            self.code = self.status_code
        else:
            self.code = code

        if r_code is None:
            self.r_code = self.code
        else:
            self.r_code = r_code

    def __str__(self):
        return self.detail


class BadRequestData(APIException):
    status_code = 400
    default_detail = "Bad Request Data."