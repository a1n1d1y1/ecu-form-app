import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Page settings
st.set_page_config(page_title="ECU Submission Form", layout="centered")

st.title("🔧 ECU Submission Form")
st.markdown("Please fill out the form below based on the requirements.")

# Tabs for teams (Point 1)
tab1, tab2, tab3 = st.tabs(["📦 EOL", "🛠️ Service", "🔍 Diagnostics"])

# Common input
module_name = st.text_input("Module Name", help="Enter the name of the ECU/module being documented.")
form_data = {
    "Timestamp": datetime.now(),
    "Module Name": module_name,
}

# Tab 1 – EOL
with tab1:
    st.subheader("📦 EOL Requirements")
    form_data["Team"] = "EOL"
    form_data["Source Address"] = st.text_input("Source Address", help="Enter the ECU's communication address (e.g., 0x72)")
    form_data["VCP Name"] = st.text_input("VCP Name", help="Enter the .vcp configuration name used for flashing")
    form_data["Protocol"] = st.text_input("Protocol")
    form_data["Baud Rate"] = st.text_input("Baud Rate", help="Mention supported baud rates (e.g., 500k, 1M)")
    form_data["Wiring Information"] = st.text_input("Wiring Information")

    st.markdown("### 🧠 Programming Details")
    form_data["Diagnostic Session Control 0x10"] = st.text_input("Diagnostic Session Control 0x10")
    form_data["Tester Present 0x3E"] = st.text_input("Tester Present 0x3E")
    form_data["Read Data by Identifier 0x22"] = st.text_input("Read Data by Identifier 0x22")

    st.markdown("### 🔐 Cyber Security Details")
    form_data["SEED Request 0x27"] = st.text_input("SEED Request 0x27")
    form_data["SEED Length 128 bits"] = st.text_input("SEED Length 128 bits")
    form_data["Algorithm Owner"] = st.text_input("Algorithm Owner")
    form_data["Type of Algorithm"] = st.text_input("Type of Algorithm")
    form_data["Key Length 128 bits"] = st.text_input("Key Length 128 bits")
    form_data["Key Request 0x27"] = st.text_input("Key Request 0x27")

    st.markdown("### 🧬 Fingerprint Programming")
    form_data["Fingerprint DID"] = st.text_input("Fingerprint DID")
    form_data["Fingerprint Data"] = st.text_input("Fingerprint Data")
    form_data["Read Fingerprint Data 0x22"] = st.text_input("Read Fingerprint Data 0x22")
    form_data["Write Fingerprint Data 0x2E"] = st.text_input("Write Fingerprint Data 0x2E")
    form_data["Data Transfer 0x34"] = st.text_input("Data Transfer 0x34")
    form_data["Programming Control 0x31"] = st.text_input("Programming Control 0x31")
    form_data["Routine Control 0x31"] = st.text_input("Routine Control 0x31")
    form_data["Retain Data 0x31"] = st.text_input("Retain Data 0x31")
    form_data["ECU Reset 0x11"] = st.text_input("ECU Reset 0x11")
    form_data["After Reset ECU Wait Time"] = st.text_input("After Reset ECU Wait Time")

    st.markdown("### 🔌 Adapter Requirements")
    form_data["Adapter supported"] = st.selectbox("Adapter Supported?", ["Nbridges", "Nexiq", "VCIT"])

# Tab 2 – Service
with tab2:
    st.subheader("🛠️ Service Requirements")
    form_data["Team"] = "Service"
    form_data["Service Procedures"] = st.text_area("Service Procedures", help="Steps to be followed for servicing this module.")
    form_data["Software Version"] = st.text_input("Software Version", help="Expected or current software version installed.")
    form_data["Reset Behavior"] = st.text_input("Reset Behavior After Flash")
    form_data["Requires Special Tool"] = st.selectbox("Requires Special Tool?", ["Yes", "No"])

# Tab 3 – Diagnostics
with tab3:
    st.subheader("🔍 Diagnostics Requirements")
    form_data["Team"] = "Diagnostics"
    form_data["Diagnostic Protocol"] = st.text_input("Diagnostic Protocol", help="Mention UDS, KWP2000, etc.")
    form_data["Supported PIDs"] = st.text_area("Supported PIDs", help="List all PIDs supported by this module.")
    form_data["Error Code Behavior"] = st.text_input("Error Code Behavior")
    form_data["Special Diagnostic Modes"] = st.text_area("Special Diagnostic Modes")

# Submit & Save
if st.button("Submit"):
    submission_df = pd.DataFrame([form_data])
    output_file = "ecu_master_submissions.xlsx"

    if os.path.exists(output_file):
        existing_df = pd.read_excel(output_file)
        updated_df = pd.concat([existing_df, submission_df], ignore_index=True)
    else:
        updated_df = submission_df

    updated_df.to_excel(output_file, index=False)

    st.success("✅ Submission successful!")
    st.info(f"Your {form_data['Team']} data for module '{module_name}' has been saved.")
