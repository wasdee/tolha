import pytest
from tolha.models.invoice import InvoiceResponse

@pytest.fixture
def response():
    json_payload = """
    {
    "dataList":[
        {
            "object":"invoice",
            "invoiceNumber":"W-IN-16-6411-0484127",
            "isRequiredSR":false,
            "periodDescription":"ค่าใช้บริการวันที่ 24/10/2021 - 23/11/2021 (Due Date 16/12/2021)",
            "periodFrom":"24/10/2021",
            "periodTo":"23/11/2021",
            "paymentDueDate":"16/12/2021",
            "totalBalance":"455.51",
            "outstandingBalance":"0.00",
            "isPayable":false,
            "eventSeq":"211124000",
            "billingSystem":"NONBOS",
            "billCycle":"พฤศจิกายน 2564",
            "remark":"สามารถดูใบแจ้งค่าใช้บริการได้หลังจากสิ้นสุดรอบบิลแล้ว 7 วัน"
        },
        {
            "object":"invoice",
            "invoiceNumber":"W-IN-16-6410-0542372",
            "isRequiredSR":false,
            "periodDescription":"ค่าใช้บริการวันที่ 24/09/2021 - 23/10/2021 (Due Date 15/11/2021)",
            "periodFrom":"24/09/2021",
            "periodTo":"23/10/2021",
            "paymentDueDate":"15/11/2021",
            "totalBalance":"565.70",
            "outstandingBalance":"0.00",
            "isPayable":false,
            "eventSeq":"211024000",
            "billingSystem":"NONBOS",
            "billCycle":"ตุลาคม 2564",
            "remark":"สามารถดูใบแจ้งค่าใช้บริการได้หลังจากสิ้นสุดรอบบิลแล้ว 7 วัน"
        },
        {
            "object":"invoice",
            "invoiceNumber":"W-IN-16-6409-0848128",
            "isRequiredSR":false,
            "periodDescription":"ค่าใช้บริการวันที่ 24/08/2021 - 23/09/2021 (Due Date 16/10/2021)",
            "periodFrom":"24/08/2021",
            "periodTo":"23/09/2021",
            "paymentDueDate":"16/10/2021",
            "totalBalance":"698.75",
            "outstandingBalance":"0.00",
            "isPayable":false,
            "eventSeq":"210924000",
            "billingSystem":"NONBOS",
            "billCycle":"กันยายน 2564",
            "remark":"สามารถดูใบแจ้งค่าใช้บริการได้หลังจากสิ้นสุดรอบบิลแล้ว 7 วัน"
        }
    ],
    "resultCode":"20000",
    "resultDesc":"Success",
    "developerMessage":"Success"
    }
    """
    return json_payload

def test_invoice(response):
    invoice_response = InvoiceResponse.parse_raw(response)
    assert len(invoice_response.data_list) == 3
