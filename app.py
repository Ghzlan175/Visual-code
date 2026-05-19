import streamlit as st
import base64

# ---------------- إعداد الصفحة ----------------

st.set_page_config(
    page_title="Ghzlan AL-Rashidi",
    page_icon="✨",
    layout="wide"
)

# ---------------- QR Code ----------------

with open("QR.jpeg", "rb") as image_file:
    qr_base64 = base64.b64encode(image_file.read()).decode()

drive_url = "https://drive.google.com/drive/folders/1iQAwK4MJc2qY7GIf2XUJyms26E8HoMtN?usp=drive_link"

# ---------------- التصميم ----------------

st.markdown("""
<style>

html, body, [class*="css"]{
    font-family: sans-serif;
    color: white;
}

/* الخلفية */

[data-testid="stAppViewContainer"]{
    background:
    linear-gradient(
    135deg,
    #050505,
    #12061d,
    #1d0033
    );

    overflow-x:hidden;
}

/* الهيدر */

[data-testid="stHeader"]{
    background: rgba(0,0,0,0);
}

/* إزالة المسافات */

.block-container{
    padding-top: 2rem;
    padding-bottom: 6rem;
}

/* العنوان */

.hero-title{
    font-size:95px;
    font-weight:900;
    line-height:0.95;

    background: linear-gradient(
    90deg,
    #ff66d9,
    #c026ff,
    #7c3aed
    );

    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;

    animation: fadeUp 1s ease;
}

/* النص الفرعي */

.hero-sub{
    font-size:28px;
    color:#fbcfe8;
    margin-top:10px;
    margin-bottom:35px;

    animation: fadeUp 1.4s ease;
}

/* بطاقات */

.glass{
    background: rgba(255,255,255,0.05);

    padding:28px;

    border-radius:28px;

    backdrop-filter: blur(12px);

    border:1px solid rgba(255,255,255,0.08);

    margin-top:25px;

    transition:0.4s;

    animation: fadeUp 1s ease;
}

.glass:hover{
    transform: translateY(-5px);

    box-shadow:0px 0px 30px rgba(255,0,170,0.25);
}

/* العناوين */

.section-title{
    font-size:34px;
    font-weight:bold;
    margin-bottom:18px;

    background: linear-gradient(
    90deg,
    #ff66d9,
    #9333ea
    );

    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

/* النصوص */

.main-text{
    font-size:20px;
    line-height:1.7;
    color:#f8fafc;
}

/* المهارات */

.skill{
    background: linear-gradient(
    135deg,
    #ff4fd8,
    #7c3aed
    );

    padding:14px;

    border-radius:16px;

    text-align:center;

    font-weight:bold;

    margin:8px 0;

    color:white;

    transition:0.3s;
}

.skill:hover{
    transform:scale(1.05);
}

/* روابط */

a{
    color:#f9a8d4;
    text-decoration:none;
}

a:hover{
    color:white;
}

/* QR */

.qr-box{
    text-align:center;
}

.qr-box img{
    border-radius:25px;
    transition:0.4s;
}

.qr-box img:hover{
    transform:scale(1.06);
}

/* الأنيميشن */

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

/* الكائنات المتحركة */

.animation-area{
    position:fixed;
    bottom:0;
    left:0;
    width:100%;
    height:120px;
    pointer-events:none;
    z-index:999;
}

/* الديناصور */

.dino{
    position:absolute;
    bottom:10px;
    left:-120px;
    font-size:70px;

    animation: runDino 18s linear infinite;
}

/* القطوة */

.cat{
    position:absolute;
    bottom:12px;
    right:-120px;
    font-size:60px;

    animation: runCat 18s linear infinite;
}

@keyframes runDino{
    0%{
        left:-120px;
    }

    100%{
        left:110%;
    }
}

@keyframes runCat{
    0%{
        right:-120px;
    }

    100%{
        right:110%;
    }
}

/* الفوتر */

.footer{
    text-align:center;
    padding:50px;
    color:#c084fc;
    font-size:18px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- الكائنات المتحركة ----------------

st.markdown("""
<div class="animation-area">

<div class="dino">
🦖
</div>

<div class="cat">
🐈
</div>

</div>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------

st.markdown("""
<div class="hero-title">
Ghzlan <br>
AL-Rashidi
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-sub">
Computer Science Graduate
</div>
""", unsafe_allow_html=True)

# ---------------- التواصل ----------------

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="glass">

    <div class="section-title">
    Contact
    </div>

    <div class="main-text">

    📞 +966 50 220 3750<br>

    📧 ghzlanalrashidi@gmail.com<br>

    📍 Unaizah, Al-Qassim, Saudi Arabia

    </div>

    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="glass">

    <div class="section-title">
    Links
    </div>

    <div class="main-text">

    🔗 <a href="https://github.com/Ghzlan175" target="_blank">
    github.com/Ghzlan175
    </a><br><br>

    🔗 <a href="https://linkedin.com/in/Ghzlan-alrashidi" target="_blank">
    linkedin.com/in/Ghzlan-alrashidi
    </a>

    </div>

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
<div class="glass">

<div class="section-title">
Education
</div>

<div class="main-text">

<strong>Bachelor of Science in Computer Science</strong><br>

Al-Qassim University (2020 - 2025)<br>

GPA : 4.70 / 5.00<br>

Second-Class Honors

</div>

</div>
""", unsafe_allow_html=True)

# ---------------- المهارات ----------------

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
    "OCR Technology"
]

cols = st.columns(5)

for i, skill in enumerate(skills):

    with cols[i % 5]:

        st.markdown(
            f'<div class="skill">{skill}</div>',
            unsafe_allow_html=True
        )

# ---------------- المشاريع ----------------

st.markdown("""
<div class="glass">

<div class="section-title">
Projects
</div>

<div class="main-text">

<strong>SmartLab | Graduation Project</strong><br><br>

• Developed a smart laboratory management system
using Python, Flutter, and SQLite.<br>

• Integrated OCR technology
for automated text recognition.<br>

• Designed a user-friendly interface
to improve workflow efficiency.

</div>

</div>
""", unsafe_allow_html=True)

# ---------------- الخبرات ----------------

st.markdown("""
<div class="glass">

<div class="section-title">
Work Experience
</div>

<div class="main-text">

<strong>
IT Intern | King Saud Hospital
</strong><br><br>

• Developed and maintained
the hospital website using WordPress.<br>

• Managed databases using SQLite.<br>

• Provided technical support for systems.

</div>

</div>
""", unsafe_allow_html=True)

# ---------------- اللغات ----------------

st.markdown("""
<div class="glass">

<div class="section-title">
Languages
</div>

<div class="main-text">

• Arabic<br>
• English

</div>

</div>
""", unsafe_allow_html=True)

# ---------------- QR ----------------

st.markdown(f"""
<div class="glass qr-box">

<div class="section-title">
Portfolio QR Code
</div>

<div class="main-text">
Scan or click the QR Code
</div>

<br>

<a href="{drive_url}" target="_blank">
<img src="data:image/jpeg;base64,{qr_base64}" width="250">
</a>

</div>
""", unsafe_allow_html=True)

# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer">

© 2026 Ghzlan AL-Rashidi

</div>
""", unsafe_allow_html=True)