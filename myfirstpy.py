import argparse
from datetime import datetime  # Import datetime module

def pcal_todayVbd(bd_day):
    # รับข้อมูลวันปัจจุบัน (วัน/เดือน)
    today = datetime.today()
    today_day = today.day
    today_month = today.month
    
    # กำหนดเดือนและวันของวันเกิด
    birth_day = bd_day
    birth_month = today_month  # ใช้เดือนปัจจุบัน

    # คำนวณว่ามีวันเหลือกี่วัน
    if birth_day < today_day:
        # ถ้าคุณเกิดแล้วในเดือนนี้ ให้ไปวันเกิดปีถัดไป
        next_birthday = datetime(today.year + 1, birth_month, birth_day)
    else:
        # ถ้ายังไม่ถึงวันเกิด ให้ไปวันเกิดในปีนี้
        next_birthday = datetime(today.year, birth_month, birth_day)

    # คำนวณความแตกต่างระหว่างวันนี้กับวันเกิด
    days_left = (next_birthday - today).days
    return days_left


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
        type=int,
        required=True,
        help='Input for birthday of the user in format DD (Day of the month only)'
    )

    args = parser.parse_args()
    return args


def printHello(who):
    print(f"Hello World, {who}!!")


if __name__ == "__main__":
    input_v = parse_input()
    print("This is my first .py file.")
    printHello(input_v.name)
    
    days_left = pcal_todayVbd(input_v.bd)
    print(f"Your birthday is in {days_left} days from today!")
