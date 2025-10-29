from collections import UserDict
from entities.record import Record
from exceptions.conflict_error import ConflictError
from exceptions.not_found_error import NotFoundError


class AddressBook(UserDict):
    record_counter: int = 0

    def add_record(self, record: Record) -> None:
        if any(str(existing) == str(record) for existing in self.data.values()):
            raise ConflictError("Record")
        AddressBook.record_counter += 1
        self.data[AddressBook.record_counter] = record

    def find(self, contact_name: str) -> Record:
        key = self._find_key(contact_name)
        return self.data[key]

    def delete(self, contact_name: str) -> None:
        key = self._find_key(contact_name)
        del self.data[key]

    def _find_key(self, contact_name: str) -> int:
        key = next((k for k, r in self.data.items() if r.name.value == contact_name), None)
        if not key:
            raise NotFoundError("Contact")
        return key

