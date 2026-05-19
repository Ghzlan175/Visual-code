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

drive_url = "https://drive.google.com/drive/folders/1iQAwK4MJc2qY7GIf2XUJyms26E8HoMtN?usp=drive_link"

# ---------------- التصميم ----------------

st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
background: linear-gradient(
135deg,
#050505,
#12051f,
#1f0a2e
);
background-attachment: fixed;
overflow-x:hidden;
}

[data-testid="stHeader"]{
background: rgba(0,0,0,0);
}

html, body, [class*="css"]{
font-family:sans-serif;
color:white;
scroll-behavior:smooth;
}

.block-container{
padding-top:2rem;
padding-bottom:4rem;
}

.hero-title{
font-size:100px;
font-weight:900;
line-height:1;

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

.glass{
background: rgba(255,255,255,0.05);
padding:35px;
border-radius:30px;
backdrop-filter: blur(12px);
margin-top:30px;
border:1px solid rgba(255,255,255,0.08);

box-shadow:
0px 0px 20px rgba(176,38,255,0.12);

transition:0.4s;

animation: fadeUp 1s ease;
}

.glass:hover{
transform:translateY(-8px);
box-shadow:
0px 0px 40px rgba(255,79,216,0.25);
}

.section-title{
font-size:38px;
font-weight:800;
margin-bottom:20px;

background: linear-gradient(
90deg,
#ff4fd8,
#b026ff
);

-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.contact-card{
background: rgba(255,255,255,0.05);
padding:20px;
border-radius:20px;
text-align:center;
font-size:20px;
margin:10px;
border:1px solid rgba(255,255,255,0.08);

transition:0.3s;
}

.contact-card:hover{
transform:translateY(-5px);
background: rgba(255,255,255,0.08);
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

box-shadow:
0px 0px 15px rgba(176,38,255,0.3);
}

.skill:hover{
transform:scale(1.05);
box-shadow:
0px 0px 30px rgba(255,79,216,0.4);
}

.qr-box{
text-align:center;
}

.qr-box img{
border-radius:25px;
transition:0.4s;

box-shadow:
0px 0px 25px rgba(255,79,216,0.25);
}

.qr-box img:hover{
transform:scale(1.05);

box-shadow:
0px 0px 45px rgba(255,79,216,0.5);
}

.footer{
text-align:center;
padding:40px;
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

/* الأنيميشن */

.fade-section{
animation: fadeUp 1s ease;
}

@keyframes fadeUp{

from{
opacity:0;
transform:translateY(60px);
}

to{
opacity:1;
transform:translateY(0px);
}

}

/* الشخصيات الكرتونية */

.character{
position:fixed;
bottom:20px;
z-index:999;
font-size:45px;
animation: moveCharacter linear infinite;
opacity:0.9;
}

.character1{
left:-100px;
animation-duration:18s;
}

.character2{
left:-200px;
bottom:80px;
animation-duration:25s;
}

.character3{
left:-300px;
bottom:140px;
animation-duration:30s;
}

@keyframes moveCharacter{
0%{
transform:translateX(0);
}
100%{
transform:translateX(130vw);
}
}

</style>
""", unsafe_allow_html=True)

# ---------------- الرسوم المتحركة ----------------

st.markdown("""
<div class="character character1">🩷</div>
<div class="character character2">✨</div>
<div class="character character3">💜</div>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------

st.markdown("""
<div class="fade-section">

<h1 class="hero-title">
Ghzlan <br>
AL-Rashidi
</h1>

<p class="hero-sub">
Computer Science Graduate
</p>

</div>
""", unsafe_allow_html=True)

# ---------------- CONTACT ----------------

st.markdown("""
<div class="section-title">
Contact
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="contact-card">
    📞 +966 50 220 3750
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="contact-card">
    📧 ghzlanalrashidi@gmail.com
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="contact-card">
    📍 Unaizah, Al-Qassim, Saudi Arabia
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="contact-card">
    🔗 <a href="https://github.com/Ghzlan175" target="_blank">
    github.com/Ghzlan175
    </a>

    <br><br>

    🔗 <a href="https://linkedin.com/in/Ghzlan-alrashidi" target="_blank">
    linkedin.com/in/Ghzlan-alrashidi
    </a>
    </div>
    """, unsafe_allow_html=True)

# ---------------- PROFILE ----------------

st.markdown("""
<div class="glass fade-section">

<div class="section-title">
Profile
</div>

<p style="font-size:22px; line-height:2; color:#f8fafc;">

Computer Science graduate with a strong academic record
(Second Class Honors).

Skilled in software development,
data analysis,
and web technologies.

Passionate about problem-solving,
continuous learning,
and developing impactful technical solutions.

</p>

</div>
""", unsafe_allow_html=True)

# ---------------- EDUCATION ----------------

st.markdown("""
<div class="glass fade-section">

<div class="section-title">
Education
</div>

<p style="font-size:22px; line-height:2;">

Bachelor of Science in Computer Science <br>

Al-Qassim University (2020 - 2025) <br>

GPA : 4.70 / 5.00 <br>

Second-Class Honors

</p>

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

<p style="font-size:22px; line-height:2;">

<strong>SmartLab | Graduation Project</strong>

<br><br>

• Developed a smart laboratory management system
using Python, Flutter, and SQLite.

<br><br>

• Integrated OCR technology for automated text recognition.

<br><br>

• Designed a user-friendly interface
to improve workflow efficiency.

</p>

</div>
""", unsafe_allow_html=True)

# ---------------- EXPERIENCE ----------------

st.markdown("""
<div class="glass fade-section">

<div class="section-title">
Work Experience
</div>

<p style="font-size:22px; line-height:2;">

<strong>
IT Intern | King Saud Hospital
</strong>

<br><br>

• Developed and maintained the hospital website using WordPress.

<br><br>

• Managed databases using SQLite.

<br><br>

• Provided technical support for systems.

</p>

</div>
""", unsafe_allow_html=True)

# ---------------- LANGUAGES ----------------

st.markdown("""
<div class="glass fade-section">

<div class="section-title">
Languages
</div>

<p style="font-size:22px; line-height:2;">

• Arabic

<br><br>

• English

</p>

</div>
""", unsafe_allow_html=True)

# ---------------- QR CODE ----------------

st.markdown(f"""
<div class="glass qr-box fade-section">

<div class="section-title">
Portfolio QR Code
</div>

<p style="font-size:20px; color:#f5d0fe;">
Click the QR Code
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