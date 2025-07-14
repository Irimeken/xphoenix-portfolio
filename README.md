# xphoenix-portfolio
My personal portfolio built with AWS S3, CloudFront, and Route 53.
# 🌟 xPhoenix Portfolio Website

Welcome to my personal portfolio — built to showcase my work, certifications, and passion for digital innovation and transformation.

This project is a fully responsive, serverless-powered static website designed and developed by **Irimekyen Salome Samuel**.

---

## 🔗 Live Site

> 🌐 Coming Soon – will be deployed on GitHub Pages or a custom domain.

---

## 🧰 Tech Stack

| Frontend | Backend (Contact Form) |
|----------|-------------------------|
| HTML5 + CSS3 | AWS Lambda (Python) |
| Responsive Web Design | AWS API Gateway |
| GitHub Pages (optional) | AWS SES (Simple Email Service) |

---

## 📬 Contact Form (Serverless)

The contact form is powered by a secure, serverless backend using:

- **Amazon API Gateway** – to expose the form submission endpoint
- **AWS Lambda** – to handle the request and send emails via...
- **Amazon SES** – to deliver the message to my inbox

> ✅ CORS-enabled  
> ✅ Rate-limited via API Gateway settings  
> ✅ Successfully tested on deployed version

---

## 🗂️ Folder Structure

```bash
xphoenix-portfolio/
├── index.html
├── about.html
├── certifications.html
├── projects.html
├── contact.html
├── blog.html
└── README.md
