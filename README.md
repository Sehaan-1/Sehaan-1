<!-- =========================
Sehaan Rahman — GitHub Profile
========================= -->

<div align="center">

<img alt="Header" src="https://capsule-render.vercel.app/api?type=waving&color=0:0F2027,55:203A43,100:2C5364&height=190&section=header&text=Sehaan%20Rahman&fontSize=52&fontColor=ffffff&fontAlignY=38&desc=Applied%20AI%20%7C%20ML%20Engineering%20%7C%20Data%20Science%20%7C%20Reliability-minded%20Systems&descAlignY=64&descSize=16" />

<p>
  <a href="https://www.linkedin.com/in/sehaan-rahman-967648296/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white&style=for-the-badge" height="28" alt="LinkedIn" />
  </a>
  <a href="mailto:sehaanincollege@gmail.com" target="_blank">
    <img src="https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white&style=for-the-badge" height="28" alt="Email" />
  </a>
  <a href="https://github.com/Sehaan-1" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white&style=for-the-badge" height="28" alt="GitHub" />
  </a>
</p>

<img src="https://visitor-badge.laobi.icu/badge?page_id=Sehaan-1.Sehaan-1" alt="visitors" />

<br/><br/>

<a href="https://github.com/Sehaan-1">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&pause=1200&color=9BE9FF&center=true&vCenter=true&width=860&lines=Building+evaluation-first+AI+systems+that+ship.;RAG+%E2%86%92+retrieval+%2B+rules+%2B+guardrails+%2B+measurable+eval.;Computer+Vision+%E2%86%92+real-time+pipelines+%2B+tracking+%2B+deployment.;Data+Science+%E2%86%92+clean+EDA+%2B+forecasting+%2B+reproducible+dashboards." alt="Typing intro" />
</a>

<br/><br/>

<img height="185" src="https://media.giphy.com/media/qgQUggCGvnkNC/giphy.gif" alt="Coding gif" />

</div>

---

## About
I’m a CS student at **VIT Bhopal** focused on building **applied AI systems** that are *reproducible, testable, and measurable*.

**What I optimize for**
- **Evaluation-first ML** (clear baselines, metrics, ablations, error analysis)
- **Reliability-minded engineering** (idempotency, recovery paths, clean interfaces)
- **Practical deployment** (Docker, CI workflows, sensible defaults, clear runbooks)

**Roles I’m targeting**
- **AI/ML Engineer (Applied AI, RAG, CV, MLOps-minded)**
- **Data Scientist / Analyst (EDA, forecasting, experimentation, dashboards)**

---

## Featured Projects (with real engineering depth)

<div align="center">

<a href="https://github.com/Sehaan-1/Tender-Royal-Pulse">
  <img src="https://github-readme-stats.vercel.app/api/pin/?username=Sehaan-1&repo=Tender-Royal-Pulse&theme=dracula&hide_border=false" />
</a>
<a href="https://github.com/Sehaan-1/crossborder-legal-rag">
  <img src="https://github-readme-stats.vercel.app/api/pin/?username=Sehaan-1&repo=crossborder-legal-rag&theme=dracula&hide_border=false" />
</a>

<a href="https://github.com/Sehaan-1/sar---suspicious-activity-recognition">
  <img src="https://github-readme-stats.vercel.app/api/pin/?username=Sehaan-1&repo=sar---suspicious-activity-recognition&theme=dracula&hide_border=false" />
</a>
<a href="https://github.com/Sehaan-1/xai-fraud-detection">
  <img src="https://github-readme-stats.vercel.app/api/pin/?username=Sehaan-1&repo=xai-fraud-detection&theme=dracula&hide_border=false" />
</a>

</div>

---

### 1) Tender Royal Pulse — resilient public procurement crawler (Playwright + typed pipeline)
Repo: **Tender-Royal-Pulse**

**Problem**
- Extract **50,000+** public tenders from India’s **eProcure/CPPP** portal, which is hostile to scraping (session-bound URLs, dynamic pages, rate limiting).

**Technical highlights**
- **Headless scraping** with Playwright (session persistence + re-auth on expiry)
- **Reliability engine**: heartbeat + stale task recovery, graceful shutdown, and a **retry taxonomy**
- **Idempotent upserts** with durable keys to prevent duplicates across runs
- Strong SWE discipline: **Pydantic models**, strict typing, lint gates, tests, and a structured repo layout

**Outputs**
- Export to **CSV** (analyst-friendly) and **JSONL** (pipeline-friendly)

---

