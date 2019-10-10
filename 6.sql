.print Question 6 - ndemarco


select p.fname, p.lname from persons p, marriages m where (m.p1_fname = 'Michael' and m.p1_lname = 'Fox' and m.p2_fname = p.fname and p.lname = m.p2_lname ) or ( m.p1_fname = p.fname and m.p2_lname = p.lname) order by m.regdate desc limit 1;
