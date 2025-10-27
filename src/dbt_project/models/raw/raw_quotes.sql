select
    *
from
    {{ source('raw_data', 'quotes') }}
