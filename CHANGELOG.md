# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-05-17

### Added
- **[glowup-orchestration]** - Adăugare pipeline de automatizare GitHub Actions (`.github/workflows/ci.yml`) pentru validarea sintaxei de infrastructură (Anca).
- **[glowup-frontend]** - Crearea unei interfețe grafice interactive de tip MVP folosind Streamlit, structurată pe 5 tab-uri corespunzătoare specificațiilor din temă (Anca & Anda).
- **[glowup-frontend]** - Eliminarea totală a problemelor de politică CORS prin asigurarea comunicației directe server-to-server (Anca & Anda).
- **[glowup-logic]** - Implementarea algoritmului de generare rutină inteligentă `GET /logic/generate-routine/:username` cu sortare clinică bazată pe consistență și pH (Anda).
- **[glowup-io]** - Extinderea schemei PostgreSQL cu 3 tabele relaționale complexe: `user_profiles`, `products` și `user_shelf` (Anda).
- **[glowup-io]** - Implementarea endpoint-ului `POST /io/shelf` cu clauză de auto-creare profil (`upsert`) pentru eliminarea conflictelor de cheie străină (Anda).
- **[glowup-io]** - Implementarea endpoint-ului `GET /io/shelf/:username` pentru calcularea dinamică a termenelor de valabilitate (PAO) direct din baza de date (Anda).
- **[glowup-auth]** - Actualizarea rutei `POST /auth/register` pentru a colecta dinamic proprietățile tenului și a le injecta criptat în token-ul JWT (Anca).

### Changed
- **[glowup-orchestration]** - Adaptarea fișierului `docker-compose.yml` pentru conformitate strictă cu standardul Docker Swarm prin eliminarea proprietăților incompatibile în cluster (Anca).
- **[glowup-orchestration]** - Redirecționarea portului extern PostgreSQL la `5433:5432` pentru eliminarea conflictelor de porturi cu mediile locale (Anca).

---

## [0.2.0] - 2026-05-10

### Added
- **[glowup-orchestration]** - Trecerea la arhitectura de producție Docker Swarm prin orchestrarea microserviciilor custom, configurarea replicilor multiple și setarea limitelor hardware (Anca).
- **[glowup-logic]** - Implementare algoritm de business pentru detectarea incompatibilităților severe de skincare în sesiuni simultane (ex: Retinol + AHA/BHA) (Anda).
- **[glowup-logic]** - Implementarea comunicării HTTP interne asincrone pentru interogarea directă a serviciului de date (Anda).
- **[glowup-logic]** - Optimizarea procesului de containerizare prin curățarea dependențelor specifice sistemului gazdă din `requirements.txt` (Anda).
- **[glowup-auth]** - Implementare generare de token-uri reale securizate (JWT) pentru gestionarea sesiunilor utilizatorilor (Anca).
- **[glowup-io]** - Implementare schemă bază de date și script de creare automată a tabelului `inventory` la inițializarea containerului (Anda).

---

## [0.1.0] - 2026-04-23

### Added
- **[glowup-orchestration]** - Infrastructura de bază a proiectului prin crearea repository-urilor publice ale organizației (Anca).
- **[glowup-orchestration]** - Fișierul `docker-compose.yml` cu definirea rețelelor izolate Docker `frontend-nw` și `backend-nw` (Anda).
- **[glowup-orchestration]** - Integrarea mediului pentru baze de date prin adăugarea serviciilor PostgreSQL și pgAdmin (Anda).
- **[glowup-orchestration]** - Configurarea utilitarului Portainer pentru asigurarea managementului vizual al containerelor (Anca).
- **[glowup-orchestration]** - Sistemul de monitorizare și observabilitate integrat, folosind Prometheus și Grafana cu dashboard dedicat (Anda).
- **[glowup-auth]** - Structura de bază pentru Microserviciul de Autentificare (Auth MS) dezvoltat în Node.js (Anca).
- **[glowup-auth]** - Rutele inițiale de test `/health` și `/register` pentru verificarea comunicării HTTP (Anca).
- **[glowup-auth]** - Containerizarea inițială a aplicației prin scrierea fișierului `Dockerfile` (Anca).
- **[glowup-logic]** - Fundația pentru Microserviciul de Logică folosind Python și FastAPI, incluzând ruta `/check-routine` și fișierul `Dockerfile` (Anda).
- **[glowup-io]** - Structura de bază pentru Microserviciul de Date (IO MS) în Node.js, scriptul de conexiune la bază și fișierul `Dockerfile` (Anda).