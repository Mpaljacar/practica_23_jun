mecanismos = ['KPC', 'NDM', 'OXA-48']

query_multi = f"""
SELECT 
    a.id AS aislamiento_id,
    a.fecha_aislamiento,
    a.bacteria,
    GROUP_CONCAT(DISTINCT m.mecanismo) AS mecanismos_detectados
FROM 
    aislamientos a
JOIN 
    mecanismos_resistencia m ON a.id = m.aislamiento_id
WHERE 
    m.mecanismo IN ({','.join(['?']*len(mecanismos))})
GROUP BY 
    a.id, a.fecha_aislamiento, a.bacteria
HAVING 
    COUNT(DISTINCT m.mecanismo) >= 2
ORDER BY 
    a.fecha_aislamiento DESC;
"""

df_multi = pd.read_sql_query(query_multi, conn, params=mecanismos)
print(df_multi)
