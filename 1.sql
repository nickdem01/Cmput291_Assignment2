
.print Question 1 - ndemarco


select p.fname, p.lname, p.phone from persons p, vehicles v, registrations r where v.make = 'Chevrolet' and v.model = 'Camaro' and v.year = 1969 and v.vin = r.vin and p.fname = r.fname and p.lname = r.lname;
