import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
import json
import io
import base64
import re
import os
from datetime import datetime

# Load saved keys from .env file if it exists
try:
    from dotenv import load_dotenv
    load_dotenv(dotenv_path=".env", override=False)
    DOTENV_AVAILABLE = True
except ImportError:
    DOTENV_AVAILABLE = False
import anthropic
try:
    from groq import Groq
    GROQ_AVAILABLE = True
except ImportError:
    GROQ_AVAILABLE = False
try:
    import PyPDF2
    PDF_SUPPORT = True
except ImportError:
    try:
        import pypdf as PyPDF2
        PDF_SUPPORT = True
    except ImportError:
        PDF_SUPPORT = False

# ─────────────────────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CareerCompass AI",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────────────────────────────────────
# CUSTOM CSS — refined dark-accented theme
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

:root {
    --bg: #0d0f14;
    --surface: #161920;
    --surface2: #1e2230;
    --accent: #6c63ff;
    --accent2: #00d4aa;
    --accent3: #ff6b6b;
    --text: #e8eaf0;
    --muted: #8b90a0;
    --border: #2a2f40;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    color: var(--text);
}

.stApp { background: var(--bg); }

h1, h2, h3, h4 {
    font-family: 'Syne', sans-serif !important;
    font-weight: 700;
}

.main-header {
    background: linear-gradient(135deg, #6c63ff22 0%, #00d4aa11 100%);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 2rem 2.5rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
}
.main-header::before {
    content: '🧭';
    position: absolute;
    right: 2rem;
    top: 50%;
    transform: translateY(-50%);
    font-size: 5rem;
    opacity: 0.12;
}
.main-header h1 {
    font-size: 2.6rem;
    background: linear-gradient(135deg, #6c63ff, #00d4aa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0 0 0.4rem 0;
}
.main-header p {
    color: var(--muted);
    font-size: 1.05rem;
    margin: 0;
}

.step-indicator {
    display: flex;
    gap: 0.5rem;
    margin-bottom: 1.5rem;
    align-items: center;
}
.step-dot {
    width: 32px; height: 32px;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    font-size: 0.85rem;
    border: 2px solid var(--border);
    color: var(--muted);
    background: var(--surface);
    transition: all 0.3s;
}
.step-dot.active {
    background: var(--accent);
    border-color: var(--accent);
    color: white;
    box-shadow: 0 0 16px #6c63ff55;
}
.step-dot.done {
    background: var(--accent2);
    border-color: var(--accent2);
    color: #0d0f14;
}
.step-line {
    flex: 1;
    height: 2px;
    background: var(--border);
    border-radius: 1px;
}
.step-line.done { background: var(--accent2); }

.card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1rem;
}
.career-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1.6rem;
    margin-bottom: 1.2rem;
    position: relative;
    overflow: hidden;
    transition: border-color 0.3s;
}
.career-card:hover { border-color: var(--accent); }
.career-card .rank-badge {
    position: absolute;
    top: 1rem; right: 1rem;
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    color: white;
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: 0.75rem;
    padding: 0.25rem 0.7rem;
    border-radius: 20px;
    letter-spacing: 0.05em;
}
.career-card h3 {
    font-family: 'Syne', sans-serif;
    font-size: 1.3rem;
    color: var(--text);
    margin: 0 0 0.4rem 0;
}
.career-card .description {
    color: var(--muted);
    font-size: 0.93rem;
    margin-bottom: 1rem;
}

.match-bar-container {
    margin: 0.6rem 0;
}
.match-bar-label {
    display: flex;
    justify-content: space-between;
    font-size: 0.82rem;
    color: var(--muted);
    margin-bottom: 0.3rem;
}
.match-bar-track {
    background: var(--border);
    border-radius: 4px;
    height: 6px;
    overflow: hidden;
}
.match-bar-fill {
    height: 100%;
    border-radius: 4px;
    background: linear-gradient(90deg, var(--accent), var(--accent2));
    transition: width 0.8s ease;
}

.skill-tag {
    display: inline-block;
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 0.2rem 0.7rem;
    font-size: 0.78rem;
    color: var(--muted);
    margin: 0.15rem;
}
.skill-tag.have {
    background: #00d4aa18;
    border-color: #00d4aa55;
    color: var(--accent2);
}
.skill-tag.missing {
    background: #ff6b6b18;
    border-color: #ff6b6b55;
    color: var(--accent3);
}

.stat-chip {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 0.3rem 0.8rem;
    font-size: 0.82rem;
    color: var(--muted);
    margin: 0.2rem;
}

.info-box {
    background: #6c63ff11;
    border: 1px solid #6c63ff33;
    border-radius: 10px;
    padding: 0.9rem 1.2rem;
    font-size: 0.88rem;
    color: var(--muted);
    margin-bottom: 1rem;
}

