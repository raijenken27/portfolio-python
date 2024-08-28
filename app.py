import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Jerome Garcia | Full-stack Developer", layout="centered")

# Sidebar or header image (optional)
image = Image.open('images/Jerome Garcia Profile.png')
st.image(image, width=150, caption="Jerome Garcia")

# Title and Introduction
st.title("Jerome Garcia")
st.subheader("Full-stack Developer")
st.write("""
Hi there! I'm Jerome Garcia, a passionate Full-stack Developer with a knack for turning ideas into reality through code. 
With a diverse set of skills ranging from front-end design to back-end development, I create seamless and efficient web applications.
I thrive on problem-solving and constantly seek to enhance my expertise in the latest technologies.
""")

# Skills Section
st.header("Skills")
st.write("""
- **Front-end:** HTML, CSS, JavaScript, React, Vue.js
- **Back-end:** Node.js, Python, Django, Flask, Ruby on Rails
- **Databases:** MySQL, PostgreSQL, MongoDB
- **DevOps:** Docker, Kubernetes, Jenkins, AWS, Azure
- **Others:** Git, Agile, TDD, RESTful APIs, GraphQL
""")

# Projects Section
st.header("Projects")
st.write("### [Project 1: E-commerce Web App](#)")
st.write("""
Developed a full-fledged e-commerce platform using React and Django. The platform features a responsive design, 
secure payment integration, and a powerful admin dashboard.
""")
st.write("### [Project 2: Real-time Chat Application](#)")
st.write("""
Built a real-time chat application using Node.js and Socket.io. The app supports multiple chat rooms, user authentication, 
and real-time notifications.
""")
st.write("### [Project 3: Personal Blog](#)")
st.write("""
Created a personal blog using Vue.js and Flask. The blog features a clean, minimalist design, SEO optimization, 
and easy content management.
""")

# Experience Section
st.header("Experience")
st.write("### Senior Full-stack Developer at XYZ Tech")
st.write("**2019 - Present**")
st.write("""
Lead the development of several high-profile projects, mentoring junior developers and collaborating closely 
with the design and product teams to deliver exceptional digital experiences.
""")

st.write("### Full-stack Developer at ABC Innovations")
st.write("**2016 - 2019**")
st.write("""
Contributed to the development of multiple web applications, focusing on both front-end user experience 
and back-end server-side logic.
""")

# Contact Section
st.header("Get in Touch")
st.write("Feel free to reach out to me for any project collaborations or job opportunities!")
st.write("- **Email:** jerome.garcia@example.com")
st.write("- **LinkedIn:** [linkedin.com/in/jeromegarcia](#)")
st.write("- **GitHub:** [github.com/jeromegarcia](#)")

# Footer
st.markdown("---")
st.write("© 2024 Jerome Garcia. All rights reserved.")

# Optional: Add a dark mode toggle
if st.sidebar.button("Toggle Dark Mode"):
    st.markdown("""
    <style>
    body {
        background-color: #1E1E1E;
        color: #FFFFFF;
    }
    </style>
    """, unsafe_allow_html=True)
