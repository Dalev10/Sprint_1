#@Author: Diego Alejandro Vergara Ruiz
class Email():

    _address: str
    _category: str
    _valid: bool

    def __init__(self, address: str = "", category: str = "Unknown", valid: bool = False) -> None:
        self._address = address
        self._category = category
        self._valid = valid

    def get_address(self) -> str:
        return self._address

    def get_category(self) -> str:
        return self._category

    def get_valid(self) -> bool:
        return self._valid

    def set_address(self, address: str) -> None:
        self._address = address

    def set_category(self, category: str) -> None:
        self._category = category

    def set_valid(self, valid: bool) -> None:
        self._valid = valid

    def __str__(self) -> str:
        status = "Valid" if self._valid else "Invalid"
        return f"Email: {self._address}, Category: {self._category}, Status: {status}"