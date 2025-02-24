# AIPrototype2024
Ai Prototyping 2024 Phuris Kruacharee Student ID: 643020514-7

# 📅 Calendar
|  ᴄʟᴀꜱꜱ  |     ᴅᴀᴛᴇ      |               ᴅᴇꜱᴄʀɪᴘᴛɪᴏɴ                        | ʟᴇᴄᴛᴜʀᴇ  | 
|:-------:|:-------------:|:-----------------------------------------------:|:---------:|
|   1     |  DEC 3, 2024  | ᴜʙᴜɴᴛᴜ ᴄᴏᴍᴍᴀɴᴅ ʟɪɴᴇ                         | [ʟᴇᴄᴛᴜʀᴇ]() |
|   2     |  DEC 11, 2024 | ᴠɪʀᴛᴜᴀʟ ᴍᴀᴄʜɪɴᴇꜱ                            | [ʟᴇᴄᴛᴜʀᴇ]() |
|   3     |  DEC 24, 2024 | ᴄʟᴏᴜᴅ ᴠᴍ                                  | [ʟᴇᴄᴛᴜʀᴇ]() |
|   4     |  JAN 7, 2025  | ᴡᴇʙ ᴘᴀɢᴇ                                 | [ʟᴇᴄᴛᴜʀᴇ]() |
|   5     |  JAN 21, 2025 | ᴇɴᴠɪʀᴏɴᴍᴇɴᴛ ᴄᴏɴᴅᴀ                         | [ʟᴇᴄᴛᴜʀᴇ]() |
|   6     |  FEB 19, 2025 | ᴡᴇʙ ꜱᴇʀᴠɪᴄᴇ                              | [ʟᴇᴄᴛᴜʀᴇ]() |


# 💼 Contents
<details> 
  <summary> ᴜʙᴜɴᴛᴜ ᴄᴏᴍᴍᴀɴᴅ ʟɪɴᴇ </summary>
  
# Command Line พื้นฐานบน Ubuntu
## 1. คำสั่งพื้นฐาน
* list ทุกๆ file/folder ที่อยู่ใน folder ปัจจุบัน
  ```
  $ls
  ```
  ```
  $ls -{option}
  #ex
  $ls -ltr # บอกรายบละเอียดไฟล์
  ```
* ระบุตำแหน่งปัจจุบันที่เราอยู่ในระบบ
  ```
  $pwd
  ```  
## 2. การจัดการ Folder และ File
* create folder
  ```
  $mkdir {foldername}
  ```
* create file 
  ```
  $vi {filename}  # สร้างและเปิดไฟล์ขึ้นมาแก้ไข
  $vi {filename.py} # python file
  #กด i เพื่อแก้ไข
  #กด esc + :wq (ออกแบบ save สิ่งที่เราพิมพ์เข้าไป)
  #กด esc + :q! (ออกแบบไม่ save สิ่งที่อัปลงไป)
  ```
  เวลาจะพิมพ์ กด ***i*** แล้วมันจะขึ้นว่า ***INSERT*** แล้วถึงพิมพ์ได้
  หลังจากนั้นเมื่อพิมพ์เสร็จต้องการที่จะบันทึกให้กด ***esc*** แล้วพิมพ์ **:wq** (write and quit)
* เปิดไฟล์ขึ้นมาดูที่เขียนเฉยๆ
  ```
  $cat {filename}
  ```
* run code Python 
  ```
  $python {filename.py}
  ```
* delete folder
  ```
  $rm -R {foldername}
  ```
* delete file
  ```
  $rm {filename}
  ```
* เปลี่ยนชื่อ file
  ```
  $mv {file เดิม} {file ใหม่}
  $mv ./{file เดิม} ./{file ใหม่}
  # $mv file1 filex # เปลี่ยนชื่อจาก file1 เป็น filex
  ```
* change directory (เข้าไปในfolder)
  ```
  $cd {foldername}
  ```
* ออกจาก folder
  ```
  $cd # home
  $cd ~ # home
  $cd .. # ออกมา 1 step
  $cd ../.. # ออกมา 2 step
  ```
## 3. การ copy และการย้าย file/folder
ที่อยู่ของ File/Folder ในตอนสุดท้าย

