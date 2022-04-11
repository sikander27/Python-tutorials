#!/usr/bin/python3


from ast import Pass


def main():    
    expenses_journal = {}
    no_of_people = int(input("Enter no. of people: "))
    for person in range(no_of_people):
        name = "person_{}".format(person +1)
        print("Enter expense for {}".format(name))
        expense = list(map(int, input().split()))
        expenses_journal[name] = expense

    print(expenses_journal)
    print_statement(expenses_journal)
    print("Total expense: {}".format(get_expense()))

def split_it():
    pass
    

def print_statement(expenses_journal):
    print("Name | Amount_spend")
    for person in expenses_journal.keys():
        print("{} | {}".format(person, get_expense(person)))

def get_expense(expenses_journal, name=None):
    if name:
        expense_list = expenses_journal[name]
        return sum(expense_list)
    else:
        total_expense = []
        total_expense_list = expenses_journal.values()
        for expense_list in total_expense_list:
            total_expense.append(sum(expense_list))
        return sum(total_expense)


if __name__ == '__main__':
    main()