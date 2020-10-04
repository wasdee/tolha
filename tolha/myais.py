from playwright import sync_playwright
from loguru import logger
# p = sync_playwright().start()

def get_recent_call_history(phone_number, password, national_id):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.newPage()
        # login
        page.goto('https://myais.ais.co.th/login')
        page.type("input[name='a mobile input']",phone_number)
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
            invoices = response.json()
            logger.debug(invoices)
        # page.on('request', print)


        # in case you want other bill hisory
        # .check-box .check , .check-box img
        # .check-box img = [bill1]
        # .billing-row-detail:nth-child(3) .check [bill2]
        # .billing-row-detail:nth-child(4) .check [bill3]

        # XHR call history(**/filter)
        url = "**/usages/billed/group/VOICE/chargedetail/filter"
        with page.expect_response(url):
            page.click("#btnApproveUsageDetailSeaching")
            response = page.waitForResponse(url)
            call_usage = response.json()
            logger.debug(call_usage)


        browser.close()

        return call_usage

# p.stop()
