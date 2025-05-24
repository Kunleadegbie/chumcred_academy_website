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
    <p  style="text-align: justify;">Chumcred Academy is a subsidiary of Chumcred Limited — a forward-thinking training and capacity development institute. 
    We empower individuals and businesses with relevant, market-driven knowledge and practical skills tailored to today’s fast-changing world.
Welcome to Chumcred Academy — your trusted partner for transformative education, training, and professional development.<br> <br>
Chumcred Academy is the educational and capacity-building arm of Chumcred Limited, a dynamic enterprise committed to delivering strategic business support, professional consulting, and human capital development solutions. Our Academy was established as an integral part of the Chumcred ecosystem, operating as a dedicated platform for nurturing talents, enhancing skills, and providing market-relevant education without constituting a separate legal entity. <br> <br>
At Chumcred Academy, we understand the pivotal role that continuous learning and strategic capacity building play in today’s fast-paced, technology-driven, and increasingly volatile global economy. Our mission is to empower individuals, organizations, and institutions with the knowledge, competencies, and practical tools they need to thrive in competitive business environments and ever-evolving industries.
</p>
 <p  style="text-align: justify;">🎯 <b> Our Vision </b> <br>
To become a leading hub for transformative education and capacity development in Africa — fostering future-ready professionals, resilient businesses, and data-driven decision makers equipped to lead in a complex global landscape.
</p>

 <p  style="text-align: justify;">🎯 <b> Our Mission </b> <br>
To deliver innovative, market-aligned, and impact-driven training programs, professional development services, and strategic educational initiatives that build capacity, enhance business outcomes, and drive sustainable growth for individuals and organizations.
</p>
<p  style="text-align: justify;">📚 <b> What We Do </b> <br>
Chumcred Academy specializes in the provision of high-impact educational services and consultancy across diverse sectors. Our services are meticulously designed to address emerging needs in modern business, finance, management, and technology ecosystems. Our core offerings include:<br> <br>
•	<b> Capacity Building and Training Programs </b> <br>
We design and deliver practical, industry-focused training sessions for individuals, groups, and corporate clients. Our training programs span key areas such as Credit Management, Finance Essentials, Leadership and Business Management, Data Analytics, and Artificial Intelligence for Business Leaders.<br> <br>
•	<b> Coaching and Personal Development Services </b> <br> 
Through our structured coaching programs, we empower professionals and entrepreneurs to unlock their potential, enhance personal effectiveness, and achieve career and business objectives. <br> <br>
•	<b> Digital Learning Solutions </b> <br> 
Recognizing the importance of flexibility and accessibility, Chumcred Academy offers virtual classes, webinars, online workshops, and digital resource libraries to provide continuous learning opportunities anytime, anywhere.
•	<b> Vocational and Entrepreneurial Training Programs </b> <br> 
We are committed to fostering entrepreneurship and employability. Our tailored vocational and entrepreneurial programs equip participants with the practical skills and strategic insights required to build sustainable ventures and create job opportunities in the modern economy. <br> <br>
•	<b> Business Support and Development Advisory </b> <br> 
In collaboration with Chumcred Limited’s consulting arm, we provide advisory services, business incubation, mentorship programs, market access facilitation, and process outsourcing services for startups, SMEs, and corporate organizations seeking to optimize operations, penetrate new markets, and scale efficiently.<br> <br>
•	<b> Research, Feasibility Studies, and Strategic Assessments </b> <br> 
Our experienced team conducts needs assessments, market research, feasibility studies, and other strategic analyses for clients in both public and private sectors, providing actionable intelligence to support evidence-based decision making. <br> <br>
•	<b> Event Management and Professional Engagement Platforms </b> <br> 
Chumcred Academy organizes and coordinates a wide array of professional gatherings, including conferences, seminars, workshops, symposia, and webinars — designed to facilitate knowledge exchange, networking, and collaborative problem-solving on industry-critical topics.
</p>
<p  style="text-align: justify;">
📌 <b> Focus Areas </b> <br>
While our training and consulting services cut across various industries and disciplines, we maintain a strategic focus on the following thematic areas:<br>
•	<b> Credit Risk Management and Finance </b> <br>
•	<b> Business Management and Leadership </b> <br>
•	<b> Data Analytics and Business Intelligence </b> <br>
•	<b> Artificial Intelligence Essentials for Decision Makers </b> <br>
•	<b> Entrepreneurial Strategy and SME Development </b> <br>
These focus areas reflect our commitment to addressing critical capacity gaps in financial services, business strategy, technology adoption, and human capital development.

