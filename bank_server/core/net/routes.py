import uuid

from flask import Flask, Response, make_response, request

from core.model.payment_log import PaymentLog
from core.model.deposit_cards_request import DepositCardsRequest
from core.model.deposit_cards_response import DepositCardsResponse
from core.model.pay_request import PayRequest
from core.model.pay_response import PayResponse

from core.data_base.data_base import data_base


def init_app(app: Flask) -> None:

    @app.route('/')
    def hello() -> Response:
        response = make_response('Server is running\n')
        response.status_code = 200
        return response

    @app.route('/api/deposit-cards', methods=['GET'])
    def deposit_cards() -> Response:
        deposit_cards_request = DepositCardsRequest.from_json(request.data.decode())

        cards = data_base.selectDepositCards(deposit_cards_request)

        deposit_card_response = DepositCardsResponse(cards)

        response = make_response(deposit_card_response.to_json())
        response.content_type = 'application/json'
        response.status_code = 200

        return response

    @app.route('/api/pay', methods=['POST'])
    def pay() -> Response:
        pay_request = PayRequest.from_json(request.data.decode())

        card = data_base.selectDepositCard(pay_request)

        if card is None:
            response = make_response()
            response.status_code = 404
            return response

        if card.balance < pay_request.payment_amount:
            response = make_response()
            response.status_code = 404
            return response

        card.balance -= pay_request.payment_amount

        data_base.updateDepositCard(card)

        log = PaymentLog(
            id=0,
            deposit_card_id=card.id,
            payment_amount=pay_request.payment_amount,
            organization_name='BENZO',
            payment_key=uuid.uuid4().hex,
        )

        data_base.insertPaymentLog(log)

        pay_reponce = PayResponse(log.payment_key)

        response: Response = make_response(pay_reponce.to_json())
        response.content_type = 'application/json'
        response.status_code = 200

        return response
