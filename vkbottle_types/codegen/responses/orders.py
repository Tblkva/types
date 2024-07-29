import typing

from vkbottle_types.base_model import Field
from vkbottle_types.objects import OrdersAmount, OrdersOrder, OrdersSubscription
from vkbottle_types.responses.base_response import BaseResponse


class OrdersChangeStateResponse(BaseResponse):
    response: str = Field()


class OrdersGetAmountResponse(BaseResponse):
    response: typing.List[OrdersAmount] = Field()


class OrdersGetByIdResponse(BaseResponse):
    response: typing.List[OrdersOrder] = Field()


class OrdersGetUserSubscriptionByIdResponse(BaseResponse):
    response: "OrdersSubscription" = Field()


class OrdersGetUserSubscriptionsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class OrdersGetResponse(BaseResponse):
    response: typing.List[OrdersOrder] = Field()
