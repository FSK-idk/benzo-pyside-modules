from enum import Enum


class DepositCardTableColumn(Enum):
    ID = 'id'
    ISSUER = 'issuer'
    NUMBER = 'number'
    EXPIRATION_DATE = 'expiration_date'
    HOLDER_NAME = 'holder_name'
    BALANCE = 'balance'
