import sys
from src.logger import logging

def error_message_detail(error, error_detail: sys):
    try:
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown"
        line_no = exc_tb.tb_lineno if exc_tb else "Unknown"
        error_message = f"Error occurred in script [{file_name}] at line [{line_no}]: {str(error)}"
        return error_message
    except Exception as e:
        return f"Failed to extract error details: {str(e)}"


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        self.error_message = error_message_detail(error_message, error_detail)
        logging.error(self.error_message)  # Log it when exception is created
        super().__init__(self.error_message)

    def __str__(self):
        return self.error_message
