<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.png">
    <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.png">
    <img src="assets/banner-dark.png" width="100%" alt="Sehaan Ur Rahman — Applied AI, machine learning systems, data engineering">
  </picture>
</div>

<p align="center">
  <a href="https://www.linkedin.com/in/sehaan-rahman-967648296/">LinkedIn</a>
  &nbsp;·&nbsp;
  <a href="mailto:sehaanincollege@gmail.com">Email</a>
  &nbsp;·&nbsp;
  <a href="https://github.com/Sehaan-1?tab=repositories">Repositories</a>
</p>

<br>

## What I do

I build AI and data systems, and I spend most of my time on the part that starts after the demo works: whether the retrieval actually retrieves, whether the pipeline survives a malformed record at 3 a.m., whether the policy still holds under a retry storm. The work is mostly Python — services with typed contracts, evaluation harnesses, deterministic pipelines — with enough Go, Rust, C++, C# and TypeScript to understand where the real constraints live.

Computer science undergraduate at **VIT Bhopal**, building in the open.

<br>

## How I work

**Measure before claiming.**  
Baselines, metrics and ablations ship with the model, not after it. Retrieval recall and refusal accuracy, inter-annotator agreement coefficients, p50/p95 latency — a number with a denominator, or it doesn't go in the README.

**Design for the failure case.**  
Idempotent writes, quarantine paths for bad rows, bounded queues, graceful shutdown, chaos and crash-recovery tests, and an explicit taxonomy of what can go wrong instead of a silent retry.

**Keep the seams honest.**  
Typed contracts at every boundary, read paths that cannot take down write paths, one-command deploys, and migrations that run themselves on first boot.

**Leave the reasoning visible.**  
Architecture decision records, datasheets, annotation guidelines and dashboards that state their own sample sizes and caveats.

<br>

## Stack

**Languages**  
Python · TypeScript · SQL · Go · Rust · C++20 · C# · Java · Kotlin · R · JavaScript · Dart

**Machine learning**  
PyTorch · scikit-learn · XGBoost · SHAP · Hugging Face Transformers · FAISS · BM25 hybrid retrieval · YOLOv8 · ByteTrack · CLIP · OpenCV · Thompson sampling and drift detection (ADWIN) · off-policy evaluation

**Data & evaluation**  
pandas · NumPy · DuckDB · dbt · Airflow · medallion architecture · inter-annotator agreement (Cohen, Fleiss, Krippendorff) · annotation QA workflows · data-quality scorecards · datasheets and ADRs · pytest, property-based testing, CI gates

**Web & product**  
FastAPI · Pydantic v2 · SQLAlchemy 2.0 · Node.js · Express · Spring Boot · React 19 · Next.js · Vite · Tailwind CSS · Three.js · Leaflet · D3 · TanStack Query · WebSockets · Jetpack Compose · Flutter · PostgreSQL · SQLite (WAL) · Redis · MySQL · Drizzle ORM · Flyway

**Infrastructure & observability**  
Docker and Compose · GitHub Actions · Prometheus · Grafana · nginx · Caddy · Cloudflare · Vercel · AWS (S3, Lambda) · GCP · healthchecks and staged rollouts

**Systems programming**  
Lock-free ring buffers and atomics · memory arenas · FastCDC chunking · TLS 1.3 framing · Lua scripting inside Redis · BLE/GATT and ESP32 firmware · dependency-free parsing, encoding and rendering in Rust

<br>

## Domains

**Applied AI** — retrieval-augmented systems with hybrid search and refusal guards; explainability served per prediction; classification over messy real-world text.

**Evaluation & data quality** — agreement statistics implemented from scratch, annotation protocols, pilot reports, and pipelines that refuse to report a metric without its sample size.

**Data engineering** — ingestion with quarantine, deterministic transforms, warehouse modelling, cohort and LTV analysis.

**Systems & reliability** — incident response automation, rate limiting at the edge, crash-safe synchronisation, and low-latency C++ where the microseconds are the point.

<br>

## Selected work

The pinned repositories below are the best entry points. Every number quoted in a project's README is reproducible from the repo itself — measured, not estimated.

<br>

<p align="center">
  <sub>Open to conversations about applied AI, data systems and reliability work — <a href="mailto:sehaanincollege@gmail.com">email is the fastest route</a>.</sub>
</p>
