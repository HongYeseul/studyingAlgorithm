-- 코드를 입력하세요
SELECT
    user.USER_ID,
    user.NICKNAME AS NICKNAME,
    SUM(PRICE) AS TOTAL_SALES

FROM
    USED_GOODS_BOARD AS board
        JOIN USED_GOODS_USER AS user
        ON (board.WRITER_ID = user.USER_ID)
    
WHERE
    board.STATUS = 'DONE'
    
GROUP BY
    user.USER_ID

HAVING
    TOTAL_SALES >= 700000

ORDER BY
    TOTAL_SALES