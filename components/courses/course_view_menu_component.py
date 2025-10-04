import re
import allure
from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.button import Button


class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.edit_button = Button(page, 'course-view-edit-menu-item', 'Edit')
        self.delete_button = Button(page, 'course-view-delete-menu-item', 'Delete')
        self.menu_button = Button(page, 'course-view-menu-button', 'Menu')

    @allure.step('Open course menu at index "{index}" and click edit')
    def click_edit(self, index: int):
        self.menu_button.click(nth=index)

        self.edit_button.check_visible(nth=index)
        self.edit_button.click(nth=index)
        self.check_current_url(re.compile('.*/#/courses/.*'))

    @allure.step('Open course menu at index "{index}" and click delete')
    def click_delete(self, index: int):
        self.menu_button.click(nth=index)

        self.delete_button.check_visible(nth=index)
        self.delete_button.click(nth=index)
