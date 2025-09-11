def get_mask_card_number(card_number: str) -> str:
    """Функция проверяет размер номера банковской карты на корректность
    и затем маскирует ее в формате XXXX XX** **** XXXX"""
    if card_number is None:
        raise ValueError("введите номер карты")
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("номер карты должен быть из 16 цифр")
    masks_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return masks_number


def get_mask_account(card_account: str) -> str:
    """Функция проверяет размер счкта на корректность
    и затем маскирует ее в формате XXXX XX** **** XXXX"""
    if card_account is None:
        raise ValueError("введите номер карты")
    if len(card_account) != 20 or not card_account.isdigit():
        raise ValueError("номер счета должен быть из 20 цифр")
    masks_account = f"**{card_account[-4:]}"
    return masks_account


# card_number = 7000792289606361
#
# def get_mask_card_number(card_number: int) -> str:
#     """принимает номер карты"""
#     card_number_str = str(card_number)
#     form_str_1 = card_number_str[:6]
#     form_str_2 = "******"
#     form_str_3 = card_number_str[:12]
#     total_form_str = form_str_1 + form_str_2 + form_str_3
#     new_str = [total_form_str[i:i+4] for i in range(0, len(total_form_str), 4)]
#     return "".join(new_str)
#
# print(get_mask_card_number(card_number))
#
# def get_mask_account(card_number):
#     """принимает номер карты"""
#     pass
