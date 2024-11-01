-- 코드를 작성해주세요

# SELECT
#     user.id,
#     user.email,
#     user.first_name,
#     user.last_name
    
# FROM
#     DEVELOPERS AS user
#     JOIN SKILLCODES as skill
#     ON (user.SKILL_CODE & skill.CODE) = skill.code

# WHERE
#     skill.CATEGORY = 'Front End'

# ORDER BY
#     user.id


SELECT DISTINCT ID,EMAIL,d.FIRST_NAME,d.LAST_NAME
FROM DEVELOPERS d 
    JOIN SKILLCODES s
WHERE 
    d.SKILL_CODE & s.CODE = s.CODE 
    AND s.CATEGORY = 'Front End'
ORDER BY ID;