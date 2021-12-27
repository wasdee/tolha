from typing import Dict, Optional, List
from pydantic import BaseModel, Field
import datetime

from pydantic.types import Json
from .response import BaseResponse
from fastapi_utils.api_model import APIModel


class Column(APIModel):
    text: str
    column_property: dict

class RowProperty(APIModel):
    level: Optional[int] = None
    is_summary_row: bool

class Row(APIModel):
    row_property: RowProperty
    columns: List[Column|Dict]

class UsageDetailGroup(BaseModel):
    headers: List[Row]
    rows: List[Row]

class Data(APIModel):
    usage_detail_groups: List[UsageDetailGroup]
    aunjai_service_flag: bool
    notfind: bool

class CallUsageResponse(BaseResponse):
    data: Data

class Call(BaseModel):
    datetime: datetime.datetime

    destination_phoneNumber: str
    destination_network: str

    origin: str
    destination: str

    addons: str

    duration: datetime.timedelta
    calculated_cost: float
    actual_cost: float

    note: str = ''

    @staticmethod
    def parse_usage_detail_groups_raw(usage_detail_groups: UsageDetailGroup):
        sections = {}
        current_section = None
        for row in usage_detail_groups[0].rows:
            if row.row_property.is_summary_row:
                assert row.columns[0].text not in sections
                current_section = sections[row.columns[0].text] = []
            else:
                current_section.append({h.text:(v.text if not isinstance(v, dict) else '') for h,v in zip(usage_detail_groups[0].headers[0].columns, row.columns) })
        
        return sections

    @classmethod
    def parse_usage_detail_groups(cls,usage_detail_groups: UsageDetailGroup) -> List['Call']:
        calls = []

        sections = cls.parse_usage_detail_groups_raw(usage_detail_groups)
        for section_name, calls_ in sections.items():
            for call in calls_:
                calls.append(cls.parse_dict(call, note=section_name.split(' ')[0]))
        
        return calls

    @classmethod
    def parse_dict(cls, d: dict, note: str='') -> 'Call':
        dt = datetime.datetime.strptime(f"{d['วันที่']} {d['เวลา']}", r"%d/%m/%Y %H:%M:%S")
        min_,sec = duration = d['หน่วย'].split(':')
        return cls(
            datetime=dt,
            destination_phoneNumber=d['หมายเลขปลายทาง'],
            destination_network=d['เครือข่าย'],
            origin=d['ต้นทาง'],
            destination=d['ปลายทาง'],
            addons=d['บริการเสริม'],
            duration=datetime.timedelta(minutes=int(min_), seconds=int(sec)),
            calculated_cost=d['ค่าบริการที่ใช้จริง (บาท)'],
            actual_cost=d['ค่าบริการที่เรียกเก็บ (บาท)']
        )
