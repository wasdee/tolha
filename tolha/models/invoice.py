from pydantic import Field
from typing import List
from .response import BaseResponse

from fastapi_utils.api_model import APIModel

class Invoice(APIModel):
    invoice_number: str 
    is_required_sr: bool = Field(..., alias='isRequiredSR')
    period_description: str 
    period_from: str 
    period_to: str 
    payment_due_date: str 
    total_balance: str 
    outstanding_balance: str 
    is_payable: bool 
    event_seq: str 
    billing_system: str 
    bill_cycle: str 
    remark: str 

class InvoiceResponse(BaseResponse):
    data_list: List[Invoice]