.metric-card {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.2rem;
    text-align: center;
}
.metric-value {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.metric-label {
    font-size: 0.8rem;
    color: var(--muted);
    margin-top: 0.3rem;
}

/* Streamlit widget overrides */
.stButton > button {
    background: linear-gradient(135deg, var(--accent), #8b5cf6) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 600 !important;
    padding: 0.6rem 1.8rem !important;
    transition: opacity 0.2s !important;
}
.stButton > button:hover { opacity: 0.88 !important; }

div[data-testid="stSelectbox"] > div,
div[data-testid="stTextInput"] > div > div {
    background: var(--surface2) !important;
    border-color: var(--border) !important;
    border-radius: 8px !important;
    color: var(--text) !important;
}

.stProgress > div > div {
    background: linear-gradient(90deg, var(--accent), var(--accent2)) !important;
}

.stFileUploader {
    background: var(--surface2) !important;
    border: 2px dashed var(--border) !important;
    border-radius: 12px !important;
}

div[data-testid="stExpander"] {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
}

.stRadio > label { color: var(--text) !important; }
.stSlider > div > div > div { background: var(--accent) !important; }

section[data-testid="stSidebar"] {
    background: var(--surface) !important;
    border-right: 1px solid var(--border) !important;
}

.section-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid var(--border);
}

.progression-step {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    padding: 0.7rem 1rem;
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 8px;
    margin-bottom: 0.5rem;
}
.progression-arrow {
    color: var(--accent2);
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# ENHANCED DATASET — 25 careers with rich fields
# ─────────────────────────────────────────────────────────────────────────────
# ─────────────────────────────────────────────────────────────────────────────
# EXPANDED DATASET — 75 careers across 20+ industries
# ─────────────────────────────────────────────────────────────────────────────
# ─────────────────────────────────────────────────────────────────────────────
# DATASET — imported from data.py (keeps this file lean)
# To add careers: edit data.py
# ─────────────────────────────────────────────────────────────────────────────
from data import data

df = pd.DataFrame(data)

# ─────────────────────────────────────────────────────────────────────────────
# MODEL TRAINING with TF-IDF
# ─────────────────────────────────────────────────────────────────────────────
@st.cache_resource
def build_vectorizers(df):
    """
    Build separate TF-IDF vectorizers for skills and interests so each
    dimension can be weighted independently. No ML classifier — pure
    semantic similarity which is far more accurate for a 1-sample-per-class dataset.
    """
    # Skills vectorizer — bigrams, high vocab
    skill_tfidf = TfidfVectorizer(
        ngram_range=(1, 2),
        max_features=3000,
        sublinear_tf=True,          # dampens effect of very common terms
        min_df=1,
    )
    skill_tfidf.fit(df['skills'].str.lower())
    skill_matrix = skill_tfidf.transform(df['skills'].str.lower())

    # Interests vectorizer — unigrams only (interests are short phrases)
    interest_tfidf = TfidfVectorizer(
        ngram_range=(1, 2),
        max_features=1500,
        sublinear_tf=True,
        min_df=1,
    )
    interest_tfidf.fit(df['interests'].str.lower())
    interest_matrix = interest_tfidf.transform(df['interests'].str.lower())

    # Industry/title vectorizer for keyword boosts
    title_tfidf = TfidfVectorizer(ngram_range=(1, 1), max_features=500)
    title_tfidf.fit((df['job_title'] + " " + df['industry']).str.lower())
    title_matrix = title_tfidf.transform((df['job_title'] + " " + df['industry']).str.lower())

    return skill_tfidf, skill_matrix, interest_tfidf, interest_matrix, title_tfidf, title_matrix

skill_tfidf, skill_matrix, interest_tfidf, interest_matrix, title_tfidf, title_matrix = build_vectorizers(df)

# Keep old tfidf alive for any legacy references
tfidf = skill_tfidf
le = LabelEncoder()
le.fit(df['job_title'])
rf_model = None
gb_model = None
rf_acc = 0.0
gb_acc = 0.0
X_train = skill_matrix


# ─────────────────────────────────────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────
def expand_interests_to_skills(interests_str, skills_str):
    """
    Map hobby/interest keywords to relevant technical skills so the
    recommendation engine can match them to careers.
    E.g. 'gaming' → adds 'unity, c#, game design, unreal engine'
    """
    INTEREST_SKILL_MAP = {
        # Gaming & Esports
        "gaming":          "unity, c#, game design, unreal engine, c++, gameplay programming, gaming",
        "games":           "unity, c#, game design, unreal engine, gaming",
        "video games":     "unity, c#, game design, unreal engine, gameplay programming",
        "esports":         "game knowledge, strategy, coaching, video analysis, esports",
        "game design":     "unity, unreal engine, game design, level design, c#",
        "game dev":        "unity, c#, c++, game design, gameplay programming",
        "game development":"unity, c#, c++, game design, gameplay programming",
        "rpg":             "unity, game design, c#, storytelling, game development",
        "fps":             "unity, unreal engine, c++, game design, gameplay programming",
        "mobile gaming":   "unity, kotlin, swift, mobile app, game design",
        "game streaming":  "streaming, obs, content creation, social media, gaming",
        "twitch":          "streaming, content creation, social media, community management",
        "game art":        "3d modeling, blender, maya, concept art, unity",
        "vr gaming":       "unity, unreal engine, openxr, vr, c#, 3d modeling",

        # Music & Audio
        "music":           "music theory, ableton, logic pro, fl studio, mixing, sound design",
        "singing":         "music theory, vocal production, audio engineering, ableton",
        "guitar":          "music theory, sound design, audio engineering, mixing",
        "piano":           "music theory, music composition, midi, ableton",
        "drums":           "music theory, rhythm, audio engineering, mixing",
        "dj":              "ableton, fl studio, mixing, sound design, music production",
        "music production":"ableton, logic pro, fl studio, mixing, mastering, sound design",
        "beatmaking":      "fl studio, ableton, midi, sound design, music production",
        "audio":           "audio engineering, mixing, mastering, pro tools, sound design",
        "podcast":         "audio engineering, content creation, editing, storytelling",
        "music theory":    "music theory, music composition, ableton, logic pro",

        # Art & Design
        "art":             "photoshop, illustrator, creativity, drawing, visual design",
        "drawing":         "illustration, photoshop, procreate, sketching, visual design",
        "painting":        "photoshop, procreate, illustration, creativity, color theory",
        "illustration":    "illustrator, photoshop, procreate, drawing, visual design",
        "digital art":     "photoshop, procreate, illustrator, digital illustration",
        "concept art":     "photoshop, procreate, concept art, 3d modeling, illustration",
        "comics":          "illustration, storyboarding, photoshop, storytelling",
        "anime":           "animation, illustration, blender, maya, 3d modeling",
        "graphic design":  "photoshop, illustrator, indesign, typography, branding",
        "logo design":     "illustrator, photoshop, branding, typography, figma",
        "ui design":       "figma, wireframing, prototyping, ui design, ux",
        "ux design":       "figma, user research, wireframing, prototyping, ux",
        "web design":      "html, css, figma, ux, ui design, responsive design",
        "fashion":         "fashion design, illustration, sketching, trend analysis, cad",
        "photography":     "photography, lightroom, photoshop, composition, visual storytelling",
        "videography":     "video editing, premiere pro, davinci resolve, cinematography",
        "filmmaking":      "video editing, premiere pro, storytelling, cinematography",
        "animation":       "blender, maya, after effects, animation, rigging",
        "3d modeling":     "blender, maya, 3ds max, 3d modeling, animation",
        "interior design": "autocad, sketchup, interior design, space planning, color theory",

        # Technology & Coding
        "coding":          "python, javascript, programming, algorithms, data structures",
        "programming":     "python, java, javascript, algorithms, data structures, oop",
        "hacking":         "cybersecurity, penetration testing, ethical hacking, networking",
        "cybersecurity":   "network security, penetration testing, cryptography, firewalls",
        "web development": "html, css, javascript, react, node.js, rest api",
        "app development": "flutter, react native, swift, kotlin, mobile app",
        "machine learning":"python, machine learning, tensorflow, scikit-learn, statistics",
        "artificial intelligence": "python, machine learning, deep learning, nlp, tensorflow",
        "robotics":        "ros, python, c++, embedded systems, kinematics, control systems",
        "electronics":     "circuit design, pcb, embedded systems, microcontrollers, iot",
        "iot":             "iot, embedded systems, python, mqtt, sensors, microcontrollers",
        "blockchain":      "solidity, ethereum, web3, smart contracts, cryptography",
        "crypto":          "cryptocurrency, blockchain, trading, defi, tokenomics",
        "vr":              "unity, unreal engine, openxr, vr, c#, 3d modeling",
        "ar":              "unity, arcore, arkit, augmented reality, c#",
        "hardware":        "embedded systems, circuit design, fpga, microcontrollers, pcb",
        "open source":     "git, programming, community, documentation, collaboration",
        "linux":           "linux, bash, shell, networking, system administration",

        # Sports & Fitness
        "sports":          "sports coaching, performance analysis, fitness, teamwork",
        "football":        "sports coaching, performance analysis, fitness, teamwork",
        "basketball":      "sports coaching, performance analysis, fitness, teamwork",
        "cricket":         "sports coaching, performance analysis, data analysis, fitness",
        "tennis":          "sports coaching, performance analysis, fitness, agility",
        "swimming":        "exercise science, fitness, coaching, injury prevention",
        "athletics":       "exercise science, strength training, fitness, sports coaching",
        "gym":             "exercise science, personal training, nutrition, strength training",
        "fitness":         "exercise science, program design, nutrition, personal training",
        "yoga":            "yoga, wellness, anatomy, coaching, mindfulness",
        "cycling":         "exercise science, fitness, endurance training, nutrition",
        "martial arts":    "physical fitness, coaching, discipline, self defense",
        "swimming":        "exercise science, fitness, coaching, injury prevention",
        "esports coaching":"game knowledge, coaching, video analysis, strategy, performance",

        # Science & Nature
        "science":         "research, data analysis, laboratory, scientific writing",
        "biology":         "biology, lab techniques, research, genetics, cell biology",
        "chemistry":       "chemistry, lab techniques, research, organic chemistry",
        "physics":         "physics, mathematics, research, problem solving",
        "astronomy":       "research, data analysis, python, physics, observation",
        "environment":     "environmental analysis, sustainability, gis, ecology",
        "nature":          "ecology, field work, sustainability, environmental analysis",
        "animals":         "biology, ecology, wildlife management, field work",
        "space":           "aerospace, physics, mathematics, research, engineering",
        "medicine":        "patient care, diagnosis, pharmacology, anatomy, clinical skills",
        "psychology":      "psychology, counseling, empathy, research, behavioral analysis",
        "neuroscience":    "neuroscience, research, data analysis, biology, psychology",

        # Business & Finance
        "business":        "business strategy, communication, leadership, problem solving",
        "entrepreneurship":"business strategy, leadership, product development, fundraising",
        "startups":        "business strategy, product development, agile, leadership, pitching",
        "investing":       "financial analysis, valuation, excel, market analysis, portfolio management",
        "stocks":          "financial analysis, equity research, trading, technical analysis",
        "trading":         "trading, technical analysis, market analysis, risk management",
        "finance":         "financial analysis, accounting, excel, financial modeling",
        "marketing":       "digital marketing, seo, social media, content creation, branding",
        "economics":       "economics, data analysis, statistics, financial analysis, research",
        "real estate":     "real estate, property valuation, sales, market analysis, negotiation",

        # Writing & Media
        "writing":         "writing, editing, content creation, storytelling, research",
        "blogging":        "writing, seo, wordpress, content creation, storytelling",
        "journalism":      "writing, journalism, research, interviewing, fact checking",
        "storytelling":    "writing, storytelling, content creation, editing",
        "social media":    "social media, content creation, community management, analytics",
        "youtube":         "video editing, content creation, storytelling, social media",
        "tiktok":          "content creation, video editing, social media, trends",
        "instagram":       "photography, content creation, social media, branding",
        "acting":          "communication, performing arts, creativity, public speaking",
        "theatre":         "performing arts, communication, creativity, direction",
        "public speaking": "public speaking, communication, presentation, leadership",

        # Travel & Culture
        "travel":          "travel planning, geography, customer service, communication",
        "languages":       "communication, translation, cultural awareness, linguistics",
        "history":         "research, writing, analytical thinking, documentation",
        "culture":         "communication, cultural awareness, research, social sciences",
        "cooking":         "culinary techniques, food safety, recipe development, kitchen management",
        "baking":          "culinary techniques, food safety, recipe development, kitchen management",
        "food":            "culinary techniques, food safety, nutrition, recipe development",

        # Social & Community
        "volunteering":    "community outreach, social work, empathy, communication",
        "teaching":        "teaching, curriculum development, communication, mentoring",
        "helping others":  "empathy, counseling, social work, communication, patient care",
        "community":       "community management, social work, communication, advocacy",
        "leadership":      "leadership, team management, strategic planning, communication",
        "teamwork":        "teamwork, collaboration, communication, project management",

        # Other Hobbies
        "photography":     "photography, lightroom, photoshop, visual storytelling, composition",
        "reading":         "research, analytical thinking, writing, critical thinking",
        "chess":           "strategic thinking, problem solving, analytical thinking, decision making",
        "puzzle":          "problem solving, analytical thinking, logical reasoning",
        "mathematics":     "mathematics, statistics, data analysis, python, problem solving",
        "investing":       "financial modeling, portfolio management, market analysis, valuation",
        "cars":            "mechanical engineering, automotive, cad, problem solving",
        "architecture":    "autocad, revit, architectural design, structural analysis",
        "gardening":       "agronomy, soil science, sustainability, environmental science",
        "fashion design":  "fashion design, illustration, sketching, trend analysis",

        # Performing Arts & Dance
        "dancing":         "dancing, choreography, performance, rhythm, stage presence, flexibility",
        "dance":           "dancing, choreography, performance, rhythm, stage presence",
        "ballet":          "ballet, dancing, choreography, flexibility, stage presence, classical dance",
        "hip hop":         "dancing, hip hop, choreography, rhythm, performance, stage presence",
        "classical dance":  "classical dance, dancing, choreography, stage presence, performance",
        "contemporary":    "contemporary dance, dancing, choreography, performance, movement",
        "choreography":    "choreography, dancing, performance, creative direction, stage production",
        "acting":          "acting, improvisation, script reading, character development, stage presence",
        "theatre":         "acting, theatre, directing, script analysis, stage presence, performance",
        "singing":         "singing, vocal training, music theory, performance, stage presence",
        "performing arts": "dancing, acting, singing, stage presence, performance, creativity",
        "modeling":        "modeling, posing, runway walking, fashion, photography, social media",
        "fashion modeling": "modeling, posing, runway walking, fashion knowledge, social media",

        # Beauty & Lifestyle
        "makeup":          "makeup application, color theory, skincare, special effects makeup, client consultation",
        "beauty":          "makeup application, skincare, beauty, color theory, client consultation",
        "skincare":        "skincare, beauty, product knowledge, client consultation, dermatology",
        "styling":         "fashion styling, wardrobe planning, color coordination, trend awareness",
        "fashion styling":  "styling, fashion trends, wardrobe planning, color coordination",
        "tattoo":          "tattooing, illustration, drawing, color theory, custom design",
        "body art":        "tattooing, illustration, drawing, color theory, custom design",

        # Food, Cooking & Nutrition
        "cooking":         "culinary techniques, food safety, recipe development, kitchen management",
        "baking":          "culinary techniques, baking, recipe development, food safety",
        "food":            "culinary techniques, food safety, nutrition, recipe development",
        "nutrition":       "nutrition science, diet planning, meal planning, health coaching, food safety",
        "diet":            "nutrition science, diet planning, meal planning, health coaching",
        "food blogging":   "cooking, food photography, recipe writing, content creation, seo, social media",
        "food photography":"food photography, photography, lightroom, styling, content creation",
        "chef":            "culinary techniques, kitchen management, menu design, food safety, creativity",
        "baking":          "baking, recipe development, food safety, culinary techniques, creativity",

        # Crafts & DIY
        "woodworking":     "woodworking, carpentry, hand tools, blueprint reading, joinery",
        "carpentry":       "carpentry, woodworking, construction, blueprint reading, hand tools",
        "crafts":          "crafts, creativity, design, diy, hand skills, art",
        "diy":             "woodworking, carpentry, construction, problem solving, hand tools",
        "jewellery":       "jewellery design, gemology, cad, sketching, metalworking",
        "jewelry":         "jewellery design, gemology, cad, sketching, metalworking",
        "pottery":         "crafts, creativity, design, art, hand skills, sculpture",
        "knitting":        "crafts, creativity, design, fashion, textiles",
        "sewing":          "fashion design, sewing, pattern making, textiles, creativity",

        # Travel & Languages
        "travel":          "travel planning, geography, customer service, communication, cultural awareness",
        "travelling":      "travel planning, geography, communication, cultural awareness, tourism",
        "backpacking":     "travel planning, geography, adventure, communication, cultural awareness",
        "languages":       "multilingual communication, translation, cultural awareness, linguistics",
        "translation":     "translation, multilingual communication, proofreading, localization",
        "linguistics":     "linguistics, translation, communication, research, cultural awareness",
        "culture":         "cultural awareness, communication, research, social sciences, languages",
        "history":         "research, writing, analytical thinking, documentation, cultural knowledge",

        # Wellness & Spiritual
        "yoga":            "yoga, asana practice, meditation, anatomy, mindfulness, wellness coaching",
        "meditation":      "meditation, mindfulness, yoga, wellness, coaching, mental health",
        "wellness":        "wellness coaching, nutrition, fitness, mindfulness, counseling",
        "mindfulness":     "mindfulness, meditation, yoga, mental health, counseling, wellness",
        "spirituality":    "meditation, yoga, mindfulness, wellness, philosophy, counseling",

        # Social Work & Helping
        "volunteering":    "community outreach, social work, empathy, communication, advocacy",
        "helping others":  "empathy, counseling, social work, communication, patient care",
        "community":       "community management, social work, communication, advocacy",
        "social work":     "case management, advocacy, counseling, community resources, empathy",
        "psychology":      "psychology, counseling, research, human behavior, assessment",
        "life coaching":   "coaching, goal setting, motivational interviewing, empathy, communication",
        "coaching":        "coaching, communication, goal setting, leadership, mentoring",
    }

    skills_lower = skills_str.lower()
    interests_lower = interests_str.lower()
    extra_skills = []

    for keyword, mapped_skills in INTEREST_SKILL_MAP.items():
        # Check both skills and interests fields for hobby keywords
        if keyword in interests_lower or keyword in skills_lower:
            extra_skills.append(mapped_skills)

    if extra_skills:
        all_skills = skills_str + ", " + ", ".join(extra_skills)
    else:
        all_skills = skills_str

    return all_skills


def get_recommendations(skills, education, interests, experience, model_choice="Ensemble", top_n=3):
    """
    Pure similarity-based recommendation engine.
    Weights: Skills 60% | Interests 30% | Experience fit 7% | Education 3%
    Education is kept minimal so skills/interests drive results.
    """
    # ── Step 1: Normalize & expand ────────────────────────────────────────
    skills    = normalize_skills(skills)
    interests = normalize_skills(interests)
    skills    = expand_interests_to_skills(interests, skills)

    # ── Step 2: Skill similarity (60%) ───────────────────────────────────
    # Use the dedicated skill vectorizer for highest accuracy
    user_skill_vec = skill_tfidf.transform([skills.lower()])
    skill_sim      = cosine_similarity(user_skill_vec, skill_matrix)[0]

    # Exact keyword overlap bonus — rewards careers that share more exact skills
    user_skill_set  = {s.strip().lower() for s in skills.split(",") if len(s.strip()) > 2}
    exact_bonus     = np.array([
        len(user_skill_set & {s.strip().lower() for s in df.iloc[i]['skills'].split(",")})
        / max(len({s.strip().lower() for s in df.iloc[i]['skills'].split(",")}), 1)
        for i in range(len(df))
    ])

    # Combined skill score: 70% TF-IDF similarity + 30% exact overlap
    skill_score = 0.70 * skill_sim + 0.30 * exact_bonus

    # ── Step 3: Interest similarity (30%) ────────────────────────────────
    # Also compare user interests against career interests field
    if interests.strip():
        user_int_vec  = interest_tfidf.transform([interests.lower()])
        interest_sim  = cosine_similarity(user_int_vec, interest_matrix)[0]

        # Also match interests against job titles/industry names
        user_title_vec = title_tfidf.transform([interests.lower() + " " + skills.lower()])
        title_sim      = cosine_similarity(user_title_vec, title_matrix)[0]

        interest_score = 0.75 * interest_sim + 0.25 * title_sim
    else:
        interest_score = np.zeros(len(df))

    # ── Step 4: Experience fit (7%) ───────────────────────────────────────
    EXP_ORDER = {"entry": 0, "junior": 1, "mid": 2, "senior": 3}
    user_exp  = EXP_ORDER.get(experience.lower(), 1)
    exp_score = np.array([
        1.0 - abs(EXP_ORDER.get(df.iloc[i]['experience'].lower(), 1) - user_exp) / 3.0
        for i in range(len(df))
    ])

    # ── Step 5: Education fit (3%) — minimal weight ───────────────────────
    EDU_ORDER = {"highschool": 0, "associate": 1, "bachelor": 2, "master": 3, "phd": 4}
    user_edu  = EDU_ORDER.get(education.lower(), 2)
    edu_score = np.array([
        1.0 - max(EDU_ORDER.get(df.iloc[i]['education'].lower(), 2) - user_edu, 0) / 4.0
        for i in range(len(df))
    ])
    # Note: having MORE education than required is not penalized (only having less is)

    # ── Step 6: Combine with weights ──────────────────────────────────────
    combined = (
        0.60 * skill_score +
        0.30 * interest_score +
        0.07 * exp_score +
        0.03 * edu_score
    )

    # ── Step 7: Rank and return ───────────────────────────────────────────
    top_idx = combined.argsort()[::-1][:top_n]
    results = []
    for idx in top_idx:
        raw   = float(combined[idx])
        # Scale match_pct so top result shows meaningfully high %
        # Normalize relative to best possible score in this search
        best  = float(combined.max()) if combined.max() > 0 else 1.0
        pct   = int((raw / best) * 95) if idx == top_idx[0] else int((raw / best) * 92)
        pct   = max(min(pct, 98), 10)   # clamp between 10–98%
        results.append({
            "career":    df.iloc[idx],
            "score":     raw,
            "match_pct": pct,
        })
    # Re-scale so #1 always shows highest, #2 slightly less, etc.
    if results:
        top_pct = results[0]["match_pct"]
        for i, r in enumerate(results):
            r["match_pct"] = max(top_pct - i * 5, 10)
    return results


def skill_gap(user_skills_str, career_skills_str):
    user_set   = {s.strip().lower() for s in user_skills_str.split(",") if s.strip()}
    career_set = {s.strip().lower() for s in career_skills_str.split(",") if s.strip()}
    have    = user_set & career_set
    missing = career_set - user_set
    return sorted(have), sorted(missing)


def detect_unknown_career(skills_str, interests_str):
    """
    Check if the user's input contains a specific career/role title
    that doesn't exist in our dataset. Returns the detected title or None.
    """
    # Common role indicator words — if user types these, they mean a specific career
    role_indicators = [
        "dancer", "dancing", "choreographer", "singer", "actor", "actress",
        "pilot", "astronaut", "chef", "barista", "bartender", "sommelier",
        "tattoo artist", "model", "makeup artist", "stylist", "dj",
        "streamer", "youtuber", "vlogger", "podcaster", "influencer",
        "magician", "comedian", "stand-up", "anchor", "news anchor",
        "referee", "umpire", "athlete", "cricketer", "footballer",
        "swimmer", "gymnast", "boxer", "wrestler", "mma fighter",
        "photographer", "videographer", "cinematographer",
        "florist", "wedding planner", "event planner",
        "astrologer", "tarot reader", "life coach",
        "dog trainer", "pet groomer", "veterinarian",
        "ethical hacker", "bug bounty hunter", "game streamer",
        "esports player", "speedrunner", "cosplayer",
        "drone pilot", "drone operator", "uav operator",
        "perfumer", "fragrance designer", "sommelier",
        "voice actor", "voice over artist", "narrator",
        "asmr creator", "mukbang", "food critic", "restaurant critic",
        "art therapist", "music therapist", "dance therapist",
        "urban planner", "town planner", "landscape architect",
        "forensic scientist", "crime scene investigator", "profiler",
        "fire fighter", "paramedic", "rescue diver", "coast guard",
        "librarian", "archivist", "museum curator", "art curator",
        "sign language interpreter", "braille transcriber",
        "gemologist", "mineralogist", "paleontologist",
        "mythologist", "anthropologist", "archaeologist",
        "standup comedian", "improv artist", "mime",
        "calligrapher", "graffiti artist", "muralist", "sculptor",
        "taxidermist", "embalmer", "mortician", "funeral director",
        "sommelier", "chocolatier", "pastry chef", "cake designer",
        "forex trader", "day trader", "quant trader",
        "podcast host", "radio jockey", "rj", "disc jockey",
        "certified financial planner", "tax consultant",
        "immigration consultant", "visa consultant",
        "nanny", "au pair", "childcare worker", "babysitter",
    ]

    combined = (skills_str + " " + interests_str).lower()

    # Check against dataset job titles first
    dataset_titles = set(df['job_title'].str.lower().tolist())

    for indicator in role_indicators:
        if indicator in combined:
            # Check if it's already well-covered in dataset
            if not any(indicator in title for title in dataset_titles):
                # Capitalize properly
                return " ".join(w.capitalize() for w in indicator.split())

    return None


def ai_generate_career(career_title, user_skills, user_interests, user_education, user_experience):
    """
    Use Groq/Anthropic to generate a full career profile for any job title
    not found in the dataset. Returns a dict matching the dataset schema.
    """
    api_key  = st.session_state.get("groq_api_key", "")
    provider = st.session_state.get("ai_provider", "Groq (Free)")
    ant_key  = st.session_state.get("anthropic_api_key", "")

    prompt = f"""You are a career data expert. Generate a detailed, accurate career profile for: "{career_title}"

User profile context:
- Skills: {user_skills}
- Interests: {user_interests}
- Education: {user_education}
- Experience level: {user_experience}

Return ONLY a valid JSON object with EXACTLY these fields (no markdown, no explanation, no extra text):
{{
  "job_title": "{career_title}",
  "skills": "comma separated list of 10-12 specific, real skills required for this exact role",
  "education": "one of: highschool, associate, bachelor, master, phd",
  "interests": "comma separated list of 6-8 interests that genuinely match people in this career",
  "experience": "one of: entry, junior, mid, senior",
  "description": "2 clear sentences describing what this professional actually does day-to-day",
  "salary_min": <realistic annual salary integer in USD>,
  "salary_max": <realistic annual salary integer in USD>,
  "demand": "one of: Very High, High, Moderate, Low",
  "industry": "the specific industry this role belongs to",
  "progression": ["Entry Level Title", "Mid Title", "Senior Title", "Lead Title", "Top Title"],
  "certifications": ["Most relevant cert 1", "Most relevant cert 2", "Most relevant cert 3"],
  "courses": ["https://real-course-url-1.com", "https://real-course-url-2.com"]
}}"""

    try:
        raw = None
        if provider == "Groq (Free)" and api_key and GROQ_AVAILABLE:
            from groq import Groq
            client = Groq(api_key=api_key)
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are a career data API. Always respond with valid JSON only. Never add markdown, explanations, or extra text."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=900,
                temperature=0.2,
            )
            raw = response.choices[0].message.content.strip()
        elif ant_key:
            client = anthropic.Anthropic(api_key=ant_key)
            response = client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=900,
                messages=[{"role": "user", "content": prompt}],
            )
            raw = response.content[0].text.strip()
        else:
            return None

        # Strip markdown code fences if present
        raw = re.sub(r"^```[a-z]*\n?", "", raw).strip()
        raw = re.sub(r"\n?```$", "", raw).strip()

        # Sometimes model wraps in extra text — extract just the JSON
        json_match = re.search(r'\{.*\}', raw, re.DOTALL)
        if json_match:
            raw = json_match.group()

        career_data = json.loads(raw)

        # Validate & fill defaults for any missing fields
        defaults = {
            "salary_min": 40000, "salary_max": 120000,
            "demand": "Moderate", "industry": "General",
            "progression": [
                f"Junior {career_title}", career_title,
                f"Senior {career_title}", f"Lead {career_title}",
                f"Head of {career_title}"
            ],
            "certifications": ["Relevant Industry Certification"],
            "courses": ["https://www.coursera.org", "https://www.udemy.com"],
        }
        for k, v in defaults.items():
            if k not in career_data or not career_data[k]:
                career_data[k] = v

        # Ensure salary_min/max are integers
        career_data["salary_min"] = int(career_data.get("salary_min", 40000))
        career_data["salary_max"] = int(career_data.get("salary_max", 120000))

        return career_data

    except Exception:
        return None


