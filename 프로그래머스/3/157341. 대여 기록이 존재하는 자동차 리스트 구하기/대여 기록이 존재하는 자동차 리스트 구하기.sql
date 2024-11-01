-- 코드를 입력하세요
SELECT
    DISTINCT car.car_id
    
FROM
    CAR_RENTAL_COMPANY_CAR AS car
        JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS history
        ON (car.CAR_ID = history.CAR_ID)

WHERE
    MONTH(history.START_DATE) = 10
    AND car.CAR_TYPE = '세단'

ORDER BY
    car.car_id desc