
import streamlit as st
from research_intelligence_agent.graph import workflow

st.set_page_config(
    page_title="Research Intelligence Agent",
    page_icon="🔎",
    layout="wide",
)

# ---------- Header ----------
st.title("🔎 Research Intelligence Agent")
st.caption(
    "Research a question using web search and AI-powered synthesis."
)

# ---------- Input ----------
query = st.text_area(
    "What do you want to research?",
    placeholder="e.g. Corrective RAG vs normal RAG in 2026",
    height=120,
)

research_clicked = st.button(
    "🔍 Research",
    type="primary",
    use_container_width=True,
)

# ---------- Run the graph ----------
if research_clicked:
    if not query.strip():
        st.warning("Please enter a research question.")
    else:
        try:
            with st.spinner("Searching the web and analysing sources..."):
                result = workflow.invoke({"query": query.strip()})

            st.session_state["research_result"] = result
            st.session_state["research_query"] = query.strip()

        except Exception as e:
            st.error(f"Research failed: {e}")

# ---------- Display results ----------
if "research_result" in st.session_state:
    result = st.session_state["research_result"]

    st.divider()
    st.subheader("Research Report")
    st.caption(f"Question: {st.session_state['research_query']}")

    response = result.get("response", "")

    if response:
        st.markdown(response)
    else:
        st.warning("No response was returned. Check your chat node.")

    # ---------- Sources ----------
    sources = result.get("retrieved_info", [])

    if sources:
        st.divider()
        st.subheader(f"Sources ({len(sources)})")

        for i, source in enumerate(sources, start=1):
            title = source.get("title", f"Source {i}")
            url = source.get("url", "")
            content = source.get("content", "")

            with st.expander(f"{i}. {title}"):
                if url:
                    st.markdown(f"[Open source]({url})")
                if content:
                    st.write(content)
