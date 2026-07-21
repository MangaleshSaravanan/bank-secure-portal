from secrets import token_hex
from database import check_table
def login(level,userid,pwd):
        exist=check_table(level,userid,pwd)
        if exist and level=='admin':
            return 'adm-'+token_hex(16)+''
        elif exist and level=='customer':
            return 'cus-'+token_hex(16)+''
        return False

def verify_token(token):
     pass