def normalize_skills(raw_skills_str):
    """
    Normalize and expand user-entered skills using aliases.
    Maps common abbreviations, alternate names, and typos to canonical forms
    so they match what's in the dataset.
    """
    ALIASES = {
        # Programming
        "py": "python", "js": "javascript", "ts": "typescript",
        "c plus plus": "c++", "cpp": "c++", "csharp": "c#", "c sharp": "c#",
        "golang": "go", "golang lang": "go", "node": "node.js", "nodejs": "node.js",
        "reactjs": "react", "react.js": "react", "vuejs": "vue", "vue.js": "vue",
        "angularjs": "angular", "nextjs": "next.js", "nuxtjs": "nuxt",
        "rb": "ruby", "rails": "ruby on rails", "ror": "ruby on rails",
        "kt": "kotlin", "sw": "swift",
        # Web
        "html5": "html", "css3": "css", "sass": "css", "scss": "css",
        "rest": "rest api", "restful": "rest api", "api": "rest api",
        "graphql api": "graphql", "websocket": "rest api",
        "wp": "wordpress", "woocommerce": "wordpress",
        # Data & AI
        "ml": "machine learning", "dl": "deep learning", "ai": "machine learning",
        "artificial intelligence": "machine learning", "gen ai": "llm",
        "generative ai": "llm", "large language model": "llm",
        "nlp": "nlp", "natural language processing": "nlp",
        "cv": "computer vision", "image recognition": "computer vision",
        "tf": "tensorflow", "torch": "pytorch",
        "sklearn": "scikit-learn", "sci-kit learn": "scikit-learn",
        "hf": "huggingface", "hugging face": "huggingface",
        "data science": "data analysis", "data eng": "data pipelines",
        "bi": "power bi", "powerbi": "power bi", "power-bi": "power bi",
        "tableau desktop": "tableau", "looker studio": "looker",
        "pyspark": "spark", "apache spark": "spark",
        "apache kafka": "kafka", "apache airflow": "airflow",
        "data warehouse": "data warehousing", "dw": "data warehousing",
        "ab testing": "a/b testing", "split testing": "a/b testing",
        # Cloud & DevOps
        "amazon web services": "aws", "amazon aws": "aws",
        "microsoft azure": "azure", "google cloud platform": "gcp",
        "gcp cloud": "gcp", "google cloud": "gcp",
        "k8s": "kubernetes", "kube": "kubernetes",
        "tf infra": "terraform", "iac": "terraform",
        "github ci": "github actions", "gitlab ci": "ci/cd",
        "continuous integration": "ci/cd", "continuous delivery": "ci/cd",
        "continuous deployment": "ci/cd",
        "devops engineer": "devops", "site reliability": "sre",
        "ubuntu": "linux", "debian": "linux", "centos": "linux",
        # Databases
        "postgres": "postgresql", "psql": "postgresql",
        "mongo": "mongodb", "mongo db": "mongodb",
        "mysql db": "mysql", "mariadb": "mysql",
        "elastic": "elasticsearch", "elk": "elasticsearch",
        "dynamo": "dynamodb", "dynamo db": "dynamodb",
        "firestore": "firebase", "realtime db": "firebase",
        "db design": "database design", "database": "database design",
        "sql server": "sql", "t-sql": "sql", "pl/sql": "sql",
        "mssql": "sql", "ms sql": "sql",
        # Security
        "cyber security": "cybersecurity", "info security": "cybersecurity",
        "infosec": "cybersecurity", "appsec": "cybersecurity",
        "pentest": "penetration testing", "pen testing": "penetration testing",
        "bug bounty": "penetration testing", "red team": "penetration testing",
        "blue team": "incident response", "soc analyst": "siem",
        "security operations": "siem", "firewall": "firewalls",
        "zero-trust": "zero trust", "devsecops": "cybersecurity",
        # Design
        "ps": "photoshop", "adobe ps": "photoshop",
        "ai": "illustrator", "adobe ai": "illustrator",
        "adobe figma": "figma", "ui/ux": "ux", "ui ux": "ux",
        "user interface": "ui design", "user experience": "ux",
        "xd": "adobe xd", "adobe after effects": "after effects",
        "adobe premiere": "premiere pro", "fcpx": "final cut pro",
        "resolve": "davinci resolve", "da vinci": "davinci resolve",
        "3d": "3d modeling", "3ds": "3ds max", "3d max": "3ds max",
        "sw cad": "solidworks", "solid works": "solidworks",
        "auto cad": "autocad", "cad design": "autocad",
        "fl": "fl studio", "ableton live": "ableton",
        "logic": "logic pro", "pro tool": "pro tools",
        # Business & Management
        "pm": "project management", "proj mgmt": "project management",
        "pmo": "project management", "project lead": "project management",
        "agile methodology": "agile", "agile scrum": "scrum",
        "sprint": "scrum", "kanban board": "kanban",
        "ms project": "project management", "jira software": "jira",
        "product owner": "agile", "product roadmap": "roadmapping",
        "okr": "strategic planning", "kpi": "strategic planning",
        "ops": "operations management", "biz dev": "business strategy",
        "bizdev": "business strategy", "b-plan": "business strategy",
        "crm software": "crm", "sfdc": "salesforce", "sf": "salesforce",
        "hubspot crm": "crm", "zoho": "crm",
        "erp system": "erp", "sap erp": "sap", "oracle erp": "erp",
        "ms office": "excel", "microsoft office": "excel",
        "microsoft excel": "excel", "spreadsheet": "excel",
        "powerpoint": "presentation", "ppt": "presentation",
        "ms word": "writing", "word processing": "writing",
        # Finance
        "fin modeling": "financial modeling", "financial model": "financial modeling",
        "dcf analysis": "dcf", "discounted cash flow": "dcf",
        "gaap accounting": "gaap", "us gaap": "gaap",
        "ifrs accounting": "ifrs", "cfa exam": "cfa",
        "cpa exam": "accounting", "acca": "accounting",
        "fin analysis": "financial analysis", "fp&a": "financial modeling",
        "investment analysis": "valuation", "equity": "equity research",
        "fixed income": "fixed income", "bonds": "fixed income",
        "derivatives trading": "derivatives", "options": "derivatives",
        "crypto": "cryptocurrency", "btc": "cryptocurrency",
        "web 3": "web3", "web 3.0": "web3", "defi protocol": "defi",
        "nfts": "nft", "non-fungible": "nft",
        # Healthcare
        "patient assessment": "patient care", "bedside manner": "patient care",
        "emr": "ehr", "electronic health records": "ehr",
        "electronic medical records": "ehr", "epic systems": "ehr",
        "pharmacy": "pharmacology", "drug therapy": "pharmacology",
        "pharm": "pharmacology", "rx": "pharmacology",
        "lab work": "lab techniques", "lab skills": "lab techniques",
        "blood draw": "specimen analysis", "phlebotomy": "specimen analysis",
        "pt": "physical therapy", "physiotherapy": "physical therapy",
        "occupational therapy": "rehabilitation", "ot": "rehabilitation",
        "mental health counseling": "counseling", "therapy": "counseling",
        "psychotherapy": "counseling", "cbt therapy": "cbt",
        "clinical psychology": "psychology", "behavioral health": "mental health",
        "med school": "diagnosis", "clinical medicine": "diagnosis",
        "differential diagnosis": "diagnosis", "clinical assessment": "diagnosis",
        # Engineering
        "mech eng": "mechanics", "mechanical design": "solidworks",
        "thermo": "thermodynamics", "fluid mech": "fluid dynamics",
        "structural eng": "structural analysis", "finite element": "fea",
        "circuit": "circuit design", "circuits": "circuit design",
        "power eng": "power systems", "dsp": "signal processing",
        "plc programming": "plc", "scada systems": "scada",
        "embedded": "embedded systems", "firmware": "embedded systems",
        "real time os": "rtos", "field programmable": "fpga",
        "microcontroller": "microcontrollers", "arduino": "microcontrollers",
        "raspberry pi": "embedded systems", "esp32": "embedded systems",
        "internet of things": "iot", "iot devices": "iot",
        "robotic": "robotics", "robot operating system": "ros",
        "civil eng": "structural analysis", "structural": "structural analysis",
        "surveying": "surveying", "geo tech": "geotechnical",
        "hvac": "mechanical engineering", "piping design": "piping",
        "process eng": "process simulation", "chem proc": "chemical processes",
        # Marketing
        "search engine optimization": "seo", "on-page seo": "seo",
        "technical seo": "seo", "link building": "seo",
        "search engine marketing": "sem", "google search ads": "google ads",
        "pay per click": "ppc", "paid ads": "google ads",
        "facebook marketing": "facebook ads", "meta ads": "facebook ads",
        "instagram ads": "facebook ads", "social media marketing": "social media",
        "smm": "social media", "community mgmt": "community management",
        "email campaigns": "email marketing", "mailchimp": "email marketing",
        "content writing": "content creation", "blog writing": "writing",
        "copy": "copywriting", "ad copy": "copywriting",
        "brand": "branding", "brand identity": "branding",
        "pr specialist": "pr", "public affairs": "pr",
        "digital marketing specialist": "digital marketing",
        "growth hacking": "digital marketing", "growth marketing": "digital marketing",
        "ga4": "google analytics", "google analytics 4": "google analytics",
        "analytics": "google analytics", "web analytics": "google analytics",
        # Education
        "curriculum": "curriculum development", "lesson plan": "lesson planning",
        "classroom": "classroom management", "pedagogy": "teaching",
        "e learning": "e-learning", "online learning": "e-learning",
        "moodle": "lms", "canvas lms": "lms", "blackboard": "lms",
        "instructional": "instructional design", "id": "instructional design",
        "corporate learning": "training", "l&d": "training",
        "public speak": "public speaking", "presentation skills": "public speaking",
        # Soft Skills
        "team work": "teamwork", "team player": "teamwork",
        "time mgmt": "time management", "organized": "organization",
        "detail oriented": "attention to detail", "detail-oriented": "attention to detail",
        "creative": "creativity", "innovative": "creativity",
        "flexible": "adaptability", "fast learner": "adaptability",
        "self starter": "self-motivation", "motivated": "self-motivation",
        "hardworking": "work ethic", "dedicated": "work ethic",
        "eq": "emotional intelligence", "interpersonal skills": "interpersonal",
        "communication skills": "communication", "verbal communication": "communication",
        "written communication": "writing", "presentation skills": "presentation",
        "multi task": "multitasking", "multi-task": "multitasking",
        "people skills": "interpersonal", "relationship building": "networking",
        "persuasive": "persuasion", "influencing": "persuasion",
        # Future / AI
        "prompt eng": "prompt engineering", "prompt design": "prompt engineering",
        "chatgpt api": "llm", "openai api": "llm", "gpt": "llm",
        "gpt-4": "llm", "claude api": "llm", "ai tools": "llm",
        "rag": "llm", "retrieval augmented": "llm",
        "ai governance": "ai ethics", "responsible ai": "ai ethics",
        "mlops engineer": "mlops", "model deployment": "mlops",
        "robotic process": "rpa", "rpa tools": "rpa",
        "automation tools": "rpa", "no code automation": "rpa",
        "climate change": "climate science", "climate data": "climate science",
        "solar": "solar energy", "solar panel": "solar energy",
        "wind": "wind energy", "wind turbine": "wind energy",
        "green energy": "renewable energy", "clean energy": "renewable energy",
        "self driving": "autonomous vehicles", "av": "autonomous vehicles",
        "lidar sensor": "lidar", "point cloud": "lidar",
        "digital twins": "digital twin", "iot twin": "digital twin",
        "vr": "virtual reality", "ar": "augmented reality",
        "xr": "virtual reality", "mixed reality": "virtual reality",
        # Trades & Others
        "wiring": "electrical wiring", "electrician work": "electrical wiring",
        "plumbing": "plumbing systems", "pipe work": "pipe fitting",
        "flying": "flight operations", "pilot": "flight operations",
        "aviation": "flight operations", "atc": "radar systems",
        "police work": "law enforcement", "policing": "law enforcement",
        "cooking": "culinary techniques", "chef skills": "culinary techniques",
        "baking": "culinary techniques", "food prep": "culinary techniques",
        "haccp": "food safety", "food hygiene": "food safety",
        "hotel management": "hospitality management",
        "tourism": "travel planning", "travel agent": "travel planning",
        "fitness": "exercise science", "gym": "strength training",
        "workout": "strength training", "personal training": "personal training",
    }

    tokens = [s.strip().lower() for s in raw_skills_str.split(",") if s.strip()]
    expanded = []
    for token in tokens:
        canonical = ALIASES.get(token, token)
        expanded.append(canonical)
        # Also keep original if different, so both forms match
        if canonical != token:
            expanded.append(token)

    return ", ".join(dict.fromkeys(expanded))  # deduplicate, preserve order


