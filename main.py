from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

df = pd.read_excel('./docs/data.xlsx')
out_df = pd.DataFrame(columns=['id', 'industry', 'about'])
s = Service(ChromeDriverManager().install())
#driver = webdriver.Chrome('./drivers/chromedriver')
driver = webdriver.Chrome(service=s)
for index, row in df.iterrows():
    item_id = str(row.iloc[0])
    try:
        url = "https://www.reuters.com/companies/" + item_id + ".T"
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".TextLabel__text-label___3oCVw.TextLabel__black___2FN-Z.TextLabel__serif___3lOpX.Profile-body-2Aarn")))
        about = driver.find_element(By.CSS_SELECTOR, ".TextLabel__text-label___3oCVw.TextLabel__black___2FN-Z.TextLabel__serif___3lOpX.Profile-body-2Aarn").text
        industry = driver.find_element(By.CSS_SELECTOR, ".About-section-3ooPI.industry .TextLabel__text-label___3oCVw.TextLabel__black___2FN-Z.TextLabel__regular___2X0ym.About-value-3oDGk:nth-child(2)").text
    except:
        about = "err"
        industry = "err"
    df2 = pd.DataFrame({"id": [item_id], "industry": [industry], "about": [about]})
    out_df = out_df.append(df2)
    print(df2)
driver.close()
out_df.to_excel('./docs/output_2.xlsx')