### 2) Cross-Border Legal RAG — hybrid retrieval + rule layer + measurable evaluation
Repo: **crossborder-legal-rag** (includes **System Card** + **Privacy Policy**)

**What it does**
- Answers cross-border legal scenario questions using EU regulations as the knowledge base:
  - deterministic **rule layer**
  - **hybrid retrieval** (BM25 + dense embeddings)
  - **reranking**
  - **refusal guard** when retrieval quality is insufficient
  - cited “memo-style” answers with traceable sources

**System design details**
- Hybrid retrieval blends **BM25 top-k** with **FAISS vector search**
- Adds deduplication + (optional) **cross-encoder reranking**
- Provides a reproducible **evaluation harness** and a published report

**Reported evaluation (v1.0.0)**
- Article Recall (overall): **~78%**
- Refusal Accuracy: **~85%**
- p95 latency (Space, warm): **~9s**

---

### 3) SAR — Suspicious Activity Recognition System (real-time CV, multi-service, Docker Compose)
Repo: **sar---suspicious-activity-recognition**

**What it is**
- A real-time security surveillance platform with:
  - React dashboard (live feeds, events, analytics)
  - Node/Express backend (API + Socket.IO)
  - Python AI worker (OpenCV + YOLOv8 + ByteTrack)

**Engineering challenges solved**
- Multi-camera concurrency (dynamic thread orchestration)
- Web streaming input support via **yt-dlp**
- Real-time alerts pushed via **WebSockets**
- Data retention + cleanup to prevent silent disk exhaustion
- One-command deployment with **Docker Compose**

---

### 4) Real-Time XAI Fraud Detection — FastAPI model serving + SHAP explainability + MLOps framing
Repo: **xai-fraud-detection**

**Problem**
- Fraud detection is heavily imbalanced; accuracy can be misleading.
- The model must be **explainable** (regulatory + analyst usability).

**Technical highlights**
- **XGBoost + SMOTE** for class imbalance
- **SHAP TreeExplainer** for per-prediction feature attributions
- **FastAPI** serving layer with Pydantic validation
- **/metrics** endpoint (Prometheus-style monitoring)
- CI/CD pipeline and containerized deployment workflow (Docker + cloud-oriented structure)

---

<details>
  <summary><b>Additional DS project: COVID-19 Global Vaccination Analysis & SARIMA Forecasting</b></summary>

Repo: **covid-vaccination-analysis**

- Streamlit dashboard for EDA + rankings + comparisons
- SARIMA forecasting: `SARIMA(2,1,2)×(1,1,1,7)` with confidence intervals
- Test coverage for data quality (date parsing, non-negative values, rolling averages, forecast clipping)
</details>

---

## Stack (grouped by how I use it)
<div align="left">

**Core**
<br/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="34" alt="Python" title="Python" />
<img width="10"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" height="34" alt="TypeScript" title="TypeScript" />
<img width="10"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" height="34" alt="JavaScript" title="JavaScript" />
<img width="10"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg" height="34" alt="Java" title="Java" />
<img width="10"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/r/r-original.svg" height="34" alt="R" title="R" />

<br/><br/>

**AI / CV / Data**
<br/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/opencv/opencv-original.svg" height="34" alt="OpenCV" title="OpenCV" />
<img width="10"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" height="34" alt="SQLite" title="SQLite" />

<br/><br/>

**Web**
<br/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg" height="34" alt="React" title="React" />
<img width="10"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg" height="34" alt="Node.js" title="Node.js" />
<img width="10"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" height="34" alt="HTML5" title="HTML5" />
<img width="10"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" height="34" alt="CSS3" title="CSS3" />

<br/><br/>

**DevOps / Cloud**
<br/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" height="34" alt="Docker" title="Docker" />
<img width="10"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" height="34" alt="Git" title="Git" />
<img width="10"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" height="34" alt="AWS" title="AWS" />
<img width="10"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/googlecloud/googlecloud-original.svg" height="34" alt="GCP" title="GCP" />

</div>

---

## GitHub Stats
<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=Sehaan-1&show_icons=true&include_all_commits=true&count_private=true&theme=dracula&hide_border=false" height="165" alt="stats"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs?username=Sehaan-1&layout=compact&langs_count=7&theme=dracula&hide_border=false" height="165" alt="top langs"/>
  <br/>
  <img src="https://streak-stats.demolab.com?user=Sehaan-1&theme=dark&hide_border=false&border_radius=8" height="190" alt="streak"/>
</div>

---

<div align="center">
  <img alt="Footer" src="https://capsule-render.vercel.app/api?type=waving&color=0:0F2027,55:203A43,100:2C5364&height=120&section=footer" />
</div>
