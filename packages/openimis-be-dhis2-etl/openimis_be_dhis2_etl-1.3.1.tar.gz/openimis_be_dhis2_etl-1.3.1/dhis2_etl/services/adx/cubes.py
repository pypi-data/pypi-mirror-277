from django_adx.models.adx.definition import ADXMappingDefinition
from django_adx.models.adx.time_period import ISOFormatPeriodType
from dhis2_etl.services.adx.groups import (
    get_claim_hf_group,
    get_enrolment_location_group,
)


def get_claim_cube(period: str) -> ADXMappingDefinition:
    period_type = ISOFormatPeriodType()
    period_obj = period_type.build_period(period)
    return ADXMappingDefinition(
        period_type=period_type, groups=[get_claim_hf_group(period_obj)]
    )


def get_enrollment_cube(period: str) -> ADXMappingDefinition:
    period_type = ISOFormatPeriodType()
    period_obj = period_type.build_period(period)
    return ADXMappingDefinition(
        period_type=period_type,
        groups=[
            get_enrolment_location_group(period_obj),
        ],
    )
