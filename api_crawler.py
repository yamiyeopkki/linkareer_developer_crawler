import requests
import pandas as pd

results = []

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
}

for page in range(1, 8):
    url = f"https://linkareer.com/api/activities?filterBy_q=개발&filterType=CATEGORY&orderBy_direction=DESC&orderBy_field=CREATED_AT&page={page}"
    print(f"{page}페이지 요청 중...")
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json().get("data", [])
        for item in data:
            results.append({
                "제목": item.get("title", "없음"),
                "링크": f"https://linkareer.com/detail/{item.get('id')}",
                "기관명": item.get("company_name", "없음"),
                "모집기간": item.get("date_display", "없음"),
                "혜택": item.get("benefit", "없음"),
            })
    else:
        print(f"{page}페이지 에러: {response.status_code}")

df = pd.DataFrame(results)
df.to_csv("링커리어_API_크롤링.csv", index=False, encoding="utf-8-sig")
print("✅ API 크롤링 완료! CSV 저장됨.")