def extract_skills_from_text(text):
    """Comprehensive keyword-based skill extractor covering 400+ skills and aliases."""
    all_skills = [
        # ── Programming Languages ──────────────────────────────────────────
        "python", "java", "javascript", "typescript", "c++", "c#", "c", "r",
        "go", "rust", "swift", "kotlin", "php", "ruby", "scala", "matlab",
        "perl", "bash", "shell", "html", "css", "sql", "nosql", "graphql",
        "assembly", "solidity", "dart", "elixir", "haskell", "lua", "groovy",
        "fortran", "cobol", "vba", "powershell", "julia", "clojure", "erlang",
        "f#", "ocaml", "prolog", "lisp", "scheme", "tcl", "awk",
        # ── Web & Mobile ──────────────────────────────────────────────────
        "react", "vue", "angular", "node.js", "django", "flask", "fastapi",
        "spring", "express", "next.js", "nuxt", "flutter", "react native",
        "ios", "android", "xamarin", "webpack", "rest api", "microservices",
        "wordpress", "shopify", "webflow", "tailwind", "bootstrap",
        "svelte", "remix", "gatsby", "laravel", "rails", "asp.net",
        "socket.io", "redis", "nginx", "apache", "oauth", "jwt",
        "html5", "css3", "sass", "responsive design", "pwa",
        # ── Data & AI/ML ─────────────────────────────────────────────────
        "machine learning", "deep learning", "nlp", "computer vision",
        "tensorflow", "pytorch", "scikit-learn", "keras", "huggingface",
        "transformers", "pandas", "numpy", "scipy", "matplotlib", "seaborn",
        "data analysis", "data visualization", "statistics", "tableau",
        "power bi", "looker", "spark", "hadoop", "kafka", "airflow", "dbt",
        "etl", "data pipelines", "mlops", "bigquery", "snowflake",
        "databricks", "data warehousing", "feature engineering", "a/b testing",
        "statistical modeling", "regression", "classification", "clustering",
        "reinforcement learning", "gan", "llm", "prompt engineering",
        "rag", "langchain", "vector database", "pinecone", "weaviate",
        "time series", "forecasting", "anomaly detection", "recommendation systems",
        "xgboost", "lightgbm", "random forest", "neural networks", "lstm",
        "bert", "gpt", "stable diffusion", "diffusion models", "fine-tuning",
        "data cleaning", "data wrangling", "data mining", "exploratory data analysis",
        # ── Cloud & DevOps ────────────────────────────────────────────────
        "aws", "azure", "gcp", "docker", "kubernetes", "terraform", "ansible",
        "jenkins", "github actions", "ci/cd", "linux", "unix", "devops",
        "sre", "monitoring", "serverless", "lambda", "cloud security",
        "networking", "load balancing", "nginx", "prometheus", "grafana",
        "elk stack", "splunk", "datadog", "new relic", "heroku",
        "digitalocean", "cloudflare", "vagrant", "puppet", "chef",
        "helm", "istio", "service mesh", "api gateway",
        "infrastructure as code", "gitops", "argocd", "sonarqube",
        # ── Databases ─────────────────────────────────────────────────────
        "mysql", "postgresql", "mongodb", "redis", "oracle", "sqlite",
        "dynamodb", "cassandra", "elasticsearch", "firebase", "database design",
        "performance tuning", "replication", "mariadb", "cockroachdb",
        "supabase", "planetscale", "neo4j", "graph database",
        "time series database", "influxdb", "clickhouse", "duckdb",
        # ── Security & Networking ─────────────────────────────────────────
        "network security", "cybersecurity", "penetration testing",
        "ethical hacking", "cryptography", "firewalls", "siem",
        "incident response", "vulnerability assessment", "owasp", "soc",
        "risk assessment", "compliance", "iso 27001", "nist", "zero trust",
        "wireshark", "metasploit", "burp suite", "nmap", "kali linux",
        "threat modeling", "malware analysis", "digital forensics",
        "pci dss", "gdpr", "hipaa compliance", "sox compliance",
        "identity management", "iam", "sso", "mfa", "pki",
        "devsecops", "security audit", "red team", "blue team",
        # ── Design & Creative ──────────────────────────────────────────────
        "photoshop", "illustrator", "figma", "adobe xd", "sketch",
        "indesign", "after effects", "premiere pro", "final cut pro",
        "davinci resolve", "blender", "maya", "cinema 4d", "3d modeling",
        "animation", "motion graphics", "typography", "branding",
        "color theory", "wireframing", "prototyping", "user research",
        "usability testing", "ux", "ui design", "graphic design",
        "visual design", "information architecture", "design thinking",
        "photography", "lightroom", "video editing", "color grading",
        "compositing", "autocad", "revit", "sketchup", "3ds max",
        "rhino", "solidworks", "cad", "ableton", "logic pro",
        "fl studio", "pro tools", "mixing", "mastering", "sound design",
        "canva", "capcut", "procreate", "clip studio", "midjourney",
        "stable diffusion", "dall-e", "adobe firefly", "generative design",
        "packaging design", "print design", "web design", "logo design",
        "brand identity", "illustration", "storyboarding", "concept art",
        # ── Business & Management ──────────────────────────────────────────
        "leadership", "project management", "agile", "scrum", "kanban",
        "waterfall", "prince2", "pmp", "budgeting", "forecasting",
        "strategic planning", "stakeholder management", "communication",
        "negotiation", "problem solving", "critical thinking",
        "decision making", "change management", "risk management",
        "process improvement", "lean", "six sigma", "business analysis",
        "requirements gathering", "process modeling", "documentation",
        "consulting", "business strategy", "competitive analysis",
        "market research", "erp", "sap", "salesforce", "crm", "jira",
        "confluence", "ms project", "asana", "trello", "notion",
        "monday.com", "clickup", "slack", "microsoft teams", "zoom",
        "okr", "kpi", "reporting", "data-driven decision making",
        "people management", "team building", "performance management",
        "succession planning", "workforce planning",
        # ── Finance & Accounting ───────────────────────────────────────────
        "accounting", "financial modeling", "valuation", "dcf", "excel",
        "bloomberg", "financial reporting", "gaap", "ifrs", "tax",
        "auditing", "quickbooks", "investment banking", "m&a",
        "capital markets", "portfolio management", "trading",
        "derivatives", "fixed income", "equity research", "actuarial",
        "probability", "quantitative analysis", "financial analysis", "cfa",
        "blockchain", "cryptocurrency", "defi", "technical analysis",
        "market analysis", "financial planning", "wealth management",
        "private equity", "venture capital", "fund management",
        "risk modeling", "credit analysis", "due diligence",
        "mergers and acquisitions", "ipo", "corporate finance",
        "cost accounting", "management accounting", "payroll",
        "accounts payable", "accounts receivable", "reconciliation",
        "tax planning", "transfer pricing", "treasury management",
        # ── Healthcare & Science ───────────────────────────────────────────
        "patient care", "clinical skills", "diagnosis", "pharmacology",
        "anatomy", "physiology", "nursing", "medical devices", "ehr",
        "hipaa", "clinical trials", "lab techniques", "microscopy",
        "specimen analysis", "hematology", "microbiology", "pathology",
        "rehabilitation", "physical therapy", "mental health", "cbt",
        "counseling", "empathy", "active listening", "crisis intervention",
        "psychology", "research", "scientific writing", "grant writing",
        "peer review", "data collection", "genomics", "bioinformatics",
        "genetics", "molecular biology", "cell biology", "chemistry",
        "biochemistry", "organic chemistry", "laboratory", "gis",
        "field work", "environmental analysis", "ecology", "sustainability",
        "geology", "mineralogy", "epidemiology", "public health",
        "biostatistics", "clinical research", "drug development",
        "radiology", "oncology", "cardiology", "neurology", "pediatrics",
        "surgery", "emergency medicine", "primary care", "telemedicine",
        "medical imaging", "ultrasound", "mri", "ct scan", "ecg",
        "vaccination", "infection control", "wound care", "palliative care",
        # ── Engineering ───────────────────────────────────────────────────
        "thermodynamics", "mechanics", "fluid dynamics", "structural analysis",
        "fea", "circuit design", "pcb", "power systems", "signal processing",
        "plc", "scada", "embedded systems", "rtos", "fpga",
        "microcontrollers", "iot", "robotics", "ros", "kinematics",
        "control systems", "simulink", "ansys", "abaqus",
        "construction management", "surveying", "hydraulics",
        "soil mechanics", "geotechnical", "manufacturing", "cnc",
        "quality control", "lean manufacturing", "reservoir engineering",
        "drilling", "process simulation", "aspen", "piping",
        "aerospace", "aerodynamics", "composite materials", "welding",
        "3d printing", "additive manufacturing", "tolerancing", "gd&t",
        "reverse engineering", "failure analysis", "vibration analysis",
        "acoustic engineering", "thermal analysis", "computational fluid dynamics",
        "building information modeling", "bim", "geospatial analysis",
        # ── Marketing & Communications ─────────────────────────────────────
        "seo", "sem", "google ads", "facebook ads", "social media",
        "content creation", "email marketing", "copywriting",
        "content strategy", "brand management", "pr", "media relations",
        "crisis communication", "event planning", "influencer marketing",
        "digital marketing", "ppc", "conversion optimization",
        "google analytics", "hubspot", "community management", "instagram",
        "tiktok", "twitter", "linkedin", "youtube", "storytelling",
        "writing", "editing", "proofreading", "journalism",
        "investigative reporting", "interviewing", "fact checking",
        "broadcasting", "audio engineering", "live streaming",
        "affiliate marketing", "content marketing", "video marketing",
        "podcast", "newsletter", "growth marketing", "product marketing",
        "market segmentation", "customer journey", "persona development",
        "brand strategy", "creative direction", "campaign management",
        "media buying", "programmatic advertising", "retargeting",
        "conversion funnel", "landing page optimization", "a/b testing",
        # ── Education & Training ───────────────────────────────────────────
        "curriculum development", "lesson planning", "classroom management",
        "assessment", "teaching", "mentoring", "tutoring", "e-learning",
        "instructional design", "lms", "adult learning", "training",
        "coaching", "facilitation", "public speaking", "workshop design",
        "needs analysis", "blended learning", "gamification",
        "educational technology", "scorm", "xapi", "articulate",
        "academic advising", "student support", "special education",
        "english teaching", "tefl", "tesol", "early childhood",
        # ── Sales & Customer Service ───────────────────────────────────────
        "sales", "cold calling", "pipeline management", "objection handling",
        "upselling", "client relations", "account management",
        "customer service", "customer success", "retail", "b2b sales",
        "b2c sales", "territory management", "salesforce crm",
        "real estate", "property valuation", "market analysis",
        "negotiation", "closing techniques", "prospecting", "lead generation",
        "customer retention", "churn reduction", "nps", "customer experience",
        "inside sales", "field sales", "enterprise sales", "solution selling",
        "saas sales", "channel sales", "partner management",
        # ── Legal, HR & Social Services ───────────────────────────────────
        "legal research", "contract drafting", "case management",
        "court procedures", "document review", "e-discovery", "compliance",
        "regulatory", "litigation", "advocacy", "community outreach",
        "social justice", "recruitment", "talent acquisition",
        "employee relations", "compensation", "hris", "onboarding",
        "labor law", "diversity and inclusion", "dei", "employee engagement",
        "conflict resolution", "mediation", "arbitration",
        # ── Hospitality, Travel & Culinary ────────────────────────────────
        "customer service", "hospitality management", "food safety",
        "kitchen management", "menu design", "recipe development",
        "plating", "inventory management", "cooking", "travel planning",
        "itinerary design", "booking systems", "gds", "tour planning",
        "hotel operations", "revenue management", "event management",
        "catering", "bartending", "sommelier", "food and beverage",
        "front desk", "concierge", "guest relations",
        # ── Sports, Fitness & Wellness ─────────────────────────────────────
        "exercise science", "program design", "nutrition", "strength training",
        "personal training", "sports coaching", "performance analysis",
        "video analysis", "scouting", "sports analytics", "injury prevention",
        "sports medicine", "athletic training", "yoga", "pilates",
        "physical conditioning", "sports psychology", "team coaching",
        # ── Future & Emerging Tech ────────────────────────────────────────
        "prompt engineering", "llm", "chatgpt", "chain of thought",
        "ai evaluation", "ai ethics", "bias detection", "data governance",
        "responsible ai", "digital twin", "simulation", "rpa", "uipath",
        "automation anywhere", "robotic process automation",
        "decision science", "behavioral economics", "metaverse",
        "virtual worlds", "nft", "tokenomics", "web3", "defi",
        "smart contracts", "climate science", "carbon accounting", "esg",
        "tcfd", "gri", "carbon footprint", "renewable energy", "solar energy",
        "wind energy", "grid integration", "autonomous vehicles",
        "self-driving", "lidar", "sensor fusion", "path planning",
        "human-ai interaction", "conversational design", "ai ux",
        "human factors", "augmented reality", "virtual reality",
        "spatial computing", "edge computing", "quantum computing",
        "5g", "blockchain architecture", "dao", "zero knowledge proofs",
        # ── Skilled Trades & Practical ────────────────────────────────────
        "electrical wiring", "circuit installation", "nec code",
        "journeyman", "pipe fitting", "plumbing systems", "drainage",
        "gas piping", "blueprint reading", "flight operations",
        "instrument flying", "crew resource management", "weather analysis",
        "aircraft systems", "navigation", "law enforcement", "criminal law",
        "investigation", "physical fitness", "community relations",
        # ── Government & Policy ───────────────────────────────────────────
        "public administration", "policy implementation", "governance",
        "legislative analysis", "regulatory analysis", "judicial procedure",
        "constitutional law", "public policy", "policy research",
        "stakeholder engagement", "grant management", "government relations",
        # ── Agriculture & Environment ──────────────────────────────────────
        "agronomy", "soil science", "crop management", "precision agriculture",
        "irrigation", "pest management", "plant genetics", "field trials",
        "remote sensing", "environmental monitoring", "water quality",
        "air quality", "impact assessment", "epa regulations",
        "conservation", "wildlife management", "forestry",
        # ── Soft Skills (Universal) ───────────────────────────────────────
        "teamwork", "collaboration", "time management", "organization",
        "attention to detail", "creativity", "adaptability", "multitasking",
        "self-motivation", "work ethic", "emotional intelligence",
        "conflict resolution", "presentation", "interpersonal",
        "patience", "cultural awareness", "networking", "persuasion",
        "analytical thinking", "research skills", "initiative",
        "accountability", "reliability", "professionalism",
        "cross-functional collaboration", "stakeholder communication",
        "continuous learning", "growth mindset",
    ]
    text_lower = text.lower()
    found = [skill for skill in all_skills if skill in text_lower]
    seen = set()
    unique_found = []
    for s in found:
        if s not in seen:
            seen.add(s)
            unique_found.append(s)
    return ", ".join(unique_found)

