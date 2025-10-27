select
    *
from
    {{ source('raw_data', 'policies') }}
