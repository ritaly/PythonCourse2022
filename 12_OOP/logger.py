# class Logger:
#     def __init__(self, log):
#         self.log = log
#
#     def show_log(self):
#         print(self.value())
#
# class WarningLog:
#     def value(self):
#         return 'Ostrzeżenie z systemu'
#
# class ErrorLog:
#     def value(self):
#         return 'Uwaga błąd z systemu'
#
# class InfoLog:
#     def value(self):
#         return 'Informacja z systemu'
#
#
# def main():
#     error = ErrorLog()
#     log = Logger(error)
#     log.show_log()
#
#
# if __name__ == '__main__':
#     main()
#
