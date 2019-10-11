.print Question 8 - ndemarco

select v.year, v.color, v.model from vehicles v group by v.year,v.color,v.model order by count(v.color) desc, v.year desc, count(v.model) desc;
