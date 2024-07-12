import streamlit as st
import google.generativeai as palm

import requests 
import streamlit as st
from streamlit_lottie import st_lottie

import streamlit as st


import base64
from fpdf import FPDF

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://images.pexels.com/photos/67823/match-matches-sticks-lighter-67823.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
background-size: 180%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
</style>"""
st.markdown(page_bg_img, unsafe_allow_html=True)







def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



st.title("JobSwift: Accelarating Careers with AI-Powered Application")
st.markdown("---")







# with open('app.css') as f:
#     st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

#configure the API with API key
palm.configure(api_key="AIzaSyAITURcsuvg8Rr2HqkYNKi3N05KKK7LJwc")

model_name="models/text-bison-001"

def load_lottie_url(url: str):
    import requests
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

# Function to generate resume
def generate_resume(name, experience, skills, projects, education, awards):
    prompt = f"My name is {name}. I have {experience} years of experience in {skills}."
    prompt += f"\n\nProjects:\n{projects}\n\nEducation:\n{education}\n\nAwards and Recognition:\n{awards}"
    response = palm.generate_text(model=model_name, prompt=prompt)
    return response.result

# Function to generate resume as PDF
def generate_resume_pdf(name, experience, skills, projects, education, awards):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Adding content to PDF
    pdf.cell(200, 10, txt=f"My name is {name}. I have {experience} years of experience in {skills}.", ln=True)
    pdf.cell(200, 10, txt=f"\nProjects:\n{projects}\n\nEducation:\n{education}\n\nAwards and Recognition:\n{awards}", ln=True)

    # Save PDF
    pdf_filename = "resume.pdf"
    pdf.output(pdf_filename)

    return pdf_filename

# Function to generate cover letter
def generate_cover_letter(company_name, job_title,):
    prompt = f"Dear hiring manager,\n\nI am writing to express my interest in the {job_title} position at {company_name}."
    response = palm.generate_text(model=model_name, prompt=prompt)
    return response.result


# Function to generate cover letter as PDF
def generate_cover_letter_pdf(company_name, job_title):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Adding content to PDF
    pdf.multi_cell(0, 10, f"Dear hiring manager,")

    pdf.ln(10)  # Add a new line for spacing

    pdf.multi_cell(0, 10, f"I am writing to express my interest in the {job_title} position at {company_name}.")
    
    pdf.ln(10)  # Add a new line for spacing

    pdf.multi_cell(0, 10, "I have over [X] years of experience in [relevant skills] and believe I would be a valuable asset to your team.")

    # Save PDF
    pdf_filename = "cover_letter.pdf"
    pdf.output(pdf_filename)

    return pdf_filename

# Function to generate interview preparation questions
def generate_interview_questions(skills):
    prompt = f"Interview Preparation Questions Based on Skills: {skills}"
    response = palm.generate_text(model=model_name, prompt=prompt)
    return response.result

# Function to generate interview questions as PDF
def generate_interview_questions_pdf(skills):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Adding content to PDF
    pdf.cell(200, 10, txt=f"Interview Preparation Questions Based on Skills: {skills}", ln=True)

    # Save PDF
    pdf_filename = "interview_questions.pdf"
    pdf.output(pdf_filename)

    return pdf_filename

# Function to download PDF
def download_pdf(text, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 12)
    for line in text.split('\n'):
        pdf.cell(200, 10, txt = line, ln = True, align = 'L')
    pdf.output(filename)

def main():
    st.sidebar.title("Navigation")
    option = st.sidebar.selectbox("Go to", ["Home", "Generate Resume", "Generate Cover Letter", "Generate Interview Questions"])

    if option == "Home":
        st.title("Welcome to the Resume Generator Home Page")
        st.write("This application helps you generate resumes, cover letters, and interview preparation questions.")
        st.write("Use the navigation on the left to select an option.")
        lottie_animation_home = "https://lottie.host/3deadefe-46cc-4ce5-98b7-722540b538d2/lRl6yc50pf.json"
        lottie_anime_json_home = load_lottie_url(lottie_animation_home)

        # Display the Lottie animation in the container
        st_lottie(
            lottie_animation_home,
            speed=10,
            width=400,
            height=400,
            key="lottie_animation_home"
        )
    elif option == "Generate Resume":
        st.subheader("Generate Resume")
        lottie_animation_resume = "https://lottie.host/197de7a6-16dd-40e3-8cb7-7dd4379b9418/KJxL77W05N.json"
        lottie_anime_json_resume = load_lottie_url(lottie_animation_resume)

        # Display the Lottie animation in the container
        st_lottie(
            lottie_animation_resume,
            speed=10,
            width=200,
            height=200,
            key="lottie_animation_resume"
        )
        name = st.text_input("Enter your name")
        experience = st.number_input("Enter your years of experience", min_value=0, step=1)
        skills = st.text_area("Enter your skills")
        projects = st.text_area("Enter your projects")
        education = st.text_area("Enter your education")
        awards = st.text_area("Enter your awards and recognition")

        


        if st.button("Generate"):
            if name and experience and skills and projects and education and awards:
                # Generate resume as PDF
                pdf_filename = generate_resume_pdf(name, experience, skills, projects, education, awards)
                resume = generate_resume(name, experience, skills, projects, education, awards)
                st.write(resume)

                
                # Provide a download link
                with open(pdf_filename, "rb") as f:
                    st.download_button(label="Download Resume PDF", data=f.read(), file_name="resume.pdf", mime="application/pdf")
            
                st.success("Resume PDF generated and ready for download!")
            else:
                 st.warning("Please fill in all the fields.")
    elif option == "Generate Cover Letter":
        st.subheader("Generate Cover Letter")
        lottie_animation_cover_letter = "https://lottie.host/6e001989-a25b-470f-903d-68f7cfcf53ef/5AVMFfim4z.json"
        lottie_anime_json_cover_letter = load_lottie_url(lottie_animation_cover_letter)

        # Display the Lottie animation in the container
        st_lottie(
            lottie_animation_cover_letter,
            speed=10,
            width=200,
            height=200,
            key="lottie_animation_cover_letter"
        )
        company_name = st.text_input("Enter the company name")
        job_title = st.text_input("Enter the job title")
        if st.button("Generate"):
            if company_name and job_title:
                cover_letter = generate_cover_letter(company_name, job_title)
                # Generate cover letter as PDF
                pdf_filename = generate_cover_letter_pdf(company_name, job_title)
                st.write(cover_letter)

                # Provide a download link
                with open(pdf_filename, "rb") as f:
                    st.download_button(label="Download Cover Letter PDF", data=f.read(), file_name="cover_letter.pdf", mime="application/pdf")
                
                st.success("Cover Letter PDF generated and ready for download!")

            

                
            else:
                st.warning("Please fill in all the fields.")
    elif option == "Generate Interview Questions":
        st.subheader("Generate Interview Questions")
        lottie_animation_interview = "https://lottie.host/6ae907f4-0ec1-48b3-97ce-c14040703bc8/6rAcNVUhYx.json"
        lottie_anime_json_interview = load_lottie_url(lottie_animation_interview)

        # Display the Lottie animation in the container
        st_lottie(
            lottie_animation_interview,
            speed=10,
            width=300,
            height=300,
            key="lottie_animation_interview"
        )
        skills = st.text_area("Enter your skills")
        if st.button("Generate"):
            if skills:
                interview_questions = generate_interview_questions(skills)
                # Generate interview questions as PDF
                pdf_filename = generate_interview_questions_pdf(skills)
                st.write(interview_questions)

                # Provide a download link
                with open(pdf_filename, "rb") as f:
                    st.download_button(label="Download Interview Questions PDF", data=f.read(), file_name="interview_questions.pdf", mime="application/pdf")
                
                st.success("Interview Questions PDF generated and ready for download!")

                
            else:
                st.warning("Please enter your skills")

if __name__ == "__main__":

    main()