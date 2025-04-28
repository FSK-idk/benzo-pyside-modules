from core.model.deposit_card_table_column import DepositCardTableColumn
from core.model.sort_order import SortOrder


class Query:
    @staticmethod
    def createDepositCardTable() -> str:
        return """
            CREATE TABLE IF NOT EXISTS DepositCard (
                id                      INTEGER     NOT NULL,
                issuer                  TEXT        NOT NULL,
                number                  TEXT        NOT NULL,
                expiration_date         TEXT        NOT NULL,
                holder_name             TEXT        NOT NULL,
                balance                 INTEGER     NOT NULL,
                PRIMARY KEY (id),
                UNIQUE (number),
                CHECK (issuer != '' AND number != '' AND expiration_date != '' AND holder_name != '')
            )
        """

    @staticmethod
    def insertDepositCard() -> str:
        return """
            INSERT OR IGNORE INTO DepositCard (
                issuer,
                number,
                expiration_date,
                holder_name,
                balance
            )
            VALUES (?, ?, ?, ?, ?)
        """

    @staticmethod
    def selectDepositCards(sort_by: DepositCardTableColumn, sort_order: SortOrder) -> str:
        query = f"""
            SELECT id, issuer, number, expiration_date, holder_name, balance FROM DepositCard
            WHERE
                issuer LIKE ? AND
                number LIKE ? AND
                holder_name LIKE ?
        """

        if (sort_by == DepositCardTableColumn.EXPIRATION_DATE):
            query += f"""
                ORDER BY
                    date(expiration_date) {'ASC' if sort_order == SortOrder.ASC else 'DESC'}
            """
        else:
            query += f"""
                ORDER BY
                    {sort_by.value} {'ASC' if sort_order == SortOrder.ASC else 'DESC'}
            """

        return query

    @staticmethod
    def selectDepositCard() -> str:
        return """
            SELECT id, issuer, number, expiration_date, holder_name, balance FROM DepositCard
            WHERE
                number LIKE ? AND
                expiration_date LIKE ? AND
                holder_name LIKE ?
            LIMIT 1
        """

    @staticmethod
    def selectDepositCardIdByNumber() -> str:
        return """
            SELECT id FROM DepositCard
            WHERE
                number = ?
            LIMIT 1
        """

    @staticmethod
    def updateDepositCard() -> str:
        return """
            UPDATE DepositCard
            SET
                balance = ?
            WHERE
                id = ?
        """

    @staticmethod
    def createPaymentLogTable() -> str:
        return """
            CREATE TABLE IF NOT EXISTS PaymentLog (
                id                      INTEGER     NOT NULL,
                deposit_card_id         INTEGER     NOT NULL,
                payment_amount          INTEGER     NOT NULL,
                organization_name       TEXT        NOT NULL,
                payment_key             TEXT        NOT NULL,
                PRIMARY KEY (id),
                FOREIGN KEY (deposit_card_id) REFERENCES DepositCard (id),
                CHECK (organization_name != '' AND payment_key != '')
            )
        """

    @staticmethod
    def insertPaymentLog() -> str:
        return """
            INSERT OR IGNORE INTO PaymentLog (
                deposit_card_id,
                payment_amount,
                organization_name,
                payment_key
            )
            VALUES (?, ?, ?, ?)
        """
