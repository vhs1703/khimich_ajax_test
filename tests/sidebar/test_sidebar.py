import pytest
from contextlib import nullcontext as does_not_raise
from utils.logger_utils import get_logger


logger = get_logger()

def test_sidebar_elements(main_page_fixture):
    logger.info('Starting Test If all sidebar elements are')
    assert main_page_fixture.is_sidebar_elements() == 4

def test_sidebar_button(main_page_fixture):
    logger.info('Starting Test If sidebar button is')
    assert main_page_fixture.is_sidebar_button() == 1

def test_elements_clickable(main_page_fixture):
    logger.info('Starting Test If all sidebar elements are clickable')
    assert main_page_fixture.is_sidebar_elements_clickable() == [(True,True),(True,True),(True,True),(True,True)]

def test_button_clickable(main_page_fixture):
    logger.info('Starting Test If sidebar button is clickable')
    assert main_page_fixture.is_sidebar_button_clickable() == (True,True)

    
