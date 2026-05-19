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
background: linear-gradient(
135deg,
#050505,
#0f0a1f,
#1a0026
);
background-attachment: fixed;
overflow:hidden;
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

.hero-title{
font-size:100px;
font-weight:900;
line-height:1;
margin-top:80px;

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
font-size:32px;
color:#f5d0fe;
margin-top:20px;
margin-bottom:40px;

animation: fadeUp 1.5s ease;
}

/* ---------------- التواصل ---------------- */

.contact-box{
display:flex;
gap:20px;
flex-wrap:wrap;
margin-top:30px;
margin-bottom:30px;
}

.contact-card{
flex:1;
min-width:260px;

background: rgba(255,255,255,0.06);

padding:25px;

border-radius:25px;

backdrop-filter: blur(10px);

border:1px solid rgba(255,255,255,0.1);

transition:0.4s;

box-shadow:0px 0px 20px rgba(176,38,255,0.15);
}

.contact-card:hover{
transform:translateY(-8px);
box-shadow:0px 0px 35px rgba(255,79,216,0.35);
}

.contact-title{
font-size:24px;
font-weight:bold;
margin-bottom:15px;

background: linear-gradient(
90deg,
#ff4fd8,
#b026ff
);

-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.contact-text{
font-size:20px;
line-height:2;
color:#f8fafc;
}

/* ---------------- البطاقات ---------------- */

.glass{
background: rgba(255,255,255,0.05);

padding:35px;

border-radius:30px;

backdrop-filter: blur(12px);

margin-top:35px;

border:1px solid rgba(255,255,255,0.1);

box-shadow:0px 0px 20px rgba(176,38,255,0.15);

transition:0.4s;

animation: fadeUp 1s ease;
}

.glass:hover{
transform:translateY(-6px);
box-shadow:0px 0px 35px rgba(255,79,216,0.3);
}

.section-title{
font-size:40px;
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

/* ---------------- المهارات ---------------- */

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
transform:scale(1.08);
box-shadow:0px 0px 30px rgba(255,79,216,0.6);
}

/* ---------------- QR ---------------- */

.qr-box{
text-align:center;
margin-top:40px;
}

.qr-box img{
border-radius:25px;
transition:0.4s;
box-shadow:0px 0px 30px rgba(255,79,216,0.35);
}

.qr-box img:hover{
transform:scale(1.06);
box-shadow:0px 0px 45px rgba(255,79,216,0.6);
}

/* ---------------- دوائر متحركة ---------------- */

.floating{
position:fixed;
border-radius:50%;
filter:blur(2px);
animation:float 8s infinite ease-in-out;
z-index:-1;
opacity:0.35;
}

.circle1{
width:120px;
height:120px;
background:#ff4fd8;
top:10%;
left:5%;
}

.circle2{
width:180px;
height:180px;
background:#7a5cff;
top:40%;
right:8%;
animation-delay:2s;
}

.circle3{
width:100px;
height:100px;
background:#b026ff;
bottom:10%;
left:20%;
animation-delay:4s;
}

.circle4{
width:150px;
height:150px;
background:#ff4fd8;
bottom:20%;
right:15%;
animation-delay:1s;
}

@keyframes float{

0%{
transform:translateY(0px) translateX(0px);
}

50%{
transform:translateY(-30px) translateX(15px);
}

100%{
transform:translateY(0px) translateX(0px);
}

}

/* ---------------- شخصيات كرتونية تمشي ---------------- */

.walker{
position:fixed;
bottom:0;
font-size:60px;
z-index:999;
animation:walk 18s linear infinite;
}

.walker2{
position:fixed;
bottom:40px;
font-size:55px;
z-index:999;
animation:walk2 22s linear infinite;
}

@keyframes walk{

0%{
left:-10%;
}

100%{
left:110%;
}

}

@keyframes walk2{

0%{
right:-10%;
}

100%{
right:110%;
}

}

/* ---------------- الفوتر ---------------- */

.footer{
text-align:center;
padding:50px;
font-size:18px;
color:#c084fc;
}

/* ---------------- ظهور ناعم ---------------- */

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

# ---------------- عناصر متحركة ----------------

st.markdown("""
<div class="floating circle1"></div>
<div class="floating circle2"></div>
<div class="floating circle3"></div>
<div class="floating circle4"></div>

<div class="walker">👩🏻‍💻</div>
<div class="walker2">🚶🏻‍♀️</div>
""", unsafe_allow_html=True)

# ---------------- الرئيسية ----------------

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

# ---------------- التواصل ----------------

st.markdown("""
<div class="contact-box">

<div class="contact-card">
<div class="contact-title">Contact</div>

<div class="contact-text">

📞 +966 50 220 3750 <br>

📧 ghzlanalrashidi@gmail.com <br>

📍 Unaizah, Al-Qassim, Saudi Arabia

</div>
</div>

<div class="contact-card">
<div class="contact-title">Links</div>

<div class="contact-text">

🔗 github.com/Ghzlan175 <br><br>

🔗 linkedin.com/in/Ghzlan-alrashidi

</div>
</div>

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
and web technologies.

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

GPA : 4.70 / 5.00 <br>

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
    "Flutter",
    "Django",
    "Power BI",
    "Data Analysis",
    "HTML & CSS",
    "JavaScript",
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

• Integrated OCR technology for automated text recognition.<br>

• Designed a user-friendly interface
to improve workflow efficiency.

</p>

</div>
""", unsafe_allow_html=True)

# ---------------- EXPERIENCE ----------------

st.markdown("""
<div class="glass">

<div class="section-title">
WORK EXPERIENCE
</div>

<p style="font-size:22px; line-height:2; color:#f8fafc;">

<strong>
IT Intern | King Saud Hospital
</strong>

<br><br>

• Developed and maintained the hospital website using WordPress.<br>

• Managed databases using SQLite.<br>

• Provided technical support for systems.

</p>

</div>
""", unsafe_allow_html=True)

# ---------------- QR ----------------

drive_url = "https://drive.google.com/drive/folders/1iQAwK4MJc2qY7GIf2XUJyms26E8HoMtN?usp=drive_link"

st.markdown(f"""
<div class="glass qr-box">

<div class="section-title">
PORTFOLIO
</div>

<p style="font-size:20px; color:#f5d0fe;">
Click QR Code
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