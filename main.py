from entities.record import Record
from entities.address_book import AddressBook
from exceptions.not_found_error import NotFoundError
from exceptions.invalid_phone import InvalidPhone


def main():
    # Creating a new address book
    book = AddressBook()

    # Creating a record for John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Adding John record to the address book
    book.add_record(john_record)

    # Creating and adding a new record for Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Displaying all records in the book
    for record_id, record in book.data.items():
        print(f"ID: {record_id} - {record}")

    # Finding and editing John's phone number
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")
    print(f"\nAfter editing: {john}")

    # Searching for a specific phone number in John's record
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")

    # Deleting Jane's record
    book.delete("Jane")

    print("\nRunning test cases...")

    # Test that john exists
    assert john is not None, "John should exist"

    # Test that john has the correct phones after editing
    assert len(john.phones) == 2, "John should have 2 phones"
    assert john.find_phone("5555555555") is not None, "John should have phone 5555555555"
    assert john.find_phone("1112223333") is not None, "John should have phone 1112223333"

    # Jane should be deleted
    jane_deleted = False
    try:
        book.find("Jane")
    except NotFoundError:
        jane_deleted = True
    assert jane_deleted, "Jane should be deleted"

    # Test that non-existent contact raises NotFoundError
    contact_not_found = False
    try:
        book.find("Missing")
    except NotFoundError:
        contact_not_found = True
    assert contact_not_found, "Finding non-existent contact should raise NotFoundError"

    # Test that non-existent phone raises NotFoundError
    phone_not_found = False
    try:
        john.find_phone("9999999999")
    except NotFoundError:
        phone_not_found = True
    assert phone_not_found, "Finding non-existent phone should raise NotFoundError"

    # Try to create record and add invalid phone number
    invalid_phone_number = False
    try:
        test_record = Record("Test")
        test_record.add_phone("12345")
    except InvalidPhone:
        invalid_phone_number = True
    assert invalid_phone_number, "Adding invalid phone to record should raise InvalidPhone"

    print("All tests passed!")


if __name__ == "__main__":
    main()
