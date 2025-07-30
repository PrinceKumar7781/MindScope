import streamlit as st

def set_custom_page_config():
    st.set_page_config(
        page_title="MindScope | AI-Powered Research Insight Generator",
        layout="wide",
        page_icon="🧠",
        initial_sidebar_state="collapsed"
    )

def inject_custom_css():
    st.markdown("""
    <style>
    /* GLOBAL RESET */
    html, body, [class*="css"]  {
        font-family: 'Segoe UI', sans-serif;
        transition: background-color 0.3s ease, color 0.3s ease;
    }

    /* Buttons */
    .stButton>button {
        border-radius: 8px;
        padding: 0.6em 1.4em;
        font-weight: 600;
        border: none;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    }

    /* Upload area container styling */
    .stFileUploader {
        border: 2px dashed #6366f1;
        border-radius: 12px;
        padding: 1em;
    }

    /* Specific styles for File Uploader text */
    [data-theme="light"] .stFileUploader label,
    [data-theme="light"] .stFileUploader > div > button + div,
    [data-theme="light"] .stFileUploader span {
        color: var(--text-color) !important;
    }
    [data-theme="dark"] .stFileUploader label,
    [data-theme="dark"] .stFileUploader > div > button + div,
    [data-theme="dark"] .stFileUploader span {
        color: var(--text-color) !important;
    }


    /* Hero Header */
    .hero-header h1 {
        font-size: 3rem;
        font-weight: bold;
    }

    .hero-header p {
        font-size: 1.2rem;
        margin-top: -1rem;
        color: #6b7280;
    }

    /* Streamlit Alert Boxes: Info and Success */
    /* Light theme info */
    .stAlert.info {
        background-color: #e0f2fe; /* Light blue background */
        color: #0c4a6e !important; /* Dark blue text */
    }
    /* Dark theme info */
    [data-theme="dark"] .stAlert.info {
        background-color: #1e3a8a; /* Darker blue background */
        color: #bfdbfe !important; /* Lighter blue text */
    }

    /* Light theme success */
    .stAlert.success {
        background-color: #dcfce7; /* Light green background */
        color: #166534 !important; /* Dark green text */
    }
    /* Dark theme success */
    [data-theme="dark"] .stAlert.success {
        background-color: #166534; /* Darker green background */
        color: #bbf7d0 !important; /* Lighter green text */
    }

    /* About Expander Content Specific Styles */
    .st-expander {
        background-color: var(--background-color-secondary);
        border-radius: 10px;
        padding: 1em;
        border: 1px solid var(--border-color);
    }
    .st-expander details summary,
    .st-expander details div {
        color: var(--text-color) !important;
    }

    /* Universal text color for various Streamlit elements */
    .stText,
    .stMarkdown,
    .stLabel,
    .stBlock,
    .stTextInput>div>label,
    .stTextArea>label,
    .stSelectbox>label,
    .stRadio>label,
    .stCheckbox>label {
        color: var(--text-color) !important;
    }

    /* Input and TextArea specific styling */
    .stTextInput>div>div>input,
    .stTextArea>div>textarea {
        background-color: var(--input-background-color);
        color: var(--input-text-color) !important;
        border: 1px solid var(--input-border-color);
    }

    </style>
    """, unsafe_allow_html=True)


def theme_toggle():
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = True # Default to dark mode

    toggle = st.button("🌙 ", key="theme_toggle")
    if toggle:
        st.session_state.dark_mode = not st.session_state.dark_mode

    # Set dynamic CSS variables for theme on :root
    if st.session_state.dark_mode:
        st.markdown("""
        <style>
        :root {
            --text-color: #f8fafc;
            --background-color: #0f172a;
            --background-color-secondary: #1e293b;
            --border-color: #374151;
            --input-background-color: #1f2937;
            --input-text-color: #ffffff;
            --input-border-color: #374151;
        }
        body, .stApp {
            background-color: var(--background-color) !important; /* Ensure main app background is set */
            color: var(--text-color) !important; /* Ensure general text color is set */
        }
        .stButton>button {
            background: #4f46e5;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <style>
        :root {
            --text-color: #111827; /* Dark text for contrast */
            --background-color: #f0f2f5; /* Light grayish background for main app */
            --background-color-secondary: #e6e8eb; /* Slightly darker grayish for components */
            --border-color: #c0c0c0;
            --input-background-color: #ffffff;
            --input-text-color: #000000;
            --input-border-color: #d1d5db;
        }
        body, .stApp {
            background-color: var(--background-color) !important; /* Ensure main app background is set */
            color: var(--text-color) !important; /* Ensure general text color is set */
        }
        .stButton>button {
            background: linear-gradient(135deg, #4f46e5, #6366f1);
            color: white;
        }
        </style>
        """, unsafe_allow_html=True)


def about_section():
    with st.expander("About MindScope 🧠"):
        st.markdown("""
            <p>
                <b>MindScope</b> is a privacy-focused, AI-powered research assistant that helps users:
                <ul>
                    <li>📄 Summarize academic content</li>
                    <li>🧠 Generate mind maps</li>
                    <li>💬 Interact with intelligent Q&A modules</li>
                    <li>🎯 Practice subjective questions with AI evaluation</li>
                </ul>
            </p>
            <hr/>
            <b>👨‍💻 Author:</b> <a href="https://www.linkedin.com/in/prince-kumar-80795a349" target="_blank">Prince Kumar</a><br/>
            <b>📧 Email:</b> <a href="mailto:princekumar93782@gmail.com">princekumar93782@gmail.com</a><br/>
            <b>🔗 GitHub:</b> <a href="https://github.com/PrinceKumar7781" target="_blank">@PrinceKumar7781</a>
        """, unsafe_allow_html=True)


def hero_header():
    st.markdown("""
    <div style="margin-top:20px; margin-bottom:30px;">
        <h1 style="font-size: 3rem;">🧠 MindScope</h1>
        <p style="font-size: 1.2rem; color: #6b7280;">Your AI-Powered Research Insight Generator</p>
    </div>
    """, unsafe_allow_html=True)

def show_sidebar_info():
    pass

def footer():
    st.markdown("""
    <div style="text-align: center; margin-top: 4rem;">
        <small style="color: gray;">MindScope | © 2025 Prince Kumar</small>
    </div>
    """, unsafe_allow_html=True)