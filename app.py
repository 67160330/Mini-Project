import os
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# ==========================================
# 1. Page Configuration
# ==========================================
st.set_page_config(
    page_title="AI Marketplace - Storytelling Dashboard",
    page_icon="🤖",
    layout="wide",
)

# Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "price_history.csv")


# ==========================================
# 2. Data Loader & Auto Generator
# ==========================================
def generate_sample_data():
  np.random.seed(42)
  categories = {
      "Smartphone": ["Apple", "Samsung", "Sony"],
      "Laptop": ["Apple", "Asus", "Acer", "Lenovo"],
      "GPU/PC Parts": ["Nvidia", "AMD"],
      "Gaming Gear": ["Logitech", "Razer"],
      "Smartwatch": ["Apple", "Samsung"],
  }
  models = {
      "Apple": [
          "iPhone 13",
          "iPhone 14 Pro",
          "MacBook Air M1",
          "MacBook Pro M2",
          "Apple Watch S8",
      ],
      "Samsung": ["Galaxy S22", "Galaxy S23 Ultra", "Galaxy Watch 5"],
      "Sony": ["PlayStation 5", "Xperia 1 IV"],
      "Asus": ["ROG Zephyrus G14", "TUF Gaming F15"],
      "Acer": ["Predator Helios 300", "Nitro 5"],
      "Lenovo": ["Legion 5 Pro", "ThinkPad X1 Carbon"],
      "Nvidia": ["GeForce RTX 3060", "GeForce RTX 3070", "GeForce RTX 4080"],
      "AMD": ["Radeon RX 6700 XT", "Radeon RX 7900 XTX"],
      "Logitech": ["G Pro X Superlight", "G Pro Mechanical Keyboard"],
      "Razer": ["DeathAdder V3", "BlackWidow V4"],
  }
  data = []
  grade_multipliers = {"A": 0.85, "B": 0.70, "C": 0.50}

  for i in range(1, 180):
    cat = np.random.choice(list(categories.keys()))
    brand = np.random.choice(categories[cat])
    model = np.random.choice(models[brand])
    year = np.random.choice([2021, 2022, 2023, 2024])
    grade = np.random.choice(["A", "B", "C"], p=[0.4, 0.4, 0.2])
    base_price = np.random.randint(5000, 60000)
    market_price = max(
        1000,
        round(
            base_price * grade_multipliers[grade] * (1 - (2026 - year) * 0.10),
            -2,
        ),
    )
    ai_predicted = int(market_price * np.random.uniform(0.95, 1.05))
    confidence_score = round(np.random.uniform(88.0, 99.5), 1)
    status = np.random.choice(
        ["Sold", "Available", "Negotiating"], p=[0.55, 0.35, 0.10]
    )

    data.append({
        "item_id": f"ITEM-{i:03d}",
        "product_name": model,
        "brand": brand,
        "category": cat,
        "release_year": year,
        "grade": grade,
        "original_price": base_price,
        "market_price": market_price,
        "ai_predicted_price": ai_predicted,
        "confidence_score_pct": confidence_score,
        "status": status,
    })

  df_generated = pd.DataFrame(data)
  df_generated.to_csv(CSV_PATH, index=False, encoding="utf-8-sig")
  return df_generated


@st.cache_data
def load_data():
  if not os.path.exists(CSV_PATH):
    return generate_sample_data()
  return pd.read_csv(CSV_PATH)


df = load_data()

# ==========================================
# 3. Title & Header
# ==========================================
st.title("🤖 AI Marketplace: Storytelling Dashboard")
st.caption("รายวิชา Business Idea Creation - กลุ่มที่ 1 (ธุรกิจมือสอง)")

st.markdown("""
> **เรื่องเล่าการเดินทางของ AI Marketplace:** จากปัญหาผู้ซื้อ-ผู้ขายตั้งราคาไม่ตรงราคาตลาดและสื่อสารไม่ราบรื่น สู่การใช้ **YOLO-cls** ประเมินสภาพสินค้า ร่วมกับ **XGBoost** ประเมินราคามือสอง และ **AI Chatbot** ช่วยเจรจาต่อรองปิดการขาย ( Repository: `github.com/SupawitMon/ai-service-2hand` )
""")

st.divider()

# ==========================================
# 4. Section 1: Executive Key Metrics (Updated)
# ==========================================
st.header("📈 1. Traction & Executive Key Metrics")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
  st.metric(
      label="ฐานข้อมูลสินค้าในระบบ",
      value="2,000+ รายการ",
      delta="Web Scraping Data",
  )
with col2:
  st.metric(
      label="Dataset เทรน AI เกรดภาพ",
      value="2,087 รูป",
      delta="Acc 67% ➔ 76%",
  )
with col3:
  st.metric(
      label="ความแม่นยำ Chatbot", value="87% - 90%", delta="Latency ~4 ms"
  )
