from dataclasses import dataclass


@dataclass
class CustomerIdentity:
    account_id: str
    user_id: str


@dataclass
class CustomerInfo:
    identity: CustomerIdentity
    phone: str = ''
    type: int = 2
    name: str = ''
    email: str = ''
