import streamlit as st
import base64

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Ghzlan AL-Rashidi",
    page_icon="✨",
    layout="wide"
)

# ---------------- QR CODE ----------------

with open("QR.jpeg", "rb") as image_file:
    qr_base64 = base64.b64encode(image_file.read()).decode()

drive_url = "https://drive.google.com/drive/folders/1iQAwK4MJc2qY7GIf2XUJyms26E8HoMtN?usp=drive_link"

# ---------------- STYLE ----------------

st.markdown("""
<style>

html{
scroll-behavior:smooth;
}

body{
overflow-x:hidden;
}

[data-testid="stAppViewContainer"]{
background:
linear-gradient(
135deg,
#050505,
#13051f,
#1f0930
);
background-attachment:fixed;
color:white;
overflow-x:hidden;
}

[data-testid="stHeader"]{
background:rgba(0,0,0,0);
}

.block-container{
padding-top:3rem;
padding-bottom:5rem;
max-width:1200px;
}

/* ---------------- HERO ---------------- */

.hero{
padding-top:60px;
padding-bottom:60px;
animation:fadeUp 1s ease;
}

.hero-title{
font-size:110px;
font-weight:900;
line-height:0.9;

background:linear-gradient(
90deg,
#ff4fd8,
#c026ff,
#7c4dff
);

-webkit-background-clip:text;
-webkit-text-fill-color:transparent;

margin-bottom:20px;
}

.hero-sub{
font-size:32px;
color:#f5d0fe;
margin-bottom:40px;
font-weight:500;
}

/* ---------------- GLASS CARDS ---------------- */

.glass{
background:rgba(255,255,255,0.05);

padding:40px;

border-radius:35px;

margin-top:35px;

border:1px solid rgba(255,255,255,0.08);

backdrop-filter:blur(15px);

box-shadow:
0px 0px 30px rgba(176,38,255,0.15);

transition:0.4s;

animation:fadeUp 1s ease;
}

.glass:hover{
transform:translateY(-8px);

box-shadow:
0px 0px 45px rgba(255,79,216,0.25);
}

/* ---------------- TITLES ---------------- */

.section-title{
font-size:42px;
font-weight:800;
margin-bottom:28px;

background:linear-gradient(
90deg,
#ff4fd8,
#b026ff
);

-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

/* ---------------- TEXT ---------------- */

.main-text{
font-size:22px;
line-height:2.2;
color:#f8fafc;
}

/* ---------------- CONTACT ---------------- */

.contact-box{
background:rgba(255,255,255,0.05);

padding:24px;

border-radius:22px;

text-align:center;

font-size:20px;

margin-bottom:20px;

border:1px solid rgba(255,255,255,0.08);

transition:0.3s;
}

.contact-box:hover{
transform:translateY(-5px);

background:rgba(255,255,255,0.08);
}

/* ---------------- SKILLS ---------------- */

.skill{
background:linear-gradient(
135deg,
#ff4fd8,
#7c4dff
);

padding:18px;

border-radius:18px;

text-align:center;

font-size:18px;

font-weight:bold;

margin:8px;

color:white;

transition:0.4s;

box-shadow:
0px 0px 15px rgba(176,38,255,0.25);
}

.skill:hover{
transform:scale(1.05);

box-shadow:
0px 0px 30px rgba(255,79,216,0.35);
}

/* ---------------- QR ---------------- */

.qr-box{
text-align:center;
}

.qr-box img{
border-radius:28px;

transition:0.4s;

box-shadow:
0px 0px 25px rgba(255,79,216,0.25);
}

.qr-box img:hover{
transform:scale(1.06);

box-shadow:
0px 0px 50px rgba(255,79,216,0.45);
}

/* ---------------- FOOTER ---------------- */

.footer{
text-align:center;
padding-top:50px;
padding-bottom:20px;
font-size:18px;
color:#d8b4fe;
}

/* ---------------- LINKS ---------------- */

a{
color:#f9a8d4;
text-decoration:none;
}

a:hover{
color:white;
}

/* ---------------- ANIMATION ---------------- */

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

/* ---------------- MOVING OBJECTS ---------------- */

.float{
position:fixed;
bottom:15px;
font-size:42px;
z-index:999;
pointer-events:none;
opacity:0.85;
}

.f1{
left:-10%;
animation:move1 16s linear infinite;
}

.f2{
left:-20%;
bottom:80px;
animation:move2 24s linear infinite;
}

.f3{
left:-30%;
bottom:145px;
animation:move3 30s linear infinite;
}

@keyframes move1{
0%{transform:translateX(0);}
100%{transform:translateX(140vw);}
}

@keyframes move2{
0%{transform:translateX(0);}
100%{transform:translateX(150vw);}
}

@keyframes move3{
0%{transform:translateX(0);}
100%{transform:translateX(160vw);}
}

</style>
""", unsafe_allow_html=True)

