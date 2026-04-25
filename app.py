import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# إعدادات الصفحة
st.set_page_config(page_title="LogiPrice AI", layout="centered")

# إضافة الألوان والخلفية
st.markdown("""
    <style>
    .stApp {
        background-color: #f8f9fa;
    }
    h1 {
        color: #1E3A8A;
        text-align: center;
        border-bottom: 2px solid #1E3A8A;
        padding-bottom: 10px;
    }
    .stButton>button {
        background-color: #1E3A8A;
        color: white;
        border-radius: 8px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📊 منصة LOGI-PREDICT للتنبؤ الذكي")
st.write("")

# خانات الإدخال بشكل أنيق
dist = st.number_input("📏 المسافة المقطوعة (كم):", min_value=0, help="أدخل المسافة الكلية للشحن")
weight = st.number_input("⚖️ وزن الشحنة (كجم):", min_value=0, help="أدخل الوزن الإجمالي للبضاعة")

# نموذج التنبؤ (خوارزمية الانحدار الخطي)
X = np.array([[100, 10], [500, 50], [1000, 100], [2000, 200], [5000, 500]])
y = np.array([50, 250, 500, 1000, 2500])
model = LinearRegression().fit(X, y)

if st.button("تحليل وتوقع التكلفة"):
    if dist > 0 and weight > 0:
        prediction = model.predict([[dist, weight]])[0]
        st.balloons()
        
        # عرض النتيجة
        st.success(f"### 💰 التكلفة التقديرية: {prediction:,.2f} دولار")
        
        # نظام التوصيات الذكي
        st.write("---")
        st.subheader("💡 توصيات النظام الذكي:")
        
        if weight > 100:
            st.info("📌 **نصيحة لوجستية:** الوزن مرتفع نسبياً؛ قد يكون الشحن البحري أو التجميعي (LCL) أوفر لك من الشحن السريع.")
        else:
            st.info("📌 **نصيحة لوجستية:** الشحنة خفيفة؛ نوصي بخدمات البريد السريع لضمان السرعة والأمان.")
            
        if dist > 1500:
            st.warning("⚠️ **تنبيه:** المسافة طويلة؛ تأكد من مراجعة شروط التسليم الدولية (Incoterms) لضمان حقوقك.")
            
        st.write("✅ *تم الحساب باستخدام خوارزمية Linear Regression*")
    else:
        st.error("⚠️ يرجى إدخال قيم صحيحة للمسافة والوزن للبدء في التحليل.")