def extract_text_from_pdf(file_bytes):
    """Extract raw text from a PDF file using PyPDF2/pypdf."""
    try:
        reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text
    except Exception as e:
        return ""

def make_radar_chart(user_skills_str, career):
    categories = ["Skills Match", "Education Fit", "Interest Align", "Market Demand", "Salary Range"]
    user_skills = set(s.strip().lower() for s in user_skills_str.split(","))
    career_skills = set(s.strip().lower() for s in career["skills"].split(","))
    skill_score = len(user_skills & career_skills) / max(len(career_skills), 1) * 100

    demand_map = {"Very High": 95, "High": 75, "Moderate": 55, "Low": 30}
    salary_norm = min((career["salary_max"] / 250000) * 100, 100)

    values = [
        min(skill_score, 100),
        85 if career["education"] in ["associate", "bachelor"] else 65,
        75,
        demand_map.get(career["demand"], 50),
        salary_norm,
    ]
    values += [values[0]]
    categories += [categories[0]]

    fig = go.Figure(go.Scatterpolar(
        r=values, theta=categories, fill='toself',
        fillcolor='rgba(108,99,255,0.18)',
        line=dict(color='#6c63ff', width=2),
        marker=dict(color='#00d4aa', size=6),
    ))
    fig.update_layout(
        polar=dict(
            bgcolor='rgba(22,25,32,0.8)',
            radialaxis=dict(visible=True, range=[0, 100], gridcolor='#2a2f40', tickfont=dict(color='#8b90a0', size=9)),
            angularaxis=dict(gridcolor='#2a2f40', tickfont=dict(color='#e8eaf0', size=10)),
        ),
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=20, b=20, l=20, r=20),
        height=280,
    )
    return fig

def make_salary_chart(recommendations):
    cur    = get_currency()
    sym    = cur["symbol"]
    code   = cur["code"]
    titles = [r["career"]["job_title"] for r in recommendations]
    mins   = [convert(r["career"]["salary_min"]) for r in recommendations]
    maxs   = [convert(r["career"]["salary_max"]) for r in recommendations]
    mids   = [(a + b) / 2 for a, b in zip(mins, maxs)]

    fig = go.Figure()
    for i, (title, mn, mx, md) in enumerate(zip(titles, mins, maxs, mids)):
        fig.add_trace(go.Bar(
            name=title, x=[mx - mn], y=[title], orientation='h',
            base=[mn],
            marker=dict(color=['#6c63ff', '#00d4aa', '#ff6b6b'][i % 3], opacity=0.75),
            width=0.5,
        ))
        fig.add_trace(go.Scatter(
            x=[md], y=[title], mode='markers+text',
            marker=dict(color='white', size=8, symbol='diamond'),
            text=[fmt_salary(int(md / cur["rate"]))],
            textposition='middle right',
            textfont=dict(color='#e8eaf0', size=11), showlegend=False,
        ))

    fig.update_layout(
        barmode='overlay', showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(
            gridcolor='#2a2f40', color='#8b90a0',
            title=f'Annual Salary ({code})',
            tickprefix=sym,
            tickformat=',.0f',
        ),
        yaxis=dict(gridcolor='#2a2f40', color='#e8eaf0'),
        margin=dict(t=10, b=40, l=10, r=80), height=180,
    )
    return fig


def generate_pdf_report(user_profile, recommendations):
    """Generate a plain-text PDF-style report as bytes."""
    lines = []
    lines.append("CAREERCOMPASS AI — CAREER RECOMMENDATION REPORT")
    lines.append("=" * 55)
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")
    lines.append("USER PROFILE")
    lines.append("-" * 30)
    lines.append(f"Skills:     {user_profile['skills']}")
    lines.append(f"Education:  {user_profile['education'].capitalize()}")
    lines.append(f"Interests:  {user_profile['interests']}")
    lines.append(f"Experience: {user_profile['experience'].capitalize()}")
    lines.append("")
    lines.append("TOP CAREER RECOMMENDATIONS")
    lines.append("-" * 30)

    for rank, r in enumerate(recommendations, 1):
        c = r["career"]
        have, missing = skill_gap(user_profile['skills'], c['skills'])
        lines.append(f"\n#{rank} — {c['job_title']}")
        lines.append(f"Match Score:  {r['match_pct']}%")
        lines.append(f"Industry:     {c['industry']}")
        lines.append(f"Salary Range: {fmt_salary_range(c['salary_min'], c['salary_max'])}")
        lines.append(f"Job Demand:   {c['demand']}")
        lines.append(f"Description:  {c['description']}")
        lines.append(f"Skills You Have: {', '.join(have) if have else 'None detected'}")
        lines.append(f"Skills to Gain:  {', '.join(missing) if missing else 'All covered!'}")
        lines.append(f"Career Path: {' → '.join(c['progression'])}")
        lines.append(f"Recommended Certifications: {', '.join(c['certifications'])}")

    lines.append("\n" + "=" * 55)
    lines.append("Generated by CareerCompass AI")
    report_text = "\n".join(lines)
    return report_text.encode("utf-8")