![output](https://github.com/user-attachments/assets/a87cd1dc-052c-4afb-bd53-7564c947696f)

* หลักการ
  ```
  $cp {ที่อยู่ต้นทางของ file/folder ที่ต้องการคัดลอก} {ที่อยู่ปลายทางที่ต้องการที่จะคัดลอก file/folder ไป}
  $mv {ที่อยู่ต้นทางของ file/folder ที่ต้องการย้าย} {ที่อยู่ปลายทางที่ต้องการที่จะย้าย file/folder ไป}
  ```
* Copy file
  ```
  $cp ./filex ~/testfolder1/testfolder1_1/. # ~ กลับไปที่ home ก่อน
  ```
  ```
  # copy file1 in testfolder1 to testfolder1_1_1
  $cp ./file1 ./testfolder1_1/testfolder1_1_1/.
  # cp ที่นี่/ชื่อไฟล์ ที่นี่/เข้าไปที่1_1/เข้าไปที่1_1_1/เอาไว้ตรงนี้
  ```
* Copy and change the file name
  คัดลอกไฟล์ 1 ไปที่ testfolder1_1_1 โดยให้มีชื่อว่า file2
  ```
  $cp ./file1 ./testfolder1_1/testfolder1_1_1/file2
  ```
* Copy folder
  ```
  # copy folder + change folder name แต่เอาไว้ที่เดิม
  $cp -R ./testfolder1_1_1 ./testfolder1_1_2
  ```
* Move file
  ```
  $ mv ./filex ~/testfolder2/. # ~ home
  $ mv ./filex ../../../testfolder2/.
  ```
# ยกเลิกคำสั่ง
> ctrl+c

# ขั้นตอนการสร้างไฟล์ด้วย vi

    เข้าสู่โหมดแก้ไข:
        เมื่อเปิดไฟล์ใหม่ขึ้นมาใน vi คุณจะอยู่ในโหมดปกติ (Normal Mode) ซึ่งไม่สามารถพิมพ์ข้อความได้ทันที
        กดปุ่ม i (Insert) เพื่อเข้าสู่โหมดแก้ไข (Insert Mode)

    พิมพ์ข้อความ:
        ตอนนี้คุณสามารถพิมพ์ข้อความในไฟล์ได้ เช่น:

    This is a new file.

บันทึกไฟล์:

    กดปุ่ม Esc เพื่อออกจากโหมดแก้ไข (กลับสู่ Normal Mode)
    พิมพ์ :w แล้วกด Enter เพื่อบันทึกไฟล์

ออกจากโปรแกรม vi:

    หากต้องการบันทึกและออกจากโปรแกรมพร้อมกัน:
        พิมพ์ :wq แล้วกด Enter
    หากต้องการออกโดยไม่บันทึก:
        พิมพ์ :q! แล้วกด Enter

# Homework
copy filex in testfolder1_1 to testfolder1_1_2 and change file name to filey
```
cp ./filex ~/testfolder1/testfolder1_1/testfolder1_1_2/filey
```
</details>


<details> 
  <summary> ᴠɪʀᴛᴜᴀʟ ᴍᴀᴄʜɪɴᴇꜱ </summary>

## 🌐 การใช้งาน Azure Virtual Machines (VM)
Azure Virtual Machines เป็นบริการที่ให้คุณสามารถสร้างเครื่องเสมือน (VM) บนคลาวด์ เพื่อใช้ในการพัฒนาและทดสอบแอปพลิเคชันต่าง ๆ  

### 📌 **1. การสร้าง Virtual Machine บน Azure**
1. เข้าไปที่ **Azure Portal** 👉 [https://portal.azure.com](https://portal.azure.com)
2. ไปที่ **Virtual Machines** > **Create** > **Azure Virtual Machine**
3. กำหนดค่า VM:
   - **Subscription**: เลือก Subscription ของคุณ
   - **Resource group**: สร้างหรือเลือก Resource Group
   - **Virtual Machine Name**: ตั้งชื่อ VM เช่น `phu-vm`
   - **Region**: เลือกตำแหน่งเซิร์ฟเวอร์ที่ต้องการ (แนะนำ Southeast Asia)
   - **Image**: เลือก OS เช่น `Ubuntu 20.04 LTS`
   - **Size**: เลือกขนาดของ VM ตามต้องการ
   - **Authentication Type**: 
     - เลือก `SSH public key`
     - ตั้ง **Username** เช่น `phu`
     - คัดลอก SSH Public Key ของคุณ (สร้าง key ด้วยคำสั่ง `ssh-keygen` หากยังไม่มี)
4. กด **Review + Create** แล้วกด **Create**
5. รอให้ Azure สร้าง VM เสร็จ จากนั้นไปที่ **Virtual Machines > phu-vm** แล้วดู **Public IP Address**

### 🔑 **2. การเข้าใช้งาน Virtual Machine ผ่าน SSH**
เมื่อ VM พร้อมใช้งาน คุณสามารถ SSH เข้าไปที่เซิร์ฟเวอร์ได้โดยใช้ IP Address ที่ได้รับจาก Azure  

#### 🖥 **Linux / macOS / Windows (WSL)**
1. เปิด Terminal หรือ Command Prompt (PowerShell)
2. ใช้คำสั่ง SSH เพื่อเข้า VM:
   ```sh
   ssh phu@<your-vm-ip>

# 🏠 Homework
| Homework | Description | Files |
|:--------:|:-----------|:------|
| HW1 | Calculate how many days you have lived since your birth date. | `myfirst.py` |
| HW2 | Send messages to friends using the server. | `firstflask.py` & `call_web_service.py` |