</p>

<p  style="text-align: justify;">
📢 <b> Upcoming Project </b> <br>
In our continued pursuit of excellence and thought leadership, we are currently working on a pioneering project titled: <br> <br>
<b> "Harnessing Data-Driven Credit Risk Management in a Volatile Global Economy" </b> <br> <br>
This timely initiative aims to explore how data analytics, predictive modeling, and AI-driven insights can be effectively leveraged to enhance credit risk assessment and financial decision-making processes in uncertain economic climates. The publication will feature evidence-based recommendations, case studies, and actionable frameworks for financial institutions, businesses, and policy makers.<br> <br>
Stay tuned for its official release via our resource library and professional webinar series.

</p>

<p  style="text-align: justify;">
🤝 <b> Why Choose Chumcred Academy </b> <br> <br>
•	<b> Industry-Relevant Curriculum:</b> <br> 
Our programs are developed in alignment with global business trends and the practical realities of the African market.<br> <br>
•	<b> Expert Facilitators:</b> <br> 
We engage seasoned trainers, industry experts, and certified professionals with extensive field experience.<br> <br>
•	<b> Flexible Delivery Models:</b> <br>
Learning options include physical workshops, online sessions, on-demand modules, and hybrid formats.<br> <br>
•	<b> Client-Centric Solutions: </b> <br> 
We tailor our offerings to meet the unique needs of individual clients, corporate organizations, and sector-specific challenges.<br> <br>
•	<b> Commitment to Impact: </b> <br> 
Beyond imparting knowledge, our programs are designed to produce measurable outcomes, build resilient organizations, and catalyze sustainable growth.

</p>

<p  style="text-align: justify;">
Whether you are a business leader seeking strategic insights, a professional aiming for career advancement, or an organization pursuing operational excellence — <b>Chumcred Academy</b> is your partner for knowledge-driven growth and lasting impact.
</p>


</div>

<div id="resources" class="section resources">
    <h2>Resources</h2>
    <div class="resource-link">
        📄 <a href="https://drive.google.com/file/d/1vwKbyjVilHErdS5Ao5Qw1gWP2mZu_3Ut/view?usp=sharing">How Credit Analysis is Done</a>
    <div class="resource-link">
        📄 <a href="https://drive.google.com/file/d/1kELMpX5WmXGESzidqj44uv2E8TUQfcnM/view?usp=sharing">Advanced Credit Management</a>
    </div>
<div class="resource-link">
        📄 <a href="https://drive.google.com/file/d/13uKwU1YKd2SLcWRKZbe4fghECp8PlQTR/view?usp=sharing">Digital Credit Management</a>
    <div class="resource-link">
        📄 <a href="https://drive.google.com/file/d/1bjMkLQeG2oqDVc811fksMlIV42s-GVrx/view?usp=sharing">Advanced International Credit Management 1</a>
    <div class="resource-link">
	📄 <a href="https://drive.google.com/file/d/16nNjUvWgH4YVcHzYEouBCPOxcYM3eFJp/view?usp=sharing">Emotional Intelligence for Sales Success</a>
    <div class="resource-link">
	📄 <a href="https://drive.google.com/file/d/19gTwZn71n5hV6l3r9IXgfPkrfJSO9RIo/view?usp=sharing">Sales Prospecting and Lead Generation</a>
    <div class="resource-link">

	📄 <a href="https://drive.google.com/file/d/12lG3nEfjFRFVCiDu-vCEMqA7hiJ0x8rO/view?usp=sharing">Advanced International Credit Management 2</a>
    <div class="resource-link">

	📄 <a href="https://drive.google.com/file/d/1FAXw3JA8c3UX-9rI624L48dW1ccDZkzU/view?usp=sharing">Financial Management </a>
    <div class="resource-link">


    <!-- Add more resource links here -->
