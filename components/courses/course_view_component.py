from playwright.sync_api import Page
from components.base_component import BaseComponent
from components.courses.course_view_menu_component import CourseViewMenuComponent
from elements.text import Text
from elements.image import Image
import allure


class CourseViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu = CourseViewMenuComponent(page)

        self.course_title = Text(page, 'course-widget-title-text', 'Title')
        self.course_image = Image(page, 'course-preview-image', 'Preview')
        self.course_max_score_text = Text(page, 'course-max-score-info-row-view-text', 'Max Score')
        self.course_min_score_text = Text(page, 'course-min-score-info-row-view-text', 'Min Score')
        self.course_estimated_time_text = Text(
            page, 'course-estimated-time-info-row-view-text', 'Estimated Time')

    @allure.step('Check visible course view at index "{index}"')
    def check_visible(self, index: int, title: str, max_score: str, min_score: str, estimated_time: str):
        self.course_image.check_visible(nth=index)

        self.course_title.check_visible(nth=index)
        self.course_title.check_have_text(text=title, nth=index)

        self.course_max_score_text.check_visible(nth=index)
        self.course_max_score_text.check_have_text(text=f"Max score: {max_score}", nth=index)

        self.course_min_score_text.check_visible(nth=index)
        self.course_min_score_text.check_have_text(text=f"Min score: {min_score}", nth=index)

        self.course_estimated_time_text.check_visible(nth=index)
        self.course_estimated_time_text.check_have_text(text=f"Estimated time: {estimated_time}", nth=index)
