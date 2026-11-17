
import streamlit as st
import pandas as pd

from database import (
    create_table,
    add_patient,
    get_all_patients,
    update_patient_email,
    delete_patient
)

from validators import (
    validate_email,
    validate_date_of_birth,
    validate_blood_value
)

from ai_service import generate_health_remark


# -----------------------------
# APP CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="AI Health Prediction",
    page_icon="🏥",
    layout="wide"
)

create_table()

st.title("🏥 AI-Powered Health Prediction Application")

st.caption(
    "Patient blood test management with validation, CRUD operations "
    "and AI-generated health observations."
)

st.warning(
    "This application is for demonstration purposes only and does not "
    "provide a medical diagnosis."
)


# -----------------------------
# SIDEBAR NAVIGATION
# -----------------------------
menu = st.sidebar.radio(
    "Navigation",
    ["Create Record", "View Records", "Update Record", "Delete Record"]
)


# -----------------------------
# CREATE RECORD
# -----------------------------
if menu == "Create Record":

    st.header("➕ Create Patient Record")

    full_name = st.text_input("Full Name")
    dob = st.text_input("Date of Birth (dd.mm.yyyy)")
    email = st.text_input("Email Address")

    col1, col2, col3 = st.columns(3)

    with col1:
        glucose = st.text_input("Glucose")

    with col2:
        haemoglobin = st.text_input("Haemoglobin")

    with col3:
        cholesterol = st.text_input("Cholesterol")

    if st.button("Generate AI Remark & Save"):

        errors = []

        if not full_name.strip():
            errors.append("Full Name is required.")

        email_valid, email_message = validate_email(email)

        if not email_valid:
            errors.append(email_message)

        dob_valid, formatted_dob, dob_message = validate_date_of_birth(dob)

        if not dob_valid:
            errors.append(dob_message)

        glucose_valid, glucose_value, glucose_message = validate_blood_value(
            glucose, "Glucose"
        )

        haemoglobin_valid, haemoglobin_value, haemoglobin_message = validate_blood_value(
            haemoglobin, "Haemoglobin"
        )

        cholesterol_valid, cholesterol_value, cholesterol_message = validate_blood_value(
            cholesterol, "Cholesterol"
        )

        if not glucose_valid:
            errors.append(glucose_message)

        if not haemoglobin_valid:
            errors.append(haemoglobin_message)

        if not cholesterol_valid:
            errors.append(cholesterol_message)

        if errors:

            st.error("Please correct the following errors:")

            for error in errors:
                st.write(f"❌ {error}")

        else:

            existing_records = get_all_patients()

            duplicate_found = any(
                record[1].strip().lower() == full_name.strip().lower()
                and record[2] == formatted_dob
                and record[3].strip().lower() == email.strip().lower()
                for record in existing_records
            )

            if duplicate_found:

                st.error("Duplicate patient record already exists!")

            else:

                with st.spinner("Generating AI health observation..."):

                    try:

                        remark = generate_health_remark(
                            glucose_value,
                            haemoglobin_value,
                            cholesterol_value
                        )

                    except Exception:

                        remark = (
                            "AI service is temporarily unavailable. "
                            "Please consult a qualified healthcare professional. "
                            "This is not a medical diagnosis."
                        )

                add_patient(
                    full_name.strip(),
                    formatted_dob,
                    email.strip(),
                    glucose_value,
                    haemoglobin_value,
                    cholesterol_value,
                    remark
                )

                st.success("Patient record created successfully!")

                st.subheader("🤖 AI Generated Remark")

                st.info(remark)


# -----------------------------
# READ RECORDS
# -----------------------------
elif menu == "View Records":

    st.header("📋 All Patient Records")

    records = get_all_patients()

    if records:

        df = pd.DataFrame(
            records,
            columns=[
                "ID",
                "Full Name",
                "Date of Birth",
                "Email",
                "Glucose",
                "Haemoglobin",
                "Cholesterol",
                "Remarks"
            ]
        )

        st.dataframe(
            df,
            use_container_width=True
        )

        st.success(f"Total records: {len(records)}")

    else:

        st.info("No patient records found.")


# -----------------------------
# UPDATE RECORD
# -----------------------------
elif menu == "Update Record":

    st.header("✏️ Update Patient Email")

    records = get_all_patients()

    if records:

        patient_options = {
            f"ID {record[0]} - {record[1]}": record[0]
            for record in records
        }

        selected_patient = st.selectbox(
            "Select Patient",
            list(patient_options.keys())
        )

        new_email = st.text_input("New Email Address")

        if st.button("Update Email"):

            email_valid, email_message = validate_email(new_email)

            if not email_valid:

                st.error(email_message)

            else:

                patient_id = patient_options[selected_patient]

                update_patient_email(
                    patient_id,
                    new_email.strip()
                )

                st.success("Email updated successfully!")

    else:

        st.info("No records available to update.")


# -----------------------------
# DELETE RECORD
# -----------------------------
elif menu == "Delete Record":

    st.header("🗑️ Delete Patient Record")

    records = get_all_patients()

    if records:

        patient_options = {
            f"ID {record[0]} - {record[1]}": record[0]
            for record in records
        }

        selected_patient = st.selectbox(
            "Select Patient to Delete",
            list(patient_options.keys())
        )

        st.warning(
            "This action will permanently delete the selected record."
        )

        if st.button("Delete Record"):

            patient_id = patient_options[selected_patient]

            delete_patient(patient_id)

            st.success("Patient record deleted successfully!")

    else:

        st.info("No records available to delete.")
