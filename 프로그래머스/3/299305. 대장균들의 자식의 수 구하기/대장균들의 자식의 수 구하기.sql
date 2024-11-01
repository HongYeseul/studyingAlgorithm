SELECT 
    # *
    main.ID,
    COUNT(second.PARENT_ID) AS CHILD_COUNT
    
    
FROM
    ECOLI_DATA AS main
        LEFT OUTER JOIN ECOLI_DATA AS second 
            ON main.ID = second.PARENT_ID

GROUP BY
    main.ID
    

ORDER BY
    ID