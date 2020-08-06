### 코딩테스트 연습 > SELECT

- 모든 레코드 조회하기

  ```MYSQL
  SELECT * FROM ANIMAL_INS
  ORDER BY ANIMAL_ID ASC
  ```

- 역순 정렬하기

  ```MYSQL
  SELECT NAME, DATETIME FROM ANIMAL_INS ORDER BY ANIMAL_ID DESC
  ```

- 어린 동물 찾기

  ```mysql
  SELECT ANIMAL_ID, NAME FROM ANIMAL_INS 
  WHERE INTAKE_CONDITION != 'Aged'
  ORDER BY ANIMAL_ID ASC
  ```

- 아픈 동물 찾기

  ```mysql
  SELECT ANIMAL_ID, NAME FROM ANIMAL_INS
  WHERE INTAKE_CONDITION = 'Sick'
  ORDER BY ANIMAL_ID ASC
  ```

- 동물의 아이디와 이름

  ```mysql
  SELECT ANIMAL_ID, NAME FROM ANIMAL_INS
  ORDER BY ANIMAL_ID ASC
  ```

- 여러 기준으로 정렬하기

  ```mysql
  SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS
  ORDER BY NAME ASC, DATETIME DESC
  ```

- 상위 n개 레코드

  ```mysql
  SELECT NAME FROM ANIMAL_INS
  ORDER BY DATETIME ASC LIMIT 1
  ```

- 



### 코딩테스트 연습 > SUM, MAX, MIN

- 최댓값 구하기

  ```mysql
  SELECT DATETIME FROM ANIMAL_INS
  WHERE DATETIME=(SELECT max(DATETIME) FROM ANIMAL_INS)
  ```

- 최솟값 구하기

  ```mysql
  SELECT DATETIME FROM ANIMAL_INS
  WHERE DATETIME=(SELECT min(DATETIME) FROM ANIMAL_INS)
  ```

- 동물 수 구하기

  ```mysql
  SELECT COUNT (*) FROM ANIMAL_INS
  ```

- 중복 제거하기

  ```MYSQL
  SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS
  ```

- 



### 코딩테스트 연습 > IS NULL

- 이름이 없는 동물의 아이디

  ```mysql
  SELECT ANIMAL_ID FROM ANIMAL_INS
  WHERE NAME IS NULL
  ```

- 이름이 있는 동물의 아이디

  ```mysql
  SELECT ANIMAL_ID FROM ANIMAL_INS
  WHERE NAME IS NOT NULL
  ```

- NULL 처리하기

  ```mysql
  SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name')AS NAME, SEX_UPON_INTAKE
  FROM ANIMAL_INS
  ORDER BY ANIMAL_ID
  ```

- 



### 코딩테스트 연습 > GROUP BY

- 고양이와 개는 몇 마리 있을까

  ```sqlite
  SELECT ANIMAL_TYPE, COUNT(*)
  FROM ANIMAL_INS
  GROUP BY ANIMAL_TYPE
  ORDER BY ANIMAL_TYPE 
  ```

- 입양 시각 구하기(1)

  ```mysql
  SELECT HOUR(DATETIME) HOUR, COUNT(DATETIME) COUNT
  FROM ANIMAL_OUTS
  GROUP BY HOUR(DATETIME)
  HAVING HOUR >= 9 and HOUR <= 19
  ORDER BY HOUR ASC
  ```

- 



### 코딩테스트 연습 > Summer/Winter Coding(2019)

-  우유와 요거트가 담긴 장바구니

  ```mysql
  SELECT DISTINCT A.CART_ID FROM 
   (SELECT CART_ID FROM CART_PRODUCTS WHERE NAME = 'Yogurt') as A, 
   (SELECT CART_ID FROM CART_PRODUCTS WHERE NAME = 'Milk') as B
   WHERE A.CART_ID = B.CART_ID
  ```

  