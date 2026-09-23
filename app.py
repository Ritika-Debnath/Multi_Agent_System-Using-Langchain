import time
import streamlit as st
from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ResearchMind · AI Research Agent",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@300;400;500&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    color: #e8e4dc;
}

.stApp {
    background: #0a0a0f;
    background-image:
        radial-gradient(ellipse 80% 50% at 20% -10%, rgba(255,140,50,0.12) 0%, transparent 60%),
        radial-gradient(ellipse 60% 40% at 80% 110%, rgba(255,80,30,0.08) 0%, transparent 55%);
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 3rem 4rem; max-width: 1200px; }

/* ── Hero ── */
.hero { text-align: center; padding: 3.5rem 0 2rem; }
.hero-eyebrow {
    font-family: 'DM Mono', monospace;
    font-size: 0.7rem;
    font-weight: 500;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: #ff8c32;
    margin-bottom: 1rem;
    opacity: 0.9;
}
.hero h1 {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.8rem, 6vw, 5rem);
    font-weight: 800;
    line-height: 1.0;
    letter-spacing: -0.03em;
    color: #f0ebe0;
    margin: 0 0 1rem;
}
.hero h1 span { color: #ff8c32; }
.hero-sub {
    font-size: 1.05rem;
    font-weight: 300;
    color: #a09890;
    max-width: 520px;
    margin: 0 auto;
    line-height: 1.65;
}

.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255,140,50,0.3), transparent);
    margin: 2rem 0;
}

/* ── Input card ── */
.input-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,140,50,0.15);
    border-radius: 16px;
    padding: 2rem 2.5rem;
    margin-bottom: 1.2rem;
    backdrop-filter: blur(8px);
}

.stTextInput > div > div > input {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,140,50,0.25) !important;
    border-radius: 10px !important;
    color: #f0ebe0 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 1rem !important;
    padding: 0.75rem 1rem !important;
    transition: border-color 0.2s, box-shadow 0.2s !important;
}
.stTextInput > div > div > input:focus {
    border-color: #ff8c32 !important;
    box-shadow: 0 0 0 3px rgba(255,140,50,0.12) !important;
}
.stTextInput > label {
    font-family: 'DM Mono', monospace !important;
    font-size: 0.72rem !important;
    letter-spacing: 0.15em !important;
    text-transform: uppercase !important;
    color: #ff8c32 !important;
    font-weight: 500 !important;
}

/* ── Buttons ── */
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #ff8c32 0%, #ff5a1a 100%) !important;
    color: #0a0a0f !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    letter-spacing: 0.04em !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.7rem 2.2rem !important;
    transition: transform 0.15s, box-shadow 0.15s, opacity 0.15s !important;
    box-shadow: 0 4px 20px rgba(255,140,50,0.3) !important;
}
.stButton > button[kind="primary"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 28px rgba(255,140,50,0.4) !important;
    opacity: 0.95 !important;
}
.stButton > button[kind="secondary"] {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(255,140,50,0.25) !important;
    color: #cdc8bf !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.75rem !important;
    border-radius: 8px !important;
    padding: 0.45rem 0.8rem !important;
    transition: border-color 0.15s, color 0.15s !important;
}
.stButton > button[kind="secondary"]:hover {
    border-color: #ff8c32 !important;
    color: #ff8c32 !important;
}

