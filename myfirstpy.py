import argparse
from datetime import datetime  # Import datetime module

def pcal_birthday_to_today(bd_date):
    # รับข้อมูลวันปัจจุบัน (วัน/เดือน/ปี)
    today = datetime.today()
    
    # คำนวณความแตกต่างระหว่างวันนี้กับวันเกิด
    days_passed = (today - bd_date).days
    return days_passed

def parse_input():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--name",
        type=str,
        default="Phuris",
        help="Input the name for people who are using the app",
    )

    parser.add_argument(
        '--bd',
        type=str,
        required=True,
        help='Input for birthday in DD/MM/YYYY format'
    )

    args = parser.parse_args()
    return args

def printHello(who):
    print(f"Hello World, {who}!!")

if __name__ == "__main__":
    input_v = parse_input()
    print("This is my first .py file.")
    printHello(input_v.name)
    
    # แปลงวันเกิดจากรูปแบบ string เป็น datetime object
    bd_date = datetime.strptime(input_v.bd, "%d/%m/%Y")
    
    days_passed = pcal_birthday_to_today(bd_date)
    print(f"Your birthday was {days_passed} days ago!")
