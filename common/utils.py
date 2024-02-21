import logging
import traceback


logger = logging.getLogger(__name__)


def capture_exception(e):
    formatted_error = {
        "reason": str(e),
        "traceback": traceback.format_exc(),
    }

    logger.error(formatted_error)  # Log the error

    return formatted_error


def send_handled(e):
    logger.error(msg=f"{e} {traceback.format_exc()}", exc_info=False)


class ErrorFormat:
    @staticmethod
    def get_formated(errors):
        try:
            result = {}
            for field, error in errors.items():
                result[field] = error[0]
            return result
        except Exception as e:
            capture_exception(e)
            return errors

    @staticmethod
    def get_integrity_error_field(error_tuple):
        try:
            error_tuple = str(error_tuple)
            return f'{error_tuple.split("DETAIL")[1]}'
        except IndexError:
            return error_tuple
