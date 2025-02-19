import requests
import json

# URL ของ API
url = 'http://20.255.61.79:5006/simpleAPI'

# ป้อนข้อความจากผู้ใช้
msg = input("กรุณาป้อนข้อความ: ")

# เลือกคนที่ต้องการส่งข้อความ
print("\nเลือกคนที่ต้องการส่งข้อความ:")
print("1. Tar (IP: 104.43.58.161)")
print("2. Ploy (IP: 13.75.95.136)")

choice = input("กรุณาเลือก 1 หรือ 2: ")

# กำหนด IP และชื่อผู้รับตามตัวเลือก
if choice == '1':
    recipient = "Tar"
    ip = "104.43.58.161"
elif choice == '2':
    recipient = "Ploy"
    ip = "13.75.95.136"
else:
    print("\n[ERROR] ตัวเลือกไม่ถูกต้อง! กรุณาเลือกตัวเลือกที่ถูกต้อง.")
    exit()

# ชื่อผู้ส่ง
sender = "Phu"  # ชื่อของคุณ

# สร้าง dictionary สำหรับข้อมูลที่จะส่งไป
myobj = {
    'message_key': 'message_val',
    'msg': msg,  # ใช้ข้อความที่ผู้ใช้ป้อน
    'ผู้รับ': recipient,  # ชื่อผู้รับ
    'ip': ip,  # IP ของผู้รับ
    'ผู้ส่ง': sender  # ชื่อผู้ส่ง
}

# แสดงข้อมูลก่อนส่ง
print("\nกำลังส่งข้อความ... \n")
print(f"ข้อมูลที่ส่งไป: ")
print(f"----------------------------")
print(f"ผู้ส่ง: {sender}")
print(f"ผู้รับ: {recipient}")
print(f"IP ของผู้รับ: {ip}")
print(f"ข้อความที่ส่ง: {msg}")
print(f"----------------------------\n")

# ส่งคำขอ POST
x = requests.post(url, data=json.dumps(myobj))

# ตรวจสอบผลลัพธ์และแสดงผล
if x.status_code == 200:
    print(f"การส่งข้อความสำเร็จ! คำตอบจาก API: {x.text}")
else:
    print(f"[ERROR] การส่งข้อความล้มเหลว! รหัสสถานะ: {x.status_code}")
