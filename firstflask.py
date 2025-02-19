from flask import Flask,  flash, redirect, request, render_template, make_response, url_for, render_template_string,jsonify
import json
import sys 
import random
import csv  
#import pandas as pd

app = Flask(__name__)

#web service
##api post
@app.route('/request',methods=['POST']) 
def web_service_API():

    payload = request.data.decode("utf-8")
    inmessage = json.loads(payload) # ทำ json

    print(inmessage)
    
    
    json_data = json.dumps({'y': 'received!'}) # ส่งกลับไปว่าได้รับเเล้ววว
    return json_data



@app.route("/")  #บอกว่าเรียกใช้ web ไหน
def helloworld():
    return "Hello, World!"



@app.route("/name")  #บอกว่าเรียกใช้ web ไหน
def hellophu():
    return "Hello, Phu!"


@app.route("/index", methods=['POST', 'GET'])
def indexfn():
    if request.method == "GET":
        print('we are in index(GET)', file=sys.stdout)
        namein = request.args.get('fname')  # รับพารามิเตอร์จาก query string
        print(namein, file=sys.stdout)
        return render_template("index.html", name=namein)

    elif request.method == "POST":
        print('we are in index(POST)', file=sys.stdout)
        namein = request.form.get('fname')  # รับ input จากฟอร์ม
        lastnamein = request.form.get('lname')
        print(namein, file=sys.stdout)
        print(lastnamein, file=sys.stdout)
        return render_template("index.html", name=namein)
    

faculties = [
    {
        "name": "Dr. John Doe",
        "title": "Assistant Professor",
        "department": "Department of Data Science",
        "email": "johndoe@university.edu",
        "research_area": "Machine Learning, Artificial Intelligence",
        "research_projects": ["Predictive Modeling of Financial Markets", "AI for Healthcare Diagnostics", "Deep Learning for Natural Language Processing"]
    },
    {
        "name": "Prof. Jane Smith",
        "title": "Professor",
        "department": "Department of Statistics",
        "email": "janesmith@university.edu",
        "research_area": "Biostatistics, Epidemiology",
        "research_projects": ["Statistical Methods in Cancer Research", "Epidemiological Analysis of Global Health Trends", "Biostatistical Models for Drug Development"]
    },
    {
        "name": "Dr. Emily Clark",
        "title": "Associate Professor",
        "department": "Department of Environmental Science",
        "email": "emilyclark@university.edu",
        "research_area": "Climate Change, Environmental Statistics",
        "research_projects": ["Climate Modeling for Urban Areas", "Impact of Climate Change on Biodiversity", "Statistical Analysis of Renewable Energy Adoption"]
    },
    {
        "name": "Prof. Michael Johnson",
        "title": "Professor",
        "department": "Department of Economics",
        "email": "michaeljohnson@university.edu",
        "research_area": "Econometrics, Financial Modeling",
        "research_projects": ["Econometric Models for Market Behavior", "Financial Risk Analysis Using Statistical Methods", "Machine Learning in Credit Scoring"]
    },
    {
        "name": "Dr. Supachai Pongsakorn",
        "title": "Assistant Professor",
        "department": "Department of Computer Science",
        "email": "supachaip@university.ac.th",
        "research_area": "Artificial Intelligence, Deep Learning, Data Mining",
        "research_projects": ["AI for Predictive Maintenance", "Deep Learning for Image Recognition", "Data Mining for Healthcare Insights"]
    },
    {
        "name": "Prof. Ananya Rattanapol",
        "title": "Professor",
        "department": "Department of Statistics",
        "email": "ananyar@university.ac.th",
        "research_area": "Biostatistics, Environmental Statistics",
        "research_projects": ["Statistical Models for Public Health", "Predictive Modeling in Environmental Science", "Data Analytics for Sustainable Development"]
    },
    {
        "name": "Dr. Nattapong Piyapong",
        "title": "Associate Professor",
        "department": "Department of Mathematics",
        "email": "nattapongp@university.ac.th",
        "research_area": "Mathematical Statistics, Stochastic Processes",
        "research_projects": ["Stochastic Models in Financial Markets", "Time Series Analysis for Economic Forecasting", "Risk Analysis using Mathematical Models"]
    }
]

    
    
@app.route("/research")  #บอกว่าเรียกใช้ web ไหน
def research():
    # Randomly select a faculty member
    selected_faculty = random.choice(faculties)
    
    # Get the research projects for that faculty
    projects = selected_faculty["research_projects"]
    
    return render_template('research.html', faculty=selected_faculty["name"], research_projects=projects)



