
import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# إعدادات الصفحة
st.set_page_config(page_title="Logi-Predict Platform", layout="wide")

# تصميم CSS لتحسين المظهر
st.markdown("""
    <style>
    .welcome-box {
        text-align: center;
        padding: 50px;
        background-color: #f0f2f6;
        border-radius: 20px;
        margin-bottom: 30px;
        border: 2px solid #1E3A8A;
    }
    .main-title { color: #1E3A8A; font-size: 45px; font-weight: bold; }
    .names { font-size: 20px; color: #333; margin-top: 10px; }
    .stButton>button {
        background-color: #1E3A8A;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# إدارة الصفحات باستخدام Session State
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

def go_to_app():
    st.session_state.page = 'app'

# --- الصفحة الأولى: الترحيب ---
if st.session_state.page == 'welcome':
    st.markdown('<div class="welcome-box">', unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">🌟 مرحباً بكم في منصة LOGI-PREDICT</h1>', unsafe_allow_html=True)
    st.write("---")
    st.markdown('<p class="names"><b>إعداد الطلبة:</b> اللك آية / حوحو إكرام / حنا محداد</p>', unsafe_allow_html=True)
    st.markdown('<p class="names"><b>تحت إشراف الأستاذة الفاضلة:</b> حسيني أميرة</p>', unsafe_allow_html=True)
    st.write("")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 تجربة المنصة الآن"):
            go_to_app()
    st.markdown('</div>', unsafe_allow_html=True)

# --- الصفحة الثانية: تطبيق التنبؤ ---
elif st.session_state.page == 'app':
    st.sidebar.title("🎮 لوحة التحكم")
    if st.sidebar.button("🏠 العودة للرئيسية"):
        st.session_state.page = 'welcome'
    
    st.title("📊 نظام التنبؤ الذكي والتحليل اللوجستي")
    st.write("قم بإدخال بيانات الشحنة للحصول على أدق التوقعات")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📥 مدخلات النظام")
        dist = st.number_input("📏 المسافة المقطوعة (كم):", min_value=0)
        weight = st.number_input("⚖️ وزن الشحنة (كجم):", min_value=0)
        gas_price = st.number_input("⛽ سعر الوقود الحالي (لليتر):", min_value=0.0, value=45.0)
        contract_type = st.selectbox("📦 نوع العقد (Incoterms):", ["EXW", "FOB", "CIF", "DDP"])
        currency = st.radio("💰 العملة المطلوبة:", ["USD (دولار)", "DZD (دينار جزائري)"])

    with col2:
        st.subheader("📈 النتائج والتوصيات")
        
        # خوارزمية محسنة تأخذ الوقود في الاعتبار بشكل بسيط
        X = np.array([[100, 10], [5000, 500]])
        y = np.array([50, 2500])
        model = LinearRegression().fit(X, y)

        if st.button("تحليل البيانات"):
            if dist > 0 and weight > 0:
                # حساب السعر الأساسي + تأثير سعر الوقود
                base_pred = model.predict([[dist, weight]])[0]
                fuel_factor = (gas_price / 45.0) # معامل الوقود
                final_pred = base_pred * fuel_factor
                
                # تحويل العملة
                display_price = final_pred if currency == "USD (دولار)" else final_pred * 200
                symbol = "$" if currency == "USD (دولار)" else "DA"
                
                st.success(f"### التكلفة التقديرية: {display_price:,.2f} {symbol}")
                st.balloons()
                
                st.write("---")
                st.info("💡 **توصيات المنصة:**")
                if weight > 200:
                    st.write("📌 الوزن مرتفع جداً؛ نوصي بالنقل البحري لتقليل التكاليف الإجمالية.")
                if gas_price > 50:
                    st.write("⚠️ تنبيه: أسعار الوقود مرتفعة، حاول دمج شحناتك لتقليل عدد الرحلات.")
                st.write(f"✅ العقد المختصر ({contract_type}) يتطلب مراجعة دقيقة للمسؤوليات القانونية.")
            else:
                st.error("يرجى إدخال المسافة والوزن أولاً.")

    st.sidebar.markdown("---")
    st.sidebar.write("✅ خوارزمية: Linear Regression")
    st.sidebar.write("✅ الحالة: متصل بالسحابة")
