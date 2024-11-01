-- 코드를 입력하세요
SELECT
    CONCAT('/home/grep/src/', board.board_id, '/', file.file_id, file.file_name, file.FILE_EXT)
    AS FILE_PATH

FROM
    USED_GOODS_BOARD AS board
    JOIN USED_GOODS_FILE AS file
    ON (board.board_id = file.board_id)


WHERE 
    board.VIEWS = (SELECT MAX(VIEWS) FROM USED_GOODS_BOARD)
ORDER BY 
    file.FILE_ID DESC;