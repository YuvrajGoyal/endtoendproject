import sys

def error_message_details(error, error_detail:sys):
    _,_,err_tb=error_detail.exc_info()
    file_name=err_tb.tb_frame.f_code.co_filename
    line_number=err_tb.tb_lineno
    error_message="Error ocurred in python code, file_name [{0}], line number [{1}], error message [{2}]",format(
        file_name,line_number,error_message
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail:str):
        super.__init__(error_message)
        self.error_message=error_message_details(error_message, error_detail=error_detail)
        

