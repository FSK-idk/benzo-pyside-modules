from xml.dom import minidom
import os
import csv
import json
import sqlite3

# for debug and testing

# csv_data = list()

# with open('Loyalty_Cards.csv', 'r') as csv_file:
#     csv_reader = csv.reader(filter(lambda l: l.strip(',\n'), csv_file))

#     for row in csv_reader:
#         csv_data.append(row)

#     with open('loyalty_card.json', 'w') as f:
#         print(f'{{ "LoyaltyCard": [', file=f)

#         for number, holder, balance in csv_data[1::]:
#             # print(number, holder, balance)
#             print(f'{{ "holder_name": "{holder}", "number": "{number}", "balance": {balance} }},', file=f)

#         print(f'] }}', file=f)


# import xml.etree.ElementTree as ET
# with open('deposit_card.json', 'w') as f:
#     print(f'{{ "DepositCard": [', file=f)

#     tree = ET.parse('Deposit_Cards.xml')
#     root = tree.getroot()

#     for child in root:
#         year = child[2].text[0:4]
#         month = child[2].text[5:7]
#         print(
#             f'{{ "issuer": "{child[0].text}", "number": "{child[1].text.replace(' ', '')}" , "expiration_date": "{year + '-' + month + '-01'}", "holder_name": "{child[4].text}", "balance": {child[3].text + '00'} }},', file=f)

#     tree = ET.parse('Credit_Cards.xml')
#     root = tree.getroot()

#     for child in root:
#         year = child[2].text[0:4]
#         month = child[2].text[5:7]
#         print(
#             f'{{ "issuer": "{child[0].text}", "number": "{child[1].text.replace(' ', '')}" , "expiration_date": "{year + '-' + month + '-01'}", "holder_name": "{child[4].text}", "balance": {child[3].text + '00'} }},', file=f)

#     print(f'] }}', file=f)


# with open('qwe.json') as qwe_file:

#     json_dict = json.load(qwe_file)

#     logs = json_dict['PaymentLog']

#     with open('payment_log.json', 'w') as f:
#         print(f'{{ "PaymentLog": [', file=f)

#         for log in logs:
#             print(
#                 f'{{ "deposit_card_number": "{log['CardNumber'].replace(' ', '')}", "payment_amount": "{int(log['Price'] * 100)}", "organization_name": "BENZO", "payment_key": "{log['Key']}" }},', file=f)

#         print(f'] }}', file=f)