</div>

<div id="services" class="section services">
    <h2>Services</h2>

<p  style="text-align: justify;">
📑 <b> Our Services </b> <br> <br>
At Chumcred Academy, our suite of services is crafted to empower individuals, startups, SMEs, and corporate organizations with the competencies, strategies, and tools required to thrive in today's increasingly competitive and data-driven world. Our approach is rooted in market-relevant capacity development, strategic advisory, and performance-enhancing solutions. <br> <br>
We offer a broad range of professional services, including:  <br> <br>
🎯 <b> 1. Professional Trainings and Capacity-Building Workshops </b> <br> <br>
We deliver practical, skill-based training programs and hands-on workshops aimed at boosting operational efficiency, financial prudence, leadership capacity, and technical competence.
Our programs cover: <br>
•	Financial Management & Credit Administration <br>
•	Data Analytics & Business Intelligence <br>
•	Artificial Intelligence Essentials for Business <br>
•	Corporate Strategy and Operations Optimization <br>
•	Leadership Development and Emotional Intelligence <br>
Each session is designed for measurable outcomes and immediate applicability in professional settings.

</p>

<p  style="text-align: justify;">
🎯 <b> 2. Business and Career Development Consulting </b> <br> <br>
Our consulting services help clients navigate market uncertainties, sharpen operational strategies, and advance their personal career goals. We support:<br>
•	Startups and SMEs with business planning, market entry, and risk advisory  <br>
•	Organizations with financial health audits, credit risk management, and data utilization strategies<br> 
•	Individuals with career strategy mapping, executive coaching, and industry-focused mentorship <br>
Our expert advisory services are data-driven, research-backed, and tailored to local and global market realities.<br> <br> </p>

<p  style="text-align: justify;">
🎯 <b> 3. Webinar Hosting and E-Learning Certifications</b> <br> <br>
Chumcred Academy embraces the future of education through its interactive webinars and e-learning platforms. These sessions offer flexible, real-time access to knowledge for busy professionals and learners.
We provide: <br>
•	Scheduled and on-demand webinars on trending topics <br> 
•	Online certification programs with industry recognition <br>
•	Partnerships with thought leaders and global educators for diverse learning content <br> 
•	Corporate e-learning solutions for employee training and leadership grooming  <br> <br>
</p>

<p  style="text-align: justify;">
🎯 <b> 4. Corporate Leadership Development Programs</b> <br> <br>
Through strategic programs, we cultivate the leadership competencies essential for sustainable business success.
Our interventions focus on: <br>
•	Building executive presence and decision-making capabilities <br> 
•	Change management and organizational culture alignment  <br> 
•	Succession planning and talent management strategies  <br> 
•	Team effectiveness and stakeholder engagement training <br> 
Our leadership academies are fully customizable to corporate goals and industry demands. <br> <br>
</p>

<p  style="text-align: justify;">
🎯 <b> 5. Data Analytics, Research & Market Intelligence </b> <br> <br>
Recognizing the pivotal role of data in business resilience and growth, our analytics and research services deliver evidence-based insights for strategic decision-making.
We offer: <br>
•	Data analytics training (from beginner to executive levels) <br> 
•	Business intelligence framework development  <br>
•	Market research, feasibility studies, and competitive benchmarking  <br> 
•	Performance dashboards and reporting solutions <br> 
•	Custom data analytics projects for operational optimization and credit risk evaluation <br> 
</p>

