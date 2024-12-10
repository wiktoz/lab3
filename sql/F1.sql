select count(*) as num from lessons 
group by student_id 
order by num desc 
limit 1