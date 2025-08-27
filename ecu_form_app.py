import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="ECU Submission Form")

st.title("🔧 ECU Submission Form")

st.markdown("Please fill out the form below based on the requirements.")

# Step 1: Select team
team = st.selectbox("Select Requirement to be Filled", ["EOL", "Service", "Diagnostics"])

# Step 2: Display team-specific fields
module_name = st.text_input("Module Name")

# Collect inputs dynamically based on team
form_data = {
    "Timestamp": datetime.now(),
    "Team": team,
    "Module Name": module_name,
}

if team == "EOL":
    form_data["Source Address"] = st.text_input("Source Address")
    form_data["VCP Name"] = st.text_input("VCP Name")
    form_data["Protocol"] = st.text_input("Protocol")
    form_data["Baud Rate"] = st.text_area("Baud Rate")
    form_data["Wiring Information"] = st.text_input("Wiring Inforamtion")
    st.markdown("### Programming Details")
    form_data["Diagnostic Session Control 0x10"] = st.text_input("Diagnostic Session Control 0x10")
    form_data["Tester Present 0x3E"] = st.text_input("Tester Present 0x3E")
    form_data["Read Data by Identifier 0x22"] = st.text_input("Read Data by Identifier 0x22")
    st.markdown("### Cyber Security Details")
    form_data["SEED Request 0x27"] = st.text_input("SEED Request 0x27")
    form_data["SEED Length 128 bits"] = st.text_input("SEED Length 128 bits")
    form_data["Algorithm Owner"] = st.text_input("Algorithm Owner")
    form_data["Type of Algorithm"] = st.text_input("Type of Algorithm")
    form_data["Key Length 128 bits"] = st.text_input("Key Length 128 bits")
    form_data["Key Request 0x27"] = st.text_input("Key Request 0x27")
    st.markdown("### FingerPrint Programming")
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
    st.markdown("### Adapter Requirements")
    form_data["Adapter supported"] = st.selectbox("Adapter supported.?", ["Nbridges", "Nexiq","VCIT"])
    

elif team == "Service":
    form_data["Service Procedures"] = st.text_area("Service Procedures")
    form_data["Software Version"] = st.text_input("Software Version")
    form_data["Reset Behavior"] = st.text_input("Reset Behavior After Flash")
    form_data["Requires Special Tool"] = st.selectbox("Requires Special Tool?", ["Yes", "No"])

elif team == "Diagnostics":
    form_data["Diagnostic Protocol"] = st.text_input("Diagnostic Protocol")
    form_data["Supported PIDs"] = st.text_area("Supported PIDs")
    form_data["Error Code Behavior"] = st.text_input("Error Code Behavior")
    form_data["Special Diagnostic Modes"] = st.text_area("Special Diagnostic Modes")

# Step 3: Submit & Save
if st.button("Submit"):
    # Convert to DataFrame
    submission_df = pd.DataFrame([form_data])

    # File to store all submissions
    output_file = "ecu_master_submissions.xlsx"

    # If file exists, append; else create new
    if os.path.exists(output_file):
        existing_df = pd.read_excel(output_file)
        updated_df = pd.concat([existing_df, submission_df], ignore_index=True)
    else:
        updated_df = submission_df

    updated_df.to_excel(output_file, index=False)

    # Confirmation message
    st.success(f"✅ Submission successful!")
    st.info(f"Your {team} team data for module '{module_name}' has been saved.")
