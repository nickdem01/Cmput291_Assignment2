.print Question 4 - ndemarco


select b1.fname, b1.lname from births b1 where b1.f_fname = 'Michael' and b1.f_lname = 'Fox' and b1.regdate = (select min(b1.regdate) from births b1 where b1.f_fname = 'Michael' and  b1.f_lname = 'Fox' group by b1.f_lname, b1.f_fname);
