from copy import deepcopy
from expense_tracker import calculate_category_totals

def test_empty_expenses():
    sample_expenses = []
    expected = {}

    actual = calculate_category_totals(sample_expenses)
    assert actual == expected

def test_different_categories():
    sample_expenses = [
            {
                "expense_desc": "break fast",
                "expense_amt": 10.0,
                "expense_category": "food"
            },
            {
                "expense_desc": "bus",
                "expense_amt": 5.0,
                "expense_category": "transport"
            }
        ]
    expected = {"food":10, "transport":5}
    
    actual = calculate_category_totals(sample_expenses)
    assert actual == expected

def test_repeated_categories():
    sample_expenses = [
            {
                "expense_desc": "break fast",
                "expense_amt": 10.0,
                "expense_category": "food"
            },
            {
                "expense_desc": "bus",
                "expense_amt": 5.0,
                "expense_category": "transport"
            },
            {
                "expense_desc": "lunch",
                "expense_amt": 10.0,
                "expense_category": "food"
            },
            {
                "expense_desc": "return bus",
                "expense_amt": 5.0,
                "expense_category": "transport"
            }
        ]
    expected = {"food":20.0, "transport":10.0}
    
    actual = calculate_category_totals(sample_expenses)
    assert actual == expected

def test_summary_does_not_modify_expenses():
    sample_expenses = [
                {
                    "expense_desc": "break fast",
                    "expense_amt": 10.0,
                    "expense_category": "food"
                },
                {
                    "expense_desc": "bus",
                    "expense_amt": 5.0,
                    "expense_category": "transport"
                },
                {
                    "expense_desc": "lunch",
                    "expense_amt": 10.0,
                    "expense_category": "food"
                },
                {
                    "expense_desc": "return bus",
                    "expense_amt": 5.0,
                    "expense_category": "transport"
                }
            ]

    copy_expenses = deepcopy(sample_expenses)
    calculate_category_totals(sample_expenses)
    assert sample_expenses == copy_expenses

if __name__ == "__main__":
    test_empty_expenses()
    test_different_categories()
    test_repeated_categories() 
    test_summary_does_not_modify_expenses() 
    print("All the tests are passed")