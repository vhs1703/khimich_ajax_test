import pytest
from contextlib import nullcontext as does_not_raise
from utils.logger_utils import get_logger


logger = get_logger()


@pytest.mark.parametrize("login,password,expected_result,exprectation",[
    ('test@gmail.com','testpass123',False,does_not_raise()),
    ('qa.ajax.app.automation@gmail.com','qa_automation_password',True,does_not_raise()),
    (1234,1.0,False,pytest.raises(TypeError)), # Перевірка на типи даних
    ('test@gmail.com','asdfghjk',False,pytest.raises(ValueError)), # Перевірка на довжину пароля >=10
    ('test@gmail.com','123123123123123',False,pytest.raises(ValueError)), # Перевірка на те що в паролі є букви
])

def test_user_login(user_login_fixture,login,password,expected_result,exprectation):
    logger.info(f'Starting test\nLogin: {login}\nPassword:{password}\nExpected Result: {expected_result}')
    with exprectation:
        result = user_login_fixture.auth(login,password)
        logger.info(f'End of test:\nResult: {result}\nExpected Result: {expected_result}')
        assert result == expected_result

