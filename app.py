import streamlit as st

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Ghzlan AL-Rashidi",
    page_icon="✨",
    layout="wide"
)

# ---------------- SETTINGS ----------------

with st.sidebar:

    st.title("⚙️ Settings")

    theme = st.selectbox(
        "Theme",
        ["Dark", "Light"]
    )

    language = st.selectbox(
        "Language",
        ["English", "العربية"]
    )

# ---------------- COLORS ----------------

if theme == "Dark":

    background = "linear-gradient(135deg, #050505, #0f0a1f, #1a0026)"
    text_color = "white"
    card_bg = "rgba(255,255,255,0.05)"

else:

    background = "linear-gradient(135deg, #ffffff, #fdf2f8, #ede9fe)"
    text_color = "#111827"
    card_bg = "rgba(255,255,255,0.9)"

# ---------------- LANGUAGE ----------------

if language == "English":

    hero_job = "Computer Science Graduate"

    profile_title = "PROFILE"

    profile_text = """
    Computer Science graduate with a strong academic record
    (Second Class Honors).

    Skilled in software development,
    data analysis,
    and web technologies.

    Passionate about problem-solving,
    continuous learning,
    and developing impactful technical solutions.
    """

    education_title = "EDUCATION"

    education_text = """
    Bachelor of Science in Computer Science <br>

    Al-Qassim University (2020 - 2025) <br>

    GPA : 4.70 / 5.00 <br>

    Second-Class Honors
    """

    skills_title = "TECHNICAL SKILLS"

    soft_title = "SOFT SKILLS"

    project_title = "PROJECTS"

    project_text = """
    <strong>SmartLab | Graduation Project</strong><br><br>

    • Developed a smart laboratory management system using Python, Flutter, and SQLite.<br>

    • Integrated OCR technology for automated text recognition.<br>

    • Designed a user-friendly interface to improve workflow efficiency.
    """

    work_title = "WORK EXPERIENCE"

    work_text = """
    <strong>IT Intern | King Saud Hospital</strong><br><br>

    • Developed and maintained the hospital website using WordPress.<br>

    • Managed databases using SQLite.<br>

    • Provided technical support for systems.
    """

    lang_title = "LANGUAGES"

    lang_text = """
    • Arabic <br>
    • English
    """

    contact_title = "CONTACT"

    links_title = "LINKS"

    comments_title = "COMMENTS"

    comment_placeholder = "Write your comment here..."

    send_btn = "Send"

else:

    hero_job = "خريجة علوم حاسب"

    profile_title = "نبذة عني"

    profile_text = """
    خريجة علوم حاسب بمعدل مرتفع ومرتبة الشرف الثانية.

    لدي خبرة في تطوير البرمجيات وتحليل البيانات
    وتقنيات الويب الحديثة.

    شغوفة بحل المشكلات والتعلم المستمر
    وبناء حلول تقنية فعالة.
    """

    education_title = "التعليم"

    education_text = """
    بكالوريوس علوم الحاسب <br>

    جامعة القصيم (2020 - 2025) <br>

    المعدل : 4.70 / 5.00 <br>

    مرتبة الشرف الثانية
    """

    skills_title = "المهارات التقنية"

    soft_title = "المهارات الشخصية"

    project_title = "المشاريع"

    project_text = """
    <strong>SmartLab | مشروع التخرج</strong><br><br>

    • تطوير نظام ذكي لإدارة المختبرات باستخدام Python و Flutter و SQLite.<br>

    • دمج تقنية OCR للتعرف التلقائي على النصوص.<br>

    • تصميم واجهة سهلة لتحسين كفاءة العمل.
    """

    work_title = "الخبرات"

    work_text = """
    <strong>متدربة تقنية معلومات | مستشفى الملك سعود</strong><br><br>

    • تطوير وصيانة موقع المستشفى باستخدام WordPress.<br>

    • إدارة قواعد البيانات باستخدام SQLite.<br>

    • تقديم الدعم التقني للأنظمة والأجهزة.
    """

    lang_title = "اللغات"

    lang_text = """
    • العربية <br>
    • الإنجليزية
    """

    contact_title = "التواصل"

    links_title = "الروابط"

    comments_title = "التعليقات"

    comment_placeholder = "اكتب تعليقك هنا..."

    send_btn = "إرسال"