# ---------------- MOVING OBJECTS ----------------

st.markdown("""
<div class="float f1">💜</div>
<div class="float f2">✨</div>
<div class="float f3">🩷</div>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------

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

# ---------------- CONTACT ----------------

st.markdown("""
<div class="section-title">
Contact
</div>
""", unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:

    st.markdown("""
    <div class="contact-box">
    📞 +966 50 220 3750
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="contact-box">
    📧 ghzlanalrashidi@gmail.com
    </div>
    """, unsafe_allow_html=True)

with c2:

    st.markdown("""
    <div class="contact-box">
    📍 Unaizah, Al-Qassim, Saudi Arabia
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="contact-box">

    🔗
    <a href="https://github.com/Ghzlan175" target="_blank">
    github.com/Ghzlan175
    </a>

    <br><br>

    🔗
    <a href="https://linkedin.com/in/Ghzlan-alrashidi" target="_blank">
    linkedin.com/in/Ghzlan-alrashidi
    </a>

    </div>
    """, unsafe_allow_html=True)

# ---------------- PROFILE ----------------

st.markdown("""
<div class="glass">

<div class="section-title">
Profile
</div>

<div class="main-text">

Computer Science graduate with a strong academic record
(Second Class Honors).

<br><br>

Skilled in software development,
data analysis,
and web technologies.

<br><br>

Passionate about problem-solving,
continuous learning,
and developing impactful technical solutions.

</div>

</div>
""", unsafe_allow_html=True)

# ---------------- EDUCATION ----------------

st.markdown("""
<div class="glass">

<div class="section-title">
Education
</div>

<div class="main-text">

Bachelor of Science in Computer Science

<br><br>

Al-Qassim University (2020 - 2025)

<br><br>

GPA : 4.70 / 5.00

<br><br>

Second-Class Honors

</div>

</div>
""", unsafe_allow_html=True)

# ---------------- TECHNICAL SKILLS ----------------

st.markdown("""
<div class="glass">

<div class="section-title">
Technical Skills
</div>

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
<div class="glass">

<div class="section-title">
Soft Skills
</div>

</div>
""", unsafe_allow_html=True)

soft = [
    "Problem Solving",
    "Communication",
    "Analytical Thinking",
    "Time Management",
    "Team Collaboration",
    "Attention to Detail"
]

cols2 = st.columns(3)

for i, skill in enumerate(soft):

    with cols2[i % 3]:

        st.markdown(
            f'<div class="skill">{skill}</div>',
            unsafe_allow_html=True
        )

# ---------------- PROJECTS ----------------

st.markdown("""
<div class="glass">

<div class="section-title">
Projects
</div>

<div class="main-text">

<strong>SmartLab | Graduation Project</strong>

<br><br>

• Developed a smart laboratory management system
using Python, Flutter, and SQLite.

<br><br>

• Integrated OCR technology for automated text recognition.

<br><br>

• Designed a user-friendly interface
to improve workflow efficiency.

</div>

</div>
""", unsafe_allow_html=True)

# ---------------- EXPERIENCE ----------------

st.markdown("""
<div class="glass">

<div class="section-title">
Work Experience
</div>

<div class="main-text">

<strong>
IT Intern | King Saud Hospital
</strong>

<br><br>

• Developed and maintained the hospital website using WordPress.

<br><br>

• Managed databases using SQLite.

<br><br>

• Provided technical support for systems.

</div>

</div>
""", unsafe_allow_html=True)

# ---------------- LANGUAGES ----------------

st.markdown("""
<div class="glass">

<div class="section-title">
Languages
</div>

<div class="main-text">

• Arabic

<br><br>

• English

</div>

</div>
""", unsafe_allow_html=True)

# ---------------- QR CODE ----------------

st.markdown(f"""
<div class="glass qr-box">

<div class="section-title">
Portfolio QR Code
</div>

<p style="
font-size:22px;
color:#f5d0fe;
margin-bottom:30px;
">

Click the QR Code

</p>

<a href="{drive_url}" target="_blank">

<img src="data:image/jpeg;base64,{qr_base64}" width="270">

</a>

</div>
""", unsafe_allow_html=True)

# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer">

© 2026 Ghzlan AL-Rashidi

</div>
""", unsafe_allow_html=True)