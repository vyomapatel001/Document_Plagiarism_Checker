import streamlit as st
from main import load_document, detect_exact_matches, semantic_similarity
from diff import highlight_differences

st.set_page_config(page_title="AI Plagiarism Checker", layout="wide")

st.title("🧠 AI Plagiarism Checker")
st.write("This app checks for plagiarism in two text documents using exact and semantic matching.")

# Upload files or load defaults
uploaded_file1 = st.file_uploader("Upload Document 1 (.txt)", type=["txt"])
uploaded_file2 = st.file_uploader("Upload Document 2 (.txt)", type=["txt"])

if uploaded_file1 is not None and uploaded_file2 is not None:
    doc1 = uploaded_file1.read().decode("utf-8")
    doc2 = uploaded_file2.read().decode("utf-8")
else:
    # Load default documents if available
    try:
        doc1 = load_document("doc1.txt")
        doc2 = load_document("doc2.txt")
    except:
        doc1 = ""
        doc2 = ""

doc1 = st.text_area("Document 1", height=200, value=doc1)
doc2 = st.text_area("Document 2", height=200, value=doc2)

if st.button("Check Plagiarism"):
    with st.spinner("Analyzing..."):
        # Run core logic
        exact_matches = detect_exact_matches(doc1, doc2)
        semantic_matches = semantic_similarity(doc1, doc2)
        diff_html = highlight_differences(doc1, doc2)

    st.markdown("### ✅ Exact Matches")
    if exact_matches:
        st.write(exact_matches)
    else:
        st.write("No exact matches found.")

    st.markdown("### 🔷 Semantic Matches")
    if semantic_matches:
        st.write(semantic_matches)
    else:
        st.write("No semantic matches found.")

    st.markdown("### 🎨 Highlighted Differences")
    st.markdown(diff_html, unsafe_allow_html=True)
