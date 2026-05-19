import streamlit as st
import base64

# ---------------- إعداد الصفحة ----------------

st.set_page_config(
    page_title="Ghzlan AL-Rashidi",
    page_icon="✨",
    layout="wide"
)

# ---------------- QR CODE ----------------

with open("QR.jpeg", "rb") as image_file:
    qr_base64 = base64.b64encode(image_file.read()).decode()

# ---------------- التصميم ----------------

st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
background: linear-gradient(135deg, #050505, #0f0a1f, #1a0026);
background-attachment: fixed;
}

[data-testid="stHeader"]{
background: rgba(0,0,0,0);
}

html, body, [class*="css"]{
color:white;
font-family:sans-serif;
scroll-behavior:smooth;
}

.hero-title{
font-size:95px;
font-weight:900;
line-height:1;
margin-top:70px;

background: linear-gradient(
90deg,
#ff4fd8,
#b026ff,
#7a5cff
);

-webkit-background-clip:text;
-webkit-text-fill-color:transparent;

animation: fadeUp 1s ease;
}

.hero-sub{
font-size:30px;
color:#f5d0fe;
margin-top:20px;
margin-bottom:40px;

animation: fadeUp 1.4s ease;
}

.contact{
font-size:22px;
line-height:2;
color:#fbcfe8;

animation: fadeUp 1.6s ease;
}

.glass{
background: rgba(255,255,255,0.05);

padding:35px;

border-radius:30px;

backdrop-filter: blur(12px);

margin-top:20px;

border:1px solid rgba(255,255,255,0.1);

box-shadow:0px 0px 20px rgba(176,38,255,0.15);

transition:0.4s;

animation: fadeUp 1s ease;
}

.glass:hover{
transform:translateY(-6px);
box-shadow:0px 0px 35px rgba(255,79,216,0.25);
}

