from playwright.sync_api import Page
from components.navigation.navbar_component import NavBarComponent
from components.navigation.sidebar_component import SideBarComponent
from components.charts.chart_view_component import ChartViewComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.chart_students = ChartViewComponent(page, 'students', 'bar')
        self.chart_courses = ChartViewComponent(page, 'courses', 'pie')
        self.chart_activities = ChartViewComponent(page, 'activities', 'line')
        self.chart_scores = ChartViewComponent(page, 'scores', 'scatter')
        self.toolbar = DashboardToolbarViewComponent(page)
        self.navbar = NavBarComponent(page)
        self.sidebar = SideBarComponent(page)

    def check_chart_students_visible(self):
        self.chart_students.check_visible('Students')

    def check_chart_courses_visible(self):
        self.chart_courses.check_visible('Courses')

    def check_chart_activities_visible(self):
        self.chart_activities.check_visible('Activities')

    def check_chart_scores_visible(self):
        self.chart_scores.check_visible('Scores')
