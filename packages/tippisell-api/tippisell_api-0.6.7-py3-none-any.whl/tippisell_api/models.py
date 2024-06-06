import typing
import datetime
import pydantic
import decimal


class User(pydantic.BaseModel):
    id: int
    telegram_id: typing.Optional[int]
    username: typing.Optional[str]
    balance: decimal.Decimal
    purchases_amount: typing.Optional[decimal.Decimal] = pydantic.Field(
        None, description="Сумма покупок"
    )
    refills_amount: typing.Optional[decimal.Decimal] = pydantic.Field(
        None, description="Сумма пополнений"
    )
    joined_timestamp: datetime.datetime
    last_use_timestamp: datetime.datetime


class Product(pydantic.BaseModel):
    id: int
    name: str
    description: str
    type: str
    price: float
    category_id: typing.Optional[int]
    min_buy: int
    max_buy: int
    is_infinitely: bool


class HttpResponse(pydantic.BaseModel):
    status_code: int
    result: dict


class Shop(pydantic.BaseModel):
    id: int
    web_background: str
    web_favicon: str
    web_telegram_bot_link: bool
    bot_username: str
    uuid: pydantic.UUID4
    currency: str
    create_timestamp: datetime.datetime


class GetUsersResponse(pydantic.BaseModel):
    total_count: pydantic.NonNegativeInt = pydantic.Field(
        ge=0, description="Общее количество пользователей"
    )
    data: typing.List[User]
