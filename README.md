<div align="center">

# ipynb 파일이 안 열릴 수 있으니, project.pdf 파일로 확인 부탁드립니다.
</div>




# [ &#128081; Dataton &#128081; ]
2022.03.08 부터 2022.03.11 까지 강남 Aiffel에서 주최하는 Dataton에 참여하게 되었습니다.
<br>

< H&M DATA EDA/Personalized-Fashion-Recommendation >
- 강태원 : 데이터 원본 가공, 시각화 (연령, 제품 분류)
- 민진원 (발표) : 전처리, 시각화 (젠더구분, 제품 이미지 시각화)
- 박지호 : 데이터 전처리, 시각화 (색상, 연령, 뉴스 수신 여부)
- 이민선 (조장) : 전처리, 시각화 (우편번호, PCA, GMM)
## &#128085; Introduction
현재 진행중인 Kaggle Competition에서 H&M이 제공하는 데이터를 선택했습니다.
Competiotion의 목적은 H&M 고객 맞춤형 추천시스템을 구축하는 것으로 저희조도 이에 부합하는 EDA를 진행했습니다.
해당 데이터셋을 선택한 이유는 제품정보, 고객정보, 거래정보 데이터 및 이미지 데이터를 제공 받아 다양한 EDA가 가능하기 때문입니다.

## &#128086; Contents
01. Gender 컬럼 생성

02. 월별 Top 10 이미지 파일 시각화

03. 기간별 매출

04. 계절별 매출

05. Customer Age

06. Color

07. sales_channel_id

08. Department_name

09. Garment Group Name

10. Index Goup Name

11. Club Member Status

12. Fashion_News_Frequency

13. Postal Code 

14. 계절성(seasonality)을 띄는 제품을 PCA와 Clustering을 활용한 시각화

15. PCA(Principal Component Analysis)

16. GMM(Gaussian Mixture Models)/가우시안 혼합 모델

17. EDA를 통한 인사이트

## &#128095; feature discussion
(original features)
- t_dat : 주문 날짜 ('2019-09-30' ~ '2018-10-01')
- customer_id : 고객 id (고객 수 : 974,367 명)
- article_id : 상품 id (상품 수 : 71,396 가지)
- price : 상품 가격 (0.000017 ~ 0.591525)
- sales_channel_id : 판매 루트 (1 또는 2 / 판매 루트에 대한 정확한 정보는 없음)
- colour_group_name : 컬러명
- perceived_colour_master_name: 채도명
- index_group_no : 상품 용도 분류 코드
- index_group_name : 상품 용도 분류 ('Ladieswear', 'Divided', 'Menswear', 'Sport', 'Baby/Children')
- department_name: 상품 세부 용도 분류
- garment_group_name : 상품 카테고리 분류명 (총 21개 / ex 'Skirts', 'Knitwear', 'Accessories')
- club_member_status : 멤버쉽 상태 ('ACTIVE', 'PRE-CREATE', 'LEFT CLUB')
- fashion_news_frequency : ('Regularly', 'NONE', 'Monthly')
- age : 나이 (16 ~ 99세)
-  postal_code:우편번호(암호화되어 있음)

(additional features)
- age_segment : 연령대(10대, 20대, 30대,...)
- month : 주문 월
- year_month : 년와 월만 표시(201810)
- season : 계절(spring,summer, fall, winter)
- postal_code : 우편번호(암호화되어 있음)


## &#128140; 	&#128330;
&#128147; 강태원 : 서로 머리를 맞대면서 고민하는 시간이 정말 즐거웠습니다. 서로 의논하며 데이터를 좀 더 깊게 볼 수 있었고 EDA를 통한 인사이트도 다방면으로 도출할 수 있는 기회가 되었습니다. 이번 프로젝트에서 가장 크게 느낀 점은 혼자 고민하는 것보다 여러 명이 함께 고민했을 때 시너지가 더 크게 나올 수 있다는 것이었습니다. 그리고 특히 프로젝트를 하며 조원들과 즐겁게 소통하고 서로의 열정을 공유해서 더욱 뜻깊은 시간이 되었습니다. 우리가 강남 3조로 모였다는게 큰 행운이었습니다.

&#128153; 민진원 : 다양한 관점에서 데이터를 바라보고 접근하는 부분에서 혼자하면 생각하지 못했던 부분까지 EDA를 진행할 수 있어서 너무 많은 도움이 되었습니다. 며칠 안됐지만 팀원분들과 하루의 대부분의 시간을 함께 보내서 정말 또 하나의 가족이 생긴 기분이었습니다.

&#128155; 박지호 : 이번 기회에 처음으로 큰 데이터로 깊게 프로젝트를 진행해 보았습니다. 전처리 과정(판다스)과 EDA를 진행하고 인사이트를 뽑는 과정에서 재미를 느끼고 많이 배우게 된 뜻깊은 시간이 되었습니다. 조원들 덕분에 많이 배우고 데이터 이해에 대한 시각도 넓어졌습니다. 프로젝트를 재미있게 진행할 수 있었던 가장 큰 이유는 바로 커뮤니케이션 능력이 다들 너무 좋았다는 점입니다. 커뮤니케이션 능력이 중요하다는 점 역시 몸소 느끼게 되었습니다. 우리조 커뮤니케이션 능력 최고 !!

&#128156; 이민선 : 단순히 시각화를 위한 EDA에 그치지 않고 인사이트를 얻기 위한 EDA를 진행했어서 정말 많이 배웠습니다. 팀원분들과 의견을 나누면서 몰랐던 부분들을 알게 되었고 그 과정이 즐거웠습니다. EDA에서 그치는 게 아쉽지만 저희조는 그 이후의 계획이 있어 더 기대됩니다.