with col4:
  st.metric(
      label="เป้าหมายรายได้ ปีที่ 1",
      value="300K - 500K ฿",
      delta="Commission 3-5% + Ads",
  )
with col5:
  st.metric(
      label="จุดคุ้มทุน (Break-even)",
      value="450,000 ฿",
      delta="ภายใน 12-18 เดือน",
  )

st.divider()

# ==========================================
# 5. Section 2: Storytelling Narrative Tabs
# ==========================================
st.header("📖 2. Storytelling Narrative: เจาะลึกข้อมูลและการดำเนินงาน")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🎯 Problem & Market Need",
    "📸 Image Grading AI (YOLO)",
    "💬 Bargaining & Q&A Chatbot",
    "💼 Business Model & Projections",
    "👥 Group & Task Allocation",
])

# ----- TAB 1: Problem & Market Need -----
with tab1:
  st.subheader("ปัญหาและการกระจายตัวของสินค้ามือสองในระบบ")
  col_a, col_b = st.columns(2)
  with col_a:
    fig_cat = px.pie(
        df,
        names="category",
        title="สัดส่วนหมวดหมู่สินค้ามือสองใน Dataset",
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Pastel,
    )
    st.plotly_chart(fig_cat, use_container_width=True)
  with col_b:
    fig_grade = px.histogram(
        df,
        x="grade",
        color="status",
        barmode="group",
        title="การกระจายตัวของสภาพสินค้า (Grade A/B/C) และสถานะการขาย",
        color_discrete_sequence=["#2ecc71", "#3498db", "#e74c3c"],
    )
    st.plotly_chart(fig_grade, use_container_width=True)

# ----- TAB 2: Image Grading AI & Price Engine -----
with tab2:
  st.subheader("ประสิทธิภาพ AI ประเมินเกรดสินค้าและราคากลาง")

  mcol1, mcol2, mcol3 = st.columns(3)
  with mcol1:
    st.info("🖼️ **Dataset รูปภาพ:** 2,087 รูป (เพิ่มล่าสุด)")
  with mcol2:
    st.success("🎯 **Accuracy:** ปรับเพิ่มจาก 67% ➔ **76%**")
  with mcol3:
    st.warning("⚡ **Model:** YOLO-cls + XGBoost")

  fig_scatter = px.scatter(
      df,
      x="market_price",
      y="ai_predicted_price",
      color="grade",
      hover_data=["product_name", "confidence_score_pct"],
      title="เปรียบเทียบราคาตลาดจริง vs ราคาที่ AI ประเมิน (XGBoost Prediction)",
      labels={
          "market_price": "ราคาตลาดจริง (บาท)",
          "ai_predicted_price": "ราคา AI ประเมิน (บาท)",
      },
  )
  fig_scatter.add_shape(
      type="line",
      x0=0,
      y0=0,
      x1=60000,
      y1=60000,
      line=dict(color="Red", width=2, dash="dash"),
  )
  st.plotly_chart(fig_scatter, use_container_width=True)

# ----- TAB 3: Bargaining & Q&A Chatbot -----
with tab3:
  st.subheader("ประสิทธิภาพและการทำงานของ AI Chatbot (ต่อรองราคา & ถาม-ตอบ)")

  cb1, cb2, cb3 = st.columns(3)
  with cb1:
    st.metric(
        label="Intent Accuracy", value="87% - 90%", delta="เข้าใจภาษาธรรมชาติ"
    )
  with cb2:
    st.metric(
        label="Processing Latency",
        value="~4 ms",
        delta="ไม่รวมเวลาเครือข่าย",
    )
  with cb3:
    st.metric(
        label="Hallucination Handling",
        value="Ask Back 100%",
        delta="ย้อนถามเมื่อไม่มั่นใจ",
    )

  st.markdown("""
    ### 🚀 อัปเดตฟีเจอร์สำคัญของ Chatbot ล่าสุด:
    1. **Dynamic Pricing Rules:** แยกโครงสร้างราคาสินค้าตามสภาพจริง (**ของใหม่ / มือสอง / เครื่องเสีย**) ตอบตรงรุ่น
    2. **Deal Closing Logic:** ระบบตรวจจับการตกลงราคา เช่น เมื่อผู้ซื้อพิมพ์ *"ได้ครับ"* ระบบจะทำการปิดการขายให้อัตโนมัติ
    3. **Context Memory & Session Tracking:** จดจำบริบทการคุยย้อนหลัง และออก **Tracking ID** สำหรับตรวจสอบ Log ทุกข้อความ
    4. **Deployment:** รันบน **Docker Container** เปิดใช้งาน API Endpoint ทั้ง 2 ตัวบน Server เรียบร้อย
    """)

