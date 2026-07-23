from mysql.connector import connect
from config import *

def check_table(level,uid,upwd):
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
        customerId VARCHAR(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin PRIMARY KEY, 
        customerName VARCHAR(50),
        customerPwd VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL, 
        customerDOB DATETIME
    """
    my_cur.execute(
        f"CREATE TABLE IF NOT EXISTS customer_details({cust_col}) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4"
    )

    trans_col = """
        transactionId VARCHAR(30) PRIMARY KEY, 
        customerId VARCHAR(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
        amount DECIMAL(15, 2),
        transactionType VARCHAR(20),
        transactionDate DATETIME
    """
    my_cur.execute(
        f"CREATE TABLE IF NOT EXISTS transaction_details({trans_col}) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4"
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

    "customers": [
        "customer_id",
        "first_name",
        "last_name",
        "gender",
        "dob",
        "phone",
        "email",
        "address",
        "city",
        "state",
        "pincode",
        "aadhaar_no",
        "pan_no",
        "occupation",
        "created_at",
        "status"
    ],

    "accounts": [
        "account_no",
        "customer_id",
        "account_type",
        "balance",
        "branch",
        "ifsc",
        "opened_date",
        "minimum_balance",
        "status"
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

    "kyc": [
        "kyc_id",
        "customer_id",
        "aadhaar_uploaded",
        "pan_uploaded",
        "address_proof",
        "photo_uploaded",
        "status",
        "verified_by",
        "verified_date"
    ],

    "branches": [
        "branch_id",
        "branch_name",
        "ifsc",
        "city",
        "manager"
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
