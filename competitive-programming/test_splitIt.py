from spllitIt import get_expense

TEST_EXPENSE_JOURNAL = {
    "person_1":[20, 30, 50, 60],
    "person_2":[70, 30, 50],
    "person_3":[80, 80, 80, 80, 80]
}

def test_get_expense():
    # Get total expense
    assert get_expense(TEST_EXPENSE_JOURNAL) == 710
    # Get person_1 total expense
    assert get_expense(TEST_EXPENSE_JOURNAL, "person_1") == 160


