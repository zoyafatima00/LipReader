# import streamlit as st
# from fpdf import FPDF
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email import encoders
# import json
# import os

# def send_report():
#     st.markdown('<div class="title">Send Report</div>', unsafe_allow_html=True)
#     st.markdown('<div class="subtitle">Send the analysis report to your email.</div>', unsafe_allow_html=True)

#     email = st.text_input("Enter the email address to send the report:")

#     # Load analysis results from file
#     if os.path.exists("analysis_results.json"):
#         with open("analysis_results.json", "r") as f:
#             analysis_results = json.load(f)

#         expected_text = analysis_results["expected_text"]
#         transcription = analysis_results["transcription"]
#         analysis = analysis_results["analysis"]
#         overall_similarity = analysis_results["overall_similarity"]
#         phoneme_analysis = analysis_results["phoneme_analysis"]
#     else:
#         st.error("No analysis results found. Please perform the analysis first.")
#         return

#     # Function to generate PDF report from analysis results
#     def generate_pdf_report(transcription, analysis, overall_similarity, phoneme_analysis):
#         pdf = FPDF()
#         pdf.add_page()
#         pdf.set_font("Arial", size=12)

#         pdf.cell(200, 10, txt="Speech Analysis Report", ln=True, align='C')
#         pdf.ln(10)

#         pdf.cell(200, 10, txt="Expected Phrase:", ln=True)
#         pdf.multi_cell(0, 10, expected_text.encode('latin-1', 'replace').decode('latin-1'))
#         pdf.ln(5)

#         pdf.cell(200, 10, txt="Transcription:", ln=True)
#         pdf.multi_cell(0, 10, transcription.encode('latin-1', 'replace').decode('latin-1'))
#         pdf.ln(5)

#         pdf.cell(200, 10, txt="Overall Similarity Score:", ln=True)
#         pdf.multi_cell(0, 10, f"{overall_similarity:.2f}")
#         pdf.ln(10)

#         pdf.cell(200, 10, txt="Detailed Analysis:", ln=True)
#         for item in analysis:
#             pdf.multi_cell(0, 10, f"Expected: {item['expected'].encode('latin-1', 'replace').decode('latin-1')}, Transcribed: {item['transcribed'].encode('latin-1', 'replace').decode('latin-1')}, Similarity: {item['similarity']:.2f}")
#             pdf.ln(5)

#         pdf.cell(200, 10, txt="Phoneme-level Analysis:", ln=True)
#         for result in phoneme_analysis:
#             pdf.multi_cell(0, 10, f"Phoneme: {result['phoneme'].encode('latin-1', 'replace').decode('latin-1')} (from word '{result['word'].encode('latin-1', 'replace').decode('latin-1')}'), Analysis: {result['feedback'].encode('latin-1', 'replace').decode('latin-1')}")
#             pdf.ln(5)

#         pdf_output = "speech_analysis_report.pdf"
#         pdf.output(pdf_output)
#         return pdf_output

#     # Function to send email with attachment
#     def send_email_with_attachment(to_address, attachment_path):
#         from_address = "hhzzaa512@gmail.com"
#         from_password = "pak51214"

#         msg = MIMEMultipart()
#         msg['From'] = from_address
#         msg['To'] = to_address
#         msg['Subject'] = "Speech Analysis Report"

#         attachment = MIMEBase('application', 'octet-stream')
#         attachment.set_payload(open(attachment_path, "rb").read())
#         encoders.encode_base64(attachment)
#         attachment.add_header('Content-Disposition', 'attachment; filename="speech_analysis_report.pdf"')
#         msg.attach(attachment)

#         server = smtplib.SMTP("smtp.gmail.com", 587)
#         server.starttls()
#         server.login(from_address, from_password)
#         server.sendmail(from_address, to_address, msg.as_string())
#         server.quit()

#     if st.button('Send Report'):
#         if email:
#             pdf_report = generate_pdf_report(transcription, analysis, overall_similarity, phoneme_analysis)
#             send_email_with_attachment(email, pdf_report)
#             st.success("Report sent successfully!")
#         else:
#             st.error("Please enter an email address.")
import streamlit as st
from fpdf import FPDF
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import json
import os

def send_report():
    st.markdown('<div class="title">Send Report</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Send the analysis report to your email.</div>', unsafe_allow_html=True)

    email = st.text_input("Enter the email address to send the report:")

    # Load analysis results from file
    if os.path.exists("analysis_results.json"):
        with open("analysis_results.json", "r") as f:
            analysis_results = json.load(f)

        expected_text = analysis_results["expected_text"]
        transcription = analysis_results["transcription"]
        analysis = analysis_results["analysis"]
        overall_similarity = analysis_results["overall_similarity"]
        phoneme_analysis = analysis_results["phoneme_analysis"]
    else:
        st.error("No analysis results found. Please perform the analysis first.")
        return

    # Function to generate PDF report from analysis results
    def generate_pdf_report(transcription, analysis, overall_similarity, phoneme_analysis):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="Speech Analysis Report", ln=True, align='C')
        pdf.ln(10)

        pdf.cell(200, 10, txt="Expected Phrase:", ln=True)
        pdf.multi_cell(0, 10, expected_text.encode('latin-1', 'replace').decode('latin-1'))
        pdf.ln(5)

        pdf.cell(200, 10, txt="Transcription:", ln=True)
        pdf.multi_cell(0, 10, transcription.encode('latin-1', 'replace').decode('latin-1'))
        pdf.ln(5)

        pdf.cell(200, 10, txt="Overall Similarity Score:", ln=True)
        pdf.multi_cell(0, 10, f"{overall_similarity:.2f}")
        pdf.ln(10)

        pdf.cell(200, 10, txt="Detailed Analysis:", ln=True)
        for item in analysis:
            pdf.multi_cell(0, 10, f"Expected: {item['expected'].encode('latin-1', 'replace').decode('latin-1')}, Transcribed: {item['transcribed'].encode('latin-1', 'replace').decode('latin-1')}, Similarity: {item['similarity']:.2f}")
            pdf.ln(5)

        pdf.cell(200, 10, txt="Phoneme-level Analysis:", ln=True)
        for result in phoneme_analysis:
            pdf.multi_cell(0, 10, f"Phoneme: {result['phoneme'].encode('latin-1', 'replace').decode('latin-1')} (from word '{result['word'].encode('latin-1', 'replace').decode('latin-1')}'), Analysis: {result['feedback'].encode('latin-1', 'replace').decode('latin-1')}")
            pdf.ln(5)

        pdf_output = "speech_analysis_report.pdf"
        pdf.output(pdf_output)
        return pdf_output

    # Function to send email with attachment
    def send_email_with_attachment(to_address, attachment_path):
        from_address = "your_email@gmail.com"
        from_password = "your_password"

        msg = MIMEMultipart()
        msg['From'] = from_address
        msg['To'] = to_address
        msg['Subject'] = "Speech Analysis Report"

        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload(open(attachment_path, "rb").read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', 'attachment; filename="speech_analysis_report.pdf"')
        msg.attach(attachment)

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_address, from_password)
        server.sendmail(from_address, to_address, msg.as_string())
        server.quit()

    if st.button('Send Report'):
        if email:
            pdf_report = generate_pdf_report(transcription, analysis, overall_similarity, phoneme_analysis)
            send_email_with_attachment(email, pdf_report)
            st.success("Report sent successfully!")
        else:
            st.error("Please enter an email address.")
