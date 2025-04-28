from dataclasses import dataclass


@dataclass
class PaymentSelectionData:
    used_bonuses: int
    payment_amount: int
    card_number: str
    expiration_date: str
    holder_name: str