/* ── Progress bar ── */
.stProgress > div > div > div > div {
    background-image: linear-gradient(90deg, #ff8c32, #ff5a1a) !important;
}

/* ── Step cards (with entrance + pulse animation) ── */
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(6px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes pulseGlow {
    0%, 100% { box-shadow: 0 0 0 0 rgba(255,140,50,0.35); }
    50%      { box-shadow: 0 0 0 7px rgba(255,140,50,0); }
}
.step-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 14px;
    padding: 1.3rem 1.6rem;
    margin-bottom: 1rem;
    position: relative;
    overflow: hidden;
    animation: fadeInUp 0.35s ease;
    transition: border-color 0.3s, background 0.3s;
}
.step-card.active { border-color: rgba(255,140,50,0.45); background: rgba(255,140,50,0.05); animation: fadeInUp 0.35s ease, pulseGlow 1.6s ease-in-out infinite; }
.step-card.done    { border-color: rgba(80,200,120,0.3); background: rgba(80,200,120,0.03); }
.step-card::before {
    content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 3px;
    border-radius: 14px 0 0 14px; background: rgba(255,255,255,0.05); transition: background 0.3s;
}
.step-card.active::before { background: #ff8c32; }
.step-card.done::before   { background: #50c878; }

.step-header { display: flex; align-items: center; gap: 0.8rem; }
.step-num { font-family: 'DM Mono', monospace; font-size: 0.68rem; font-weight: 500; letter-spacing: 0.15em; color: #ff8c32; opacity: 0.7; }
.step-title { font-family: 'Syne', sans-serif; font-size: 0.95rem; font-weight: 700; color: #f0ebe0; }
.step-status { margin-left: auto; font-family: 'DM Mono', monospace; font-size: 0.68rem; letter-spacing: 0.1em; }
.status-waiting { color: #555; }
.status-running { color: #ff8c32; }
.status-done    { color: #50c878; }
.step-desc { font-size: 0.82rem; color: #706860; margin-top: 0.35rem; }

/* ── Metric tiles ── */
.metric-row { display: flex; gap: 1rem; margin: 1.5rem 0; }
.metric-box {
    flex: 1; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08);
    border-radius: 12px; padding: 1rem 0.8rem; text-align: center;
}
.metric-value { font-family: 'Syne', sans-serif; font-size: 1.5rem; font-weight: 800; color: #ff8c32; }
.metric-label { font-family: 'DM Mono', monospace; font-size: 0.62rem; letter-spacing: 0.1em; text-transform: uppercase; color: #a09890; margin-top: 0.2rem; }

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] { gap: 0.4rem; border-bottom: 1px solid rgba(255,140,50,0.15); }
.stTabs [data-baseweb="tab"] {
    background: rgba(255,255,255,0.03); border-radius: 8px 8px 0 0; padding: 0.55rem 1.1rem;
    font-family: 'DM Mono', monospace; font-size: 0.76rem; letter-spacing: 0.05em; color: #a09890;
}
.stTabs [aria-selected="true"] { background: rgba(255,140,50,0.1) !important; color: #ff8c32 !important; }

/* ── Result content ── */
.result-content { font-size: 0.9rem; line-height: 1.75; color: #cdc8bf; white-space: pre-wrap; font-family: 'DM Sans', sans-serif; }

/* ── Section heading ── */
.section-heading { font-family: 'Syne', sans-serif; font-size: 1.3rem; font-weight: 700; color: #f0ebe0; margin: 0.5rem 0 1rem; }
.chip-label { font-family: 'DM Mono', monospace; font-size: 0.68rem; color: #605850; letter-spacing: 0.12em; margin: 0.2rem 0 0.6rem; }

.notice { font-family: 'DM Mono', monospace; font-size: 0.72rem; color: #605850; text-align: center; margin-top: 3rem; letter-spacing: 0.08em; }
</style>
""", unsafe_allow_html=True)


# ── Helper: build the HTML for one step card ─────────────────────────────────
def step_card_html(num: str, title: str, desc: str, state: str) -> str:
    label, status_cls = {
        "waiting": ("WAITING", "status-waiting"),
        "running": ("● RUNNING", "status-running"),
        "done":    ("✓ DONE", "status-done"),
    }[state]
    card_cls = {"running": "active", "done": "done"}.get(state, "")
    return f"""
    <div class="step-card {card_cls}">
        <div class="step-header">
            <span class="step-num">{num}</span>
            <span class="step-title">{title}</span>
            <span class="step-status {status_cls}">{label}</span>
        </div>
        <div class="step-desc">{desc}</div>
    </div>
    """


# ── Session state init ────────────────────────────────────────────────────────
if "results" not in st.session_state:
    st.session_state.results = {}
if "done" not in st.session_state:
    st.session_state.done = False
if "elapsed" not in st.session_state:
    st.session_state.elapsed = 0.0


# ── Callback for example-topic chips (runs BEFORE the widget is recreated,
#    so it's safe to change the text input's value this way) ─────────────────
def _use_example(value: str):
    st.session_state.topic_input = value


# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-eyebrow">Multi-Agent AI System</div>
    <h1>Research<span>Mind</span></h1>
    <p class="hero-sub">
        Four specialized AI agents collaborate — searching, scraping, writing,
        and critiquing — to deliver a polished research report on any topic.
    </p>
</div>
<div class="divider"></div>
""", unsafe_allow_html=True)


# ── Layout: input left, live pipeline right ──────────────────────────────────
col_input, col_gap, col_pipeline = st.columns([5, 0.5, 4])

with col_input:
    st.markdown('<div class="input-card">', unsafe_allow_html=True)
    topic = st.text_input(
        "Research Topic",
        placeholder="e.g. Quantum computing breakthroughs in 2025",
        key="topic_input",
    )
    run_btn = st.button("⚡  Run Research Pipeline", use_container_width=True, type="primary")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="chip-label">TRY AN EXAMPLE →</div>', unsafe_allow_html=True)
    examples = ["LLM agents 2025", "CRISPR gene editing", "Fusion energy progress"]
    chip_cols = st.columns(len(examples))
    for c, ex in zip(chip_cols, examples):
        with c:
            st.button(ex, key=f"ex_{ex}", use_container_width=True,
                      type="secondary", on_click=_use_example, args=(ex,))

with col_pipeline:
    st.markdown('<div class="section-heading">Pipeline</div>', unsafe_allow_html=True)

    progress_ph = st.empty()
    step_meta = {
        "search": ("01", "Search Agent", "Gathers recent web information"),
        "reader": ("02", "Reader Agent", "Scrapes & extracts deep content"),
        "writer": ("03", "Writer Chain", "Drafts the full research report"),
        "critic": ("04", "Critic Chain", "Reviews & scores the report"),
    }
    step_placeholders = {key: st.empty() for key in step_meta}

    def render_pipeline(state_dict: dict, active_step: str | None = None):
        """Redraws all 4 step cards + the progress bar to match state_dict."""
        completed = 0
        for key, ph in step_placeholders.items():
            num, title, desc = step_meta[key]
            if key in state_dict:
                status, completed = "done", completed + 1
            elif key == active_step:
                status = "running"
            else:
                status = "waiting"
            ph.markdown(step_card_html(num, title, desc, status), unsafe_allow_html=True)
        progress_ph.progress(completed / len(step_meta))

    # Initial draw: all done if we already have a finished run, else all waiting.
    render_pipeline(st.session_state.results if st.session_state.done else {})


# ── Run the pipeline (updates the cards above live, step by step) ────────────
if run_btn:
    if not topic.strip():
        st.warning("Please enter a research topic first.")
    else:
        st.session_state.results = {}
        st.session_state.done = False
        results = {}
        start_time = time.time()

        # Step 1 — Search
        render_pipeline(results, active_step="search")
        search_agent = build_search_agent()
        sr = search_agent.invoke({
            "messages": [("user", f"Find recent, reliable and detailed information about: {topic}")]
        })
        results["search"] = sr["messages"][-1].content
        render_pipeline(results)

        # Step 2 — Reader
        render_pipeline(results, active_step="reader")
        reader_agent = build_reader_agent()
        rr = reader_agent.invoke({
            "messages": [("user",
                f"Based on the following search results about '{topic}', "
                f"pick the most relevant URL and scrape it for deeper content.\n\n"
                f"Search Results:\n{results['search'][:800]}"
            )]
        })
        results["reader"] = rr["messages"][-1].content
        render_pipeline(results)

        # Step 3 — Writer
        render_pipeline(results, active_step="writer")
        research_combined = (
            f"SEARCH RESULTS:\n{results['search']}\n\n"
            f"DETAILED SCRAPED CONTENT:\n{results['reader']}"
        )
        results["writer"] = writer_chain.invoke({"topic": topic, "research": research_combined})
        render_pipeline(results)

        # Step 4 — Critic
        render_pipeline(results, active_step="critic")
        results["critic"] = critic_chain.invoke({"report": results["writer"]})
        render_pipeline(results)

        st.session_state.results = results
        st.session_state.done = True
        st.session_state.elapsed = time.time() - start_time


# ── Results ────────────────────────────────────────────────────────────────
r = st.session_state.results
if st.session_state.done and r:
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading">Results</div>', unsafe_allow_html=True)

    word_count = len(r.get("writer", "").split())
    read_time = max(1, word_count // 200)

    metrics = [
        (f"{word_count:,}", "Words"),
        (f"{read_time} min", "Read Time"),
        (f"{st.session_state.elapsed:.1f}s", "Time Taken"),
        ("✓ Complete", "Status"),
    ]
    m_cols = st.columns(4)
    for col, (val, label) in zip(m_cols, metrics):
        col.markdown(
            f'<div class="metric-box"><div class="metric-value">{val}</div>'
            f'<div class="metric-label">{label}</div></div>',
            unsafe_allow_html=True,
        )

    tab_report, tab_feedback, tab_sources = st.tabs(["📝 Report", "🧐 Critic Feedback", "🔍 Sources"])

    with tab_report:
        st.markdown(r.get("writer", ""))
        st.download_button(
            label="⬇  Download Report (.md)",
            data=r.get("writer", ""),
            file_name=f"research_report_{int(time.time())}.md",
            mime="text/markdown",
        )

    with tab_feedback:
        st.markdown(r.get("critic", ""))

    with tab_sources:
        st.markdown("**Search Agent Output**")
        st.markdown(f'<div class="result-content">{r.get("search", "")}</div>', unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("**Reader Agent Output**")
        st.markdown(f'<div class="result-content">{r.get("reader", "")}</div>', unsafe_allow_html=True)

    st.write("")
    if st.button("🔄  Start New Research", type="secondary"):
        st.session_state.results = {}
        st.session_state.done = False
        st.rerun()


# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="notice">
    ResearchMind · Powered by LangChain multi-agent pipeline · Built with Streamlit
</div>
""", unsafe_allow_html=True)