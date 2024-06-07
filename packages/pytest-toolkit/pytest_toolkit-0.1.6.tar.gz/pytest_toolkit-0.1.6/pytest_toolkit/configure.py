import logging

from gitignore_parser import parse_gitignore

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


try:
    matches = parse_gitignore(".testignore")
except:
    logger.warning(
        """
                   
    Файл .testignore не найден
    Пример:
                   
    .venv/
    __pycache__/
    .pytest_cache/
    example/
                
    """
    )
    matches = lambda _: False
