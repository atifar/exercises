from stack import LinkedList, Node
import pytest


def test_insert():
    linked_list = LinkedList()
    linked_list.insert(48)
    assert linked_list.head.get_value() == 48
    assert linked_list.head.get_next() is None


def test_insert_two_elements():
    linked_list = LinkedList()
    linked_list.insert("beton")
    linked_list.insert(431)
    assert linked_list.head.get_value() == 431
    next_head = linked_list.head.get_next()
    assert next_head.get_value() == "beton"
    assert next_head.get_next() is None


def test_size_one_element():
    linked_list = LinkedList()
    linked_list.insert(431)
    assert linked_list.size() == 1


def test_size_three_elements():
    linked_list = LinkedList()
    # Insert three elements
    for _ in range(3):
        linked_list.insert(431)
    assert linked_list.size() == 3


def test_delete_one_from_nonempty_list():
    linked_list = LinkedList()
    linked_list.insert(431)
    linked_list.insert("bacci")
    linked_list.insert(7.05)
    assert linked_list.head.get_value() == 7.05
    linked_list.delete_last()
    assert linked_list.head.get_value() == "bacci"
    # linked_list.delete_last()
    # assert linked_list.head.get_value() == 431


def test_delete_all_from_nonempty_list():
    linked_list = LinkedList()
    linked_list.insert(431)
    linked_list.insert("bacci")
    linked_list.insert(7.05)
    assert linked_list.head.get_value() == 7.05
    linked_list.delete_last()
    assert linked_list.head.get_value() == "bacci"
    linked_list.delete_last()
    assert linked_list.head.get_value() == 431
    linked_list.delete_last()
    with pytest.raises(AttributeError):
        linked_list.head.get_value()


if __name__ == '__main__':
    pytest.main()
