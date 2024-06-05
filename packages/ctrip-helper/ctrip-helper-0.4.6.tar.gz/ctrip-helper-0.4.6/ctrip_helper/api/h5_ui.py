# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  ctrip-helper
# FileName:     h5_ui.py
# Description:  TODO
# Author:       mfkifhss2023
# CreateDate:   2024/06/04
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
import time
from enum import Enum
from selenium import webdriver
from ctrip_helper.config import url_map
from ctrip_helper.utils import get_chinese_pinyin_first_letter
from ctrip_helper.libs import get_element, logger, scroll_element, click, scroll_calendar_container


class UILocatorRegx(Enum):
    airline_alias = {"locator": "xpath",
                     "regx": '//div[@id="navigation-box"]//div[contains(@class, "ListTitle_title")]'}
    airline_departure_city = {"locator": "xpath",
                              "regx": '//div[contains(@class, "CityDate_search-city-date-container")]' +
                                      '//div[@data-testid="u_departure-city"]'}
    airline_city_pinyin_first_letter = {"locator": "xpath",
                                        "regx": '//div[@class="m-indexes__menu"]//div[@id="{}"]'}
    airline_city_input = {"locator": "xpath",
                          "regx": '//div[@class="city-picker"]//div[@class="city-item"]//div[contains(text(), "{}")]'}
    airline_arrival_city = {"locator": "xpath",
                            "regx": '//div[contains(@class, "CityDate_search-city-date-container")]' +
                                    '//div[@data-testid="u_arrival-city"]'}
    airline_arrival_city_input = {"locator": "xpath",
                                  "regx": '//div[contains(@class, "CityDate_search-city-date-container")]' +
                                          '//div[@data-testid="u_arrival-city"]'}
    airline_departure_date = {"locator": "xpath",
                              "regx": '//div[contains(@class, "CityDate_search-city-date-container")]' +
                                      '//div[@data-testid="u_departure_date"]'}
    container_header = {"locator": "xpath", "regx": '//div[@class="list-head"]'}
    calendar_wrap_container = {"locator": "xpath", "regx": '//div[@class="calendar-wrap"]'}
    month_wrap_container = {"locator": "xpath",
                            "regx": '//div[@class="calendar-wrap"]//div[@id="label-{}"]'}
    airline_departure_date_input = {"locator": "xpath",
                                    "regx": '//div[@class="calendar-wrap"]//div[@data-testid="date-item-{}"]'}
    airline_search_button = {"locator": "xpath",
                             "regx": '//div[contains(@class, "CityDate_search-city-date-container")]' +
                                     '//div[contains(@class, "search-btn")]'}


