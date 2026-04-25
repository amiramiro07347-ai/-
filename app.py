import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# إعدادات الصفحة
st.set_page_config(page_title="Logi-Predict Platform", layout="wide")

# تصميم الواجهة الأنيق والبسيط الذي أعجبكِ
st.markdown("""
    <style>
    .welcome-box {
        text-align: center;
        padding: 40px;
        background-color: #ffffff;
        border-radius: 20px;
        margin: 40px auto;
        border: 2px solid #1E3A8A;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
        max-width: 800px;
    }
    .main-title { color: #1E3A8A; font-size: 35px; font-weight: bold; }
    .stButton>button {
        background-color: #1E3A8A;
        color: white;
        border-radius: 10px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# إدارة التنقل
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

# --- الصفحة الأولى: الترحيب والأسماء ---
if st.session_state.page == 'welcome':
    st.markdown('<div class="welcome-box">', unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">🌟 منصة LOGI-PREDICT للتنبؤ اللوجستي</h1>', unsafe_allow_html=True)
    st.write("---")
    st.write("### إعداد الطلبة:")
    st.write("اللك آية / حوحو إكرام / حنا محداد")
    st.write("### تحت إشراف الأستاذة:")
    st.write("حسيني أميرة")
    st.write("<br>", unsafe_allow_html=True)
    
    if st.button("🚀 تجربة المنصة الآن"):
        st.session_state.page = 'app'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- الصفحة الثانية: تطبيق الحسابات والتوصية بالوسيلة ---
elif st.session_state.page == 'app':
    st.sidebar.title("⚙️ التحكم")
    if st.sidebar.button("🏠 العودة للرئيسية"):
        st.session_state.page = 'welcome'
        st.rerun()
    
    st.title("📊 نظام التحليل والتنبؤ الذكي")
    st.write("أدخل البيانات للحصول على التكلفة والوسيلة الأنسب")
    st.write("---")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📥 مدخلات الشحنة")
        dist = st.number_input("📏 المسافة المقطوعة (كم):", min_value=0)
        weight = st.number_input("⚖️ وزن الشحنة (كجم):", min_value=0)
        gas_price = st.number_input("⛽ سعر الوقود (DZD):", value=45.97)
        contract = st.selectbox("📦 نوع العقد (Incoterms):", ["EXW", "FOB", "CIF", "DDP"])
        currency = st.radio("💰 عرض النتيجة بـ:", ["USD (دولار)", "DZD (دينار جزائري)"], horizontal=True)

    with col2:
        st.subheader("📈 النتائج والتوصيات")
        
        # نموذج الحساب
        X = np.array([[100, 10], [5000, 500]])
        y = np.array([50, 2500])
        model = LinearRegression().fit(X, y)

        if st.button("تحليل وتوقع التكلفة"):
            if dist > 0 and weight > 0:
                # حساب السعر
                base_price = model.predict([[dist, weight]])[0]
                fuel_impact = gas_price / 45.97
                final_usd = base_price * fuel_impact
                
                result = final_usd if currency == "USD (دولار)" else final_usd * 210
                symbol = "$" if currency == "USD (دولار)" else "DA"
                
                st.success(f"### التكلفة المتوقعة: {result:,.2f} {symbol}")
                
                # --- إضافة تحديد وسيلة النقل الأنسب ---
                st.write("---")
                st.markdown("#### 🚢 وسيلة النقل الأنسب:")
                
                if weight < 100 and dist > 1000:
                    mode = "✈️ الشحن الجوي (Air Freight)"
                    advice = "نظراً لصغر الوزن وبعد المسافة، الجو هو الأسرع والأضمن."
                elif weight > 1000 and dist > 1500:
                    mode = "🚢 الشحن البحري (Sea Freight)"
                    advice = "الوزن كبير والمسافة طويلة؛ البحر هو الخيار الأكثر اقتصادية."
                elif dist <= 800:
                    mode = "🚛 النقل البري (Road Transport)"
                    advice = "للمسافات القصيرة والمتوسطة، البر يوفر مرونة أكبر في التوصيل."
                else:
                    mode = "⛓️ النقل متعدد الوسائط (Multimodal)"
                    advice = "تحتاج هذه الرحلة لدمج أكثر من وسيلة (بري + بحري) لتقليل التكلفة والمخاطر."
                
                st.info(f"**الوسيلة المقترحة:** {mode}")
                st.write(advice)
                
                st.balloons()
            else:
                st.error("يرجى إدخال المسافة والوزن")

    st.sidebar.markdown("---")
    st.sidebar.info("تخصص: Logistics & Transport")