# ─────────────────────────────────────────────────────────────────────────────
# CURRENCY CONFIG  (base salaries stored in USD, converted on display)
# ─────────────────────────────────────────────────────────────────────────────
CURRENCIES = {
    "INR – Indian Rupee (₹)":          {"symbol": "₹",  "code": "INR", "rate": 83.5},
    "USD – US Dollar ($)":              {"symbol": "$",  "code": "USD", "rate": 1.0},
    "EUR – Euro (€)":                   {"symbol": "€",  "code": "EUR", "rate": 0.92},
    "GBP – British Pound (£)":          {"symbol": "£",  "code": "GBP", "rate": 0.79},
    "AED – UAE Dirham (د.إ)":           {"symbol": "د.إ","code": "AED", "rate": 3.67},
    "SGD – Singapore Dollar (S$)":      {"symbol": "S$", "code": "SGD", "rate": 1.34},
    "AUD – Australian Dollar (A$)":     {"symbol": "A$", "code": "AUD", "rate": 1.53},
    "CAD – Canadian Dollar (C$)":       {"symbol": "C$", "code": "CAD", "rate": 1.36},
    "JPY – Japanese Yen (¥)":           {"symbol": "¥",  "code": "JPY", "rate": 151.0},
    "CNY – Chinese Yuan (¥)":           {"symbol": "¥",  "code": "CNY", "rate": 7.24},
    "MYR – Malaysian Ringgit (RM)":     {"symbol": "RM", "code": "MYR", "rate": 4.72},
    "SAR – Saudi Riyal (﷼)":            {"symbol": "﷼",  "code": "SAR", "rate": 3.75},
    "BDT – Bangladeshi Taka (৳)":       {"symbol": "৳",  "code": "BDT", "rate": 110.0},
    "PKR – Pakistani Rupee (Rs)":       {"symbol": "Rs", "code": "PKR", "rate": 278.0},
    "NPR – Nepalese Rupee (Rs)":        {"symbol": "Rs", "code": "NPR", "rate": 133.5},
    "ZAR – South African Rand (R)":     {"symbol": "R",  "code": "ZAR", "rate": 18.6},
}

DEFAULT_CURRENCY = "INR – Indian Rupee (₹)"


def get_currency():
    """Return the currently selected currency config dict."""
    key = st.session_state.get("selected_currency", DEFAULT_CURRENCY)
    return CURRENCIES.get(key, CURRENCIES[DEFAULT_CURRENCY])


def fmt_salary(usd_amount):
    """
    Convert a USD salary to the selected currency and format it
    with a smart abbreviation (k / L / Cr for INR, k / M for others).
    """
    cur = get_currency()
    amount = usd_amount * cur["rate"]
    sym    = cur["symbol"]
    code   = cur["code"]

    if code == "INR":
        if amount >= 1_00_00_000:   # 1 Cr+
            return f"{sym}{amount/1_00_00_000:.1f} Cr"
        elif amount >= 1_00_000:     # 1 L+
            return f"{sym}{amount/1_00_000:.1f} L"
        else:
            return f"{sym}{amount/1_000:.1f}k"
    elif code == "JPY":
        if amount >= 1_000_000:
            return f"{sym}{amount/1_000_000:.1f}M"
        return f"{sym}{amount/1_000:.0f}k"
    else:
        if amount >= 1_000_000:
            return f"{sym}{amount/1_000_000:.1f}M"
        return f"{sym}{amount/1_000:.1f}k"


def fmt_salary_range(usd_min, usd_max):
    """Return 'X – Y' formatted string in selected currency."""
    return f"{fmt_salary(usd_min)} – {fmt_salary(usd_max)}"


def convert(usd_amount):
    """Convert USD amount to selected currency value (raw float)."""
    return usd_amount * get_currency()["rate"]


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
if "step" not in st.session_state:
    st.session_state.step = 1
if "profile" not in st.session_state:
    st.session_state.profile = {}
if "results" not in st.session_state:
    st.session_state.results = None
if "history" not in st.session_state:
    st.session_state.history = []
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []
if "chat_career" not in st.session_state:
    st.session_state.chat_career = None

# ─────────────────────────────────────────────────────────────────────────────
# KEY PERSISTENCE — save/load from .env file in the app directory
# ─────────────────────────────────────────────────────────────────────────────
ENV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")

