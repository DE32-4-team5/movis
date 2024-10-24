from datetime import datetime, timedelta
from textwrap import dedent
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import (
        PythonOperator,
        PythonVirtualenvOperator,
        BranchPythonOperator,
)
import pandas as pd
import requests

with DAG(
	'Transfer_Location',
	default_args={
		'depends_on_past': False,
		'retries': 0,
		'retry_delay': timedelta(minutes=3),
		'execution_timeout': timedelta(hours=2),
		},

		max_active_runs=1,
		max_active_tasks=3,
		description='Transform moviedata to address using API',
		schedule_interval="@yearly",
		start_date=datetime(2016, 1, 1),
		catchup=True,
		tags=['API','movie','transform'],
		) as dag:


#Pair Programming
#TODO first

# 1. API 요청하여 movielist 받아오기
# 1-1. 받아올 데이터는 1년을 기준으로 진행 16년 1월 1일에 시작해서 15년 데이터를 가져옴
# 2. 가져온 데이터는
# (1) movieCd
# (2) movieNm
# (3) movieNmEn
# (4) openDt
# (5) repGenreNm
# (6) repNationNm
# (7) peopleNm
# 으로 잘라내어서 저장

# 3. mariaDB 접속포트 전달받기 // 6033
# 4. 받아낸 df를 포트에 접속해서 집어넣기

def requestData():
# API 요청하여 df를 받기
# 기본 요청 URL : http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.xml (또는 .json)
# key	문자열(필수)	발급받은키 값을 입력합니다.
# openStartDt	문자열	YYYY형식의 조회시작 개봉연도를 입력합니다.
# openEndDt	문자열	YYYY형식의 조회종료 개봉연도를 입력합니다.

# key
# url = http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?=
	key = "c724c27ff6d4e73af853bd2afefb0401"
	openStartDt = "{{ ds_nodash[:4] }}"
	openEndDt = "{{ ds_nodash[:4] }}"

	url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json"
	params = {
		"key": key,
		"openStartDt": openStartDt,
		"openEndDt": openEndDt
	}

	response = requests.get(url, params=params)

    if response.status_code == 200:
        result = response.json()
        pg = (result["movieListResult"]["totCnt"] // 10) + 1
        for i in range(1,pg+1):
            params["curPage"] = i
            res = requests.get(url, params=params)
            result_pg = res.json()
            real_result = result_pg['movieListResult']['movieList']
            all_data.extend(real_result)
        return all_data

	else:
		print("Request Failed : ", response.status.code)
def jsontodf(): # json파일 데이터프레임으로 변경
    data = requestData()
    df = pd.DataFrame(data)
    df2 = df[['movieCd', 'movieNm', 'movieNmEn', 'openDt', 'repGenreNm', 'repNationNm', 'directors']] # 원하는 열 추출
    df2["directors"] = df2["directors"].apply(lambda x: x[0]['peopleNm']) # 감독명 열 변환

    return df2
