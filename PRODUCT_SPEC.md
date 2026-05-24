# 📝 Product Specification: Smart Class AI Attendance

## 1. Executive Summary
**Smart Class** is an advanced biometric attendance platform designed to eliminate the friction of manual roll calls. It utilizes state-of-the-art Computer Vision and Audio Signal Processing to verify identities through facial recognition and speaker verification, providing a secure and automated experience for both educators and students.

## 2. Product Overview
The system is divided into two primary portals:
- **Teacher Portal**: Administrative control center for managing subjects, reviewing AI-generated attendance logs, and initiating roll calls via photo/voice uploads.
- **Student Portal**: Self-service enrollment interface where students register their biometric profiles (Face ID & Voice ID) and join classes via unique subject codes.

## 3. Core Features & User Flows

### 3.1 Teacher Ecosystem
- **Account Management**: Secure registration and login using hashed credentials (bcrypt).
- **Subject Creation**: Dynamic generation of subjects with unique join codes and QR code sharing.
- **AI-Assisted Attendance**:
    - **Photo-Based**: Upload classroom images; system extracts embeddings and matches against the student database.
    - **Voice-Based**: Record/upload classroom audio; system performs speaker diarization and verification.
- **Attendance Analytics**: View and export historical logs for each subject.

### 3.2 Student Ecosystem
- **Biometric Enrollment**: Seamless capture of face and voice samples.
- **Class Enrollment**: Automated joining of subjects via deep links or manual code entry.
- **Personal Dashboard**: View individual attendance records and enrollment status.

## 4. Technical Architecture
- **UI Framework**: Streamlit (Python)
- **Backend Infrastructure**: Supabase (PostgreSQL with RLS)
- **Computer Vision Pipeline**: `face_recognition` (utilizing `dlib` HOG/CNN models)
- **Audio Intelligence**: `Resemblyzer` (utilizing SincNet for d-vector extraction)
- **Security**: Environment-based secrets management and salted bcrypt hashing.

## 5. Design System
The application adheres to an **Industrial Precision** design language, drawing inspiration from Bugatti aesthetics:
- **Color Palette**: Near-pure blacks, deep greys, and vibrant status accents.
- **Typography**: Inter / Roboto for modern readability.
- **Layout**: "Glassmorphism" containers with glowing shadow borders.

## 6. Known Limitations
- **Environmental Dependencies**: Accuracy is significantly impacted by ambient lighting (for Face ID) and background noise (for Voice ID).
- **Network Dependency**: Real-time operations require a stable connection to the Supabase backend.

---
*Document Version: 1.0.0*  
*Last Updated: 2026-05-15*
