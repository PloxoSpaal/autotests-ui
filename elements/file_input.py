from elements.base_element import BaseElement
import allure
from tools.logger import get_logger


logger = get_logger('FILE INPUT')


class FileInput(BaseElement):
    @property
    def type_of(self) -> str:
        return "file input"

    def set_input_files(self, file: str, nth: int = 0, **kwargs):
        step = f'Set file "{file}" to the {self.type_of} "{self.name}"'
        with allure.step(step):
            logger.info(step)
            locator = self.get_locator(nth, **kwargs)
            locator.set_input_files(file)

    def clean_input_files(self, nth: int = 0, **kwargs):
        step = f'Clear file from {self.type_of} "{self.name}"'
        with allure.step(step):
            logger.info(step)
            locator = self.get_locator(nth, **kwargs)
            locator.clear()