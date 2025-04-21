import pandas as pd
from sqlalchemy import create_engine

# 1. 불러올 CSV 파일명
csv_file = '링커리어_개발공고_상세'  # ← 너가 만든 파일명으로 바꿔줘

# 2. MySQL 연결 정보
# 형식: 'mysql+pymysql://사용자이름:비밀번호@호스트/DB이름'
engine = create_engine('mysql+pymysql://park:0120@127.0.0.1/work24db')

# 3. CSV 불러오기
try:
    df = pd.read_csv(csv_file)
    print(f"📄 CSV 불러오기 완료: {csv_file}")
except Exception as e:
    print("❌ CSV 파일을 불러오는 중 오류:", e)
    exit()

# 4. 데이터 저장 (jobs 테이블에 append)
try:
    df.to_sql(name='jobs', con=engine, if_exists='append', index=False)
    print("✅ CSV 데이터가 MySQL DB에 저장되었습니다.")
except Exception as e:
    print("❌ DB 저장 중 오류:", e)