def load_saved_keys():
    """Read keys directly from .env file into session state (no dotenv needed)."""
    if not os.path.exists(ENV_FILE):
        return
    with open(ENV_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if "=" in line and not line.startswith("#"):
                k, _, v = line.partition("=")
                k, v = k.strip(), v.strip().strip('"').strip("'")
                if k == "GROQ_API_KEY" and "groq_api_key" not in st.session_state:
                    st.session_state.groq_api_key = v
                elif k == "ANTHROPIC_API_KEY" and "anthropic_api_key" not in st.session_state:
                    st.session_state.anthropic_api_key = v

def save_key_to_env(key_name: str, value: str):
    """Write or update a key in the .env file."""
    lines = []
    found = False
    if os.path.exists(ENV_FILE):
        with open(ENV_FILE, "r") as f:
            lines = f.readlines()
    new_lines = []
    for line in lines:
        if line.strip().startswith(f"{key_name}="):
            new_lines.append(f'{key_name}="{value}"\n')
            found = True
        else:
            new_lines.append(line)
    if not found:
        new_lines.append(f'{key_name}="{value}"\n')
    with open(ENV_FILE, "w") as f:
        f.writelines(new_lines)

# Load saved keys on every page load
load_saved_keys()

# ─────────────────────────────────────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding: 1rem 0;">
        <div style="font-family:'Syne',sans-serif; font-size:1.4rem; font-weight:800;
                    background:linear-gradient(135deg,#6c63ff,#00d4aa);
                    -webkit-background-clip:text; -webkit-text-fill-color:transparent;">
            🧭 CareerCompass
        </div>
        <div style="color:#8b90a0; font-size:0.8rem; margin-top:0.3rem;">AI-Powered Career Guidance</div>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("🔑 AI Chatbot Setup", expanded=False):
        # Provider selector
        ai_provider = st.selectbox(
            "AI Provider",
            ["Groq (Free)", "Anthropic Claude (Paid)"],
            index=0,
            help="Groq is free with no region restrictions. Anthropic requires paid credits."
        )
        st.session_state.ai_provider = ai_provider

        if ai_provider == "Groq (Free)":
            st.markdown(
                '<div style="color:#00d4aa; font-size:0.78rem; margin-bottom:6px;">'
                'Free forever · No card needed · Works in India.<br>'
                'Get key at <a href="https://console.groq.com/keys" target="_blank" '
                'style="color:#6c63ff;">console.groq.com/keys</a></div>',
                unsafe_allow_html=True
            )
            saved_groq = st.session_state.get("groq_api_key", "")
            typed_key = st.text_input(
                "Groq API key",
                type="password",
                placeholder="gsk_...",
                value=saved_groq,
                key="groq_key_input",
            )
            if typed_key and typed_key != saved_groq:
                st.session_state.groq_api_key = typed_key
                save_key_to_env("GROQ_API_KEY", typed_key)
            elif typed_key:
                st.session_state.groq_api_key = typed_key

            if st.session_state.get("groq_api_key"):
                st.markdown(
                    '<div style="color:#00d4aa; font-size:0.82rem;">✓ Key saved — will auto-load next time</div>',
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    '<div style="color:#8b90a0; font-size:0.78rem;">Paste your key once — it\'s saved automatically</div>',
                    unsafe_allow_html=True
                )

        else:
            saved_ant = st.session_state.get("anthropic_api_key", "")
            typed_key = st.text_input(
                "Anthropic API key",
                type="password",
                placeholder="sk-ant-...",
                value=saved_ant,
                key="api_key_input",
            )
            if typed_key and typed_key != saved_ant:
                st.session_state.anthropic_api_key = typed_key
                save_key_to_env("ANTHROPIC_API_KEY", typed_key)
            elif typed_key:
                st.session_state.anthropic_api_key = typed_key

            if st.session_state.get("anthropic_api_key"):
                st.markdown(
                    '<div style="color:#00d4aa; font-size:0.82rem;">✓ Key saved — will auto-load next time</div>',
                    unsafe_allow_html=True
                )
            elif typed_key:
                st.markdown(
                    '<div style="color:#ff6b6b; font-size:0.82rem;">⚠️ Key should start with sk-ant-</div>',
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    '<div style="color:#8b90a0; font-size:0.78rem;">'
                    'Get key at <a href="https://console.anthropic.com/settings/keys" target="_blank" '
                    'style="color:#6c63ff;">console.anthropic.com</a></div>',
                    unsafe_allow_html=True
                )

    st.markdown("---")
    st.markdown('<div class="section-title">⚙️ Model Settings</div>', unsafe_allow_html=True)
    model_choice = st.selectbox("Algorithm", ["Ensemble", "Random Forest", "Gradient Boosting"])
    top_n = st.slider("Results to show", 1, 5, 3)

    st.markdown("---")
    st.markdown('<div class="section-title">💱 Salary Currency</div>', unsafe_allow_html=True)
    selected_currency = st.selectbox(
        "Display salaries in",
        list(CURRENCIES.keys()),
        index=list(CURRENCIES.keys()).index(DEFAULT_CURRENCY),
        key="selected_currency",
        help="All salaries are stored in USD and converted at approximate rates."
    )
    cur = CURRENCIES[selected_currency]
    st.markdown(
        f'<div style="color:#8b90a0; font-size:0.78rem; margin-top:4px;">'
        f'1 USD ≈ {cur["rate"]} {cur["code"]} &nbsp;|&nbsp; '
        f'Symbol: <b style="color:#e8eaf0">{cur["symbol"]}</b>'
        f'</div>',
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.markdown('<div class="section-title">📁 Resume Upload</div>', unsafe_allow_html=True)

    accept_types = ["txt", "pdf"] if PDF_SUPPORT else ["txt"]
    label = "Upload your resume (.txt or .pdf)" if PDF_SUPPORT else "Upload your resume (.txt)"
    if not PDF_SUPPORT:
        st.markdown('<div style="color:#ff6b6b; font-size:0.78rem;">⚠️ Install PyPDF2 for PDF support:<br><code>pip install PyPDF2</code></div>', unsafe_allow_html=True)

    uploaded_file = st.file_uploader(label, type=accept_types)
    if uploaded_file:
        file_bytes = uploaded_file.read()
        if uploaded_file.name.lower().endswith(".pdf"):
            if PDF_SUPPORT:
                with st.spinner("Reading PDF..."):
                    text = extract_text_from_pdf(file_bytes)
                if not text.strip():
                    st.warning("Could not extract text from PDF. It may be scanned/image-based. Try a text-based PDF or paste skills manually.")
                    text = ""
            else:
                st.error("PyPDF2 not installed. Run: pip install PyPDF2")
                text = ""
        else:
            text = file_bytes.decode("utf-8", errors="ignore")

        if text:
            extracted = extract_skills_from_text(text)
            if extracted:
                skill_count = len(extracted.split(','))
                st.success(f"✓ Extracted {skill_count} skills from your resume")
                st.session_state.profile["auto_skills"] = extracted
                # Show a preview of extracted text
                with st.expander("📄 Resume text preview"):
                    st.text(text[:800] + ("..." if len(text) > 800 else ""))
            else:
                st.warning("No recognizable skills found. Try entering them manually.")

    st.markdown("---")
    st.markdown('<div class="section-title">🕘 Session History</div>', unsafe_allow_html=True)
    if st.session_state.history:
        for i, h in enumerate(st.session_state.history[-3:]):
            st.markdown(f"""<div class="card" style="padding:0.7rem; margin-bottom:0.5rem;">
                <div style="font-size:0.78rem; color:#8b90a0;">{h['time']}</div>
                <div style="font-size:0.85rem; color:#e8eaf0;">{h['top']}</div>
            </div>""", unsafe_allow_html=True)
    else:
        st.markdown('<div style="color:#8b90a0; font-size:0.85rem;">No history yet.</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<div class="section-title">ℹ️ How It Works</div>', unsafe_allow_html=True)
    st.markdown("""<div style="color:#8b90a0; font-size:0.82rem; line-height:1.6;">
        <b style="color:#e8eaf0">TF-IDF</b> vectorizes your profile.<br>
        <b style="color:#e8eaf0">Ensemble</b> of RF + GBM predicts fit.<br>
        <b style="color:#e8eaf0">Cosine similarity</b> measures skill match.<br>
        Combined score ranks careers.
    </div>""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# MAIN CONTENT
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""<div class="main-header">
    <h1>CareerCompass AI</h1>
    <p>Discover your ideal career path with machine learning-powered recommendations</p>
</div>""", unsafe_allow_html=True)

# Step indicators
step = st.session_state.step
steps = ["Education", "Skills", "Interests", "Results"]
indicator_html = '<div class="step-indicator">'
for i, s in enumerate(steps, 1):
    cls = "active" if i == step else ("done" if i < step else "")
    indicator_html += f'<div class="step-dot {cls}">{i}</div>'
    if i < len(steps):
        indicator_html += f'<div class="step-line {"done" if i < step else ""}"></div>'
indicator_html += '</div>'
st.markdown(indicator_html, unsafe_allow_html=True)

# ─── STEP 1: Education & Experience ──────────────────────────────────────────
if step == 1:
    st.markdown('<div class="section-title">🎓 Step 1: Education & Experience</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        education = st.selectbox("Highest Education Level",
            ["highschool", "associate", "bachelor", "master", "phd"],
            index=2,
            help="Select your highest completed or expected degree")
    with col2:
        experience = st.selectbox("Experience Level",
            ["entry", "junior", "mid", "senior"],
            index=1,
            help="How many years of professional experience do you have?")

    exp_desc = {"entry": "0–1 years", "junior": "1–3 years", "mid": "3–7 years", "senior": "7+ years"}
    st.markdown(f'<div class="info-box">📌 {exp_desc[experience]} of professional experience</div>', unsafe_allow_html=True)

    if st.button("Next →", key="step1"):
        st.session_state.profile["education"] = education
        st.session_state.profile["experience"] = experience
        st.session_state.step = 2
        st.rerun()

# ─── STEP 2: Skills ──────────────────────────────────────────────────────────
elif step == 2:
    st.markdown('<div class="section-title">🛠 Step 2: Your Skills</div>', unsafe_allow_html=True)

    default_skills = st.session_state.profile.get("auto_skills", "")
    skills = st.text_area(
        "Enter your skills (comma-separated)",
        value=default_skills,
        placeholder="e.g. python, data analysis, communication, excel",
        height=100,
        help="Be specific — list tools, languages, soft skills, and domain knowledge"
    )

    if skills:
        skill_list = [s.strip() for s in skills.split(",") if s.strip()]
        st.markdown(f'<div class="info-box">✓ {len(skill_list)} skills detected</div>', unsafe_allow_html=True)
        cols = st.columns(min(len(skill_list), 6))
        for i, s in enumerate(skill_list[:12]):
            with cols[i % 6]:
                st.markdown(f'<span class="skill-tag have">{s}</span>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("← Back", key="step2b"):
            st.session_state.step = 1
            st.rerun()
    with col2:
        if st.button("Next →", key="step2"):
            if not skills.strip():
                st.error("Please enter at least one skill.")
            else:
                st.session_state.profile["skills"] = skills
                st.session_state.step = 3
                st.rerun()

# ─── STEP 3: Interests ───────────────────────────────────────────────────────
elif step == 3:
    st.markdown('<div class="section-title">💡 Step 3: Interests & Preferences</div>', unsafe_allow_html=True)

    interests = st.text_input(
        "Your interests (comma-separated)",
        placeholder="e.g. data, research, problem solving, creativity",
        help="Think about topics you enjoy reading about, hobbies, or subjects you loved in school"
    )

    st.markdown("**Industry Preference** (optional)")
    industries = ["Any", "Technology", "Finance", "Healthcare", "Education", "Marketing", "Engineering", "Creative", "Business", "Science", "Performing Arts", "Sports & Fitness", "Hospitality", "Legal", "Government", "Sustainability", "Future Tech"]
    industry_pref = st.select_slider("", options=industries, value="Any")

    personality = st.radio(
        "Work style preference",
        ["Analytical / Data-driven", "Creative / Visual", "People-oriented / Leadership", "Technical / Engineering", "Mixed"],
        horizontal=True
    )

    st.markdown("---")
    st.markdown("**🔍 Looking for a specific career not in our list?**")
    st.markdown('<div style="color:#8b90a0; font-size:0.83rem; margin-bottom:0.5rem;">Type any job title and our AI will generate a full career profile for it instantly.</div>', unsafe_allow_html=True)
    custom_career = st.text_input(
        "Custom career (optional)",
        placeholder="e.g. Drone Pilot, Perfumer, Ethical Hacker, Streetwear Designer...",
        key="custom_career_input"
    )

    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("← Back", key="step3b"):
            st.session_state.step = 2
            st.rerun()
    with col2:
        if st.button("🔍 Find My Career", key="step3"):
            if not interests.strip():
                st.error("Please enter at least one interest.")
            else:
                st.session_state.profile["interests"]     = interests
                st.session_state.profile["industry_pref"] = industry_pref
                st.session_state.profile["personality"]   = personality
                st.session_state.profile["custom_career"] = custom_career.strip()
                st.session_state.step = 4

                # Auto-detect if user typed a specific career not in dataset
                if not custom_career.strip():
                    auto_detected = detect_unknown_career(
                        st.session_state.profile["skills"], interests
                    )
                    if auto_detected:
                        st.session_state.profile["custom_career"] = auto_detected

                # Run dataset recommendations
                results = get_recommendations(
                    st.session_state.profile["skills"],
                    st.session_state.profile["education"],
                    interests,
                    st.session_state.profile["experience"],
                    model_choice, top_n
                )
                st.session_state.results = results
                st.session_state.ai_career = None  # reset

                # Save to history
                st.session_state.history.append({
                    "time": datetime.now().strftime("%H:%M"),
                    "top": results[0]["career"]["job_title"] if results else "N/A"
                })
                st.rerun()

# ─── STEP 4: Results ─────────────────────────────────────────────────────────
elif step == 4:
    results = st.session_state.results
    profile = st.session_state.profile

    if not results:
        st.error("No results found. Please try again.")
        if st.button("Start Over"):
            st.session_state.step = 1
            st.rerun()
    else:
        # ── AI Career Generator ───────────────────────────────────────────
        custom_career = profile.get("custom_career", "").strip()
        top_score     = results[0]["score"] if results else 0

        # Trigger AI generation if: custom career entered OR dataset confidence is low
        LOW_CONFIDENCE = top_score < 0.25
        generate_ai    = bool(custom_career) or LOW_CONFIDENCE

        if generate_ai:
            target_title = custom_career if custom_career else (
                profile.get("skills", "").split(",")[0].strip().title() + " Specialist"
            )
            has_key = st.session_state.get("groq_api_key") or st.session_state.get("anthropic_api_key")

            if has_key:
                # Only generate once per session per title
                cache_key = f"ai_career_{target_title.lower()}"
                if cache_key not in st.session_state:
                    if LOW_CONFIDENCE and not custom_career:
                        st.info(f"🤖 Our dataset doesn't have a strong match for your profile. Using AI to generate a custom career recommendation...")
                    else:
                        st.info(f"🤖 Generating AI career profile for **{target_title}**...")

                    with st.spinner("AI is building your career profile..."):
                        ai_career = ai_generate_career(
                            target_title,
                            profile.get("skills", ""),
                            profile.get("interests", ""),
                            profile.get("education", "bachelor"),
                            profile.get("experience", "junior"),
                        )
                    st.session_state[cache_key] = ai_career
                else:
                    ai_career = st.session_state[cache_key]

                if ai_career:
                    st.markdown(f"""
                    <div style="background:linear-gradient(135deg,#6c63ff11,#00d4aa11);
                                border:1px solid #6c63ff44; border-radius:14px;
                                padding:1rem 1.4rem; margin-bottom:1.5rem;">
                        <div style="font-family:'Syne',sans-serif; font-size:0.78rem;
                                    color:#6c63ff; font-weight:600; letter-spacing:0.08em;
                                    margin-bottom:0.5rem;">✨ AI-GENERATED CAREER PROFILE</div>
                        <div style="font-family:'Syne',sans-serif; font-size:1.25rem;
                                    font-weight:700; color:#e8eaf0; margin-bottom:0.3rem;">
                            {ai_career['job_title']}
                        </div>
                        <div style="color:#8b90a0; font-size:0.88rem; margin-bottom:0.8rem;">
                            {ai_career['description']}
                        </div>
                        <div>
                            <span class="stat-chip">🏭 {ai_career['industry']}</span>
                            <span class="stat-chip">📈 {ai_career['demand']} Demand</span>
                            <span class="stat-chip">💰 {fmt_salary_range(ai_career['salary_min'], ai_career['salary_max'])}</span>
                            <span class="stat-chip">🎓 {ai_career['education'].capitalize()}</span>
                        </div>
                        <div style="margin-top:0.8rem;">
                            <div style="font-size:0.82rem; color:#8b90a0; margin-bottom:0.4rem;">Required Skills</div>
                            <div>{"".join([f'<span class="skill-tag">{s.strip()}</span>' for s in ai_career["skills"].split(",")[:10]])}</div>
                        </div>
                        <div style="margin-top:0.8rem;">
                            <div style="font-size:0.82rem; color:#8b90a0; margin-bottom:0.4rem;">Career Path</div>
                            <div style="display:flex; flex-wrap:wrap; gap:0.3rem; align-items:center;">
                                {"".join([f'<span class="stat-chip" style="background:#6c63ff18;border-color:#6c63ff44;color:#a8a3ff;">{p}</span>{"<span style=color:#00d4aa;font-weight:bold;>→</span>" if i < len(ai_career["progression"])-1 else ""}' for i, p in enumerate(ai_career["progression"])])}
                            </div>
                        </div>
                        <div style="margin-top:0.8rem;">
                            <div style="font-size:0.82rem; color:#8b90a0; margin-bottom:0.3rem;">Recommended Certifications</div>
                            <div>{"".join([f'<span class="skill-tag">{c}</span>' for c in ai_career["certifications"]])}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                    # Job portal links for AI career
                    st.markdown("**🌐 Apply for This Role**")
                    jq = ai_career['job_title'].replace(" ", "%20")
                    jq_plus = ai_career['job_title'].replace(" ", "+")
                    jq_naukri = ai_career['job_title'].replace(" ", "-").lower()
                    portals_html = f'''<div style="display:flex;flex-wrap:wrap;gap:0.5rem;margin:0.5rem 0;">
                        <a href="https://www.linkedin.com/jobs/search/?keywords={jq}&location=India" target="_blank" style="display:inline-flex;align-items:center;gap:0.4rem;background:#0077b518;border:1px solid #0077b544;color:#0077b5;text-decoration:none;border-radius:8px;padding:0.4rem 0.9rem;font-size:0.82rem;font-weight:500;">💼 LinkedIn</a>
                        <a href="https://www.naukri.com/{jq_naukri}-jobs" target="_blank" style="display:inline-flex;align-items:center;gap:0.4rem;background:#4CAF5018;border:1px solid #4CAF5044;color:#4CAF50;text-decoration:none;border-radius:8px;padding:0.4rem 0.9rem;font-size:0.82rem;font-weight:500;">🏢 Naukri</a>
                        <a href="https://in.indeed.com/jobs?q={jq_plus}&l=India" target="_blank" style="display:inline-flex;align-items:center;gap:0.4rem;background:#2164f318;border:1px solid #2164f344;color:#2164f3;text-decoration:none;border-radius:8px;padding:0.4rem 0.9rem;font-size:0.82rem;font-weight:500;">🔍 Indeed</a>
                        <a href="https://internshala.com/jobs/{jq_naukri}-jobs/" target="_blank" style="display:inline-flex;align-items:center;gap:0.4rem;background:#00b5ad18;border:1px solid #00b5ad44;color:#00b5ad;text-decoration:none;border-radius:8px;padding:0.4rem 0.9rem;font-size:0.82rem;font-weight:500;">🎓 Internshala</a>
                    </div>'''
                    st.markdown(portals_html, unsafe_allow_html=True)
                    st.markdown("---")
                else:
                    st.warning("⚠️ AI couldn't generate a profile right now. Showing dataset results below.")
            else:
                if custom_career:
                    st.markdown(f"""<div class="info-box">
                        💡 <b>"{custom_career}"</b> isn't in our dataset yet. 
                        To instantly generate a full AI career profile for any job title,
                        add your free Groq API key in the sidebar 
                        (click <b>🔑 AI Chatbot Setup</b> → get key at 
                        <a href="https://console.groq.com/keys" target="_blank" style="color:#6c63ff;">console.groq.com/keys</a>).
                        Showing closest dataset matches below.
                    </div>""", unsafe_allow_html=True)
                elif LOW_CONFIDENCE:
                    st.markdown("""<div class="info-box">
                        💡 Your input seems to be a niche or unlisted career. 
                        Add your free Groq key in the sidebar to get an AI-generated
                        profile for any career instantly. Showing closest matches below.
                    </div>""", unsafe_allow_html=True)
        # Header metrics
        cols = st.columns(4)
        metrics = [
            ("Top Match", results[0]["career"]["job_title"], "🏆"),
            ("Match Score", f"{results[0]['match_pct']}%", "🎯"),
            ("Salary Range", fmt_salary_range(results[0]['career']['salary_min'], results[0]['career']['salary_max']), "💰"),
            ("Job Demand", results[0]["career"]["demand"], "📈"),
        ]
        for col, (label, val, icon) in zip(cols, metrics):
            with col:
                st.markdown(f"""<div class="metric-card">
                    <div style="font-size:1.4rem">{icon}</div>
                    <div class="metric-value" style="font-size:1.3rem">{val}</div>
                    <div class="metric-label">{label}</div>
                </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Salary comparison chart
        with st.expander("💰 Salary Range Comparison", expanded=True):
            st.plotly_chart(make_salary_chart(results), use_container_width=True, key="salary_chart")

        # Career cards
        st.markdown('<div class="section-title">🏆 Your Top Career Matches</div>', unsafe_allow_html=True)

        for rank, r in enumerate(results, 1):
            c = r["career"]
            have, missing = skill_gap(profile.get("skills", ""), c["skills"])
            match_pct = r["match_pct"]

            with st.expander(f"#{rank} · {c['job_title']} — {match_pct}% match · {c['industry']}", expanded=(rank == 1)):

                col_left, col_right = st.columns([3, 2])

                with col_left:
                    st.markdown(f"""<div class="career-card">
                        <div class="rank-badge">#{rank} MATCH</div>
                        <h3>{c['job_title']}</h3>
                        <p class="description">{c['description']}</p>
                        <div class="match-bar-container">
                            <div class="match-bar-label">
                                <span>Overall Match</span><span>{match_pct}%</span>
                            </div>
                            <div class="match-bar-track">
                                <div class="match-bar-fill" style="width:{match_pct}%"></div>
                            </div>
                        </div>
                        <div style="margin:0.8rem 0">
                            <span class="stat-chip">🏭 {c['industry']}</span>
                            <span class="stat-chip">📈 {c['demand']} Demand</span>
                            <span class="stat-chip">🎓 {c['education'].capitalize()}</span>
                            <span class="stat-chip">⏱ {c['experience'].capitalize()}</span>
                        </div>
                    </div>""", unsafe_allow_html=True)

                with col_right:
                    st.plotly_chart(make_radar_chart(profile.get("skills",""), c), use_container_width=True, key=f"radar_chart_{rank}")

                # Skill gap
                st.markdown("**🟢 Skills You Already Have**")
                if have:
                    tags = "".join([f'<span class="skill-tag have">✓ {s}</span>' for s in have])
                    st.markdown(tags, unsafe_allow_html=True)
                else:
                    st.markdown('<span style="color:#8b90a0; font-size:0.85rem">No direct skill matches — but that\'s okay!</span>', unsafe_allow_html=True)

                st.markdown("**🔴 Skills to Develop**")
                if missing:
                    tags = "".join([f'<span class="skill-tag missing">+ {s}</span>' for s in missing])
                    st.markdown(tags, unsafe_allow_html=True)
                else:
                    st.markdown('<span style="color:#00d4aa; font-size:0.85rem">🎉 You already have all the key skills!</span>', unsafe_allow_html=True)

                # Career progression
                st.markdown("**🛤 Career Progression Roadmap**")
                prog_html = '<div style="display:flex; flex-wrap:wrap; gap:0.4rem; align-items:center; margin:0.5rem 0;">'
                for i, p in enumerate(c["progression"]):
                    prog_html += f'<span class="stat-chip" style="background:#6c63ff18; border-color:#6c63ff44; color:#a8a3ff;">{p}</span>'
                    if i < len(c["progression"]) - 1:
                        prog_html += '<span style="color:#00d4aa; font-weight:bold;">→</span>'
                prog_html += '</div>'
                st.markdown(prog_html, unsafe_allow_html=True)

                # Certifications
                st.markdown("**🏅 Recommended Certifications**")
                cert_html = "".join([f'<span class="skill-tag">{cert}</span>' for cert in c["certifications"]])
                st.markdown(cert_html, unsafe_allow_html=True)

                # Learning resources
                st.markdown("**📚 Learning Resources**")
                for url in c["courses"]:
                    st.markdown(f"- [{url}]({url})")

                # ── Job Portal Links ──────────────────────────────────────
                st.markdown("**🌐 Apply for This Role**")
                job_query = c["job_title"].replace(" ", "%20").replace("/", "%20")
                job_query_plus = c["job_title"].replace(" ", "+").replace("/", "+")
                job_query_naukri = c["job_title"].replace(" ", "-").replace("/", "-").lower()

                portals = [
                    {
                        "name": "LinkedIn",
                        "icon": "💼",
                        "url": f"https://www.linkedin.com/jobs/search/?keywords={job_query}&location=India",
                        "color": "#0077b5",
                        "bg": "#0077b518",
                        "border": "#0077b544",
                    },
                    {
                        "name": "Naukri",
                        "icon": "🏢",
                        "url": f"https://www.naukri.com/{job_query_naukri}-jobs",
                        "color": "#4CAF50",
                        "bg": "#4CAF5018",
                        "border": "#4CAF5044",
                    },
                    {
                        "name": "Indeed",
                        "icon": "🔍",
                        "url": f"https://in.indeed.com/jobs?q={job_query_plus}&l=India",
                        "color": "#2164f3",
                        "bg": "#2164f318",
                        "border": "#2164f344",
                    },
                    {
                        "name": "Glassdoor",
                        "icon": "🪟",
                        "url": f"https://www.glassdoor.co.in/Job/india-{job_query_naukri}-jobs-SRCH_IL.0,5_IN115_KO6,{6+len(c['job_title'])}.htm",
                        "color": "#0caa41",
                        "bg": "#0caa4118",
                        "border": "#0caa4144",
                    },
                    {
                        "name": "Internshala",
                        "icon": "🎓",
                        "url": f"https://internshala.com/jobs/{job_query_naukri}-jobs/",
                        "color": "#00b5ad",
                        "bg": "#00b5ad18",
                        "border": "#00b5ad44",
                    },
                    {
                        "name": "Wellfound",
                        "icon": "🚀",
                        "url": f"https://wellfound.com/jobs?q={job_query_plus}",
                        "color": "#ef4444",
                        "bg": "#ef444418",
                        "border": "#ef444444",
                    },
                ]

                portal_html = '<div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin:0.6rem 0;">'
                for p in portals:
                    portal_html += f'''
                        <a href="{p["url"]}" target="_blank" style="
                            display:inline-flex; align-items:center; gap:0.4rem;
                            background:{p["bg"]}; border:1px solid {p["border"]};
                            color:{p["color"]}; text-decoration:none;
                            border-radius:8px; padding:0.4rem 0.9rem;
                            font-size:0.82rem; font-weight:500;
                            transition:opacity 0.2s;">
                            {p["icon"]} {p["name"]}
                        </a>'''
                portal_html += '</div>'
                portal_html += f'<div style="color:#8b90a0; font-size:0.75rem; margin-top:0.3rem;">🔎 Searching for: <em>{c["job_title"]}</em> in India — click any portal to view live listings</div>'
                st.markdown(portal_html, unsafe_allow_html=True)

        # Download report
        st.markdown("---")
        col_dl, col_restart = st.columns([2, 1])
        with col_dl:
            report_bytes = generate_pdf_report(profile, results)
            st.download_button(
                label="📥 Download Full Report (.txt)",
                data=report_bytes,
                file_name=f"career_report_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
                mime="text/plain",
            )
        with col_restart:
            if st.button("🔄 Start New Assessment"):
                st.session_state.step = 1
                st.session_state.profile = {}
                st.session_state.results = None
                st.session_state.chat_messages = []
                st.session_state.chat_career = None
                st.rerun()

        # ── AI CAREER CHATBOT ─────────────────────────────────────────────────
        st.markdown("---")
        st.markdown("""<div style="margin-bottom:1rem;">
            <div style="font-family:'Syne',sans-serif; font-size:1.3rem; font-weight:700; color:#e8eaf0;">
                🤖 AI Career Advisor
            </div>
            <div style="color:#8b90a0; font-size:0.88rem; margin-top:0.3rem;">
                Ask anything about your recommended careers — salary negotiation, day-in-the-life,
                required skills, interview tips, switching industries, and more.
            </div>
        </div>""", unsafe_allow_html=True)

        # Career selector for chat context
        career_names = [r["career"]["job_title"] for r in results]
        selected_chat_career = st.selectbox(
            "Ask about a specific career:",
            ["All my recommendations"] + career_names,
            key="chat_career_select"
        )

        # Suggested quick questions
        st.markdown('<div style="font-size:0.82rem; color:#8b90a0; margin-bottom:0.5rem;">Quick questions:</div>', unsafe_allow_html=True)
        quick_cols = st.columns(4)
        quick_questions = [
            "What does a typical day look like?",
            "How do I break into this field?",
            "What salary should I negotiate for?",
            "What are the biggest challenges?",
        ]
        for i, (col, q) in enumerate(zip(quick_cols, quick_questions)):
            with col:
                if st.button(q, key=f"quick_{i}"):
                    st.session_state.chat_messages.append({"role": "user", "content": q})
                    st.session_state.chat_career = selected_chat_career
                    st.rerun()

        # Chat history display
        chat_container = st.container()
        with chat_container:
            for msg in st.session_state.chat_messages:
                if msg["role"] == "user":
                    st.markdown(f"""<div style="display:flex; justify-content:flex-end; margin:0.6rem 0;">
                        <div style="background:#6c63ff; color:white; border-radius:16px 16px 4px 16px;
                                    padding:0.7rem 1.1rem; max-width:75%; font-size:0.9rem; line-height:1.5;">
                            {msg['content']}
                        </div>
                    </div>""", unsafe_allow_html=True)
                else:
                    st.markdown(f"""<div style="display:flex; justify-content:flex-start; margin:0.6rem 0; gap:0.6rem;">
                        <div style="width:32px; height:32px; border-radius:50%; background:linear-gradient(135deg,#6c63ff,#00d4aa);
                                    display:flex; align-items:center; justify-content:center; flex-shrink:0;
                                    font-size:0.85rem; margin-top:2px;">🤖</div>
                        <div style="background:#1e2230; border:1px solid #2a2f40; color:#e8eaf0;
                                    border-radius:4px 16px 16px 16px; padding:0.7rem 1.1rem;
                                    max-width:80%; font-size:0.9rem; line-height:1.6;">
                            {msg['content'].replace(chr(10), '<br>')}
                        </div>
                    </div>""", unsafe_allow_html=True)

        # Auto-reply to any pending unanswered user message
        if (st.session_state.chat_messages
                and st.session_state.chat_messages[-1]["role"] == "user"):

            # Build system prompt with full career context
            if selected_chat_career == "All my recommendations":
                context_careers = results
            else:
                context_careers = [r for r in results if r["career"]["job_title"] == selected_chat_career]

            career_context_str = ""
            for r in context_careers:
                c = r["career"]
                have, missing = skill_gap(profile.get("skills", ""), c["skills"])
                career_context_str += f"""
Career: {c['job_title']}
Industry: {c['industry']}
Match Score: {r['match_pct']}%
Salary Range: {fmt_salary_range(c['salary_min'], c['salary_max'])}
Job Demand: {c['demand']}
Description: {c['description']}
Required Skills: {c['skills']}
Skills the user already has: {', '.join(have) if have else 'None matched'}
Skills the user needs to develop: {', '.join(missing) if missing else 'All covered'}
Career Progression: {' → '.join(c['progression'])}
Recommended Certifications: {', '.join(c['certifications'])}
Education Required: {c['education'].capitalize()}
"""

            system_prompt = f"""You are CareerCompass AI, a warm, knowledgeable career advisor embedded in a career recommendation app.

The user has completed a career assessment with this profile:
- Skills: {profile.get('skills', 'Not provided')}
- Education: {profile.get('education', 'Not provided')}
- Interests: {profile.get('interests', 'Not provided')}
- Experience Level: {profile.get('experience', 'Not provided')}

Their recommended career(s) context:
{career_context_str}

Your job is to answer their questions specifically and helpfully using the context above.
Be conversational, encouraging, and practical. Give concrete actionable advice.
Keep responses concise (3-5 sentences or a short bullet list). 
Do not repeat the career data back verbatim — synthesize it into natural advice.
If asked something outside career guidance, politely redirect to career topics."""

            with st.spinner("CareerCompass AI is thinking..."):
                provider = st.session_state.get("ai_provider", "Groq (Free)")

                if provider == "Groq (Free)":
                    api_key = st.session_state.get("groq_api_key", "")
                    if not api_key:
                        reply = "⚠️ No Groq key set. Get your free key at console.groq.com/keys and paste it in the sidebar."
                    elif not GROQ_AVAILABLE:
                        reply = "⚠️ Groq library not installed. Run: pip install groq"
                    else:
                        try:
                            client = Groq(api_key=api_key)
                            messages = [{"role": "system", "content": system_prompt}]
                            messages += [
                                {"role": m["role"], "content": m["content"]}
                                for m in st.session_state.chat_messages
                            ]
                            response = client.chat.completions.create(
                                model="llama-3.3-70b-versatile",
                                messages=messages,
                                max_tokens=600,
                            )
                            reply = response.choices[0].message.content
                        except Exception as e:
                            err = str(e)
                            if "401" in err or "invalid_api_key" in err.lower():
                                reply = "⚠️ Invalid Groq key. Double-check the key in the sidebar — it should start with 'gsk_'."
                            elif "429" in err:
                                reply = "⚠️ Groq rate limit hit. Wait a moment and try again."
                            else:
                                reply = f"⚠️ Groq error: {err}"

                else:
                    api_key = st.session_state.get("anthropic_api_key", "")
                    if not api_key:
                        reply = "⚠️ No Anthropic key set. Paste your key in the sidebar."
                    else:
                        try:
                            client = anthropic.Anthropic(api_key=api_key)
                            api_messages = [
                                {"role": m["role"], "content": m["content"]}
                                for m in st.session_state.chat_messages
                            ]
                            response = client.messages.create(
                                model="claude-haiku-4-5-20251001",
                                max_tokens=600,
                                system=system_prompt,
                                messages=api_messages,
                            )
                            reply = response.content[0].text
                        except anthropic.AuthenticationError:
                            reply = "⚠️ Invalid Anthropic key. It should start with 'sk-ant-'."
                        except Exception as e:
                            reply = f"⚠️ Anthropic error: {str(e)}"

            st.session_state.chat_messages.append({"role": "assistant", "content": reply})
            st.rerun()

        # Chat input
        st.markdown("<div style='margin-top:0.8rem;'></div>", unsafe_allow_html=True)
        with st.form(key="chat_form", clear_on_submit=True):
            col_input, col_send = st.columns([5, 1])
            with col_input:
                user_input = st.text_input(
                    "Message",
                    placeholder="Ask anything about your career recommendations...",
                    label_visibility="collapsed",
                )
            with col_send:
                send = st.form_submit_button("Send →")

        if send and user_input.strip():
            st.session_state.chat_messages.append({"role": "user", "content": user_input.strip()})
            st.session_state.chat_career = selected_chat_career
            st.rerun()

        # Clear chat button
        if st.session_state.chat_messages:
            if st.button("🗑 Clear chat", key="clear_chat"):
                st.session_state.chat_messages = []
                st.rerun()