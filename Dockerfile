# Python 3.11-slim을 기반 이미지로 사용
FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /app

# git 설치
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Git 저장소에서 프로젝트 코드 복제
RUN git clone https://github.com/chan2slo/newsfeeder_bot.git .

# Python 의존성 설치
RUN pip install -r requirements.txt

# 텔레그램 봇 스크립트 실행
CMD ["python", "./newsfeeder_bot.py"]