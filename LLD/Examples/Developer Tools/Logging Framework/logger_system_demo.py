from logger_system import LoggerSystem
from log_appender import ConsoleAppender, FileAppender
from log_formatter import TextFormatter, JSONFormatter

class LoggerSystemDemo:
    @staticmethod
    def main():
        logger = LoggerSystem()
        text_formatter = TextFormatter()
        json_formatter = JSONFormatter()

        logger.set_log_formatter(json_formatter)

        # add appenders
        console_appender = ConsoleAppender(json_formatter)
        file_appender = FileAppender(json_formatter, file_name="data.txt")

        logger.add_log_appenders(console_appender)
        logger.add_log_appenders(file_appender)

        # logs
        logger.info("This is info.")
        logger.warn("This is warning!!")
        logger.error("This is error!!!")

if __name__ == "__main__":
    LoggerSystemDemo.main()