<p  style="text-align: justify;"> 
📑 <b> Training Programs </b> <br> <br>
At Chumcred Academy, our training programs are crafted to bridge the gap between formal knowledge and market-relevant competencies. We believe education should be transformative, practical, and strategically aligned with industry realities. 
Our programs are delivered through a mix of: <br>
•	Physical classroom sessions </b> <br>
•	Virtual instructor-led training (VILT) <br>
•	E-learning and self-paced modules  <br>
•	Executive masterclasses and certification bootcamps <br> <br>
</P>

<p  style="text-align: justify;"> 
📚 <b> Program Categories: </b> <br> <br>
🟢 <b> Financial Literacy and Credit Management </b> <br>
•	Credit Risk Analysis & Lending Decisions <br>
•	Financial Reporting and Cash Flow Management <br>
•	Loan Performance Monitoring & Debt Recovery Techniques <br>
•	Data-Driven Credit Portfolio Management <br> <br>
🟢 <b> Data Analytics and Business Intelligence </b> <br>
•	Data Analysis with Excel, SQL, and Power BI <br>
•	Python for Business Analytics <br>
•	Predictive Analytics for Decision Support <br>
•	Dashboard Development and Reporting Automation <br> <br>
🟢 <b> Management and Leadership Development </b> <br>
•	Executive Leadership Essentials <br>
•	Emotional Intelligence in Corporate Leadership <br>
•	Organizational Culture and Change Management <br>
•	High-Performance Team Building <br> <br>
🟢 <b> AI Essentials for Business </b> <br>
•	Introduction to Artificial Intelligence Concepts <br>
•	AI Tools for Business Efficiency <br>
•	Ethical AI and Responsible Data Practices <br>
•	AI-Powered Customer Service and Operational Automation <br> <br>
Each program culminates in a certificate of completion, practical projects, and post-training support resources.
</p>

<p  style="text-align: justify;"> 
📑 <b> Upcoming Project Feature: Harnessing Data-Driven Credit Risk Management in a Volatile Global Economy </b> <br> <br>
In an increasingly uncertain global economy, the ability to <b> leverage data for credit decisioning and risk mitigation </b> is no longer optional — it is imperative. As part of our ongoing commitment to providing forward-thinking, evidence-based insights,  Chumcred Academy is currently finalizing a groundbreaking research project  titled: <br> <br>
📊 <b> "Harnessing Data-Driven Credit Risk Management in a Volatile Global Economy" </b> <br> <br> 
This project explores how financial institutions, fintech startups, and credit providers can adopt advanced data analytics tools to manage risk, predict borrower behavior, and protect credit portfolios amid market volatility.<br>
Key Focus Areas:  <br> 
•	Assessing current credit risk models in emerging markets <br>
•	Exploring predictive analytics applications for borrower profiling <br>
•	Developing dynamic credit scoring frameworks <br>
•	Identifying early warning indicators using operational and transactional data <br>
•	Mitigating credit losses through real-time data insights <br> <br>
<b> Deliverables: </b> <br>
•	A comprehensive industry white paper<br>
•	Practical toolkits for credit risk management teams <br>
•	Webinar and panel discussions featuring financial experts and data scientist <br>
•	Customized training sessions for financial services firms and credit managers <br> <br>
<b>Release Date: </b> Q3 2025 <br> <br>
<b>Target Audience: </b> Banks, Fintech companies, Microfinance Institutions, Credit Bureaus, Regulatory Bodies, and Business Analysts.<br> <br>
Stay tuned for updates via our website and newsletter as we prepare to unveil findings that will reshape credit risk strategy for organizations operating in volatile economic climates.
 
</p>





</div>

<div id="contact" class="section contact">
    <h2>Contact Us</h2>
<p  style="text-align: justify;">
📞 <b>Connect With Us </b> <br>
At Chumcred Academy, we are passionate about helping you unlock your full potential, navigate today’s complexities, and lead boldly into the future. 
For inquiries, partnership opportunities, or to register for our upcoming training programs: </p>

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
