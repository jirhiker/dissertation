select distinct
    l.identifier, s.name, mat.name
from
    meas_analysistable as m
        join
    gen_LabTable as l ON l.id = m.lab_id
        join
    gen_sampletable as s ON s.id = l.sample_id
        join
    gen_projecttable as p ON p.id = s.project_id
		join
	gen_MaterialTable as mat on mat.id=s.material_id
where
    m.step = '' and p.name = 'Minna Bluff'