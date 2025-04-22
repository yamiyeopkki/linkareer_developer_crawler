from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def crawl_linkareer_development_activities(max_page=7):
    results = []
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)

    for page in range(1, max_page + 1):
        url = f"https://linkareer.com/list/activity?filterBy_q=%EA%B0%9C%EB%B0%9C&filterType=CATEGORY&orderBy_direction=DESC&orderBy_field=CREATED_AT&page={page}"
        driver.get(url)

        # "활동 카드" 들이 로드될 때까지 최대 15초 기다림
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.image-link")))
        cards = driver.find_elements(By.CSS_SELECTOR, "a.image-link")

        for card in cards:
            try:
                title_elem = card.find_element(By.XPATH, ".//img[@alt]")
                title = title_elem.get_attribute("alt").strip()
                detail_url = "https://linkareer.com" + card.get_attribute("href")

                # 결과 저장 (host, period는 추출 안 되는 경우 빈값 처리)
                results.append({
                    "활동명": title,
                    "주최기관": "",
                    "모집기간": "",
                    "상세페이지": detail_url
                })

            except Exception as e:
                print(f"Error parsing card: {e}")

    driver.quit()
    return results

if __name__ == "__main__":
    data = crawl_linkareer_development_activities(max_page=7)
    df = pd.DataFrame(data)
    print(df)
    df.to_csv("링커리어_개발_활동_크롤링.csv", encoding="utf-8-sig", index=False)
