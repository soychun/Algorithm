LIKE 문법
https://lcs1245.tistory.com/entry/SQL-LIKE-%EC%97%B0%EC%82%B0%EC%9E%90-%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%B6%80%EB%B6%84%EC%9D%BC%EC%B9%98-%EA%B2%80%EC%83%89

SELECT *
FROM 테이블
WHERE 칼럼 LIKE '쓰고싶은 문장'


JOIN 문법
https://yoo-hyeok.tistory.com/98


https://school.programmers.co.kr/learn/courses/30/lessons/131120
-- 코드를 입력하세요
SELECT P.MEMBER_ID, P.MEMBER_NAME, P.GENDER, DATE_FORMAT(P.DATE_OF_BIRTH,'%Y-%m-%d') AS DATA_OF_BIRTH
FROM MEMBER_PROFILE AS P
WHERE P.DATE_OF_BIRTH LIKE '%-03-%' AND P.GENDER LIKE 'W' AND P.TLNO IS NOT NULL
ORDER BY P.MEMBER_ID ASC


https://school.programmers.co.kr/learn/courses/30/lessons/131537
-- 코드를 입력하세요
SELECT DATE_FORMAT(F.SALES_DATE,'%Y-%m-%d') AS SALES_DATE,PRODUCT_ID,NULL AS USER_ID,SALES_AMOUNT
FROM OFFLINE_SALE AS F
WHERE SALES_DATE LIKE '%-03-%'

UNION

SELECT DATE_FORMAT(N.SALES_DATE,'%Y-%m-%d') AS SALES_DATE,PRODUCT_ID,USER_ID,SALES_AMOUNT
FROM ONLINE_SALE AS N
WHERE SALES_DATE LIKE '%-03-%'

order by SALES_DATE, product_id, user_id

https://velog.io/@juwon9733/SQL-%EA%B3%A0%EB%93%9D%EC%A0%90-Kit-SELECT-%EC%98%A4%ED%94%84%EB%9D%BC%EC%9D%B8%EC%98%A8%EB%9D%BC%EC%9D%B8-%ED%8C%90%EB%A7%A4-%EB%8D%B0%EC%9D%B4%ED%84%B0-%ED%86%B5%ED%95%A9%ED%95%98%EA%B8%B0

DISTINCT
https://school.programmers.co.kr/learn/courses/30/lessons/59408


NOT NULL 복습할 것
https://school.programmers.co.kr/questions/34610

입양시각구하기(1)
모든 답변 사례 분석해서 내 것으로 만들 것
https://school.programmers.co.kr/learn/courses/30/lessons/59412

입양시각구하기(2)
문제 아예 못풀었음
https://school.programmers.co.kr/learn/courses/30/lessons/59413

IFNULL
NULL일 경우 ifnull(expr1,expr2);
만약에 expr1이 null이라면, expr2를 리턴합니다. 그렇지 않다면, expr1을 리턴합니다
SELECT WAREHOUSE_ID,	WAREHOUSE_NAME,	ADDRESS	,	IFNULL(FREEZER_YN,'N')