

.print Question 2 - ndemarco


select b2.fname, b2.lname from births b1, births b2 where b1.fname = 'Michael' and b1.lname = 'Fox' and b2.f_fname = b1.f_fname and b2.m_fname = b1.m_fname and b2.f_lname = b1.f_lname and b2.m_lname = b1.m_lname and b1.fname || b1.lname != b2.fname || b2.lname;
