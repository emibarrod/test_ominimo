with source as (
    select * from {{ ref('raw_quotes') }}
)

select
    quote_id::varchar as quote_id,
    product::varchar as product,
    price::float as price,
    technical_price::float as technical_price,
    created_at::timestamp as created_at
from source