# main.py

import os
import hashlib
from sentence_transformers import SentenceTransformer, util
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)


# -----------------------------
# 🔹 Load Document
# -----------------------------
def load_document(path):
    if not os.path.exists(path):
        print(f"❌ File not found: {path}")
        return ""
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()


# -----------------------------
# 🔹 Exact Match Detection (n-gram + hashing)
# -----------------------------
def get_ngrams(text, n=5):
    words = text.split()
    ngrams = []
    for i in range(len(words) - n + 1):
        chunk = " ".join(words[i:i + n])
        hash_val = hashlib.md5(chunk.encode()).hexdigest()
        ngrams.append((chunk, hash_val))
    return ngrams

def detect_exact_matches(text1, text2, n=5):
    ngrams1 = get_ngrams(text1, n)
    ngrams2 = get_ngrams(text2, n)

    hash_set2 = {h for _, h in ngrams2}
    matches = [(chunk, h) for chunk, h in ngrams1 if h in hash_set2]
    return matches


# -----------------------------
# 🔹 AI Semantic Similarity
# -----------------------------
def semantic_similarity(doc1, doc2, model_name='all-MiniLM-L6-v2', threshold=0.8):
    model = SentenceTransformer(model_name)

    sentences1 = [s.strip() for s in doc1.split('.') if s.strip()]
    sentences2 = [s.strip() for s in doc2.split('.') if s.strip()]

    if not sentences1 or not sentences2:
        return []

    embeddings1 = model.encode(sentences1, convert_to_tensor=True)
    embeddings2 = model.encode(sentences2, convert_to_tensor=True)

    cosine_scores = util.cos_sim(embeddings1, embeddings2)

    similar_pairs = []
    for i in range(len(sentences1)):
        for j in range(len(sentences2)):
            score = cosine_scores[i][j].item()
            if score >= threshold:
                similar_pairs.append({
                    "doc1_sentence": sentences1[i],
                    "doc2_sentence": sentences2[j],
                    "score": round(score, 3)
                })

    return similar_pairs


# -----------------------------
# 🔹 CLI Execution
# -----------------------------
def main():
    print("📘 AI Plagiarism Checker with Exact and Semantic Matching\n")

    doc1_path = 'doc1.txt'
    doc2_path = 'doc2.txt'

    print("📂 Loading documents...")
    text1 = load_document(doc1_path)
    text2 = load_document(doc2_path)

    if not text1 or not text2:
        print("⚠️ One or both documents are empty or missing.")
        return

    # 🔍 Exact Matches
    exact_matches = detect_exact_matches(text1, text2)
    print(f"\n✅ Exact Matches Found: {len(exact_matches)}\n")
    for match, _ in exact_matches[:10]:  # Only first 10 shown
        print(f"• {match}")

    # 🤖 Semantic Matches
    semantic_matches = semantic_similarity(text1, text2)
    print(f"\n🔷 Semantic Matches Found: {len(semantic_matches)}\n")

    for match in semantic_matches:
        print(f"• Similarity: {match['score']:.2f}")
        print(f"  Doc1: {match['doc1_sentence']}")
        print(f"  Doc2: {match['doc2_sentence']}")
        print("-" * 60)

    # 🧮 Plagiarism Estimate
    sents1 = [s.strip() for s in text1.split('.') if s.strip()]
    total_matches = len(exact_matches) + len(semantic_matches)
    est_percent = (total_matches / max(len(sents1), 1)) * 100
    print(f"\n📊 Estimated Overall Plagiarism: {est_percent:.2f}%\n")


if __name__ == "__main__":
    main()
