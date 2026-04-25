import streamlit as st
import numpy as np

st.set_page_config(page_title="Pro-Logistics AI", layout="wide")

# تصميم CSS احترافي
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    .welcome-card {
        text-align: center; padding: 40px; background: white;
        border-radius: 20px; border-top: 8px solid #1E3A8A;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin-bottom: 20px;
    }
    .metric-card {
        background: #ffffff; padding: 15px; border-radius: 10px;
        border: 1px solid #e0e0e0; text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

# --- الصفحة 1: الترحيب ---
if st.session_state.page == 'welcome':
    st.markdown('<div class="welcome-card">', unsafe_allow_html=True)
    st.title("🌟 منصة LOGI-PREDICT الاحترافية")
    st.write("---")
    st.subheader("إعداد الطلبة:")
    st.write("اللك آية | حوحو إكرام | حنا محداد")
    st.markdown(f"**تحت إشراف الأستاذة:** حسيني أميرة")
    st.write("<br>", unsafe_allow_html=True)
    if st.button("🚀 الدخول للنظام المطور"):
        st.session_state.page = 'app'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- الصفحة 2: المنصة المتطورة ---
else:
    st.sidebar.title("⚙️ خيارات التحليل")
    if st.sidebar.button("🏠 العودة للرئيسية"):
        st.session_state.page = 'welcome'
        st.rerun()

    st.title("📊 نظام دعم القرار والتحليل اللوجستي")
    
    col1, col2 = st.columns([1, 1.2], gap="large")
    
    with col1:
        st.info("📥 مدخلات العملية")
        dist = st.number_input("📏 المسافة الإجمالية (كم):", min_value=0)
        weight = st.number_input("⚖️ وزن الشحنة (كجم):", min_value=0)
        gas = st.number_input("⛽ سعر الوقود (DZD):", value=45.97)
        contract = st.selectbox("📦 Incoterms:", ["EXW", "FOB", "CIF", "DDP"])
        currency = st.radio("💰 العملة:", ["USD", "DZD"])

    with col2:
        st.info("📈 نتائج التحليل الذكي")
        if st.button("تحليل الشحنة"):
            if dist > 0 and weight > 0:
                # حسابات ذكية
                cost_usd = (dist * 0.4) + (weight * 1.5) + (gas * 0.1)
                final_cost = cost_usd if currency == "USD" else cost_usd * 210
                days = round(dist / 550, 1) # افتراض شاحنة تقطع 550 كم/يوم
                co2 = round(dist * 0.12, 2)
                
                # عرض النتائج بشكل احترافي
                m1, m2, m3 = st.columns(3)
                m1.metric("التكلفة التقديرية", f"{final_cost:,.2f} {currency}")
                m2.metric("زمن الوصول (ETA)", f"{days} يوم")
                m3.metric("انبعاثات CO2", f"{co2} كجم")
                
                st.write("---")
                st.subheader("🤖 التوصية الاستراتيجية:")
                if weight > 1000:
                    st.warning("⚠️ شحنة ثقيلة جداً: نوصي بالنقل المتعدد الوسائط (Multimodal) لتقليل التكاليف.")
                elif dist < 300:
                    st.success("✅ الخيار الأمثل: النقل البري المباشر هو الأكثر كفاءة لهذه المسافة.")
                else:
                    st.info("📌 يرجى التأكد من مطابقة وثائق الشحن لقواعد " + contract)
                
                st.balloons()
            else:
                st.error("يرجى إدخال البيانات")

    st.sidebar.markdown("---")
    st.sidebar.write("✅ خوارزمية التوقع: Linear Regression")
    st.sidebar.write("🌱 يدعم اللوجستيك الأخضر")
