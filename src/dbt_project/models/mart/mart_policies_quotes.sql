select
   p.*,
   q.*
from {{ ref('int_policies') }} p
   left join {{ ref('int_quotes') }} q
      on p.quote_id = p.quote_id