# This function will save the form data into a CSV file
def save_to_csv(name, email, message):
    with open('contact_form_data.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header if the file is empty
        if file.tell() == 0:
            writer.writerow(["Name", "Email", "Message"])
        # Write the form data
        writer.writerow([name, email, message])



@app.route('/upload', methods=['GET', 'POST'])  # เริ่มเเรก Get ไป return
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        file.save('File_uploaded')
        return render_template("index.html",name= 'upload completed')

    return '''  
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
    
@app.route("/stathtml", methods=['POST', 'GET'])
def stathtml():
    
    return ''' 

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Stat KKU - Homepage</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f9;
                color: #333;
            }
            header {
                background-color: #0078d7;
                color: white;
                padding: 1rem 0;
                text-align: center;
            }
            nav {
                background-color: #005ea6;
                display: flex;
                justify-content: center;
                padding: 0.5rem 0;
            }
            nav a {
                color: white;
                text-decoration: none;
                margin: 0 1rem;
            }
            nav a:hover {
                text-decoration: underline;
            }
            main {
                padding: 2rem;
                text-align: center;
            }
            footer {
                background-color: #0078d7;
                color: white;
                text-align: center;
                padding: 1rem 0;
                position: fixed;
                bottom: 0;
                width: 100%;
            }
            

        p {
            margin: 10px 0;
            text-align: justify;
        }
        

/* Paragraph Styling */
p {
    font-size: 16px;
    margin-bottom: 10px;
    color: #555;
    line-height: 1.6;
}

/* Links Styling */
a {
    font-weight: bold;
}

ul {
    list-style-type: none;
    padding: 0;
}

ul li {
    margin-bottom: 8px;
}

/* Styling for Contact Section */
#contact ul {
    padding-left: 20px;
}

#contact a {
    font-size: 16px;
    font-weight: normal;
    color: #007BFF;
}

#contact p {
    margin-bottom: 15px;
}

/* Styling for Programs Section */
#programs p {
    font-size: 16px;
    margin-bottom: 10px;
    color: #555;
    line-height: 1.6;
}

#programs p:first-of-type {
    font-weight: bold;
}

        </style>
    </head>
    <body>
        <header>
            <h1>Welcome to Stat KKU</h1>
            <p>Department of Statistics, Khon Kaen University</p>
        </header>
        <nav>
            <a href="#about">About Us</a>
            <a href="#programs">Programs</a>
            <a href="/research">Research</a>
            <a href="/contact">Contact</a>
        </nav>
        <main>
            <section id="about">
                <h2>About Us</h2>
