
# 🤖 AI Marketplace: Storytelling Dashboard
**รายวิชา Business Idea Creation (กลุ่มที่ 1 - ธุรกิจแพลตฟอร์มสินค้ามือสอง)**

🌐 **Live Dashboard:** [https://mini-project-ettpu2uirbiakszuracssj.streamlit.app/](https://mini-project-ettpu2uirbiakszuracssj.streamlit.app/)



---

## 📌 ภาพรวมโปรเจกต์ (Project Overview)

แพลตฟอร์มกลางสำหรับซื้อขายสินค้ามือสองที่แก้ปัญหาเรื่องความไม่โปร่งใสของการตั้งราคาและการประเมินสภาพสินค้า โดยนำเทคโนโลยี AI เข้ามาช่วยในกระบวนการทำงาน:

* **YOLO-cls:** ประเมินเกรดสภาพสินค้าอัตโนมัติจากรูปถ่าย (Grade A, B, C)
* **XGBoost:** ประเมินราคากลางที่เหมาะสมจากข้อมูลประวัติการซื้อขายจริง
* **AI Chatbot:** ระบบต่อรองราคาและตอบคำถามอัตโนมัติ ช่วยปิดการขายได้รวดเร็วขึ้น

---

## 📊 ส่วนประกอบของ Dashboard (`app.py`)

แดชบอร์ดนี้ออกแบบเชิงเล่าเรื่อง (Storytelling Dashboard) แบ่งออกเป็น 5 ส่วนหลัก:

1. **Traction & Key Metrics:** สรุปตัวเลขสำคัญ (Dataset 2,000+ รายการ, ความแม่นยำ Chatbot 87-90%, ประมาณการรายได้ปีแรก 300K-500K THB)
2. **Problem & Market Need:** สภาพปัญหา สัดส่วนสินค้า และการกระจายตัวของเกรดสินค้าในตลาดมือสอง
3. **Image Grading & Price AI:** เปรียบเทียบประสิทธิภาพโมเดลประเมินราคาและเกรดสภาพ
4. **Bargaining & Chatbot:** ประสิทธิภาพและระบบเจรจาต่อรองราคาของ AI
5. **Business Model & Financial Projections:** โครงสร้างรายได้ จุดคุ้มทุน (Break-even 450,000 บาท) และประมาณการ 3 ปี
6. **Group & Task Allocation:** โครงสร้างทีมและการแบ่งงานสมาชิก 10 คน

---

## 📁 โครงสร้าง Repository (Project Structure)

```text
.
├── README.md               # เอกสารอธิบายโปรเจกต์และคู่มือใช้งาน
├── app.py                  # โค้ดหลัก Streamlit แสดงผล Web Dashboard
├── price_history.csv       # ชุดข้อมูลประวัติการซื้อขายสินค้ามือสอง
├── requirements.txt        # รายชื่อ Library ที่ใช้รันโปรแกรม
└── .gitignore              # ไฟล์ตั้งค่าการยกเว้นอัปโหลดไฟล์ขยะขึ้น Git

```

---

## 💻 วิธีการติดตั้งและรันบนเครื่อง Local (Getting Started)

1. **Clone Repository นี้ลงเครื่อง:**
```bash
git clone [https://github.com/67160330/Mini-Project.git](https://github.com/67160330/Mini-Project.git)
cd Mini-Project

```


2. **ติดตั้ง dependencies ทั้งหมด:**
```bash
pip install -r requirements.txt

```


3. **สั่งรัน Streamlit Dashboard:**
```bash
streamlit run app.py

```



---

## 👥 สมาชิกในกลุ่มและการแบ่งหน้าที่ (Team & Task Allocation)

| หน้าที่ / ฝ่าย | ชื่อ-นามสกุล (ชื่อเล่น) | บทบาทความรับผิดชอบหลัก |
| --- | --- | --- |
| **Project Leader** | ณัทฐิกา ครุยาศรัทธา | บริหารภาพรวมโครงการ และประสานงานระหว่างฝ่าย |
| **Support Leader** | ณัฐวุฒิ จันทกูล (บีม) | จัดทำ Business Model Canvas (BMC) และจัดทำเอกสาร |
| **Man Support** | คามิน ครอบบัวบาน (ต้า) | ศึกษาพฤติกรรมผู้บริโภค รวบรวมข้อมูลตลาดสินค้ามือสอง |
| **Man Support** | ธนบูรณ์ ชนะ (แสตมป์) | จัดทำสื่อนำเสนอ รวบรวมผลและสรุปรายงาน |
| **Tech Leader** | ศุภวิชญ์ จิตรดี (ม่อน) | ออกแบบ AI Architecture, API และโครงสร้าง Backend |
| **Man Tech** | กันต์ธร ใจใหญ่ (กันต์) | เทรนโมเดล YOLO-cls และ XGBoost ประเมินราคากลาง |
| **Man Tech** | ณัฏฐชัย ดีชัยยะ (ต้นน้ำ) | พัฒนา AI Chatbot ต่อรองราคา และจุดเชื่อมต่อ API |
| **QA Leader** | ธนากร เรืองศิริ (มิก) | ควบคุมคุณภาพระบบ (QA) วางแผน Test Case |
| **Man QA** | ปัญญพัฒน์ ทรงศร (ทีม) | ทำ Data Labeling ติดแท็กรูปภาพสินค้า และเก็บ Bug Report |
| **Man QA** | กิตติพัฒน์ แน่นอุดร (โบท) | ทดสอบระบบแบบ Regression Test และตรวจความถูกต้องของ Dashboard |

```

```
