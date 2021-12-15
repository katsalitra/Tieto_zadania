# zrobiłam te testy tak jak było w poleceniu - tylko w selenium bez uzycia frameworków do testów np pytesta


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

se = Service(executable_path='./chromedriver')
driver = webdriver.Chrome(service=se)

validUserName = '1anna1_zi@wp.pl'
validUserPassword = "Jamnik123!"
invalidUserName = 'xxxxx@wp.pl'
invalidUserPassword = "Jajko123!"
emptyUserName= ""
emptyUserPassword=""
expectedErrorMessage = 'Podany login i/lub hasło są nieprawidłowe.'


def logIn_with_valid_credentials(validUserName, validUserPassword):
    driver.get('https://poczta.wp.pl')
    try:
        assert 'Poczta - Najlepsza Poczta, największe załączniki - WP' in driver.title
    except Exception as e:
        print(r"This isn't proper site, go to: https://poczta.wp.pl")
        return 'FAIL'
    else:
        driver.find_element(By.ID, 'login').send_keys(validUserName)
        driver.find_element(By.ID, 'password').send_keys(validUserPassword)
        driver.find_element(By.CSS_SELECTOR, "button[class='sc-bdvvtL sc-gsDKAQ styled__SubmitButton-sc-1bs2nwv-2 ekJwFE hIxhWw jyhBDA']").click()
        if driver.find_element(By.XPATH, '//*[@id="folder-1"]/div[2]'):
            driver.quit()
            return 'PASS'
        else:
            return 'FAIL'
# print(logIn_with_valid_credentials(validUserName, validUserPassword))


def logIn_with_invalid_username(invalidUserName,validUserPassword):
    driver.get('https://poczta.wp.pl')
    try:
        assert 'Poczta - Najlepsza Poczta, największe załączniki - WP' in driver.title
    except Exception as e:
        print(r"This isn't proper site, go to: https://poczta.wp.pl")
        return 'FAIL'
    else:
        driver.find_element(By.ID, 'login').send_keys(invalidUserName)
        driver.find_element(By.ID, 'password').send_keys(validUserPassword)
        driver.find_element(By.CSS_SELECTOR, "button[class='sc-bdvvtL sc-gsDKAQ styled__SubmitButton-sc-1bs2nwv-2 ekJwFE hIxhWw jyhBDA']").click()
        if driver.find_element(By.XPATH,'//*[@id="stgMain"]/div/div/div[1]/form/div[3]/span').text == expectedErrorMessage:
            driver.quit()
            return 'PASS'
        else:
            return 'FAIL'
# print(logIn_with_invalid_username(invalidUserName, validUserPassword))


def logIn_with_invalid_password(validUserName,invalidUserPassword):
    driver.get('https://poczta.wp.pl')
    try:
        assert 'Poczta - Najlepsza Poczta, największe załączniki - WP' in driver.title
    except Exception as e:
        print(r"This isn't proper site, go to: https://poczta.wp.pl")
        return 'FAIL'
    else:
        driver.find_element(By.ID, 'login').send_keys(validUserName)
        driver.find_element(By.ID, 'password').send_keys(invalidUserPassword)
        driver.find_element(By.CSS_SELECTOR, "button[class='sc-bdvvtL sc-gsDKAQ styled__SubmitButton-sc-1bs2nwv-2 ekJwFE hIxhWw jyhBDA']").click()
        if driver.find_element(By.XPATH,'//*[@id="stgMain"]/div/div/div[1]/form/div[3]/span').text == expectedErrorMessage:
            driver.quit()
            return 'PASS'
        else:
            return 'FAIL'
# print(logIn_with_invalid_password(validUserName,invalidUserPassword))


def logIn_with_invalid_both_credentials(invalidUserName,invalidUserPassword):
    driver.get('https://poczta.wp.pl')
    try:
        assert 'Poczta - Najlepsza Poczta, największe załączniki - WP' in driver.title
    except Exception as e:
        print(r"This isn't proper site, go to: https://poczta.wp.pl")
        return 'FAIL'
    else:
        driver.find_element(By.ID, 'login').send_keys(invalidUserName)
        driver.find_element(By.ID, 'password').send_keys(invalidUserPassword)
        driver.find_element(By.CSS_SELECTOR, "button[class='sc-bdvvtL sc-gsDKAQ styled__SubmitButton-sc-1bs2nwv-2 ekJwFE hIxhWw jyhBDA']").click()
        if driver.find_element(By.XPATH,'//*[@id="stgMain"]/div/div/div[1]/form/div[3]/span').text == expectedErrorMessage:
            driver.quit()
            return 'PASS'
        else:
            return 'FAIL'
# print(logIn_with_invalid_both_credentials(invalidUserName,invalidUserPassword))


