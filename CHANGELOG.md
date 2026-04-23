# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-04-23

### Added
- **`[glowup-orchestration]`**: Infrastructura de bază prin crearea repository-urilor publice ale organizației (Anca).
- **`[glowup-orchestration]`**: Fișierul `docker-compose.yml` cu definirea rețelelor izolate Docker (`frontend-nw`, `backend-nw`) (Anda).
- **`[glowup-orchestration]`**: Mediul pentru baze de date integrat, adăugând **PostgreSQL** și utilitarul **pgAdmin** în fișierul de orchestrare (Anda).
- **`[glowup-orchestration]`**: Utilitarul **Portainer** pentru asigurarea gestiunii din UI a containerelor și a clusterului (Anca).
- **`[glowup-orchestration]`**: Sistemul de monitorizare și observabilitate integrat, folosind **Prometheus** și **Grafana** cu dashboard dedicat (Anda).
- **`[glowup-auth]`**: Structura de bază pentru **Microserviciul de Autentificare (Auth MS)** folosind Node.js (Anca).
- **`[glowup-auth]`**: Rutele de test `/health` și `/register` pentru a demonstra comunicarea HTTP (Anca).
- **`[glowup-auth]`**: Containerizarea inițială a aplicației prin scrierea fișierului `Dockerfile` (Anca).
- **`[glowup-logic]`**: Fundația pentru **Microserviciul de Logică (Business Logic MS)** folosind Python și FastAPI, incluzând ruta de test `/check-routine` și fișierul `Dockerfile` (Anda).
- **`[glowup-io]`**: Structura de bază pentru **Microserviciul de Date (IO MS)** în Node.js, scriptul de conexiune la baza de date principală și fișierul `Dockerfile` (Anda).