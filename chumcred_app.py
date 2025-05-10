import streamlit as st

# Page configuration
st.set_page_config(page_title="Chumcred Academy", layout="wide")

# Load logo image
from PIL import Image
logo = Image.open("images/logo.png")

# Display logo
st.image(logo, width=250)

# HTML + CSS + JS template
html_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
    body {
        font-family: 'Arial', sans-serif;
        margin: 0;
        padding: 0;
    }
    .navbar {
        overflow: hidden;
        background-color: #51C3C3;
        position: fixed;
        top: 0;
        width: 100%;
        z-index: 1000;
        text-align: center;
    }
    .navbar a {
        display: inline-block;
        color: white;
        text-align: center;
        padding: 18px 20px;
        text-decoration: none;
        font-size: 17px;
    }
    .navbar a:hover {
        background-color: #3BA9A9;
    }
    .section {
        padding: 80px 20px;
        text-align: left;
    }
    .about, .resources, .services, .contact, .blog {
        padding-top: 80px;
    }
    h2 {
        color: #51C3C3;
        text-align: left;
    }
    .resource-link {
        margin: 8px 0;
    }
    .footer {
        background-color: #51C3C3;
        color: #ffffff;
        text-align: center;
        padding: 25px 10px;
        margin-top: 30px;
        font-size: 14px;
        border-top: 2px solid #3BA9A9;
    }
</style>

<script>
        function scrollToSection(sectionId) {
            document.getElementById(sectionId).scrollIntoView({behavior: 'smooth'});
        }
    </script>
</head>
<body>

<div class="navbar">
    <a href="javascript:void(0)" onclick="scrollToSection('about')">About Us</a>
    <a href="javascript:void(0)" onclick="scrollToSection('resources')">Resources</a>
    <a href="javascript:void(0)" onclick="scrollToSection('services')">Services</a>
    <a href="javascript:void(0)" onclick="scrollToSection('contact')">Contact Us</a>
    <a href="javascript:void(0)" onclick="scrollToSection('blog')">Blog</a>
</div>

<div id="about" class="section about">
    <h2>About Us</h2>
    <p>Chumcred Academy is a subsidiary of Chumcred Limited — a forward-thinking training and capacity development institute. 
    We empower individuals and businesses with relevant, market-driven knowledge and practical skills tailored to today’s fast-changing world.</p>
</div>

<div id="resources" class="section resources">
    <h2>Resources</h2>
    <div class="resource-link">
        📄 <a href="https://drive.google.com/your-pdf-link-1" target="_blank">Introduction to Data Analytics (PDF)</a>
    </div>
    <div class="resource-link">
        📄 <a href="https://drive.google.com/your-pdf-link-2" target="_blank">Business Strategy 101 (PDF)</a>
    </div>
    <!-- Add more resource links here -->
</div>

<div id="services" class="section services">
    <h2>Services</h2>
    <ul>
        <li>Professional Trainings and Workshops</li>
        <li>Consulting for Business and Career Development</li>
        <li>Webinar Hosting and Online Certifications</li>
        <li>Corporate Leadership Development</li>
        <li>Data Analytics and Research Services</li>
    </ul>
</div>

<div id="contact" class="section contact">
    <h2>Contact Us</h2>
    <p>📞 +234 8025420200</p>
    <p>📧 chumcred@gmail.com</p>
    <p>🏢 60, Akerele Street, Surulere, Lagos, Nigeria</p>
</div>

<div id="blog" class="section blog">
    <h2>Blog</h2>
    <p>Stay tuned for insightful articles, event recaps, and industry updates from Chumcred Academy!</p>
</div>

<div class="footer">
    &copy; 2025 Chumcred Academy. All rights reserved.
</div>

</body>
</html>
"""

# Render HTML
st.components.v1.html(html_code, height=1500, scrolling=True)
