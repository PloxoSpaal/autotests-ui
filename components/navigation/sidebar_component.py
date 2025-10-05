from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component import SidebarListItemComponent
from playwright.sync_api import Page
import allure
import re
from tools.routes import AppRoute


class SideBarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.dashboard_list_item = SidebarListItemComponent(page, 'dashboard')
        self.courses_list_item = SidebarListItemComponent(page, 'courses')
        self.logout_list_item = SidebarListItemComponent(page, 'logout')

    @allure.step('Check visible sidebar')
    def check_visible(self):
        self.courses_list_item.check_visible('Courses')
        self.dashboard_list_item.check_visible('Dashboard')
        self.logout_list_item.check_visible('Logout')

    @allure.step('Click dashboard on sidebar')
    def click_dashboard(self):
        self.dashboard_list_item.navigate(re.compile(AppRoute.DASHBOARD))

    @allure.step('Click courses on sidebar')
    def click_courses(self):
        self.courses_list_item.navigate(re.compile(AppRoute.COURSES))

    @allure.step('Click logout on sidebar')
    def click_logout(self):
        self.logout_list_item.navigate(re.compile(AppRoute.LOGIN))
