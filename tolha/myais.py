from playwright import sync_playwright
from loguru import logger
from tolha import Call, Invoice, CallUsageResponse, InvoiceResponse
from typing import Dict, List, Tuple

InvoiceBillCycle = str

def get_all_call_history(phone_number_or_username, password, national_id) -> Tuple[List[Invoice], Dict[InvoiceBillCycle,List[Call]]]:
    """
    get up to 3 month of call usage
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.newPage()

        # login
        page.goto('https://myais.ais.co.th/login')
        page.type("input[name='a mobile input']",phone_number_or_username)
        page.click("button[type=submit]")
        page.click("button[id=btnLoginFormPassword]")
        page.type("input[id='txtLoginFormPassword']", password)
        page.click("button[id=btnLoginFormSubmitLogin2]")

        # access page
        page.waitForSelector("myais-sidebar-menu:nth-child(4) .menu-content")
        page.goto("https://myais.ais.co.th/balance/usage")

        #fill national id
        page.type("input[id='input-idcard']", national_id)

        # XHR **/invoice
        url = '**/invoices'
        with page.expect_response(url):
            page.click("button[type=submit]")
            response = page.waitForResponse(url)

            invoice_response = InvoiceResponse.parse_raw(response.body())

            call_usages = dict()
            for i, invoice in enumerate(invoice_response.data_list):
                if i != 0: # it selects the first already
                    page.click(f'.billing-row-detail:nth-child({2+i}) .check')

                # XHR call history(**/filter)
                url = "**/usages/billed/group/VOICE/chargedetail/filter"
                with page.expect_response(url):
                    page.click("#btnApproveUsageDetailSeaching")
                    response = page.waitForResponse(url)

                    call_usage_response = CallUsageResponse.parse_raw(response.body())

                    call_usages[invoice.bill_cycle]= Call.parse_usage_detail_groups(call_usage_response.data.usage_detail_groups)

                page.click('myais-gray-button > button')
                page.waitForResponse('**/invoices')


        browser.close()

        return invoice_response.data_list, call_usages