def logIn_with_empty_username_field(emptyUserName,validUserPassword):
    driver.get('https://poczta.wp.pl')
    try:
        assert 'Poczta - Najlepsza Poczta, największe załączniki - WP' in driver.title
    except Exception as e:
        print(r"This isn't proper site, go to: https://poczta.wp.pl")
        return 'FAIL'
    else:
        driver.find_element(By.ID, 'login').send_keys(emptyUserName)
        driver.find_element(By.ID, 'password').send_keys(validUserPassword)
        driver.find_element(By.CSS_SELECTOR, "button[class='sc-bdvvtL sc-gsDKAQ styled__SubmitButton-sc-1bs2nwv-2 ekJwFE hIxhWw jyhBDA']").click()
        try:
            assert 'Poczta - Najlepsza Poczta, największe załączniki - WP' in driver.title
            driver.quit()
            return 'PASS'
        except Exception as e:
            print(r"This isn't proper site, go to: https://poczta.wp.pl")
            return 'FAIL'
# print(logIn_with_empty_username_field(emptyUserName,validUserPassword))



def logIn_with_empty_password_field(validUserName,emptyUserPassword):
    driver.get('https://poczta.wp.pl')
    try:
        assert 'Poczta - Najlepsza Poczta, największe załączniki - WP' in driver.title
    except Exception as e:
        print(r"This isn't proper site, go to: https://poczta.wp.pl")
        return 'FAIL'
    else:
        driver.find_element(By.ID, 'login').send_keys(validUserName)
        driver.find_element(By.ID, 'password').send_keys(emptyUserPassword)
        driver.find_element(By.CSS_SELECTOR, "button[class='sc-bdvvtL sc-gsDKAQ styled__SubmitButton-sc-1bs2nwv-2 ekJwFE hIxhWw jyhBDA']").click()
        try:
            assert 'Poczta - Najlepsza Poczta, największe załączniki - WP' in driver.title
            driver.quit()
            return 'PASS'
        except Exception as e:
            print(r"This isn't proper site, go to: https://poczta.wp.pl")
            return 'FAIL'
# print(logIn_with_empty_password_field(validUserPassword,emptyUserPassword))



def logIn_with_both_credentials_empty(emptyUserName,emptyUserPassword):
    driver.get('https://poczta.wp.pl')
    try:
        assert 'Poczta - Najlepsza Poczta, największe załączniki - WP' in driver.title
    except Exception as e:
        print(r"This isn't proper site, go to: https://poczta.wp.pl")
        return 'FAIL'
    else:
        driver.find_element(By.ID, 'login').send_keys(emptyUserName)
        driver.find_element(By.ID, 'password').send_keys(emptyUserPassword)
        driver.find_element(By.CSS_SELECTOR, "button[class='sc-bdvvtL sc-gsDKAQ styled__SubmitButton-sc-1bs2nwv-2 ekJwFE hIxhWw jyhBDA']").click()
        try:
            assert 'Poczta - Najlepsza Poczta, największe załączniki - WP' in driver.title
            driver.quit()
            return 'PASS'
        except Exception as e:
            print(r"This isn't proper site, go to: https://poczta.wp.pl")
            return 'FAIL'

# print(logIn_with_both_credentials_empty(emptyUserName,emptyUserPassword))


def logIn_with_valid_UpperCase_username(validUserName, validUserPassword):
    driver.get('https://poczta.wp.pl')
    try:
        assert 'Poczta - Najlepsza Poczta, największe załączniki - WP' in driver.title
    except Exception as e:
        print(r"This isn't proper site, go to: https://poczta.wp.pl")
        return 'FAIL'
    else:
        driver.find_element(By.ID, 'login').send_keys(validUserName.upper())
        driver.find_element(By.ID, 'password').send_keys(validUserPassword)
        driver.find_element(By.CSS_SELECTOR, "button[class='sc-bdvvtL sc-gsDKAQ styled__SubmitButton-sc-1bs2nwv-2 ekJwFE hIxhWw jyhBDA']").click()
        if driver.find_element(By.XPATH, '//*[@id="folder-1"]/div[2]'):
            driver.quit()
            return 'PASS'
        else:
            return 'FAIL'
# print(logIn_with_valid_UpperCase_username(validUserName, validUserPassword))




def logIn_with_valid_UpperCase_password(validUserName, validUserPassword):
    driver.get('https://poczta.wp.pl')
    try:
        assert 'Poczta - Najlepsza Poczta, największe załączniki - WP' in driver.title
    except Exception as e:
        print(r"This isn't proper site, go to: https://poczta.wp.pl")
        return 'FAIL'
    else:
        driver.find_element(By.ID, 'login').send_keys(validUserName)
        driver.find_element(By.ID, 'password').send_keys(validUserPassword.upper())
        driver.find_element(By.CSS_SELECTOR, "button[class='sc-bdvvtL sc-gsDKAQ styled__SubmitButton-sc-1bs2nwv-2 ekJwFE hIxhWw jyhBDA']").click()
        if driver.find_element(By.XPATH,'//*[@id="stgMain"]/div/div/div[1]/form/div[3]/span').text == expectedErrorMessage:
            driver.quit()
            return 'PASS'
        else:
            return 'FAIL'
# print(logIn_with_valid_UpperCase_password(validUserName, validUserPassword))






