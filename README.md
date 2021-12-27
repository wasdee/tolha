# Tolha - โทรหา
เข้าถึงประวัติการโทรของตัวเองง่ายๆ จากค่ายมือถือของคุณ
> ช่วยคุณนับความคิดถึงใครซักคนแบบ programmable


## Highlight and Feature
1. fully-type, with `pydantic`
2. no docs, since api is so simple #hackerStyle
3. Support Python 3.10.1+ #hackerStyle

## Get Started
```bash
# support python 3.10+
pip install tolha
```

```python
from tolha.myais import get_all_call_history

# type down, myais credential
invoices, call_usages = get_all_call_history(phone_number_or_username='0995555555', password='password1234', national_id='1515566254125')

print(invoices[0])
# Invoice(invoice_number='W-IN-16-6412-xxxxxx', is_required_sr=False, period_description='ค่าใช้บริการวันที่ 24/11/2021 - 23/12/2021 (Due Date 15/01/2022)', period_from='24/11/2021', period_to='23/12/2021', payment_due_date='15/01/2022', total_balance='405.75', outstanding_balance='0.00', is_payable=False, event_seq='211224000', billing_system='NONBOS', bill_cycle='ธันวาคม 2564', remark='สามารถดูใบแจ้งค่าใช้บริการได้วันที่ 30 ธ.ค. 2564')


print(call_usages['ธันวาคม 2564'][0])
# Call(datetime=datetime.datetime(2021, 11, 24, 9, 43), destination_phoneNumber='08xxxxxxxx', destination_network='AIS', origin='Udon Thani', destination='AIS', addons='', duration=datetime.timedelta(seconds=60), calculated_cost=1.5, actual_cost=0.0, note='')
```

## Dev

### This is a movement.
<a href="https://imgflip.com/i/5z7hhh"><img src="https://i.imgflip.com/5z7hhh.jpg" title="made at imgflip.com"/></a><div>

Feel free to join and enlighten yourself, make your life a bit more programmable.

### Roadmap
1. add other metric
2. make cli
3. add other telco
4. add async
5. add other non telco - read facebook messenger dump/ google duo dump

### Tools for CSS Selector
use <https://chrome.google.com/webstore/detail/selectorgadget/mhjhnkcfbdhnjickkkdbjoemdmbfginb>
