def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """фильтрует список словарей по наличию Executed в state"""
    filtered_transactions = []

    for transaction in transactions:
        if transaction.get("state") == state:
            filtered_transactions.append(transaction)
    return filtered_transactions


def sort_by_date(transactions: list[dict], is_reverse: bool = True) -> list[dict]:
    """сортирует по дате"""
    sorted_transactions = sorted(transactions, key=lambda x: x["date"])
    return sorted_transactions
