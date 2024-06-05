import os

from dotenv import load_dotenv
from rl_test_common import Config
from rl_test_storage_handlers.file.params.file_data import FileData
from rl_test_storage_handlers.file.params.file_destination import \
    FileDestination
from rl_test_storage_handlers.file.text_file_handler import TextFileHandler
from rl_test_task_3.data_parsers.input_data_parser import InputDataParser

load_dotenv()


class Client:
    __config: Config = Config(os.getenv('CONFIG_FILE_PATH'))

    __text_file_handler: TextFileHandler = TextFileHandler()

    __input_data_parser: InputDataParser = InputDataParser()

    def client_code(self):
        input_file_content: FileData = self.__text_file_handler.read(
            FileDestination(self.__config.task_3_input_file_name))

        parsed_data: dict[int, str] = self.__input_data_parser.get_parsed_data(
            input_file_content.get())

        lexicographically_sorted_characters: dict[int, str] = {}

        for key, value in parsed_data.items():
            lexicographically_sorted_characters[key] = ''.join(sorted(value))

        sorted_dict: dict[int, str] = dict(
            sorted(lexicographically_sorted_characters.items(), key=lambda item: item[1]))

        result: dict[int, str] = {}

        for key in sorted_dict:
            result[key] = parsed_data[key]

        print(result)
