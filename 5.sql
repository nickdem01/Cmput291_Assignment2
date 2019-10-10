.print Question 5 - ndemarco


select d.fname, d.lname from demeritNotices d where date('now', '-2 year') <= d.ddate group by d.fname, d.lname having sum(points) >= 15;
