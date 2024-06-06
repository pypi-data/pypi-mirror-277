
# KRX 한국거래소 데이터 API 


##### ============================================================
## Overview
##### ============================================================
[ KRX Sub-Domains ]

KRX 정보데이터시스템
http://data.krx.co.kr

상장공시시스템(KIND)
http://kind.krx.co.kr

KRX 지수
http://index.krx.co.kr

상장공시(Listing).
http://listing.krx.co.kr

공매도 종합 포털.
http://short.krx.co.kr

KRX 증권투자 정보포털. | Securities Market Information Library of Exchange.
http://smile.krx.co.kr

표준코드시스템
https://isin.krx.co.kr



##### ============================================================
## IDE
##### ============================================================

### Terminal Python Interpreter
- krx 자체 virtual env 를 구성해야 하는데, eproxy 때문에 pymongo 도 install해야한다.
- 왠만하면, stock package에서 불러다 쓰는 방법으로 테스트하면 안되나?

### Jupyter


### 주식시장의 매매거래중단제도(Circuit Breakers)
http://regulation.krx.co.kr/contents/RGL/03/03010402/RGL03010402.jsp

### 프로그램매매
- 프로그램매매 호가효력 일시정지제도(Sidecar)
http://regulation.krx.co.kr/contents/RGL/03/03010404/RGL03010404.jsp

### 시간외종가/단일가매매
http://regulation.krx.co.kr/contents/RGL/03/03010301/RGL03010301.jsp




### Batch

##### DayTrde
- 평일(장전 아침): 매수했던 종목의 직전일 수집.
- 주말/공휴일 : 모든 종목의 당해년도 수집.
