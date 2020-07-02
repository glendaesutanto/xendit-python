import json

from dataclasses import dataclass


@dataclass(init=False)
class InvoiceBank:
    bank_code: str
    collection_type: str
    bank_account_number: str
    transfer_amount: int
    bank_branch: str
    account_holder_name: str
    identity_amount: str

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return json.dumps(vars(self), indent=4)
