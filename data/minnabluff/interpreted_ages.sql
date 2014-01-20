select distinct x.history_id, x.name, matname from 
(select ia.history_id, iah.identifier, ia.age, m.aliquot, s.name, mat.name as matname
from proc_InterpretedAgeTable as ia
join proc_InterpretedAgeHistoryTable as iah on iah.id=ia.history_id
join proc_InterpretedAgeSetTable as ias on ias.interpreted_age_id=ia.id
join meas_AnalysisTable as m on ias.analysis_id=m.id
join gen_labtable as l on m.lab_id=l.id
join gen_SampleTable as s on l.sample_id=s.id
join gen_projecttable as p on s.project_id=p.id
join gen_materialtable as mat on s.material_id=mat.id
where ia.age>8 
and p.name ='Minna Bluff'-- and ia.age_kind='plateau'
order by iah.identifier, iah.create_date desc) as x
group by x.identifier, x.aliquot
order by x.age desc