<p>
1. The Department of Statistics at Khon Kaen University offers a wide range of undergraduate and graduate programs designed to equip students with a deep understanding of statistical theory and its practical applications. The curriculum emphasizes both foundational knowledge and the latest advancements in the field, preparing students for diverse career opportunities in academia, industry, and government.
</p>
<p>
2. Faculty members at the department are accomplished researchers with expertise in areas such as data science, machine learning, biostatistics, econometrics, and experimental design. Their research contributes to solving real-world problems, from analyzing big data to improving healthcare outcomes, making the department a hub for innovative statistical research in Southeast Asia.
</p>
<p>
3. The department prides itself on fostering a supportive learning environment where students are encouraged to explore their interests and develop critical thinking skills. Through interactive lectures, hands-on workshops, and collaborative projects, students gain practical experience in statistical programming, data visualization, and predictive modeling.
</p>
<p>
4. Beyond the classroom, the department is actively engaged in community outreach and collaborative research initiatives. Faculty and students frequently work with local organizations and industries, providing statistical expertise to enhance decision-making processes in areas such as agriculture, education, public health, and environmental management.
</p>
<p>
5. The department also houses state-of-the-art facilities, including computer labs equipped with the latest statistical software and tools. These resources enable students to work on cutting-edge research projects, analyze complex datasets, and apply their skills to solve pressing societal challenges.
</p>
<p>
6. One of the department's key goals is to stay at the forefront of statistical education by integrating emerging technologies such as artificial intelligence and cloud computing into its programs. This ensures that graduates are well-prepared to navigate the rapidly evolving landscape of data science and analytics.
</p>
<p>
7. The department regularly organizes academic events, including workshops, seminars, and conferences, to bring together leading statisticians, researchers, and practitioners from around the world. These events provide valuable networking opportunities for students and faculty and foster a culture of knowledge exchange and innovation.
</p>
<p>
8. In addition to academic pursuits, the department emphasizes the importance of ethics and social responsibility in the application of statistics. Students are encouraged to consider the broader implications of their work, ensuring that statistical analyses are conducted with integrity, transparency, and a focus on societal benefit.
</p>
<p>
9. Alumni of the Department of Statistics at Khon Kaen University have gone on to excel in various fields, including finance, technology, healthcare, and education. Their achievements serve as a testament to the department's commitment to producing well-rounded, skilled professionals who make meaningful contributions to society.
</p>
<p>
10. As the demand for statistical expertise continues to grow, the Department of Statistics at Khon Kaen University remains dedicated to its mission of advancing statistical knowledge through high-quality education, impactful research, and meaningful community engagement. By nurturing the next generation of statisticians, the department aims to play a pivotal role in shaping a data-driven future.
</p>

            </section>
            <section id="programs">
                <h2>Programs</h2>
                <p>We offer a comprehensive range of undergraduate and postgraduate programs in statistics, tailored to equip students with the knowledge and skills necessary for success in both academic and professional settings. Our undergraduate program covers fundamental statistical theory, while the graduate programs offer specialized courses in areas such as data science, machine learning, biostatistics, and econometrics. Graduates are well-prepared to embark on diverse career paths in industries such as healthcare, finance, technology, and government.</p>
                <p>Our graduate programs include a Master's degree and a Ph.D. program that focus on advanced statistical techniques, cutting-edge research, and real-world applications. Students have the opportunity to work closely with faculty on innovative research projects, contributing to global advancements in statistical science.</p>
                <p>In addition, we offer professional development programs and workshops designed to help students and industry professionals keep up-to-date with the latest trends and technologies in the field of statistics.</p>
            </section>

            <section id="research">
                <h2>Research</h2>
                <p>Our faculty members are at the forefront of statistical research, contributing to a wide range of interdisciplinary fields. Through their work, they address real-world challenges by applying advanced statistical methods and tools. Research areas include, but are not limited to, data science, artificial intelligence, biostatistics, financial modeling, environmental statistics, and public health analysis. Their efforts have not only expanded the body of statistical knowledge but also provided practical solutions to pressing issues faced by society.</p>
                <p>Our research initiatives often involve collaboration with government agencies, healthcare organizations, and industry leaders, ensuring that our work has a tangible impact on real-world problems. Students and faculty participate in research projects that explore diverse topics such as predictive modeling for healthcare, statistical methods for climate change analysis, and the use of machine learning algorithms for financial forecasting.</p>
                <p>The department organizes and hosts various research seminars, workshops, and conferences to foster collaboration between statisticians, researchers, and practitioners. These events provide an excellent opportunity for students to engage with experts in the field, gain insights into cutting-edge developments, and contribute to ongoing discussions about the future of statistics and data science.</p>
            </section>

            <section id="contact">
                <h2>Contact</h2>
                <p>If you have any questions or inquiries about our programs, research, or any other aspect of the Department of Statistics, please feel free to contact us.</p>
                <p>Email: <a href="mailto:info@statkku.ac.th">info@statkku.ac.th</a></p>
                <p>Phone: <a href="tel:+6612345678">+66-1234-5678</a></p>
                <p>Location: Department of Statistics, Khon Kaen University, Khon Kaen, Thailand.</p>
                <p>Our department is located on the university campus, easily accessible for both visitors and students. Feel free to drop by our office during business hours for more information, or get in touch through email or phone.</p>
                <p>We also have a presence on social media where we share the latest updates, research highlights, and events. Follow us on:</p>

                <p>Our team is happy to assist with any inquiries and provide further details about our department and programs. We look forward to connecting with you!</p>
            </section>

        </main>
        <footer>
            <p>&copy; 2025 Stat KKU. All rights reserved.</p>
        </footer>
    </body>
    </html>

''' 
    
    
@app.route("/contact", methods=['POST', 'GET'])
def contact():

    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Process the data (save to a database, send an email, etc.)
        # For now, just printing the values for demonstration
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Message: {message}")
        
                # Save the data to CSV
        save_to_csv(name, email, message)
        print(f"save {name} {email} {message}")
        
        # After processing the form, you can redirect to a new page to show a success message
        return render_template('contact_success.html', name=name)


    return ''' 

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us - Department of Statistics</title>
    <style>
/* General styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

header {
    background-color: #0078d7;
    color: #fff;
    padding: 10px 0;
    text-align: center;
}

header h1 {
    margin: 0;
}

nav ul {
    list-style: none;
    padding: 0;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: #fff;
    text-decoration: none;
    font-weight: bold;
}

nav ul li a:hover {
    color: #ff0;
}

/* Contact Section */
#contact {
    width: 70%;
    margin: 0 auto;
    background-color: #fff;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    margin-top: 20px;
}

