SELECT
    ID,
    CASE
        WHEN NTile(4) over (order by SIZE_OF_COLONY DESC) = 1 THEN 'CRITICAL'
        WHEN NTile(4) over (order by SIZE_OF_COLONY DESC) = 2 THEN 'HIGH'
        WHEN NTile(4) over (order by SIZE_OF_COLONY DESC) = 3 THEN 'MEDIUM'
        WHEN NTile(4) over (order by SIZE_OF_COLONY DESC) = 4 THEN 'LOW'
    END AS COLONY_NAME
    
FROM
    ECOLI_DATA

# WHERE
    

ORDER BY
    ID