

import dlib
import numpy as np
import face_recognition_models
from sklearn.svm import SVC
import streamlit as st

from src.database.db import get_all_students


@st.cache_resource
def load_dlib_models():
    detector = dlib.get_frontal_face_detector() 


    sp = dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location()
    )

    facerec = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )

    return detector, sp, facerec

def get_face_embeddings(image_np):
    detector, sp, facerec = load_dlib_models()
    faces = detector(image_np, 1)

    encodings= []

    for face in faces:
        shape = sp(image_np, face)
        face_descriptor = facerec.compute_face_descriptor(image_np, shape, 1) #128 embedding

        encodings.append(np.array(face_descriptor))
    return encodings

_trained_model = None

def get_trained_model(force_retrain=False):
    global _trained_model
    if _trained_model is not None and not force_retrain:
        return _trained_model

    X = []
    y = []

    student_db = get_all_students()

    if not student_db:
        _trained_model = None
        return None
    
    for student in student_db:
        embedding = student.get('face_embedding')
        if embedding:
            X.append(np.array(embedding))
            y.append(student.get('student_id'))

    if len(X) == 0:
        _trained_model = None
        return None

    clf = None
    if len(set(y)) >= 2:
        clf = SVC(kernel='linear', probability=True, class_weight='balanced')
        try:
            clf.fit(X, y)
        except ValueError:
            _trained_model = None
            return None

    _trained_model = {'clf': clf, 'X': X, 'y': y}
    return _trained_model


def _match_nearest_student(encoding, X_train, y_train, threshold=0.6):
    best_id = None
    best_score = float('inf')

    for i, train_emb in enumerate(X_train):
        dist = np.linalg.norm(train_emb - encoding)
        if dist < best_score:
            best_score = dist
            best_id = int(y_train[i])

    if best_id is not None and best_score <= threshold:
        return best_id
    return None


def train_classifier():
    model_data = get_trained_model(force_retrain=True)
    return model_data is not None

def predict_attendance(class_image_np):
    encodings = get_face_embeddings(class_image_np)

    detected_student = {}

    model_data = get_trained_model()

    if not model_data:
        return detected_student, [], len(encodings)
    
    clf = model_data['clf']
    X_train = model_data['X']
    y_train = model_data['y']

    all_students = sorted(list(set(y_train)))
    resemblance_threshold = 0.6

    for encoding in encodings:
        if clf is not None and len(all_students) >= 2:
            predicted_id = int(clf.predict([encoding])[0])
            best_score = float('inf')
            for i, train_emb in enumerate(X_train):
                if int(y_train[i]) == predicted_id:
                    best_score = min(best_score, np.linalg.norm(train_emb - encoding))
            if best_score <= resemblance_threshold:
                detected_student[predicted_id] = True
        else:
            matched_id = _match_nearest_student(
                encoding, X_train, y_train, resemblance_threshold
            )
            if matched_id is not None:
                detected_student[matched_id] = True

    return detected_student, all_students, len(encodings)