.section-title{
font-size:38px;
font-weight:bold;
margin-bottom:20px;

background: linear-gradient(
90deg,
#ff4fd8,
#b026ff
);

-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.skill{
background: linear-gradient(
135deg,
#ff4fd8,
#7a5cff
);

padding:16px;

border-radius:18px;

text-align:center;

font-size:18px;

font-weight:bold;

margin:8px;

color:white;

transition:0.4s;

box-shadow:0px 0px 15px rgba(176,38,255,0.3);
}

.skill:hover{
transform:scale(1.06);
box-shadow:0px 0px 25px rgba(255,79,216,0.5);
}

.qr-box{
text-align:center;
margin-top:20px;
}

.qr-box img{
border-radius:25px;
transition:0.4s;
box-shadow:0px 0px 25px rgba(255,79,216,0.25);
}

.qr-box img:hover{
transform:scale(1.05);
box-shadow:0px 0px 40px rgba(255,79,216,0.5);
}

.footer{
text-align:center;
padding:50px;
font-size:18px;
color:#c084fc;
}

a{
color:#f9a8d4;
text-decoration:none;
}

a:hover{
color:white;
}

@keyframes fadeUp{

from{
opacity:0;
transform:translateY(40px);
}

to{
opacity:1;
transform:translateY(0px);
}

}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------

st.markdown("""
<h1 class="hero-title">
Ghzlan <br>
AL-Rashidi
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p class="hero-sub">
Computer Science Graduate
</p>
""", unsafe_allow_html=True)

# ---------------- CONTACT ----------------

st.markdown("""
<div class="contact">

📞 +966 50 220 3750 <br>

📧 ghzlanalrashidi@gmail.com <br>

📍 Unaizah, Al-Qassim, Saudi Arabia <br>

🔗 <a href="https://github.com/Ghzlan175" target="_blank">
github.com/Ghzlan175
</a><br>

🔗 <a href="https://linkedin.com/in/Ghzlan-alrashidi" target="_blank">
linkedin.com/in/Ghzlan-alrashidi
</a>

</div>
""", unsafe_allow_html=True)

# ---------------- PROFILE ----------------

st.markdown("""
<div class="glass">

<div class="section-title">
PROFILE
</div>

<p style="font-size:22px; line-height:2; color:#f8fafc;">

Computer Science graduate with a strong academic record
(Second Class Honors).

Skilled in software development,
data analysis,
and web technologies,
with experience building efficient systems
and extracting actionable insights from data.

Passionate about problem-solving,
continuous learning,
and developing impactful technical solutions.

</p>

</div>
""", unsafe_allow_html=True)

# ---------------- EDUCATION ----------------

st.markdown("""
<div class="glass">

<div class="section-title">
EDUCATION
</div>

<p style="font-size:22px; line-height:2; color:#f8fafc;">

Bachelor of Science in Computer Science <br>

Al-Qassim University (2020 - 2025) <br>


Second-Class Honors

</p>

</div>
""", unsafe_allow_html=True)

# ---------------- TECHNICAL SKILLS ----------------

st.markdown("""
<div class="section-title">
TECHNICAL SKILLS
</div>
""", unsafe_allow_html=True)

skills = [
    "Python",
    "Flutter Development",
    "Django Framework",
    "Power BI",
    "Data Analysis",
    "HTML & CSS",
    "JavaScript Basics",
    "Git & GitHub",
    "WordPress",
    "OCR Technology"
]

cols = st.columns(5)

for i, skill in enumerate(skills):

    with cols[i % 5]:

        st.markdown(
            f'<div class="skill">{skill}</div>',
            unsafe_allow_html=True
        )

# ---------------- SOFT SKILLS ----------------

st.markdown("""
<div class="section-title">
SOFT SKILLS
</div>
""", unsafe_allow_html=True)

soft_skills = [
    "Problem Solving",
    "Analytical Thinking",
    "Team Collaboration",
    "Communication Skills",
    "Time Management",
    "Attention to Detail"
]

cols2 = st.columns(3)

for i, skill in enumerate(soft_skills):

    with cols2[i % 3]:

        st.markdown(
            f'<div class="skill">{skill}</div>',
            unsafe_allow_html=True
        )

# ---------------- PROJECTS ----------------

st.markdown("""
<div class="glass">

<div class="section-title">
PROJECTS
</div>

<p style="font-size:22px; line-height:2; color:#f8fafc;">

<strong>SmartLab | Graduation Project</strong><br><br>

• Developed a smart laboratory management system
using Python, Flutter, and SQLite.<br>

• Integrated OCR technology for automated text recognition
and data processing.<br>

• Designed a user-friendly interface
to improve laboratory workflow efficiency.<br>

• GitHub:
<a href="https://github.com/Ghzlan175" target="_blank">
github.com/Ghzlan175
</a>

</p>

</div>
""", unsafe_allow_html=True)

# ---------------- WORK EXPERIENCE ----------------

st.markdown("""
<div class="glass">

<div class="section-title">
WORK EXPERIENCE
</div>

<p style="font-size:22px; line-height:2; color:#f8fafc;">

<strong>
IT Intern | King Saud Hospital, Unaizah
(June 2024)
</strong>

<br><br>

• Developed and maintained the hospital website using WordPress.<br>

• Managed databases using SQLite.<br>

• Digitized hospital policies and documents.<br>

• Provided technical support for hardware and software systems.<br>

• Created internal reports and presentations
using Canva and Microsoft Office.

</p>

</div>
""", unsafe_allow_html=True)

# ---------------- LANGUAGES ----------------

st.markdown("""
<div class="glass">

<div class="section-title">
LANGUAGES
</div>

<p style="font-size:22px; line-height:2; color:#f8fafc;">

• Arabic <br>

• English

</p>

</div>
""", unsafe_allow_html=True)

# ---------------- QR CODE ----------------

drive_url = "https://drive.google.com/drive/folders/1iQAwK4MJc2qY7GIf2XUJyms26E8HoMtN?usp=drive_link"

st.markdown(f"""
<div class="glass qr-box">

<p style="font-size:20px; color:#f5d0fe;">
Click the QR Code to open my portfolio
</p>

<a href="{drive_url}" target="_blank">
<img src="data:image/jpeg;base64,{qr_base64}" width="260">
</a>

</div>
""", unsafe_allow_html=True)

# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer">

© 2026 Ghzlan AL-Rashidi

</div>
""", unsafe_allow_html=True)