# ---------------- CSS ----------------

st.markdown(f"""
<style>

[data-testid="stAppViewContainer"]{{
background:{background};
background-attachment:fixed;
}}

[data-testid="stHeader"]{{
background: rgba(0,0,0,0);
}}

html, body, [class*="css"]{{
color:{text_color};
font-family:sans-serif;
scroll-behavior:smooth;
}}

.hero-title{{
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
}}

.hero-sub{{
font-size:30px;
margin-top:20px;
margin-bottom:40px;
}}

.glass{{
background:{card_bg};
padding:35px;
border-radius:30px;
backdrop-filter: blur(12px);
margin-top:30px;
border:1px solid rgba(255,255,255,0.1);
box-shadow:0px 0px 20px rgba(176,38,255,0.15);
transition:0.4s;
}}

.glass:hover{{
transform:translateY(-6px);
box-shadow:0px 0px 35px rgba(255,79,216,0.25);
}}

.section-title{{
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
}}

.skill{{
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
}}

.skill:hover{{
transform:scale(1.05);
}}

.footer{{
text-align:center;
padding:50px;
font-size:18px;
color:#c084fc;
}}

a{{
color:#f472b6;
text-decoration:none;
}}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------

st.markdown("""
<h1 class="hero-title">
Ghzlan <br>
AL-Rashidi
</h1>
""", unsafe_allow_html=True)

st.markdown(f"""
<p class="hero-sub">
{hero_job}
</p>
""", unsafe_allow_html=True)

# ---------------- CONTACT ----------------

col1, col2 = st.columns(2)

with col1:

    st.markdown(f"""
    <div class="glass">

    <div class="section-title">
    {contact_title}
    </div>

    📞 +966 50 220 3750 <br><br>

    📧 ghzlanalrashidi@gmail.com <br><br>

    📍 Unaizah, Al-Qassim, Saudi Arabia

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown(f"""
    <div class="glass">

    <div class="section-title">
    {links_title}
    </div>

    🔗 <a href="https://github.com/Ghzlan175" target="_blank">
    github.com/Ghzlan175
    </a><br><br>

    🔗 <a href="https://linkedin.com/in/Ghzlan-alrashidi" target="_blank">
    linkedin.com/in/Ghzlan-alrashidi
    </a>

    </div>
    """, unsafe_allow_html=True)

# ---------------- PROFILE ----------------

st.markdown(f"""
<div class="glass">

<div class="section-title">
{profile_title}
</div>

<p style="font-size:22px; line-height:2;">

{profile_text}

</p>

</div>
""", unsafe_allow_html=True)

# ---------------- EDUCATION ----------------

st.markdown(f"""
<div class="glass">

<div class="section-title">
{education_title}
</div>

<p style="font-size:22px; line-height:2;">

{education_text}

</p>

</div>
""", unsafe_allow_html=True)

# ---------------- TECHNICAL SKILLS ----------------

st.markdown(f"""
<div class="section-title">
{skills_title}
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

st.markdown(f"""
<div class="section-title">
{soft_title}
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

st.markdown(f"""
<div class="glass">

<div class="section-title">
{project_title}
</div>

<p style="font-size:22px; line-height:2;">

{project_text}

</p>

</div>
""", unsafe_allow_html=True)

# ---------------- WORK EXPERIENCE ----------------

st.markdown(f"""
<div class="glass">

<div class="section-title">
{work_title}
</div>

<p style="font-size:22px; line-height:2;">

{work_text}

</p>

</div>
""", unsafe_allow_html=True)

# ---------------- LANGUAGES ----------------

st.markdown(f"""
<div class="glass">

<div class="section-title">
{lang_title}
</div>

<p style="font-size:22px; line-height:2;">

{lang_text}

</p>

</div>
""", unsafe_allow_html=True)

# ---------------- COMMENTS ----------------

st.markdown(f"""
<div class="glass">

<div class="section-title">
{comments_title}
</div>

</div>
""", unsafe_allow_html=True)

comment = st.text_area("", placeholder=comment_placeholder)

if st.button(send_btn):

    st.success("✔")

# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer">

© 2026 Ghzlan AL-Rashidi

</div>
""", unsafe_allow_html=True)