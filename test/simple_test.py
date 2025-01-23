from selenium import webdriver
from pages.Authpage import AuthPage
from conftest import browser 
from pages.MainPage import MainPage


def test_auth(browser):	
    email = "lapushkagg8@gmail.com"
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, "jdKZxUV4mFC6i*/")

    auth_page = MainPage(browser)
    main_page = MainPage(browser)
    main_page.open_menu()

    info = main_page.get_account_info()

 # Проверяем, что после запуска теста URL заканчивается заданной подстрокой:
    assert auth_page.get_current_url().endswith("/user09558367/boards")
    assert info[0] == "Елизавета Сигарева"
    assert info[1] == email