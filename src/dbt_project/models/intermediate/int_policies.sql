with source as (
    select * from {{ ref('raw_policies') }}
)

select
    policy_id::varchar as policy_id,
    quote_id::varchar as quote_id,
    customer_id::varchar as customer_id,
    created_at::timestamp as created_at,
    vehicle_make::varchar as vehicle_make,
    vehicle_model::varchar as vehicle_model,
    vehicle_year::integer as vehicle_year,
    status::varchar as status
from source