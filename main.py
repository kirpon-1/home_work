from src.masks import get_mask_account, get_mask_card_number
from src.proccesing import filter_by_state, sort_by_date

if __name__ == "__main__":

    print(get_mask_card_number("7000792289606361"))
    # print(get_mask_card_number("700079228960636123"))
    # print(get_mask_card_number(""))
    print(get_mask_account("73654108430135874305"))
    # print(get_mask_account("736541084301358743056"))
    # print(get_mask_account(""))
    print(
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            ],
            "EXECUTED",  # можно оставить state потому что параметр по умолчанию
        )
    )

    print(
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            ]
        )
    )
