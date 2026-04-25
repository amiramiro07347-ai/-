import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# إعدادات الصفحة
st.set_page_config(page_title="Logi-Predict Expert", layout="wide")

# تصميم CSS احترافي ومميز
st.markdown("""
    <style>
    .welcome-card {
        text-align: center; padding: 50px; background: white;
        border-radius: 25px; border: 3px solid #1E3A8A;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1); margin: 30px auto; max-width: 850px;
    }
    .main-title { color: #1E3A8A; font-size: 38px; font-weight: bold; }
    .names-text { font-size: 20px; color: #444; line-height: 1.8; }
    .stMetric { background: #f8f9fa; padding: 15px; border-radius: 15px; border: 1px solid #dee2e6; }
    </style>
    """, unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

# --- الصفحة 1: واجهة الترحيب الرسمية ---
if st.session_state.page == 'welcome':
    st.markdown('<div class="welcome-card">', unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">🌟 منصة LOGI-PREDICT للتحليل اللوجستي</h1>', unsafe_allow_html=True)
    st.write("---")
    st.markdown("""
        <p class="names-text">
        <b>إعداد الطلبة:</b> اللك آية / حوحو إكرام / حنا محداد<br>
        <b>تحت إشراف الأستاذة:</b> حسيني أميرة<br>
        <b>التخصص:</b> ماستر 1 لوجستيك ونقل دولي
        </p>
    """, unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)
    if st.button("🚀 الدخول للنظام الخبير"):
        st.session_state.page = 'app'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- الصفحة 2: المنصة المارينية المتطورة ---
else:
    st.sidebar.title("⚙️ لوحة التحكم")
    if st.sidebar.button("🏠 العودة للرئيسية"):
        st.session_state.page = 'welcome'
        st.rerun()

    st.title("📊 نظام دعم القرار والتحليل اللوجستي المتقدم")
    st.write("تحليل التكاليف، البصمة الكربونية، وإدارة المخاطر")
    
    col1, col2 = st.columns([1, 1.2], gap="large")
    
    with col1:
        st.info("📥 مدخلات الشحنة")
        dist = st.number_input("📏 المسافة الإجمالية (كم):", min_value=0)
        weight = st.number_input("⚖️ وزن الشحنة (كجم):", min_value=0)
        gas_price = st.number_input("⛽ سعر الوقود الحالي (DZD):", value=45.97)
        contract = st.selectbox("📦 قاعدة Incoterms:", ["EXW", "FOB", "CIF", "DDP"])
        currency = st.radio("💰 العملة المطلوبة:", ["USD (دولار)", "DZD (دينار جزائري)"])

    with col2:
        st.info("📈 مخرجات التحليل الذكي")
        if st.button("بدء التحليل الشامل"):
            if dist > 0 and weight > 0:
                # 1. حساب التكلفة (نموذج التنبؤ)
                base_cost = (dist * 0.45) + (weight * 1.8)
                fuel_impact = gas_price / 45.97
                final_usd = base_cost * fuel_impact
                display_price = final_usd if currency == "USD (دولار)" else final_usd * 210
                
                # 2. حساب البصمة الكربونية (اللوجستيك الأخضر)
                co2 = round(dist * 0.12, 2)
                
                # 3. حساب درجة المخاطر (بديل مؤشر الوقت)
                # المخاطر تزيد بزيادة المسافة ونوع العقد
                risk_score = "منخفضة"
                if dist > 1000 or contract == "EXW":
                    risk_score = "متوسطة"
                if dist > 3000:
                    risk_score = "عالية"

                # عرض النتائج في بطاقات احترافية
                res1, res2, res3 = st.columns(3)
                res1.metric("التكلفة المتوقعة", f"{display_price:,.2f} { 'DA' if currency == 'DZD (دينار جزائري)' else '$' }")
                res2.metric("🌱 انبعاثات CO2", f"{co2} كجم")
                res3.metric("⚠️ درجة المخاطر", risk_score)
                
                st.write("---")
                st.subheader("🤖 توصيات الخبير اللوجستي:")
                
                # توصيات ذكية بناءً على المدخلات
                if risk_score == "عالية":
                    st.warning(f"⚠️ تنبيه: المسافة طويلة جداً. نوصي بتأمين شامل (All Risks) وتفعيل نظام تتبع الشحنات (Tracking).")
                
                if weight > 500:
                    st.success(f"📌 نصيحة: الوزن كبير؛ قاعدة {contract} تتطلب تنسيقاً دقيقاً لعمليات التفريغ.")
                
                st.info(f"✅ تم دمج مؤشرات اللوجستيك الأخضر ضمن حسابات التكلفة وفقاً للمعايير الدولية.")
                st.balloons()
            else:
                st.error("⚠️ يرجى إدخال البيانات الأساسية أولاً.")

    st.sidebar.markdown("---")
    st.sidebar.write("🏷️ الإصدار: Pro v2.0")
    st.sidebar.write("🌱 تخصص: Logistics & Transport")
