-- 코드를 입력하세요
SELECT
    user.USER_ID AS USER_ID,
    user.nickname AS NICKNAME,
    CONCAT(user.city, ' ', user.STREET_ADDRESS1, ' ', user.STREET_ADDRESS2) AS '전체주소',
    CONCAT(
        SUBSTRING(user.TLNO, 1, 3), '-',
        SUBSTRING(user.TLNO, 4, 4), '-',
        SUBSTRING(user.TLNO, 8, 4)
    ) AS '전화번호'
    

FROM
    USED_GOODS_BOARD AS board
        JOIN USED_GOODS_USER AS user
        ON (board.WRITER_ID = user.USER_ID)

# WHERE
GROUP BY
    user.user_id
HAVING
    COUNT(board.board_id) >= 3
    
ORDER BY
    user.user_id desc