from abc import ABC
import re

import dhis2_etl.builders.dhis2
import django_adx.models.adx.data as data_models
import django_adx.models.adx.definition as definition_models
from django_adx.builders.adx import ADXBuilder

