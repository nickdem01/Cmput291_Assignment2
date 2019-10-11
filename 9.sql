.print Question 9 - ndemarco

create view personDetails(fname,lname,bdate,bplace,ticketsRcvd,carsowned) as select p.fname, p.lname, p.bdate, p.bplace, count(t.tno), count(r.regno) from tickets t, registrations r, persons p where r.fname = p.fname and r.lname = p.lname and t.regno = r.regno and t.vdate >= date('now','-1 year') group by p.fname, p.lname, p.bdate, p.bplace;
