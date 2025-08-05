# Document_Plagiarism_Checker
# 📘 AI Plagiarism Checker

An AI-powered plagiarism detection tool that compares two documents using:

- ✅ **Exact Match Detection** via n-gram hashing (sliding window technique)
- 🤖 **Semantic Similarity** using Sentence Transformers (BERT-based)
- 🎨 **Color-coded Difference Highlighting** with HTML rendering
- 🌐 **Interactive Web Interface** powered by Streamlit

---

## 🔍 What This Project Does

This tool analyses two text documents and detects:
- **Exact duplicate phrases** using hashed n-grams.
- **Paraphrased or semantically similar content** using AI models.
- **Visual word-by-word differences**, color-coded for clarity.
- Presents results in a **simple, browser-based UI**.

It's designed to go beyond basic string comparison and catch reworded plagiarism.

---

## 🧾 Project Structure

| File | Description |
|------|-------------|
| `main.py` | Core backend logic: loading, exact matching, semantic similarity |
| `diff.py` | Generates HTML to highlight text differences with color |
| `streamlit_app.py` | Frontend UI built with Streamlit for interactive use |

---

## 📦 Installation

Make sure you have Python 3.7+ installed.

Then, install required dependencies:

```bash
pip install streamlit sentence-transformers numpy torch
```

## ▶️ How to Use

### 🔧 Step 1: Add Your Documents

Create two plain text files in the project folder:

- `doc1.txt`
- `doc2.txt`

Fill them with the text content you want to compare.

---

### 💻 Step 2: Run the Web App

```bash
streamlit run streamlit_app.py
```
