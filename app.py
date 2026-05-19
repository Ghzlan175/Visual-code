import streamlit as st
import base64

# ---------------- إعداد الصفحة ----------------

st.set_page_config(
    page_title="Ghzlan AL-Rashidi",
    page_icon="✨",
    layout="wide"
)

# ---------------- قراءة صورة QR ----------------

with open("QR.jpeg", "rb") as image_file:
    qr_base64 = base64.b64encode(image_file.read()).decode()

# ---------------- تصميم CSS ----------------

st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
background: linear-gradient(135deg, #050505, #0f0a1f, #1a0026);
background-attachment: fixed;
overflow-x:hidden;
}

[data-testid="stHeader"]{
background: rgba(0,0,0,0);
}

html, body, [class*="css"]{
color:white;
font-family:sans-serif;
scroll-behavior:smooth;
}

/* ---------------- العنوان ---------------- */

.hero{
padding-top:70px;
padding-bottom:30px;
animation: fadeUp 1s ease;
}

.hero-title{
font-size:90px;
font-weight:900;
line-height:1;
margin-bottom:15px;

background: linear-gradient(
90deg,
#ff4fd8,
#b026ff,
#7a5cff
);

-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.hero-sub{
font-size:28px;
color:#f5d0fe;
}

/* ---------------- التواصل ---------------- */

.contact-box{
display:flex;
gap:20px;
flex-wrap:wrap;
margin-top:25px;
margin-bottom:20px;
}

.contact-item{
flex:1;
min-width:260px;

background: rgba(255,255,255,0.05);

padding:22px;

border-radius:24px;

border:1px solid rgba(255,255,255,0.08);

font-size:19px;

line-height:2;
}

/* ---------------- البطاقات ---------------- */

.glass{
background: rgba(255,255,255,0.05);

padding:28px;

border-radius:28px;

backdrop-filter: blur(12px);

margin-top:25px;

border:1px solid rgba(255,255,255,0.08);

box-shadow:0px 0px 18px rgba(176,38,255,0.15);

transition:0.4s;

animation: fadeUp 1s ease;
}

.glass:hover{
transform:translateY(-5px);
box-shadow:0px 0px 30px rgba(255,79,216,0.28);
}

.section-title{
font-size:34px;
font-weight:800;
margin-bottom:18px;

background: linear-gradient(
90deg,
#ff4fd8,
#b026ff
);

-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.text{
font-size:20px;
line-height:1.9;
color:#f3f4f6;
}

/* ---------------- المهارات ---------------- */

.skill{
background: linear-gradient(
135deg,
#ff4fd8,
#7a5cff
);

padding:15px;

border-radius:18px;

text-align:center;

font-size:17px;

font-weight:bold;

margin:8px;

color:white;

transition:0.3s;

box-shadow:0px 0px 15px rgba(176,38,255,0.25);
}

.skill:hover{
transform:scale(1.05);
}

/* ---------------- الروابط ---------------- */

a{
color:#f9a8d4;
text-decoration:none;
font-weight:bold;
}

a:hover{
color:white;
}

/* ---------------- QR ---------------- */

.qr-box{
text-align:center;
}

.qr-box img{
border-radius:25px;
transition:0.4s;
box-shadow:0px 0px 25px rgba(255,79,216,0.3);
}

.qr-box img:hover{
transform:scale(1.05);
}

/* ---------------- القطة المتحركة ---------------- */

.cat{
position:fixed;
bottom:0;
right:-220px;
width:140px;
z-index:9999;
animation: walk 20s linear infinite;
pointer-events:none;
}

@keyframes walk{
0%{
right:-220px;
}

100%{
right:110%;
}
}

/* ---------------- ظهور العناصر ---------------- */

.fade-section{
animation: fadeUp 1s ease;
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

/* ---------------- الفوتر ---------------- */

.footer{
text-align:center;
padding:50px;
font-size:18px;
color:#c084fc;
}

</style>
""", unsafe_allow_html=True)

# ---------------- القطة المتحركة ----------------

st.markdown("""
<img class="cat" src="cat.gif">
""", unsafe_allow_html=True)

# ---------------- العنوان ----------------

st.markdown("""
<div class="hero">

<div class="hero-title">
Ghzlan <br>
AL-Rashidi
</div>

<div class="hero-sub">
Computer Science Graduate
</div>

</div>
""", unsafe_allow_html=True)

# ---------------- التواصل ----------------

st.markdown("""
<div class="contact-box">

<div class="contact-item">

📞 +966 50 220 3750 <br>

📧 ghzlanalrashidi@gmail.com <br>

📍 Unaizah, Al-Qassim, Saudi Arabia

</div>

<div class="contact-item">

🔗 <a href="https://github.com/Ghzlan175" target="_blank">
github.com/Ghzlan175
</a>

<br><br>

🔗 <a href="https://linkedin.com/in/Ghzlan-alrashidi" target="_blank">
linkedin.com/in/Ghzlan-alrashidi
</a>

</div>

</div>
""", unsafe_allow_html=True)

# ---------------- PROFILE ----------------

st.markdown("""
<div class="glass fade-section">

<div class="section-title">
Profile
</div>

<div class="text">

Computer Science graduate with a strong academic record
(Second Class Honors).

Skilled in software development,
data analysis,
and web technologies.

Passionate about problem-solving,
continuous learning,
and developing impactful technical solutions.

</div>

</div>
""", unsafe_allow_html=True)

# ---------------- EDUCATION ----------------

st.markdown("""
<div class="glass fade-section">

<div class="section-title">
Education
</div>

<div class="text">

Bachelor of Science in Computer Science <br><br>

Al-Qassim University (2020 - 2025) <br><br>

GPA : 4.70 / 5.00 <br><br>

Second-Class Honors

</div>

</div>
""", unsafe_allow_html=True)

# ---------------- TECHNICAL SKILLS ----------------

st.markdown("""
<div class="section-title">
Technical Skills
</div>
""", unsafe_allow_html=True)

skills = [
    "Python",
    "Flutter",
    "Django",
    "Power BI",
    "Data Analysis",
    "HTML & CSS",
    "JavaScript",
    "Git & GitHub",
    "WordPress",
    "OCR"
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
Soft Skills
</div>
""", unsafe_allow_html=True)

soft_skills = [
    "Problem Solving",
    "Communication",
    "Analytical Thinking",
    "Time Management",
    "Team Collaboration",
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
<div class="glass fade-section">

<div class="section-title">
Projects
</div>

<div class="text">

<b>SmartLab | Graduation Project</b><br><br>

• Developed a smart laboratory management system
using Python, Flutter, and SQLite.<br><br>

• Integrated OCR technology for automated text recognition.<br><br>

• Designed a user-friendly interface to improve workflow efficiency.

</div>

</div>
""", unsafe_allow_html=True)

# ---------------- WORK EXPERIENCE ----------------

st.markdown("""
<div class="glass fade-section">

<div class="section-title">
Work Experience
</div>

<div class="text">

<b>IT Intern | King Saud Hospital</b><br><br>

• Developed and maintained the hospital website using WordPress.<br><br>

• Managed databases using SQLite.<br><br>

• Provided technical support for systems.

</div>

</div>
""", unsafe_allow_html=True)

# ---------------- LANGUAGES ----------------

st.markdown("""
<div class="glass fade-section">

<div class="section-title">
Languages
</div>

<div class="text">

• Arabic <br><br>

• English

</div>

</div>
""", unsafe_allow_html=True)

# ---------------- QR CODE ----------------

drive_url = "https://drive.google.com/drive/folders/1iQAwK4MJc2qY7GIf2XUJyms26E8HoMtN?usp=drive_link"

st.markdown(f"""
<div class="glass qr-box fade-section">

<div class="section-title">
Portfolio QR Code
</div>

<p class="text">
Click the QR Code
</p>

<a href="{drive_url}" target="_blank">
<img src="data:image/jpeg;base64,{qr_base64}" width="240">
</a>

</div>
""", unsafe_allow_html=True)

# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer">

© 2026 Ghzlan AL-Rashidi

</div>
""", unsafe_allow_html=True)