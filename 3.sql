.print Question 3 - ndemarco

select distinct b3.fname, b3.lname from births b1, births b2, births b3, births b4 where b1.fname = 'Michael' and b1.lname = 'Fox' and ((b2.fname = b1.f_fname and b2.lname = b1.f_lname) or (b2.fname = b1.m_fname and b2.lname = b1.m_lname)) and ((b3.f_fname = b4.fname and b3.f_lname = b4.lname) or (b3.m_fname = b4.fname and b3.m_lname = b4.lname)) and b4.f_fname = b2.f_fname and b4.f_lname = b2.f_lname and b1.fname || b1.lname != b3.fname || b3.lname;
