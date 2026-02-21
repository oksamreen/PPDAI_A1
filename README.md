# PPDAI_A1 - Samreen Siddique
Repository for assignment 1, a personalized hair consultant, first stage prototype.

**Project Overview**
This Streamlit web application acts as a digital advisor for at-home hair treatments. It consolidates fragmented hair care research into a single, interactive tool. Users answer a quick three-question consultation in the sidebar, and the app instantly delivers a tailored, actionable remedy.

**The Data Pipeline**
The recommendation logic is built on a 3x3x3 nested dictionary. This matrix maps 27 distinct combinations of hair texture, primary concern, and desired goal. This deterministic pipeline ensures 100 percent accuracy for the prototype's current scope, guaranteeing that every user receives a safe, compatible regimen without the risk of AI hallucinations.

**Key Features**

** Clean, sidebar-based user interface for the consultation questionnaire.

** Simulated AI processing states to mimic an active consultant analyzing a profile.

** Deterministic, rule-based recommendation engine.

** Custom visual styling and interactive celebration animations.

**How to Run Locally**
To test this prototype on your own machine, open your terminal and ensure your Python environment is active. Then, simply type streamlit run hair_consultant.py and press enter. The application will automatically launch in your default web browser.

**Live Demo**
You can try the live prototype hosted on Streamlit Community Cloud here: https://remedyme.streamlit.app/ 

**Author**
Samreen
