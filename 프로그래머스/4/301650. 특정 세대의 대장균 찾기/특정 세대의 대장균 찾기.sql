SELECT 
    third.ID


FROM
    ECOLI_DATA AS main
        INNER JOIN ECOLI_DATA AS second ON main.ID = second.PARENT_ID
        INNER JOIN ECOLI_DATA AS third ON second.ID = third.PARENT_ID

WHERE
    main.PARENT_ID IS NULL

ORDER BY third.ID;