h2 {
    text-align: center;
    color: #333;
}

h3 {
    color: #333;
}

ul {
    list-style: none;
    padding-left: 0;
}

ul li {
    margin-bottom: 10px;
}

ul li a {
    color: #333;
    text-decoration: none;
}

ul li a:hover {
    color: #ff0;
}

/* Form styling */
form {
    margin-top: 20px;
}

form label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

form input[type="text"],
form input[type="email"],
form textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

form input[type="submit"] {
    background-color: #333;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

form input[type="submit"]:hover {
    background-color: #ff0;
    color: #333;
}

/* Footer */
footer {
    background-color: #0078d7;
    color: #fff;
    padding: 10px 0;
    text-align: center;
    margin-top: 20px;
}

footer p {
    margin: 0;
}

/* Responsive Design */
@media (max-width: 768px) {
    #contact {
        width: 90%;
    }
    
    nav ul li {
        display: block;
        margin: 5px 0;
    }
}

    </style>
</head>


<body>

    <header>
        <h1>Contact the Department of Statistics</h1>
        <nav>
            <ul>
                <li><a href="/stathtml">Home</a></li>
                <li><a href="/index">About</a></li>
                <li><a href="/programs">Programs</a></li>
                <li><a href="/research">Research</a></li>
                <li><a href="/contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <section id="contact">
        <h2>Contact Information</h2>
        <p>Feel free to reach out to us for more information or inquiries!</p>

        <h3>Contact Details</h3>
        <ul>
            <li><strong>Email:</strong> <a href="mailto:info@statkku.ac.th">info@statkku.ac.th</a></li>
            <li><strong>Phone:</strong> +66-1234-5678</li>
            <li><strong>Address:</strong> Department of Statistics, Khon Kaen University, Khon Kaen, Thailand</li>
        </ul>

        <h3>Office Hours</h3>
        <p>Our office is open Monday to Friday from 8:30 AM to 5:00 PM.</p>

        <h3>Contact Form</h3>
<form action="/contact" method="POST">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required><br><br>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required><br><br>

    <label for="message">Message:</label><br>
    <textarea id="message" name="message" rows="4" required></textarea><br><br>

    <input type="submit" value="Send Message">
    

    
</form>

    </section>

    <footer>
        <p>&copy; 2025 Department of Statistics, Khon Kaen University. All rights reserved.</p>
    </footer>

</body>

    <script>
        function displayMessage(event) {
            event.preventDefault();  // ป้องกันไม่ให้ส่งฟอร์มและรีเฟรชหน้า
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;

            // แสดงข้อความที่กรอกลงใน HTML
            const output = document.getElementById('output');
            output.innerHTML = `<h3>ข้อมูลที่กรอก:</h3>
                                <p><strong>Name:</strong> ${name}</p>
                                <p><strong>Email:</strong> ${email}</p>
                                <p><strong>Message:</strong> ${message}</p>`;
        }
    </script>
</html>



''' 



##api
@app.route('/simpleAPI', methods=['POST'])
def simpleAPI():
    try:
        # รับข้อมูลจาก request
        payload = request.data.decode("utf-8")
        inmessage = json.loads(payload)

        # แสดงข้อมูลที่ได้รับใน log
        print("\n[INFO] ข้อมูลที่ได้รับจากผู้ใช้:")
        print(f"----------------------------")
        print(f"ข้อความที่ได้รับ: {inmessage.get('msg')}")
        print(f"ผู้ส่ง: {inmessage.get('ผู้ส่ง')}")
        print(f"ผู้รับ: {inmessage.get('ผู้รับ')}")
        print(f"IP ของผู้รับ: {inmessage.get('ip')}")
        print(f"----------------------------\n")

        # สร้างข้อมูลที่ต้องการส่งกลับ
        json_data = json.dumps({'y': 'received!'})

        # ส่งข้อมูลกลับไป
        return json_data, 200  # คืนค่า HTTP Status 200 เพื่อบอกว่า request สำเร็จ

    except Exception as e:
        # ในกรณีเกิดข้อผิดพลาด
        error_message = f"[ERROR] ข้อผิดพลาด: {str(e)}"
        print(error_message)

        # ส่งข้อผิดพลาดกลับไป
        return jsonify({'error': 'เกิดข้อผิดพลาดในการประมวลผลข้อมูล'}), 400



if __name__ == "__main__":   # run code 
    app.run(host='0.0.0.0',debug=True,port=5000)#host='0.0.0.0' = run on internet ,port=5001 #host='0.0.0.0',debug=True,port=5000