class SeleniumApi(object):

    @classmethod
    def open_airline_page(cls, driver: webdriver, sleep: float = 0) -> None:
        url = url_map.get('h5_flight_list')
        driver.get(url)
        if sleep > 0:
            time.sleep(sleep)
        logger.info("打开携程H5版航班列表页")

    @classmethod
    def click_airline_alias(cls, driver: webdriver, loop: int = 1, sleep: float = 0, **kwargs) -> bool:
        airline_alias_element = get_element(
            driver=driver, locator=UILocatorRegx.airline_alias.value.get("locator"),
            regx=UILocatorRegx.airline_alias.value.get("regx"), loop=loop, sleep=sleep, **kwargs
        )
        if airline_alias_element:
            is_success = click(element=airline_alias_element, loop=loop, sleep=sleep, **kwargs)
            if is_success is True:
                logger.info("点击航线别名，修改航线的起飞-抵达城市")
                return True
        return False

    @classmethod
    def click_departure_city(cls, driver: webdriver, loop: int = 1, sleep: float = 0, **kwargs) -> bool:
        departure_city_element = get_element(
            driver=driver, locator=UILocatorRegx.airline_departure_city.value.get("locator"),
            regx=UILocatorRegx.airline_departure_city.value.get("regx"), loop=loop, sleep=sleep, **kwargs
        )
        if departure_city_element:
            is_success = click(element=departure_city_element, loop=loop, sleep=sleep, **kwargs)
            if is_success is True:
                logger.info("点击起飞城市选择框")
                return True
        return False

    @classmethod
    def click_city_pinyin_first_letter(cls, driver: webdriver, chinese_city: str, loop: int = 1, sleep: float = 0,
                                       **kwargs) -> bool:
        pinyin = get_chinese_pinyin_first_letter(chinese_str=chinese_city, is_upper=True)
        regx = UILocatorRegx.airline_city_pinyin_first_letter.value.get("regx").format(pinyin[0])
        city_pinyin_first_letter_element = get_element(
            driver=driver, locator=UILocatorRegx.airline_city_pinyin_first_letter.value.get("locator"),
            regx=regx, loop=loop, sleep=sleep, **kwargs
        )
        if city_pinyin_first_letter_element:
            is_success = click(element=city_pinyin_first_letter_element, loop=loop, sleep=sleep, **kwargs)
            if is_success is True:
                logger.info("点击城市<{}>拼音首字母【{}】成功".format(chinese_city, pinyin[0]))
                return True
        return False

    @classmethod
    def select_departure_city(cls, driver: webdriver, departure_city: str, loop: int = 1, sleep: float = 0,
                              **kwargs) -> bool:
        regx = UILocatorRegx.airline_city_input.value.get("regx").format(departure_city)
        departure_city_element = get_element(
            driver=driver, locator=UILocatorRegx.airline_city_input.value.get("locator"),
            regx=regx, loop=loop, sleep=sleep, **kwargs
        )
        if departure_city_element:
            is_success = click(element=departure_city_element, loop=loop, sleep=sleep, **kwargs)
            if is_success is True:
                logger.info("点击选择起飞城市：{}".format(departure_city))
                return True
        return False

    @classmethod
    def click_arrival_city(cls, driver: webdriver, loop: int = 1, sleep: float = 0, **kwargs) -> bool:
        arrival_city_element = get_element(
            driver=driver, locator=UILocatorRegx.airline_city_input.value.get("locator"),
            regx=UILocatorRegx.airline_arrival_city.value.get("regx"), loop=loop, sleep=sleep, **kwargs
        )
        if arrival_city_element:
            is_success = click(element=arrival_city_element, loop=loop, sleep=sleep, **kwargs)
            if is_success is True:
                logger.info("点击抵达城市选择框")
                return True
        return False

    @classmethod
    def select_arrival_city(cls, driver: webdriver, arrival_city: str, loop: int = 1, sleep: float = 0,
                            **kwargs) -> bool:
        regx = UILocatorRegx.airline_city_input.value.get("regx").format(arrival_city)
        arrival_city_elment = get_element(
            driver=driver, locator=UILocatorRegx.airline_city_input.value.get("locator"),
            regx=regx, loop=loop, sleep=sleep, **kwargs
        )
        if arrival_city_elment:
            is_success = click(driver=driver, element=arrival_city_elment, loop=loop, sleep=sleep, **kwargs)
            if is_success is True:
                logger.info("点击选择抵达城市：{}".format(arrival_city))
                return True
        return False

    @classmethod
    def click_departure_date(cls, driver: webdriver, loop: int = 1, sleep: float = 0, **kwargs) -> bool:
        departure_date_element = get_element(
            driver=driver, locator=UILocatorRegx.airline_departure_date.value.get("locator"),
            regx=UILocatorRegx.airline_departure_date.value.get("regx"), loop=loop, sleep=sleep, **kwargs
        )
        if departure_date_element:
            is_success = click(driver=driver, element=departure_date_element, loop=loop, sleep=sleep, **kwargs)
            if is_success is True:
                logger.info("点击航线起飞日期选择框")
                return True
        return False

    @classmethod
    def scroll_to_calendar_date(cls, driver: webdriver, date_str: str, loop: int = 1, sleep: float = 0,
                                **kwargs) -> bool:
        container_header_regx = UILocatorRegx.container_header.value.get("regx")
        calendar_container_regx = UILocatorRegx.calendar_wrap_container.value.get("regx")
        month_container_regx = UILocatorRegx.month_wrap_container.value.get("regx").format(date_str[:7])
        container_header_element = get_element(
            driver=driver, locator=UILocatorRegx.container_header.value.get("locator"),
            regx=container_header_regx, loop=loop, sleep=sleep, **kwargs
        )
        calendar_container_element = get_element(
            driver=driver, locator=UILocatorRegx.calendar_wrap_container.value.get("locator"),
            regx=calendar_container_regx, loop=loop, sleep=sleep, **kwargs
        )
        month_container_element = get_element(
            driver=driver, locator=UILocatorRegx.month_wrap_container.value.get("locator"),
            regx=month_container_regx, loop=loop, sleep=sleep, **kwargs
        )
        if container_header_element and calendar_container_element and month_container_element:
            scroll_calendar_container(
                driver=driver, calendar=calendar_container_element, month=month_container_element,
                container_header=container_header_element
            )
            logger.info("滚动屏幕中的日历列表至{}月，使其可见".format(date_str[:7]))
            return True
        return False

    @classmethod
    def select_departure_date_with_calendar(cls, driver: webdriver, date_str: str, loop: int = 1, sleep: float = 0,
                                            **kwargs) -> bool:
        regx = UILocatorRegx.airline_departure_date_input.value.get("regx").format(date_str)
        departure_date_element = get_element(
            driver=driver, locator=UILocatorRegx.airline_departure_date.value.get("locator"),
            regx=regx, loop=loop, sleep=sleep, **kwargs
        )
        if departure_date_element:
            scroll_element(driver=driver, element=departure_date_element)
            is_success = click(driver=driver, element=departure_date_element, loop=loop, sleep=sleep, **kwargs)
            if is_success is True:
                logger.info("选择航线起飞日期：{}".format(date_str))
                return True
        return False

    @classmethod
    def click_airline_search(cls, driver: webdriver, loop: int = 1, sleep: float = 0, **kwargs) -> bool:
        search_button = get_element(
            driver=driver, locator=UILocatorRegx.airline_search_button.value.get("locator"),
            regx=UILocatorRegx.airline_search_button.value.get("regx"), loop=loop, sleep=sleep, **kwargs
        )
        if search_button:
            is_success = click(driver=driver, element=search_button, loop=loop, sleep=sleep, **kwargs)
            if is_success is True:
                logger.info("点击航线查询页的搜索")
                return True
        return False
