import streamlit as st
import google.generativeai as genai
import os

# 1. Setup หน้าเว็บ (Branding)
st.set_page_config(page_title="Aigentic Content Engine", page_icon="🤖")
st.title("🤖 Aigentic Content Engine v1")
st.subheader("โดย Aigentic Solution | AI-Powered Marketing")

# 2. ส่วนรับข้อมูลจาก User
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("ใส่ Gemini API Key ของคุณ:", type="password")
    target_audience = st.selectbox("กลุ่มเป้าหมาย:", ["คนทั่วไปที่ตาม AI ไม่ทัน", "นักศึกษาวิศวกรรม", "เจ้าของธุรกิจ SME"])

# 3. โครงสร้าง Prompt ที่เราช่วยกันเกลา (The Soul of your Product)
def generate_content(topic, target):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-flash-latest')
    
    # นี่คือจุดที่โชว์ทักษะ Prompt Engineering ของคุณ
    prompt = f"""
    Role: คุณคือ Senior AI Consultant ที่เชี่ยวชาญการเขียนคอนเทนต์แบบ 'พี่สอนน้อง'
    Target: {target}
    Topic: {topic}
    Task: เขียนโพสต์ Facebook ที่มีโครงสร้าง:
    1. Hook ที่น่าสนใจเรื่อง AI แย่งงาน
    2. Solution 3 ขั้นตอน (Roadmap, Workshop, Tools)
    3. Call to Action ให้มาทดลองเรียนฟรี
    Constraints: ห้ามใช้คำที่ดูเป็น AI เกินไป ให้ใช้ภาษาพูดที่เป็นธรรมชาติ
    """
    
    response = model.generate_content(prompt)
    return response.text

# 4. ส่วนแสดงผลบนหน้าเว็บ
topic_input = st.text_input("คุณอยากขายอะไร? (เช่น คอร์สเรียน AI, บริการแชทบอท):")

if st.button("Generate Content ✨"):
    if not api_key:
        st.error("กรุณาใส่ API Key ใน Sidebar ก่อนครับ")
    elif not topic_input:
        st.warning("กรุณาใส่หัวข้อที่ต้องการเขียนครับ")
    else:
        with st.spinner('AI กำลังคิดให้คุณ...'):
            result = generate_content(topic_input, target_audience)
            st.markdown("---")
            st.markdown(result)
            st.success("คอนเทนต์ของคุณพร้อมใช้งานแล้ว!")