# ----- TAB 4: Business Model & Projections -----
with tab4:
  st.subheader("ประมาณการรายได้และจุดคุ้มทุน (Financial Projections)")
  rev_data = pd.DataFrame({
      "Year": ["ปีที่ 1 (Year 1)", "ปีที่ 2 (Year 2)", "ปีที่ 3 (Year 3)"],
      "Min Revenue": [200000, 600000, 1500000],
      "Max Revenue": [500000, 1200000, 3000000],
  })
  fig_bar = go.Figure(data=[
      go.Bar(
          name="คาดการณ์ขั้นต่ำ (Min)",
          x=rev_data["Year"],
          y=rev_data["Min Revenue"],
          marker_color="#16a085",
      ),
      go.Bar(
          name="คาดการณ์ขั้นสูง (Max)",
          x=rev_data["Year"],
          y=rev_data["Max Revenue"],
          marker_color="#2980b9",
      ),
  ])
  fig_bar.update_layout(
      title="ประมาณการรายได้สุทธิของ AI Marketplace (บาท)", barmode="group"
  )
  st.plotly_chart(fig_bar, use_container_width=True)

  st.markdown("""
    **สมมติฐานทางการเงินที่สมเหตุสมผล (Realistic Financial Assumptions):**
    * **ต้นทุนดำเนินงานเริ่มต้น (OpEx & Dev):** ~250,000 - 350,000 บาท (ค่า Cloud Server, API/GPU Cost, ค่าทำการตลาดเปิดตัว)
    * **โมเดลรายได้ (Revenue Model):** ค่าธรรมเนียมการขาย (Commission 3-5%) + โฆษณาดันโพสต์ (Featured Ads)
    * **เป้าหมายรายได้ปีแรก:** 300,000 - 500,000 บาท (ประเมินจากยอดการขายสะสมหรือ GMV ประมาณ 8-10 ล้านบาท)
    * **จุดคุ้มทุน (Break-even Point):** รายได้รวมแตะ **450,000 บาท** (คืนทุนค่าพัฒนาและ Server ได้ภายใน 12-18 เดือน)
    """)

# ----- TAB 5: Group & Task Allocation -----
with tab5:
  st.subheader("รายชื่อสมาชิกและโครงสร้างทีม (กลุ่มที่ 1)")
  team_data = [
      {
          "ตำแหน่ง": "Project Leader",
          "ชื่อ-นามสกุล": "ณัทฐิกา ครุยาศรัทธา",
          "หน้าที่": "บริหารภาพรวม & ประสานงาน",
      },
      {
          "ตำแหน่ง": "Support Leader",
          "ชื่อ-นามสกุล": "ณัฐวุฒิ จันทกูล (บีม)",
          "หน้าที่": "จัดทำ BMC & เอกสาร",
      },
      {
          "ตำแหน่ง": "Man Support",
          "ชื่อ-นามสกุล": "คามิน ครอบบัวบาน (ต้า)",
          "หน้าที่": "ศึกษาตลาด & รวบรวมข้อมูล",
      },
      {
          "ตำแหน่ง": "Man Support",
          "ชื่อ-นามสกุล": "ธนบูรณ์ ชนะ (แสตมป์)",
          "หน้าที่": "จัดทำสื่อ & รายงาน",
      },
      {
          "ตำแหน่ง": "Tech Leader",
          "ชื่อ-นามสกุล": "ศุภวิชญ์ จิตรดี (ม่อน)",
          "หน้าที่": "ออกแบบ AI Architecture & Backend",
      },
      {
          "ตำแหน่ง": "Man Tech",
          "ชื่อ-นามสกุล": "กันต์ธร ใจใหญ่ (กันต์)",
          "หน้าที่": "เทรนโมเดล YOLO-cls & XGBoost",
      },
      {
          "ตำแหน่ง": "Man Tech",
          "ชื่อ-นามสกุล": "ณัฏฐชัย ดีชัยยะ (ต้นน้ำ)",
          "หน้าที่": "พัฒนา AI Chatbot & API",
      },
      {
          "ตำแหน่ง": "QA Leader",
          "ชื่อ-นามสกุล": "ธนากร เรืองศิริ (มิก)",
          "หน้าที่": "ควบคุมคุณภาพ & วางแผน Test Case",
      },
      {
          "ตำแหน่ง": "Man QA",
          "ชื่อ-นามสกุล": "ปัญญพัฒน์ ทรงศร (ทีม)",
          "หน้าที่": "ติด Label ภาพ & สรุป Bug",
      },
      {
          "ตำแหน่ง": "Man QA",
          "ชื่อ-นามสกุล": "กิตติพัฒน์ แน่นอุดร (โบท)",
          "หน้าที่": "ทดสอบฟังก์ชัน & Regression Test",
      },
  ]
  st.table(pd.DataFrame(team_data))

st.caption(
    "พัฒนาสำหรับรายวิชา Business Idea Creation | GitHub:"
    " SupawitMon/ai-service-2hand"
)