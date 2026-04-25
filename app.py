import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# اختيار اسم جذاب للمشروع
st.set_page_config(page_title="LogiPrice AI")

st.title("📊 منصة LOGI-PREDICT للتنبؤ الذكي")
st.markdown("---")
st.write("حساب تكاليف النقل الدولي باستخدام خوارزمية **الانحدار الخطي**.")

# خانات الإدخال
dist = st.number_input("أدخل المسافة المقطوعة (كم):", min_value=0)
weight = st.number_input("أدخل وزن الشحنة (كجم):", min_value=0)

# بيانات تدريبية بسيطة
X = np.array([[100, 10], [500, 50], [1000, 100], [2000, 200], [5000, 500]])
y = np.array([50, 250, 500, 1000, 2500])

model = LinearRegression().fit(X, y)

# زر الحساب والنتيجة
if st.button("توقع التكلفة"):
    prediction = model.predict([[dist, weight]])
    st.balloons() # حركة جمالية للاحتفال بالنتيجة
    st.success(f"💰 التكلفة التقديرية هي: {prediction[0]:,.2f} دولار")
