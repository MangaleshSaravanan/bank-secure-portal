from mysql.connector import connect
from config import *
from security import encryptPwd,retrivePwd
from random import randint
def database():
    try:
        my_con=connect(host=HOST,user=USER,passwd=PASSWORD,port=PORT)
        my_cur=my_con.cursor()
        my_cur.execute("CREATE DATABASE IF NOT EXISTS __bop__")
        my_cur.execute("USE __bop__")
        admin_col = """
            adminId VARCHAR(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin PRIMARY KEY, 
            adminName VARCHAR(50),
            adminPwd VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL, 
            adminDOB DATETIME, 
            adminDOJ DATETIME
        """
        my_cur.execute(
            f"CREATE TABLE IF NOT EXISTS admin_details({admin_col}) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4"
        )

        cust_col = """
            `Account Number` VARCHAR(20) PRIMARY KEY,
            `First Name` VARCHAR(50) NOT NULL,
            `Last Name` VARCHAR(50) NOT NULL,
            `DOB` DATE,
            `Gender` VARCHAR(20),
            `e-mail` VARCHAR(100) UNIQUE,
            `Phone Number` VARCHAR(15),
            `PAN Number` VARCHAR(20) UNIQUE,
            `Identity Type` VARCHAR(30),
            `Identity Number` VARCHAR(50),
            `Address Line 1` VARCHAR(100),
            `Address Line 2` VARCHAR(100),
            `Address Line 3` VARCHAR(100),
            `District` VARCHAR(50),
            `State` VARCHAR(50),
            `Occupation` VARCHAR(50),
            `Password` VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL
        """

        my_cur.execute(
            f"CREATE TABLE IF NOT EXISTS customer_details ({cust_col}) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4"
        )        
    except Exception as e:
        print(e)


    bank_tables = {
        "admins": [
            "admin_id",
            "username",
            "password_hash",
            "full_name",
            "email",
            "role",
            "last_login"
        ],

        "transactions": [
            "transaction_id",
            "account_no",
            "transaction_type",
            "amount",
            "receiver_account",
            "balance_after",
            "description",
            "transaction_time",
            "admin_id"
        ],

        "audit_logs": [
            "log_id",
            "admin_id",
            "action",
            "table_name",
            "record_id",
            "action_time"
        ]
    }
try:
    my_con=connect(host=HOST,user=USER,passwd=PASSWORD,port=PORT,database="__bop__")
    my_cur=my_con.cursor()
except Exception:
    database()
def check_table(level,uid,upwd):
    global my_con,my_cur
    my_con=connect(host=HOST,user=USER,passwd=PASSWORD,database="__bop__",port=PORT)
    my_cur=my_con.cursor()
    table_name = f"{level}_details"
    id_col = f"{level}Id"
    pwd_col = f"{level}Pwd"
    try:
        query = f"SELECT * FROM {table_name} WHERE {id_col} = %s AND {pwd_col} = %s"
        my_cur.execute(query, (uid, upwd))
        result = my_cur.fetchone()
        my_cur.close()
        my_con.close()
    except Exception:
        return False
    
    if result:
        return True, level
    return False

def createAccountNumber(cursor):
    while True:
        acn = str(randint(10**15, (10**16) - 1))
        query = "SELECT 1 FROM customer_details WHERE `Account Number` = %s"
        cursor.execute(query, (acn,))
        if cursor.fetchone() is None:
            return acn
            
def storeCustomer(details):
    details["DOB"] = "-".join(details["DOB"].split("-")[::-1])
    values = list(details.values())
    with connect(host=HOST, user=USER, passwd=PASSWORD, database="__bop__", port=PORT) as conn:
        with conn.cursor() as cursor:
            acn = createAccountNumber(cursor)
            values.insert(0, acn)
            values.append(encryptPwd(values[-1]))
            values.pop(-2)
            placeholders = ", ".join(["%s"] * len(values))
            
            cursor.execute(f"INSERT INTO customer_details VALUES ({placeholders})", values)
            conn.commit()
            return acn

def searchCustomer(acn):
    with connect(host=HOST, user=USER, passwd=PASSWORD, database="__bop__", port=PORT) as conn:
        with conn.cursor() as cursor:
            if acn:
                query = f"SELECT * FROM customer_details WHERE `Account Number`=%s"%(acn,)
            else:
                query = f"SELECT * FROM customer_details"
            cursor.execute(query)
            records=cursor.fetchall()
            ret_records=[]
            for i in records:
                i=i[:-1]
                ret_records.append(i)
            return ret_records
                
            

    
if __name__=="__main__":
    database()
