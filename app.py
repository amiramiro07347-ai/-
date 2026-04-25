
import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="Logi-Predict Platform", layout="wide")

# تصميم الألوان والواجهة (CSS) لتبدو احترافية
st.markdown("""
    <style>
    .welcome-box {
        text-align: center;
        padding: 60px;
        background-color: #ffffff;
        border-radius: 25px;
        margin: 50px auto;
        border: 3px solid #1E3A8A;
        box-shadow: 10px 10px 20px rgba(0,0,0,0.1);
        max-width: 800px;
    }
    .main-title { color: #1E3A8A; font-size: 40px; font-weight: bold; margin-bottom: 20px; }
    .names { font-size: 22px; color: #333; margin: 10px 0; line-height: 1.6; }
    .supervisor { font-size: 24px; color: #1E3A8A; font-weight: bold; margin-top: 20px; }
    .stButton>button {
        background-color: #1E3A8A;
        color: white;
        border-radius: 12px;
        height: 3.5em;
        width: 100%;
        font-size: 20px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #2563EB;
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)

# إدارة التنقل بين الصفحات
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

def start_app():
    st.session_state.page = 'app'

# --- الصفحة الأولى: واجهة الترحيب والأسماء ---
if st.session_state.page == 'welcome':
    st.markdown('<div class="welcome-box">', unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">🌟 منصة LOGI-PREDICT للتنبؤ اللوجستي</h1>', unsafe_allow_html=True)
    st.write("---")
    st.markdown('<p class="names"><b>إعداد الطلبة:</b><br>اللك آية / حوحو إكرام / حنا محداد</p>', unsafe_allow_html=True)
    st.markdown('<p class="supervisor">تحت إشراف الأستاذة: حسيني أميرة</p>', unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 تجربة المنصة الآن"):
            start_app()
    st.markdown('</div>', unsafe_allow_html=True)

# --- الصفحة الثانية: تطبيق الحسابات والتوصيات ---
elif st.session_state.page == 'app':
    st.sidebar.title("🎮 لوحة التحكم")
    if st.sidebar.button("🏠 العودة للرئيسية"):
        st.session_state.page = 'welcome'
        st.rerun()
    
    st.title("📊 نظام التحليل والتنبؤ الذكي")
    st.write("أدخل البيانات التالية بدقة للحصول على التكلفة التقديرية والتوصيات اللوجستية.")
    st.write("---")
    
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.subheader("📥 مدخلات النظام")
        dist = st.number_input("📏 المسافة المقطوعة (كم):", min_value=0, step=10)
        weight = st.number_input("⚖️ وزن الشحنة (كجم):", min_value=0, step=1)
        gas_price = st.number_input("⛽ سعر الوقود الحالي (DZD):", min_value=0.0, value=45.97)
        contract = st.selectbox("📦 نوع العقد (Incoterms):", ["EXW", "FOB", "CIF", "DDP"])
        currency = st.radio("💰 عرض النتيجة بـ:", ["USD (دولار)", "DZD (دينار جزائري)"])

    with col2:
        st.subheader("📈 النتائج والتوصيات")
        
        # خوارزمية Linear Regression بسيطة للتدريب
        X = np.array([[100, 10], [500, 50], [1000, 100], [5000, 500]])
        y = np.array([50, 250, 500, 2500])
        model = LinearRegression().fit(X, y)

        if st.button("تحليل وتوقع التكلفة"):
            if dist > 0 and weight > 0:
                # حساب التكلفة بناءً على المسافة والوزن + تأثير سعر الوقود
                base_price = model.predict([[dist, weight]])[0]
                fuel_impact = gas_price / 45.97
                final_price_usd = base_price * fuel_impact
                
                # تحويل العملة
                result_price = final_price_usd if currency == "USD (دولار)" else final_price_usd * 210
                unit = "$" if currency == "USD (دولار)" else "DA"
                
                st.success(f"### 💰 التكلفة التقديرية: {result_price:,.2f} {unit}")
                st.balloons()
                
                st.write("---")
                st.info("💡 **توصيات النظام الذكي:**")
                
                if weight > 300:
                    st.write("📌 **نصيحة:** الوزن كبير؛ الشحن البحري أو عبر السكك الحديدية سيكون أوفر بكثير.")
                else:
                    st.write("📌 **نصيحة:** الشحنة مناسبة للنقل البري السريع أو الجوي.")
                
                if dist > 1000:
                    st.write("⚠️ **تنبيه:** المسافة طويلة؛ يرجى التأكد من شروط التأمين وتغطية مخاطر النقل.")
                
                st.write(f"✅ تم الحساب وفق قاعدة: **{contract}**")
            else:
                st.error("⚠️ يرجى إدخال قيم صحيحة للمسافة والوزن.")

    st.sidebar.markdown("---")
    st.sidebar.markdown("### تخصص")
    st.sidebar.info("Master 1: Logistics and International Transport")
