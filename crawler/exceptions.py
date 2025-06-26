from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementNotInteractableException,
    StaleElementReferenceException,
    WebDriverException,
    NoSuchWindowException
)


class CrawlerException(Exception):
    """Base exception class for crawler."""
    def __init__(self, message=None):
        super().__init__(message)
        self.message = message


EXCEPTION_TYPES = (
    TimeoutException,
    NoSuchElementException,
    ElementNotInteractableException,
    StaleElementReferenceException,
    WebDriverException,
    NoSuchWindowException,
    ConnectionRefusedError,
    CrawlerException,
)


class OutOfQuotaException(CrawlerException):
    """Raised when the user's quota is exceeded."""
    def __init__(self, message="Out of Quota"):
        super().__init__(message)