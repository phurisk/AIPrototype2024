# AIPrototype2024
Ai Prototyping 2024 Phuris Kruacharee Student ID: 643020514-7

- WEB_Project: [Link](https://phurisk.github.io/DentAnalyzer/)

- WEB_APP: [Link](http://20.195.15.152:5000/)

# 📅 Calendar
|  ᴄʟᴀꜱꜱ  |     ᴅᴀᴛᴇ      |               ᴅᴇꜱᴄʀɪᴘᴛɪᴏɴ                        | 
|:-------:|:-------------:|:-----------------------------------------------:|
|   1     |  DEC 3, 2024  | ᴜʙᴜɴᴛᴜ ᴄᴏᴍᴍᴀɴᴅ ʟɪɴᴇ                         | 
|   2     |  DEC 11, 2024 | ᴠɪʀᴛᴜᴀʟ ᴍᴀᴄʜɪɴᴇꜱ                            | 
|   3     |  DEC 24, 2024 | ᴄʟᴏᴜᴅ ᴠᴍ                                  | 
|   4     |  JAN 7, 2025  | ᴡᴇʙ ᴘᴀɢᴇ                                 |
|   5     |  JAN 21, 2025 | ᴇɴᴠɪʀᴏɴᴍᴇɴᴛ ᴄᴏɴᴅᴀ                         | 
|   6     |  FEB 19, 2025 | ᴡᴇʙ ꜱᴇʀᴠɪᴄᴇ                              | 


# 💼 Contents
<details> 
  <summary> ᴜʙᴜɴᴛᴜ ᴄᴏᴍᴍᴀɴᴅ ʟɪɴᴇ </summary>
  
## 👨🏻‍💻 Command Line พื้นฐานบน Ubuntu
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
Azure Virtual Machines เป็นบริการที่สามารถสร้างเครื่องเสมือน (VM) บนคลาวด์ เพื่อใช้ในการพัฒนาและทดสอบแอปพลิเคชันต่าง ๆ  

### 📌 **1. การสร้าง Virtual Machine บน Azure**
1. เข้าไปที่ **Azure Portal** 👉 [https://portal.azure.com](https://portal.azure.com)
2. ไปที่ **Virtual Machines** > **Create** > **Azure Virtual Machine**
3. กำหนดค่า VM:
   - **Resource group**: สร้างหรือเลือก Resource Group
   - **Virtual Machine Name**: ตั้งชื่อ VM เช่น `phu-vm`
   - **Region**: เลือกตำแหน่งเซิร์ฟเวอร์ที่ต้องการ (แนะนำ Southeast Asia)
   - **Image**: เลือก OS เช่น `Ubuntu 20.04 LTS`
   - **Size**: เลือกขนาดของ VM ตามต้องการ
   - **Authentication Type**: 
     - ตั้ง **Username** เช่น `phu`
     - ตั้ง **Passwords** เช่น `P1234`

4. กด **Review + Create** แล้วกด **Create**
5. รอให้ Azure สร้าง VM เสร็จ จากนั้นไปที่ **Virtual Machines > phu-vm** แล้วดู **Public IP Address**

### 🔑 **2. การเข้าใช้งาน Virtual Machine ผ่าน SSH**
เมื่อ VM พร้อมใช้งาน จะสามารถ SSH เข้าไปที่เซิร์ฟเวอร์ได้โดยใช้ IP Address  

#### 🖥 **Linux / macOS / Windows (WSL)**
1. เปิด Terminal หรือ Command Prompt
2. ใช้คำสั่ง SSH เพื่อเข้า VM:
   ```sh
   ssh phu@<your-vm-ip>
</details>



<details> 
  <summary> ᴇɴᴠɪʀᴏɴᴍᴇɴᴛ ᴄᴏɴᴅᴀ </summary>

## 🐍 การใช้งาน Conda Environment เบื้องต้น

### 📌 **1. ติดตั้ง Conda**
 Conda สามารถติดตั้งได้จาก:
- **Miniconda** 👉 [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)
  #### หรือ
- **Anaconda** 👉 [https://www.anaconda.com/products/distribution](https://www.anaconda.com/products/distribution)

ตรวจสอบว่า Conda ติดตั้งสำเร็จหรือไม่:
```sh
conda --version
```

### 📌 **2. การสร้าง Environment ใหม่**

```sh
conda create --name ai_project python=3.9
```
### 📌 **3. การ Activate และ Deactivate Environment**
การ Activate Environment
```sh
conda activate ai_project
```
การ Deactivate Environment
```sh
conda deactivate
```

### 📌 **4. การลบ Environment**

การ การลบ Environment
```sh
conda remove --name ai_project --all
```
</details>



<details> 
  <summary> ᴡᴇʙ ꜱᴇʀᴠɪᴄᴇ </summary>
  
## 💬 Web Service for Messaging

เป็น Web Service ที่สามารถส่งข้อความระหว่างผู้ใช้ได้ โดยประกอบไปด้วย 2 ส่วนหลัก:

1. **สคริปต์ฝั่งผู้ใช้ (call_web_service.py)**: ช่วยให้ผู้ใช้ป้อนข้อความและเลือกผู้รับเพื่อส่งข้อความ
2. **API ฝั่งเซิร์ฟเวอร์ (firstflask.py)**: รับข้อความจากผู้ใช้ บันทึกรายละเอียด และส่งคำตอบกลับไปยืนยันการรับข้อความ

## ส่วนประกอบ

### 1. สคริปต์ฝั่งผู้ใช้ (`call_web_service.py`)

สคริปต์ฝั่งผู้ใช้จะติดต่อกับ API ฝั่งเซิร์ฟเวอร์เพื่อส่งข้อความ โดยมีขั้นตอนดังนี้:

- ผู้ใช้จะป้อนข้อความที่ต้องการส่ง
- ผู้ใช้สามารถเลือกผู้รับได้ 2 คน: Tar หรือ Ploy
- ส่งข้อความที่เลือกไปยังเซิร์ฟเวอร์ผ่านคำขอ HTTP POST

สคริปต์จะส่งข้อมูลต่อไปนี้ไปยังเซิร์ฟเวอร์:
- `msg`: ข้อความที่ผู้ใช้ป้อน
- `ผู้รับ`: ชื่อของผู้รับข้อความ
- `ip`: ที่อยู่ IP ของผู้รับ
- `ผู้ส่ง`: ชื่อของผู้ส่งข้อความ

**Code**:
```python
import requests
import json

# URL ของ API
url = 'http://20.255.61.79:5006/simpleAPI'

# ป้อนข้อความจากผู้ใช้
msg = input("กรุณาป้อนข้อความ: ")

# เลือกคนที่ต้องการส่งข้อความ
print("\nเลือกคนที่ต้องการส่งข้อความ:")
print("1. Tar (IP: 20.255.61.79)")
print("2. Ploy (IP: 13.75.95.136)")

choice = input("กรุณาเลือก 1 หรือ 2: ")

# กำหนด IP และชื่อผู้รับตามตัวเลือก
if choice == '1':
    recipient = "Tar"
    ip = "20.255.61.79"
elif choice == '2':
    recipient = "Ploy"
    ip = "13.75.95.136"
else:
    print("\n[ERROR] ตัวเลือกไม่ถูกต้อง! กรุณาเลือกตัวเลือกที่ถูกต้อง.")
    exit()

# ชื่อผู้ส่ง
sender = "Phu"

# สร้าง dictionary สำหรับข้อมูลที่จะส่งไป
myobj = {
    'message_key': 'message_val',
    'msg': msg,
    'ผู้รับ': recipient,
    'ip': ip,
    'ผู้ส่ง': sender
}

# ส่งคำขอ POST
x = requests.post(url, data=json.dumps(myobj))

# ตรวจสอบผลลัพธ์และแสดงผล
if x.status_code == 200:
    print(f"การส่งข้อความสำเร็จ! คำตอบจาก API: {x.text}")
else:
    print(f"[ERROR] การส่งข้อความล้มเหลว! รหัสสถานะ: {x.status_code}")
```

</details>

<details> 
  <summary> ᴅᴇᴇᴘ ʟᴇᴀʀɴɪɴɢ ᴏᴠᴇʀᴠɪᴇᴡ </summary>

# Deep Learning Overview

## Introduction

**Deep Learning** คือ การเพิ่ม **layers** ให้สามารถเรียนรู้ได้เองอัตโนมัติ  
**Activation Function** ทำหน้าที่บีบค่า ไม่ให้ค่าเยอะจนโมเดลระเบิด  

## 1. ลักษณะของ Neural Networks (Neural Networks Characteristics)
![ภาพ](https://github.com/user-attachments/assets/6cdd58c9-fcaa-494b-94d9-da7a4cbb96bb)


- **แรงบันดาลใจ:** เลียนแบบการทำงานของสมองมนุษย์ในการเรียนรู้และแก้ปัญหา  
- **องค์ประกอบ:** ประกอบด้วยโหนด (**neurons**) ที่เชื่อมต่อกันเป็นชั้น (**layers**)  
- **การเรียนรู้:** เรียนรู้จากข้อมูลโดยการปรับค่าน้ำหนัก (**weights**) และค่าไบแอส (**biases**) ระหว่างโหนด  

## 2. พอร์เซปตรอน (Perceptron)
![ภาพ](https://github.com/user-attachments/assets/a46d0c81-ccb5-4594-a53a-d4cf513176bb)

- **หน่วยพื้นฐาน:** เป็นหน่วยประมวลผลพื้นฐานที่สุดของ **Neural Network**  
- **การทำงาน:**  
  1. รับอินพุตหลายค่า  
  2. คูณด้วย **weights** แต่ละค่า  
  3. บวกด้วย **bias**  
  4. ส่งผ่าน **Activation Function** เพื่อให้ได้เอาต์พุต  
- **ข้อจำกัด:** สามารถแก้ปัญหาได้เฉพาะที่ **linear separable** เท่านั้น  

## 3. Artificial Neural Network (ANN)
![ภาพ](https://github.com/user-attachments/assets/91f996c7-4c33-4f2f-8327-bfe900868e63)

- **เครือข่ายประสาทเทียม:** ประกอบด้วยหลายชั้นของ **Perceptron**  
- **Feedforward:** ข้อมูลไหลไปข้างหน้าจากชั้นอินพุตไปยังชั้นเอาต์พุต  
- **Backpropagation:** ใช้ในการปรับค่าน้ำหนักและไบแอสโดยการคำนวณ **gradient** ของฟังก์ชัน **loss**  
- **Activation Functions:** เช่น  
  - **Sigmoid**  
  - **ReLU**  
  - **Tanh**  
  ช่วยให้ ANN สามารถแก้ปัญหา **non-linear** ได้  

## 4. Convolutional Neural Networks (CNN)
![ภาพ](https://github.com/user-attachments/assets/ac24555d-4592-4e55-acc2-60a14c9ac103)

- **ออกแบบมาสำหรับ:** ประมวลผลข้อมูลที่มีโครงสร้างแบบ **Grid** เช่น **รูปภาพ**  
- **Convolutional Layers:** ใช้ **filters** ขนาดเล็กเลื่อนไปบนอินพุตเพื่อตรวจจับ **features**  
- **Feature Maps:** ผลลัพธ์จากการ **convolution** แสดงถึงการตอบสนองของฟิลเตอร์ต่อส่วนต่างๆ ของอินพุต  

## 5. Max Pooling

- **การลดขนาด (Downsampling):** ลดขนาดของ **feature maps** เพื่อลดจำนวนพารามิเตอร์  
- **หลักการ:** เลือกค่าสูงสุดจากแต่ละส่วนของ **feature map**  

## 6. Fully Connected (FC) Layer

- **การเชื่อมต่อแบบเต็ม:** ทุกโหนดในชั้น **FC** เชื่อมต่อกับทุกโหนดในชั้นก่อนหน้า  
- **หน้าที่:** ใช้ในการ **จำแนกประเภท** หรือทำการ **ทำนาย** ขั้นสุดท้าย  

## 7. Flatten Layer

- **การปรับรูปร่าง:** แปลง **feature maps** จาก **convolutional layers** ให้เป็น **เวกเตอร์ 1 มิติ**  
- **หน้าที่:** ใช้เป็นอินพุตให้กับ **Fully Connected Layers**  

## 8. Stride

- **ระยะก้าว:** ระยะที่ **filter** เลื่อนไปในแต่ละครั้งระหว่างการ **convolution**  
- **ผลกระทบ:** ควบคุมขนาดของ **output feature map**  

## 9. Batch Size

- **จำนวนข้อมูล:** จำนวนตัวอย่างข้อมูลที่ใช้ในการคำนวณ **gradient** ในแต่ละ **iteration**  
- **ผลกระทบ:** มีผลต่อ **ความเร็วในการเทรน** และ **ประสิทธิภาพของโมเดล**  

## 10. Dropout

- **เทคนิค Regularization:** สุ่มปิดการทำงานของโหนดบางส่วนในระหว่างการ **เทรน**  
- **หน้าที่:** ป้องกัน **overfitting** โดยบังคับให้โมเดลเรียนรู้ **features ที่ robust** มากขึ้น  

## 11. Freeze Layer

- **การตรึงชั้น:** หยุดการปรับค่าน้ำหนักของบางชั้นในระหว่างการเทรน  
- **การใช้งาน:**  
  - มักใช้ในการ **Transfer Learning**  
  - ใช้ประโยชน์จากความรู้ที่โมเดลได้เรียนรู้มาแล้ว  

## 12. Hierarchical Representations

- **การเรียนรู้ลำดับชั้น:** CNN เรียนรู้ **features** ที่มีความซับซ้อนมากขึ้นในแต่ละชั้น  
- **ตัวอย่าง:** ชั้นแรกอาจเรียนรู้ขอบและมุม, ชั้นต่อมาเรียนรู้รูปร่าง, และชั้นสุดท้ายเรียนรู้ส่วนประกอบของวัตถุ  

## 13. Epoch & Loss

- **Epoch:** จำนวนรอบที่โมเดลได้เห็นข้อมูลทั้งหมดในการเทรน  
- **Loss:** ฟังก์ชันที่วัดความแตกต่างระหว่างผลลัพธ์ที่โมเดลทำนายกับค่าจริง (**ground truth**) ยิ่ง **loss ต่ำ** โมเดลยิ่งแม่นยำ  

---



  </details>

# 🏠 Homework
| Homework | Description | Files |
|:--------:|:-----------|:------|
| HW1 | คำนวณจำนวนวันตั้งแต่วันเกิดจนถึงวันปัจจุบัน | [`myfirst.py`][https://github.com/thanaphornkanking/AIPrototype24/blob/main/myfirst.py] |
| HW2 | ส่งข้อความด้วย Web Service | [`firstflask.py`][https://github.com/phurisk/AIPrototype2024/blob/main/myfirstpy.py] & [`call_web_service.py`][https://github.com/phurisk/AIPrototype2024/blob/main/myfirstpy.py] |
