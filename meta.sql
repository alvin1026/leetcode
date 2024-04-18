-- a

select distinct (s.name)
from Salesperson s
join Orders o on o.salesperson_id = s.id
join Customer c on c.id = o.cust_id
where c.name = 'Samsonic'

-- b
with samsonic_salesperson as (
    select distinct s.id
    from Salesperson s
    join Orders o on o.salesperson_id = s.id
    join Customer c on c.id = o.cust_id
    where c.name = 'Samsonic'
)
select name
from Salesperson s
left join samsonic_salesperson ss on s.id = ss.id
where ss.id is null;



-- c
with orders_per_salesperson as (
    select salesperson_id, count(*) as order_count
    from Orders
    group by salesperson_id
)
select distinct (name)
from salesperson s
join orders_per_salesperson o on o.salesperson_id = s.id
where o.order_count >= 2

-- d
select name, age
from salesperson
where salary >= 100000

-- e
with unit_count_per_salesperson as (
    select salesperson_id, count(number) as unit_count
    from Orders
    group by salesperson_id
)
select distinct (name)
from salesperson s
join unit_count_per_salesperson u on u.salesperson_id = s.id
where u.unit_count > 1400

-- f
select order_date
from orders o
join customers c on c.id = o.cust_id
order by order_date
limit 1

select order_date
from orders o
join customers c on c.id = o.cust_id
order by order_date desc
limit 1
