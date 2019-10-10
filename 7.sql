.print Question 7 - ndemarco

select v.color, count(t.regno), avg(t.fine) from registrations r, vehicles v left outer join tickets t on t.regno = r.regno where date('now','+1 month') <= date(r.expiry) and r.vin = v.vin group by v.color;
