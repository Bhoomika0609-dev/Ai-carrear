# ─────────────────────────────────────────────────────────────────────────────
# data.py  —  CareerCompass AI career dataset
# Contains all 141 career profiles. Import with: from data import data
# To add a new career, append a new dict to the list below.
# ─────────────────────────────────────────────────────────────────────────────

data = [

    # ══════════════════════════════════════════════════════════════════════════
    # TECHNOLOGY
    # ══════════════════════════════════════════════════════════════════════════
    {
        "job_title": "Software Engineer",
        "skills": "python, java, javascript, algorithms, data structures, oop, system design, git, rest api, unit testing, sql, problem solving, design patterns, code review",
        "education": "bachelor", "interests": "coding, software, problem solving, development, systems, technology", "experience": "junior",
        "description": "Designs, develops, tests, and maintains software applications and systems across the full development lifecycle.",
        "salary_min": 85000, "salary_max": 160000, "demand": "Very High", "industry": "Technology",
        "progression": ["Junior Software Engineer", "Software Engineer", "Senior Software Engineer", "Staff Engineer", "Principal Engineer"],
        "certifications": ["AWS Certified Developer", "Oracle Java SE Certification", "Google Cloud Professional Developer"],
        "courses": ["https://www.theodinproject.com", "https://leetcode.com", "https://www.coursera.org/specializations/software-design-architecture"]
    },
    {
        "job_title": "Full Stack Developer",
        "skills": "html, css, javascript, typescript, react, node.js, python, sql, postgresql, mongodb, rest api, git, docker, aws, webpack, responsive design",
        "education": "bachelor", "interests": "web development, frontend, backend, coding, software, full stack, technology", "experience": "mid",
        "description": "Develops both client-side and server-side components of web applications, owning the entire technology stack.",
        "salary_min": 85000, "salary_max": 160000, "demand": "Very High", "industry": "Technology",
        "progression": ["Junior Full Stack Dev", "Full Stack Developer", "Senior Full Stack Dev", "Tech Lead", "CTO"],
        "certifications": ["Meta Full Stack Developer Certificate", "AWS Certified Developer", "MongoDB Professional Developer"],
        "courses": ["https://www.theodinproject.com", "https://fullstackopen.com", "https://www.freecodecamp.org"]
    },
    {
        "job_title": "Frontend Developer",
        "skills": "html, css, javascript, typescript, react, vue, angular, responsive design, sass, webpack, accessibility, performance optimization, figma, ui testing",
        "education": "bachelor", "interests": "web, ui design, coding, user interface, creativity, frontend, browser", "experience": "junior",
        "description": "Builds responsive, performant, and accessible user interfaces for web applications.",
        "salary_min": 70000, "salary_max": 140000, "demand": "Very High", "industry": "Technology",
        "progression": ["Junior Frontend Dev", "Frontend Developer", "Senior Frontend Dev", "Frontend Architect", "VP Engineering"],
        "certifications": ["Meta Frontend Developer", "W3C Accessibility", "Google Web Developer"],
        "courses": ["https://www.freecodecamp.org", "https://javascript.info", "https://web.dev/learn"]
    },
    {
        "job_title": "Backend Developer",
        "skills": "python, java, node.js, go, rest api, graphql, sql, nosql, postgresql, redis, docker, microservices, authentication, caching, message queues, system design",
        "education": "bachelor", "interests": "server architecture, databases, coding, backend, apis, scalability, performance", "experience": "mid",
        "description": "Develops server-side logic, databases, and APIs that power applications and handle business logic.",
        "salary_min": 80000, "salary_max": 155000, "demand": "Very High", "industry": "Technology",
        "progression": ["Junior Backend Dev", "Backend Developer", "Senior Backend Dev", "Backend Architect", "CTO"],
        "certifications": ["AWS Certified Developer", "MongoDB Developer", "Google Cloud Backend"],
        "courses": ["https://roadmap.sh/backend", "https://www.udemy.com/topic/nodejs", "https://www.coursera.org/learn/server-side-javascript"]
    },
    {
        "job_title": "Data Scientist",
        "skills": "python, r, machine learning, deep learning, statistics, pandas, numpy, scikit-learn, sql, data visualization, matplotlib, seaborn, feature engineering, hypothesis testing, jupyter",
        "education": "master", "interests": "data, analytics, research, ai, mathematics, statistics, modeling", "experience": "mid",
        "description": "Analyzes complex datasets, builds predictive models, and extracts actionable insights to drive business decisions.",
        "salary_min": 90000, "salary_max": 155000, "demand": "Very High", "industry": "Technology",
        "progression": ["Junior Data Analyst", "Data Analyst", "Data Scientist", "Senior Data Scientist", "Principal Data Scientist"],
        "certifications": ["Google Professional Data Engineer", "AWS ML Specialty", "Coursera ML Specialization (Andrew Ng)"],
        "courses": ["https://www.coursera.org/specializations/machine-learning-introduction", "https://www.kaggle.com/learn", "https://fast.ai"]
    },
    {
        "job_title": "AI / ML Engineer",
        "skills": "python, tensorflow, pytorch, deep learning, nlp, computer vision, transformers, huggingface, mlops, cuda, model deployment, feature stores, a/b testing, docker, kubernetes",
        "education": "master", "interests": "ai, deep learning, neural networks, research, mathematics, nlp, computer vision", "experience": "senior",
        "description": "Designs, trains, and deploys machine learning models and AI systems at production scale.",
        "salary_min": 130000, "salary_max": 220000, "demand": "Very High", "industry": "Technology",
        "progression": ["ML Engineer", "Senior ML Engineer", "Staff ML Engineer", "Principal Scientist", "AI Research Director"],
        "certifications": ["TensorFlow Developer Certificate", "AWS ML Specialty", "Deep Learning Specialization (deeplearning.ai)"],
        "courses": ["https://www.deeplearning.ai", "https://fast.ai", "https://huggingface.co/learn"]
    },
    {
        "job_title": "Cybersecurity Analyst",
        "skills": "network security, penetration testing, ethical hacking, siem, vulnerability assessment, incident response, cryptography, firewalls, wireshark, metasploit, owasp, nist framework, threat intelligence, python",
        "education": "bachelor", "interests": "security, hacking, networking, risk management, cyber threats, technology, forensics", "experience": "mid",
        "description": "Monitors, detects, and responds to cyber threats to protect an organization's systems and data.",
        "salary_min": 85000, "salary_max": 145000, "demand": "Very High", "industry": "Technology",
        "progression": ["SOC Analyst", "Cybersecurity Analyst", "Security Engineer", "Security Architect", "CISO"],
        "certifications": ["CompTIA Security+", "CISSP", "CEH (Certified Ethical Hacker)", "OSCP"],
        "courses": ["https://tryhackme.com", "https://www.hackthebox.com", "https://www.comptia.org/certifications/security"]
    },
    {
        "job_title": "Cloud Architect",
        "skills": "aws, azure, gcp, kubernetes, docker, terraform, ansible, cloud security, iam, networking, vpc, serverless, lambda, cost optimization, devops, infrastructure as code",
        "education": "bachelor", "interests": "cloud, infrastructure, scalability, architecture, automation, devops, distributed systems", "experience": "senior",
        "description": "Designs and governs cloud computing strategies, architectures, and migration plans for organizations.",
        "salary_min": 120000, "salary_max": 200000, "demand": "Very High", "industry": "Technology",
        "progression": ["Cloud Engineer", "Cloud Architect", "Senior Cloud Architect", "Principal Architect", "VP Engineering"],
        "certifications": ["AWS Solutions Architect Professional", "Azure Solutions Architect Expert", "GCP Professional Cloud Architect"],
        "courses": ["https://aws.amazon.com/training", "https://learn.microsoft.com/azure", "https://cloud.google.com/training"]
    },
    {
        "job_title": "DevOps Engineer",
        "skills": "ci/cd, docker, kubernetes, linux, terraform, ansible, jenkins, github actions, monitoring, prometheus, grafana, bash scripting, python, git, infrastructure as code, log management",
        "education": "bachelor", "interests": "automation, infrastructure, reliability, operations, devops, deployment, monitoring", "experience": "mid",
        "description": "Builds and maintains CI/CD pipelines, automates infrastructure, and ensures reliable software delivery.",
        "salary_min": 95000, "salary_max": 165000, "demand": "Very High", "industry": "Technology",
        "progression": ["Systems Admin", "DevOps Engineer", "Senior DevOps Engineer", "Platform Engineer", "VP Infrastructure"],
        "certifications": ["AWS DevOps Professional", "CKA (Kubernetes Administrator)", "HashiCorp Terraform Associate"],
        "courses": ["https://www.coursera.org/learn/devops-culture-and-mindset", "https://kubernetes.io/training", "https://learn.hashicorp.com/terraform"]
    },
    {
        "job_title": "UX Designer",
        "skills": "figma, user research, wireframing, prototyping, usability testing, information architecture, design thinking, accessibility, interaction design, a/b testing, user journey mapping, persona creation",
        "education": "bachelor", "interests": "design, user experience, psychology, empathy, technology, human behavior, usability", "experience": "mid",
        "description": "Researches user needs and designs intuitive, accessible product experiences that solve real problems.",
        "salary_min": 75000, "salary_max": 135000, "demand": "High", "industry": "Creative",
        "progression": ["UX Researcher", "UX Designer", "Senior UX Designer", "UX Lead", "Head of Design"],
        "certifications": ["Google UX Design Certificate", "Nielsen Norman UX Certification", "Interaction Design Foundation"],
        "courses": ["https://www.coursera.org/professional-certificates/google-ux-design", "https://www.interaction-design.org"]
    },
    {
        "job_title": "Blockchain Developer",
        "skills": "solidity, ethereum, web3.js, ethers.js, smart contracts, hardhat, truffle, ipfs, defi protocols, nft standards, cryptography, javascript, python, consensus algorithms, security auditing",
        "education": "bachelor", "interests": "blockchain, cryptocurrency, decentralization, smart contracts, web3, defi, cryptography", "experience": "mid",
        "description": "Builds decentralized applications, writes smart contracts, and integrates blockchain protocols.",
        "salary_min": 100000, "salary_max": 180000, "demand": "High", "industry": "Technology",
        "progression": ["Junior Blockchain Dev", "Blockchain Developer", "Senior Blockchain Dev", "Blockchain Architect", "Head of Web3 Engineering"],
        "certifications": ["Certified Blockchain Developer (CBA)", "ConsenSys Academy", "Cyfrin Updraft"],
        "courses": ["https://cryptozombies.io", "https://www.cyfrin.io", "https://university.alchemy.com"]
    },
    {
        "job_title": "Mobile App Developer",
        "skills": "swift, kotlin, react native, flutter, dart, ios sdk, android sdk, xcode, firebase, rest api, push notifications, app store deployment, ui/ux mobile, offline storage",
        "education": "bachelor", "interests": "mobile, apps, coding, design, ios, android, user experience", "experience": "junior",
        "description": "Develops native and cross-platform mobile applications for iOS and Android platforms.",
        "salary_min": 80000, "salary_max": 150000, "demand": "High", "industry": "Technology",
        "progression": ["Junior Mobile Dev", "Mobile Developer", "Senior Mobile Dev", "Mobile Lead", "Engineering Manager"],
        "certifications": ["Google Associate Android Developer", "Apple Developer Certification", "Meta React Native"],
        "courses": ["https://developer.apple.com/tutorials", "https://developer.android.com/courses", "https://flutter.dev/learn"]
    },
    {
        "job_title": "QA Engineer",
        "skills": "selenium, cypress, junit, pytest, api testing, postman, jmeter, test planning, bug tracking, jira, test automation, ci/cd integration, regression testing, performance testing",
        "education": "bachelor", "interests": "quality, testing, software reliability, problem solving, attention to detail, automation", "experience": "junior",
        "description": "Designs and executes test strategies to ensure software quality, reliability, and performance.",
        "salary_min": 60000, "salary_max": 115000, "demand": "High", "industry": "Technology",
        "progression": ["QA Tester", "QA Engineer", "Senior QA Engineer", "QA Lead", "QA Manager"],
        "certifications": ["ISTQB Foundation Level", "Selenium Certification", "AWS Certified DevOps"],
        "courses": ["https://testautomationu.applitools.com", "https://www.udemy.com/topic/selenium", "https://www.ministryoftesting.com"]
    },
    {
        "job_title": "Database Administrator",
        "skills": "sql, postgresql, mysql, oracle, mongodb, redis, database design, indexing, query optimization, backup and recovery, replication, high availability, performance tuning, stored procedures",
        "education": "bachelor", "interests": "databases, data management, systems, optimization, administration", "experience": "mid",
        "description": "Designs, implements, and maintains databases ensuring performance, security, and high availability.",
        "salary_min": 75000, "salary_max": 130000, "demand": "High", "industry": "Technology",
        "progression": ["Junior DBA", "Database Administrator", "Senior DBA", "Database Architect", "Head of Data Infrastructure"],
        "certifications": ["Oracle Database Certified Professional", "Microsoft Azure Database Administrator", "MongoDB Certified DBA"],
        "courses": ["https://www.oracle.com/database/technologies/appdev/learnsql.html", "https://www.postgresql.org/docs", "https://learn.microsoft.com/azure/azure-sql"]
    },
    {
        "job_title": "Data Engineer",
        "skills": "python, apache spark, kafka, airflow, dbt, sql, snowflake, bigquery, databricks, etl pipelines, data modeling, parquet, hadoop, stream processing, data warehousing",
        "education": "bachelor", "interests": "data pipelines, engineering, databases, infrastructure, big data, streaming", "experience": "mid",
        "description": "Builds scalable data pipelines and infrastructure to move, transform, and store data reliably.",
        "salary_min": 95000, "salary_max": 160000, "demand": "Very High", "industry": "Technology",
        "progression": ["Junior Data Engineer", "Data Engineer", "Senior Data Engineer", "Data Architect", "Head of Data Engineering"],
        "certifications": ["Google Professional Data Engineer", "Databricks Certified Associate", "Snowflake SnowPro Core"],
        "courses": ["https://www.coursera.org/specializations/data-engineering", "https://www.databricks.com/learn", "https://www.dbtlabs.com/learn"]
    },
    {
        "job_title": "Product Manager",
        "skills": "product strategy, roadmapping, user research, data analysis, agile, stakeholder management, a/b testing, prioritization frameworks, sql, wireframing, go-to-market strategy, okrs",
        "education": "bachelor", "interests": "product development, business strategy, technology, users, innovation, growth", "experience": "mid",
        "description": "Defines product vision, sets priorities, and coordinates cross-functional teams to deliver valuable products.",
        "salary_min": 100000, "salary_max": 175000, "demand": "High", "industry": "Technology",
        "progression": ["Associate PM", "Product Manager", "Senior PM", "Group PM", "CPO"],
        "certifications": ["Pragmatic Institute PMC", "Certified Product Manager (CPM)", "PMP"],
        "courses": ["https://www.productschool.com", "https://www.coursera.org/learn/uva-darden-digital-product-management"]
    },
    {
        "job_title": "Embedded Systems Engineer",
        "skills": "c, c++, rtos, microcontrollers, arm, fpga, assembly, i2c, spi, uart, embedded linux, iot, device drivers, oscilloscope, circuit debugging, memory management",
        "education": "bachelor", "interests": "hardware, electronics, low-level programming, iot, embedded, microcontrollers", "experience": "mid",
        "description": "Develops firmware and low-level software for microcontrollers, IoT devices, and embedded hardware.",
        "salary_min": 85000, "salary_max": 145000, "demand": "High", "industry": "Technology",
        "progression": ["Firmware Engineer", "Embedded Systems Engineer", "Senior Embedded Engineer", "Embedded Architect", "Engineering Director"],
        "certifications": ["ARM Accredited Engineer", "Embedded Systems Certificate (Coursera)", "FreeRTOS Certification"],
        "courses": ["https://www.coursera.org/specializations/embedded-systems", "https://www.edx.org/learn/embedded-systems"]
    },
    {
        "job_title": "AR/VR Developer",
        "skills": "unity, unreal engine, c#, c++, openxr, arcore, arkit, spatial audio, 3d math, shader programming, physics simulation, blender, interaction design, hand tracking, performance optimization",
        "education": "bachelor", "interests": "augmented reality, virtual reality, 3d, immersive experiences, gaming, spatial computing", "experience": "mid",
        "description": "Creates immersive AR and VR experiences for gaming, enterprise, training, and entertainment platforms.",
        "salary_min": 90000, "salary_max": 155000, "demand": "High", "industry": "Technology",
        "progression": ["Junior XR Developer", "AR/VR Developer", "Senior XR Engineer", "XR Lead", "Director of Immersive Tech"],
        "certifications": ["Unity Certified Developer", "Meta Presence Platform", "Apple Vision Pro Development"],
        "courses": ["https://learn.unity.com/pathway/xr-development", "https://developer.meta.com/horizon/documentation"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # DESIGN & CREATIVE
    # ══════════════════════════════════════════════════════════════════════════
    {
        "job_title": "Graphic Designer",
        "skills": "adobe illustrator, photoshop, indesign, typography, color theory, branding, layout design, print design, logo design, visual hierarchy, packaging, mockups",
        "education": "associate", "interests": "art, creativity, visual design, branding, media, aesthetics, print", "experience": "entry",
        "description": "Creates visual concepts for print and digital media including logos, marketing collateral, and brand identities.",
        "salary_min": 45000, "salary_max": 85000, "demand": "Moderate", "industry": "Creative",
        "progression": ["Junior Graphic Designer", "Graphic Designer", "Senior Graphic Designer", "Art Director", "Creative Director"],
        "certifications": ["Adobe Certified Professional", "Canva Design Certification"],
        "courses": ["https://www.coursera.org/learn/graphic-design", "https://www.skillshare.com/browse/graphic-design"]
    },
    {
        "job_title": "Video Editor",
        "skills": "premiere pro, after effects, davinci resolve, final cut pro, color grading, audio mixing, motion graphics, storytelling, timeline editing, visual effects, sound design, export optimization",
        "education": "associate", "interests": "film, video production, storytelling, post-production, media, animation, creativity", "experience": "entry",
        "description": "Edits raw footage into polished video content for film, social media, advertising, and broadcast.",
        "salary_min": 42000, "salary_max": 90000, "demand": "High", "industry": "Creative",
        "progression": ["Junior Editor", "Video Editor", "Senior Editor", "Post-Production Supervisor", "Creative Director"],
        "certifications": ["Adobe Certified Professional – Premiere", "DaVinci Resolve Certification", "Apple Final Cut Pro Certification"],
        "courses": ["https://www.coursera.org/learn/video-editing", "https://www.blackmagicdesign.com/products/davinciresolve/training"]
    },
    {
        "job_title": "Animator",
        "skills": "maya, blender, after effects, rigging, character animation, 3d modeling, keyframing, motion capture, compositing, render pipelines, texture mapping, unity animation",
        "education": "bachelor", "interests": "animation, 3d, art, film, character design, storytelling, creativity, motion", "experience": "junior",
        "description": "Creates 2D and 3D animated content for games, films, advertising, and digital platforms.",
        "salary_min": 50000, "salary_max": 100000, "demand": "Moderate", "industry": "Creative",
        "progression": ["Junior Animator", "Animator", "Senior Animator", "Animation Supervisor", "Animation Director"],
        "certifications": ["Autodesk Maya Certified Professional", "Blender Foundation Certification"],
        "courses": ["https://www.animationmentor.com", "https://www.blender.org/support/tutorials"]
    },
    {
        "job_title": "Content Creator / Influencer",
        "skills": "video production, scriptwriting, social media, tiktok, instagram, youtube, editing, community management, brand partnerships, seo, analytics, storytelling, thumbnails, audience growth",
        "education": "associate", "interests": "content creation, social media, creativity, entertainment, branding, video, community", "experience": "entry",
        "description": "Produces and publishes original digital content across social platforms to grow audiences and monetize through brand deals.",
        "salary_min": 30000, "salary_max": 200000, "demand": "High", "industry": "Creative",
        "progression": ["Micro Influencer", "Content Creator", "Full-time Creator", "Media Brand Owner", "Agency Founder"],
        "certifications": ["YouTube Creator Academy", "Meta Blueprint", "HubSpot Content Marketing"],
        "courses": ["https://creatoracademy.youtube.com", "https://academy.hubspot.com/courses/content-marketing"]
    },
    {
        "job_title": "Fashion Designer",
        "skills": "fashion illustration, pattern making, sewing, clo 3d, adobe illustrator, trend forecasting, fabric selection, draping, garment construction, collection planning, mood boarding",
        "education": "bachelor", "interests": "fashion, art, creativity, textiles, style, trends, apparel, aesthetics", "experience": "junior",
        "description": "Designs apparel and accessories from concept sketch to finished garment, tracking trends and expressing creative vision.",
        "salary_min": 40000, "salary_max": 95000, "demand": "Moderate", "industry": "Creative",
        "progression": ["Design Assistant", "Fashion Designer", "Senior Designer", "Creative Lead", "Creative Director"],
        "certifications": ["FIT Fashion Design Certificate", "CFDA Membership", "CLO 3D Certification"],
        "courses": ["https://www.coursera.org/learn/fashion-design", "https://www.fitnyc.edu/online-courses"]
    },
    {
        "job_title": "Photographer",
        "skills": "photography, lightroom, photoshop, composition, studio lighting, portrait photography, product photography, color correction, photo retouching, camera systems, photo editing",
        "education": "associate", "interests": "photography, art, creativity, visual storytelling, travel, portraits, commercial work", "experience": "entry",
        "description": "Captures and edits professional photographs for commercial, editorial, or artistic purposes.",
        "salary_min": 35000, "salary_max": 85000, "demand": "Moderate", "industry": "Creative",
        "progression": ["Photography Assistant", "Photographer", "Senior Photographer", "Photography Director", "Studio Owner"],
        "certifications": ["Adobe Lightroom Certified", "PPA Certification", "WPPI Certification"],
        "courses": ["https://www.coursera.org/learn/photography-basics", "https://www.kelbyone.com"]
    },
    {
        "job_title": "Interior Designer",
        "skills": "space planning, autocad, sketchup, 3ds max, revit, color theory, material selection, lighting design, client consultation, furniture specification, mood boarding, building codes",
        "education": "bachelor", "interests": "interior design, architecture, art, aesthetics, creativity, spaces, styling", "experience": "junior",
        "description": "Plans and designs functional, safe, and visually appealing interior spaces for residential and commercial clients.",
        "salary_min": 45000, "salary_max": 90000, "demand": "Moderate", "industry": "Creative",
        "progression": ["Design Assistant", "Junior Interior Designer", "Interior Designer", "Senior Designer", "Principal Designer"],
        "certifications": ["NCIDQ Certification", "LEED AP Interior Design", "ASID Professional Member"],
        "courses": ["https://www.coursera.org/learn/interior-design", "https://www.nkba.org/education"]
    },
    {
        "job_title": "Music Producer",
        "skills": "ableton live, logic pro, fl studio, mixing, mastering, music theory, sound design, midi programming, audio engineering, vocal production, sample libraries, arrangement",
        "education": "associate", "interests": "music, audio production, creativity, sound design, recording, beatmaking, entertainment", "experience": "mid",
        "description": "Composes, records, arranges, and produces music tracks for artists, films, and commercial clients.",
        "salary_min": 38000, "salary_max": 120000, "demand": "Moderate", "industry": "Creative",
        "progression": ["Studio Assistant", "Music Producer", "Senior Producer", "Executive Producer", "Label Head"],
        "certifications": ["Berklee Online Music Production", "Ableton Certified Trainer", "AES Membership"],
        "courses": ["https://www.berklee.edu/online", "https://www.ableton.com/en/packs"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # BUSINESS & MANAGEMENT
    # ══════════════════════════════════════════════════════════════════════════
    {
        "job_title": "Project Manager",
        "skills": "project planning, agile, scrum, kanban, risk management, stakeholder communication, ms project, jira, budgeting, resource allocation, change management, pmp methodology, scope management",
        "education": "bachelor", "interests": "management, planning, leadership, coordination, organization, teamwork, delivery", "experience": "senior",
        "description": "Leads projects from initiation to closure, ensuring delivery on time, within budget, and to specification.",
        "salary_min": 80000, "salary_max": 140000, "demand": "High", "industry": "Business",
        "progression": ["Project Coordinator", "Project Manager", "Senior PM", "Program Manager", "VP of Operations"],
        "certifications": ["PMP (Project Management Professional)", "CAPM", "CSM (Certified Scrum Master)", "PRINCE2"],
        "courses": ["https://www.pmi.org", "https://www.coursera.org/learn/project-management-foundations"]
    },
    {
        "job_title": "Business Analyst",
        "skills": "requirements elicitation, use case writing, sql, data analysis, process mapping, bpmn, visio, stakeholder interviews, gap analysis, user stories, excel, functional specification",
        "education": "bachelor", "interests": "business processes, data, problem solving, strategy, systems analysis, requirements", "experience": "junior",
        "description": "Bridges business and IT by gathering requirements, analyzing processes, and defining solutions.",
        "salary_min": 60000, "salary_max": 105000, "demand": "High", "industry": "Business",
        "progression": ["Junior BA", "Business Analyst", "Senior Business Analyst", "Business Architect", "VP Strategy"],
        "certifications": ["CBAP (Certified Business Analysis Professional)", "PMI-PBA", "ECBA"],
        "courses": ["https://www.iiba.org", "https://www.coursera.org/learn/business-analysis-fundamentals"]
    },
    {
        "job_title": "Operations Manager",
        "skills": "operations management, process improvement, lean, six sigma, kpi tracking, supply chain, team management, budgeting, erp, vendor management, sop development, capacity planning",
        "education": "bachelor", "interests": "operations, efficiency, management, process optimization, logistics, leadership", "experience": "senior",
        "description": "Oversees daily business operations to drive efficiency, reduce costs, and improve quality.",
        "salary_min": 75000, "salary_max": 130000, "demand": "High", "industry": "Business",
        "progression": ["Operations Coordinator", "Operations Manager", "Sr. Operations Manager", "VP of Operations", "COO"],
        "certifications": ["Lean Six Sigma Black Belt", "PMP", "Certified Operations Manager (COM)"],
        "courses": ["https://www.coursera.org/learn/operations-management", "https://www.isixsigma.com"]
    },
    {
        "job_title": "Management Consultant",
        "skills": "strategy, problem structuring, data analysis, financial modeling, excel, powerpoint, client management, business case development, benchmarking, hypothesis-driven analysis, stakeholder management",
        "education": "master", "interests": "strategy, business, consulting, economics, analysis, problem solving, corporate performance", "experience": "mid",
        "description": "Advises senior leaders on strategy, operations, and transformation to improve organizational performance.",
        "salary_min": 90000, "salary_max": 180000, "demand": "High", "industry": "Business",
        "progression": ["Business Analyst", "Consultant", "Senior Consultant", "Manager", "Partner"],
        "certifications": ["CMC (Certified Management Consultant)", "MBA", "PMP"],
        "courses": ["https://www.coursera.org/learn/strategy-business", "https://www.mbacrystalball.com/consulting"]
    },
    {
        "job_title": "Human Resources Manager",
        "skills": "recruitment, talent acquisition, employee relations, performance management, compensation, hris, onboarding, hr policy, training and development, labor law, conflict resolution, payroll",
        "education": "bachelor", "interests": "people management, organizational culture, leadership, psychology, talent, wellbeing", "experience": "mid",
        "description": "Manages the full employee lifecycle including hiring, development, performance, and retention.",
        "salary_min": 65000, "salary_max": 120000, "demand": "High", "industry": "Business",
        "progression": ["HR Coordinator", "HR Generalist", "HR Manager", "HR Director", "Chief People Officer"],
        "certifications": ["SHRM-CP", "PHR (Professional in Human Resources)", "HRCI Certification"],
        "courses": ["https://www.shrm.org/certification", "https://www.coursera.org/learn/managing-human-resources"]
    },
    {
        "job_title": "Supply Chain Manager",
        "skills": "procurement, inventory management, logistics, supplier relationship management, sap, demand forecasting, lean, six sigma, trade compliance, erp, contract negotiation, warehouse management",
        "education": "bachelor", "interests": "logistics, operations, global trade, supply chain, efficiency, procurement, planning", "experience": "senior",
        "description": "Manages the end-to-end supply chain including procurement, logistics, inventory, and supplier relationships.",
        "salary_min": 80000, "salary_max": 140000, "demand": "High", "industry": "Business",
        "progression": ["Supply Chain Analyst", "Logistics Coordinator", "Supply Chain Manager", "Director of Supply Chain", "VP Operations"],
        "certifications": ["CSCP (APICS)", "CPIM", "Six Sigma Green Belt", "CLTD"],
        "courses": ["https://www.apics.org", "https://www.coursera.org/learn/supply-chain-logistics"]
    },
    {
        "job_title": "Entrepreneur / Startup Founder",
        "skills": "business model design, fundraising, pitch decks, product development, marketing, team building, financial modeling, customer discovery, agile, networking, problem solving, go-to-market",
        "education": "bachelor", "interests": "startups, innovation, business building, risk taking, technology, disruption, leadership", "experience": "senior",
        "description": "Conceives, launches, and scales new ventures through product development, team building, and fundraising.",
        "salary_min": 0, "salary_max": 500000, "demand": "High", "industry": "Business",
        "progression": ["Idea Stage", "Pre-Seed Startup", "Seed Stage", "Series A", "Scaling / Exit"],
        "certifications": ["Y Combinator Fellowship", "Founder Institute Program", "SBA Entrepreneurship"],
        "courses": ["https://www.ycombinator.com/library", "https://www.startupschool.org"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # FINANCE & ACCOUNTING
    # ══════════════════════════════════════════════════════════════════════════
    {
        "job_title": "Financial Analyst",
        "skills": "financial modeling, dcf valuation, excel, bloomberg terminal, sql, financial statement analysis, variance analysis, budgeting, forecasting, powerpoint, equity research",
        "education": "bachelor", "interests": "finance, investment, markets, economics, data analysis, valuation, strategy", "experience": "junior",
        "description": "Analyzes financial data and builds models to guide investment, budgeting, and strategic decisions.",
        "salary_min": 65000, "salary_max": 120000, "demand": "High", "industry": "Finance",
        "progression": ["Financial Analyst", "Senior Analyst", "Finance Manager", "Director of Finance", "CFO"],
        "certifications": ["CFA (Chartered Financial Analyst)", "CPA", "FRM", "CFP"],
        "courses": ["https://www.cfainstitute.org", "https://corporatefinanceinstitute.com"]
    },
    {
        "job_title": "Accountant",
        "skills": "gaap, ifrs, tax preparation, financial reporting, quickbooks, excel, accounts payable, accounts receivable, reconciliation, auditing, bookkeeping, payroll, cost accounting",
        "education": "bachelor", "interests": "accounting, finance, numbers, compliance, tax, business, reporting", "experience": "junior",
        "description": "Maintains financial records, prepares reports, ensures compliance, and supports tax and audit functions.",
        "salary_min": 52000, "salary_max": 95000, "demand": "High", "industry": "Finance",
        "progression": ["Staff Accountant", "Senior Accountant", "Accounting Manager", "Controller", "CFO"],
        "certifications": ["CPA (Certified Public Accountant)", "CMA", "Enrolled Agent (EA)"],
        "courses": ["https://www.aicpa.org", "https://quickbooks.intuit.com/training"]
    },
    {
        "job_title": "Investment Banker",
        "skills": "financial modeling, lbo modeling, m&a analysis, dcf, comparable company analysis, capital markets, pitch books, bloomberg, excel, powerpoint, due diligence, ipo process",
        "education": "master", "interests": "finance, investment, mergers and acquisitions, capital markets, economics, deals, strategy", "experience": "junior",
        "description": "Advises corporations on mergers, acquisitions, IPOs, and capital raising in financial markets.",
        "salary_min": 100000, "salary_max": 300000, "demand": "Moderate", "industry": "Finance",
        "progression": ["Analyst", "Associate", "Vice President", "Director", "Managing Director"],
        "certifications": ["CFA", "Series 7", "Series 63", "MBA (Finance)"],
        "courses": ["https://www.wallstreetprep.com", "https://corporatefinanceinstitute.com"]
    },
    {
        "job_title": "Auditor",
        "skills": "internal audit, external audit, gaap, ifrs, risk assessment, internal controls, sox compliance, excel, audit software, financial analysis, fraud detection, report writing, regulatory compliance",
        "education": "bachelor", "interests": "compliance, finance, accounting, risk, business controls, law, investigation", "experience": "junior",
        "description": "Examines financial records and internal controls to ensure accuracy, legal compliance, and detect fraud.",
        "salary_min": 55000, "salary_max": 100000, "demand": "High", "industry": "Finance",
        "progression": ["Junior Auditor", "Staff Auditor", "Senior Auditor", "Audit Manager", "Partner"],
        "certifications": ["CPA", "CIA (Certified Internal Auditor)", "CISA", "CFE (Certified Fraud Examiner)"],
        "courses": ["https://www.aicpa.org", "https://www.theiia.org/en/learning/courses"]
    },
    {
        "job_title": "Risk Analyst",
        "skills": "risk management, value at risk (var), stress testing, financial modeling, python, r, regulatory compliance, credit risk, market risk, scenario analysis, excel, data analysis",
        "education": "bachelor", "interests": "risk, finance, mathematics, compliance, modeling, economics, statistics", "experience": "junior",
        "description": "Identifies, quantifies, and models financial and operational risks for organizations and financial institutions.",
        "salary_min": 65000, "salary_max": 115000, "demand": "High", "industry": "Finance",
        "progression": ["Risk Analyst", "Senior Risk Analyst", "Risk Manager", "Head of Risk", "Chief Risk Officer"],
        "certifications": ["FRM (Financial Risk Manager)", "PRM", "CFA", "CPA"],
        "courses": ["https://www.garp.org/frm", "https://www.coursera.org/learn/financial-risk-management"]
    },
    {
        "job_title": "Insurance Actuary",
        "skills": "actuarial mathematics, probability, statistics, excel, r, python, life tables, reserving, pricing models, solvency ii, regulatory reporting, risk modeling, exam preparation",
        "education": "bachelor", "interests": "mathematics, statistics, insurance, risk modeling, finance, probability", "experience": "junior",
        "description": "Uses mathematical models to assess financial risk for insurance companies, pension funds, and financial institutions.",
        "salary_min": 70000, "salary_max": 150000, "demand": "High", "industry": "Finance",
        "progression": ["Actuarial Analyst", "Associate Actuary", "Actuary", "Senior Actuary", "Chief Actuary"],
        "certifications": ["ASA (SOA)", "ACAS (CAS)", "FSA", "FCAS"],
        "courses": ["https://www.soa.org/education", "https://www.beanactuary.org"]
    },
    {
        "job_title": "Cryptocurrency Trader / Analyst",
        "skills": "technical analysis, on-chain analysis, defi protocols, risk management, python, trading strategies, derivatives, options, crypto research, tokenomics, portfolio management",
        "education": "bachelor", "interests": "cryptocurrency, blockchain, trading, markets, defi, finance, technology", "experience": "mid",
        "description": "Analyzes digital asset markets and executes trades using technical and fundamental crypto analysis.",
        "salary_min": 60000, "salary_max": 250000, "demand": "Moderate", "industry": "Finance",
        "progression": ["Crypto Researcher", "Crypto Analyst", "Senior Trader", "Portfolio Manager", "Head of Trading"],
        "certifications": ["Certified Cryptocurrency Expert", "CFA", "FRM"],
        "courses": ["https://www.coursera.org/learn/cryptocurrency", "https://academy.binance.com"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # HEALTHCARE
    # ══════════════════════════════════════════════════════════════════════════
    {
        "job_title": "Doctor / Physician",
        "skills": "clinical diagnosis, patient history taking, physical examination, pharmacology, differential diagnosis, ehr documentation, procedures, evidence-based medicine, patient communication, medical ethics",
        "education": "phd", "interests": "medicine, science, biology, patient care, diagnosis, helping others, research", "experience": "senior",
        "description": "Diagnoses and treats a wide range of medical conditions, providing comprehensive patient care.",
        "salary_min": 180000, "salary_max": 400000, "demand": "Very High", "industry": "Healthcare",
        "progression": ["Medical Student", "Intern", "Resident", "Attending Physician", "Department Chief"],
        "certifications": ["MD / DO License", "Board Certification (specialty)", "DEA License", "BLS/ACLS/ATLS"],
        "courses": ["https://www.ama-assn.org", "https://www.nejm.org/medical-education"]
    },
    {
        "job_title": "Nurse Practitioner",
        "skills": "advanced patient assessment, diagnosis, pharmacology, prescribing authority, ehr, clinical procedures, health education, chronic disease management, physical exam, critical care",
        "education": "master", "interests": "healthcare, patient care, medicine, science, helping others, nursing", "experience": "senior",
        "description": "Provides advanced nursing care including diagnosis, prescribing, and disease management.",
        "salary_min": 105000, "salary_max": 160000, "demand": "Very High", "industry": "Healthcare",
        "progression": ["Registered Nurse", "Charge Nurse", "Nurse Practitioner", "Senior NP", "Director of Nursing"],
        "certifications": ["ANCC FNP-BC", "AANP Certification", "BLS/ACLS"],
        "courses": ["https://www.aanp.org", "https://www.nursingworld.org"]
    },
    {
        "job_title": "Pharmacist",
        "skills": "pharmacology, drug interaction checking, dispensing, patient counseling, medication therapy management, compounding, clinical pharmacy, ehr, formulary management, inventory control",
        "education": "phd", "interests": "medicine, chemistry, patient care, drug therapy, science, healthcare", "experience": "mid",
        "description": "Dispenses medications, counsels patients, and ensures the safe and effective use of pharmaceutical therapy.",
        "salary_min": 110000, "salary_max": 150000, "demand": "High", "industry": "Healthcare",
        "progression": ["Pharmacy Intern", "Staff Pharmacist", "Clinical Pharmacist", "Pharmacy Manager", "Chief Pharmacy Officer"],
        "certifications": ["PharmD License", "Board of Pharmacy Specialties (BPS)", "BCPS"],
        "courses": ["https://www.pharmacist.com", "https://www.ashp.org"]
    },
    {
        "job_title": "Medical Researcher",
        "skills": "experimental design, clinical trials, statistical analysis, r, python, scientific writing, grant writing, literature review, irb compliance, gcp, lab techniques, data interpretation",
        "education": "phd", "interests": "medical research, science, biology, discovery, data, clinical trials, drug development", "experience": "mid",
        "description": "Conducts clinical and laboratory research to develop new treatments, drugs, and medical knowledge.",
        "salary_min": 75000, "salary_max": 140000, "demand": "High", "industry": "Healthcare",
        "progression": ["Research Assistant", "Research Associate", "Medical Researcher", "Principal Investigator", "Research Director"],
        "certifications": ["GCP Certification", "IRB Training", "ACRP Clinical Research Associate"],
        "courses": ["https://www.clinicaltrials.gov/education", "https://www.coursera.org/learn/clinical-trials"]
    },
    {
        "job_title": "Telemedicine Specialist",
        "skills": "telemedicine platforms, remote patient assessment, ehr, digital health tools, hipaa compliance, patient communication, virtual diagnosis, remote monitoring, clinical protocols",
        "education": "master", "interests": "healthcare technology, digital health, remote care, patient communication, innovation, medicine", "experience": "mid",
        "description": "Provides clinical healthcare services remotely using telemedicine platforms and digital tools.",
        "salary_min": 70000, "salary_max": 130000, "demand": "Very High", "industry": "Healthcare",
        "progression": ["Telehealth Nurse", "Telemedicine Clinician", "Senior Telemedicine Specialist", "Telehealth Director", "VP Digital Health"],
        "certifications": ["ATA Telemedicine Certification", "ANCC Telehealth", "State Medical License"],
        "courses": ["https://www.americantelemed.org", "https://www.coursera.org/learn/digital-health"]
    },
    {
        "job_title": "Healthcare Administrator",
        "skills": "healthcare operations, budgeting, hipaa compliance, ehr systems, staff management, quality improvement, patient experience, regulatory compliance, strategic planning, revenue cycle",
        "education": "master", "interests": "healthcare management, operations, policy, administration, helping others, leadership", "experience": "senior",
        "description": "Manages healthcare facility operations, staff, budgets, and regulatory compliance to deliver quality care.",
        "salary_min": 75000, "salary_max": 130000, "demand": "High", "industry": "Healthcare",
        "progression": ["Admin Coordinator", "Department Manager", "Healthcare Administrator", "VP Healthcare Operations", "CEO"],
        "certifications": ["FACHE", "CPHQ", "ACHE Fellowship"],
        "courses": ["https://www.ache.org", "https://www.coursera.org/learn/healthcare-organization-operations"]
    },
    {
        "job_title": "Physical Therapist",
        "skills": "musculoskeletal assessment, rehabilitation, manual therapy, therapeutic exercise, gait analysis, electrotherapy, patient education, documentation, anatomy, post-surgical rehab",
        "education": "master", "interests": "healthcare, rehabilitation, fitness, anatomy, movement, helping others, sports medicine", "experience": "mid",
        "description": "Helps patients recover movement, strength, and function through evidence-based physical rehabilitation.",
        "salary_min": 75000, "salary_max": 110000, "demand": "Very High", "industry": "Healthcare",
        "progression": ["PT Aide", "Physical Therapist", "Senior PT", "Clinical Specialist", "PT Director"],
        "certifications": ["DPT License", "OCS Board Certification", "NSCA-CSCS"],
        "courses": ["https://www.apta.org", "https://www.coursera.org/learn/physical-therapy"]
    },
    {
        "job_title": "Mental Health Counselor",
        "skills": "cognitive behavioral therapy, motivational interviewing, active listening, crisis intervention, treatment planning, diagnostic assessment, dsmv, group therapy, case notes, empathy",
        "education": "master", "interests": "psychology, mental health, counseling, therapy, helping others, wellbeing, human behavior", "experience": "mid",
        "description": "Provides therapeutic counseling to individuals and groups dealing with mental health and emotional challenges.",
        "salary_min": 50000, "salary_max": 90000, "demand": "Very High", "industry": "Healthcare",
        "progression": ["Counseling Intern", "Mental Health Counselor", "Licensed Counselor", "Senior Therapist", "Clinical Director"],
        "certifications": ["LPC", "LMHC", "LCSW", "NCC"],
        "courses": ["https://www.counseling.org", "https://www.nbcc.org"]
    },
    {
        "job_title": "Biomedical Engineer",
        "skills": "medical device design, fda regulatory, matlab, cad, signal processing, biomechanics, biocompatibility testing, clinical trials, iso 13485, prototyping, labview",
        "education": "bachelor", "interests": "healthcare, engineering, biology, medical devices, innovation, science, R&D", "experience": "mid",
        "description": "Designs and develops medical devices and equipment to improve patient care and clinical outcomes.",
        "salary_min": 70000, "salary_max": 125000, "demand": "High", "industry": "Healthcare",
        "progression": ["Junior BME", "Biomedical Engineer", "Senior BME", "R&D Lead", "Engineering Director"],
        "certifications": ["PE License", "CBET", "RAC (Regulatory Affairs Certification)"],
        "courses": ["https://www.bmes.org", "https://www.coursera.org/learn/biomedical-engineering"]
    },
    {
        "job_title": "Medical Laboratory Technician",
        "skills": "specimen analysis, hematology, microbiology, clinical chemistry, urinalysis, blood banking, lab equipment operation, quality control, safety protocols, microscopy",
        "education": "associate", "interests": "science, biology, healthcare, laboratory work, diagnostics, medicine", "experience": "entry",
        "description": "Performs diagnostic laboratory tests on blood, tissue, and other specimens to assist in patient diagnosis.",
        "salary_min": 45000, "salary_max": 75000, "demand": "High", "industry": "Healthcare",
        "progression": ["Lab Assistant", "MLT", "Medical Laboratory Technologist", "Lab Supervisor", "Lab Director"],
        "certifications": ["ASCP MLT Certification", "AMT MLT", "NCA Certification"],
        "courses": ["https://www.ascp.org", "https://www.amt1.com"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # ENGINEERING
    # ══════════════════════════════════════════════════════════════════════════
    {
        "job_title": "Mechanical Engineer",
        "skills": "solidworks, autocad, fea analysis, thermodynamics, fluid mechanics, gd&t, manufacturing processes, prototyping, matlab, material science, tolerance analysis, product design",
        "education": "bachelor", "interests": "engineering, mechanics, design, physics, manufacturing, product development", "experience": "mid",
        "description": "Designs, analyzes, and develops mechanical systems and products from concept through manufacturing.",
        "salary_min": 72000, "salary_max": 120000, "demand": "Moderate", "industry": "Engineering",
        "progression": ["Junior ME", "Mechanical Engineer", "Senior ME", "Lead Engineer", "Engineering Manager"],
        "certifications": ["PE License", "SolidWorks Certified Professional", "Six Sigma Green Belt"],
        "courses": ["https://www.coursera.org/learn/mechanics-of-materials", "https://www.edx.org/learn/mechanical-engineering"]
    },
    {
        "job_title": "Civil Engineer",
        "skills": "autocad, revit, structural analysis, geotechnical engineering, surveying, hydraulics, traffic engineering, cost estimation, construction management, building codes, site planning",
        "education": "bachelor", "interests": "construction, infrastructure, design, environment, public works, structures", "experience": "mid",
        "description": "Designs and supervises construction of infrastructure including roads, bridges, dams, and buildings.",
        "salary_min": 68000, "salary_max": 115000, "demand": "Moderate", "industry": "Engineering",
        "progression": ["EIT", "Civil Engineer", "Senior Civil Engineer", "Project Engineer", "VP Engineering"],
        "certifications": ["PE License (Civil)", "PMP", "LEED AP", "ASCE Membership"],
        "courses": ["https://www.coursera.org/learn/civil-engineering", "https://www.asce.org/education"]
    },
    {
        "job_title": "Electrical Engineer",
        "skills": "circuit design, pcb layout, power systems, matlab, simulink, plc programming, signal processing, embedded systems, autocad electrical, protection relay, testing and commissioning",
        "education": "bachelor", "interests": "electronics, electrical systems, physics, energy, circuits, power, technology", "experience": "mid",
        "description": "Designs and tests electrical systems, circuits, and power distribution networks.",
        "salary_min": 75000, "salary_max": 130000, "demand": "High", "industry": "Engineering",
        "progression": ["EIT", "Electrical Engineer", "Senior EE", "Lead Electrical Engineer", "Chief Electrical Officer"],
        "certifications": ["PE License (Electrical)", "IEEE Certification", "Six Sigma"],
        "courses": ["https://www.coursera.org/learn/electrical-engineering", "https://www.edx.org/learn/electrical-engineering"]
    },
    {
        "job_title": "Robotics Engineer",
        "skills": "ros, ros2, python, c++, computer vision, lidar, sensor fusion, kinematics, motion planning, control systems, matlab, simulink, gazebo simulation, robot operating systems",
        "education": "master", "interests": "robotics, automation, ai, engineering, control systems, electronics, manufacturing", "experience": "mid",
        "description": "Designs, builds, and programs robotic systems for industrial automation and intelligent applications.",
        "salary_min": 90000, "salary_max": 155000, "demand": "High", "industry": "Engineering",
        "progression": ["Robotics Technician", "Robotics Engineer", "Senior Robotics Engineer", "Robotics Lead", "Director of Robotics"],
        "certifications": ["ROS Certification", "IEEE Robotics", "Fanuc Certified Robot Technician"],
        "courses": ["https://www.coursera.org/learn/robotics", "https://www.ros.org/blog/getting-started"]
    },
    {
        "job_title": "Chemical Engineer",
        "skills": "process simulation, aspen plus, thermodynamics, reaction kinetics, mass transfer, heat transfer, process safety, p&id, matlab, quality control, six sigma, chemical plant operations",
        "education": "bachelor", "interests": "chemistry, engineering, manufacturing, energy, pharmaceuticals, process design", "experience": "mid",
        "description": "Designs and optimizes chemical processes for manufacturing, energy, pharmaceutical, and materials industries.",
        "salary_min": 75000, "salary_max": 130000, "demand": "Moderate", "industry": "Engineering",
        "progression": ["Process Engineer", "Chemical Engineer", "Senior CE", "Lead Process Engineer", "Plant Director"],
        "certifications": ["PE License (Chemical)", "Six Sigma", "OSHA PSM Certification"],
        "courses": ["https://www.aiche.org", "https://www.coursera.org/learn/chemical-engineering"]
    },
    {
        "job_title": "Architect",
        "skills": "autocad, revit, sketchup, bim, architectural design, building codes, sustainability, space planning, construction documentation, client presentations, urban planning, leed",
        "education": "master", "interests": "design, architecture, construction, art, sustainability, urban planning, spaces", "experience": "mid",
        "description": "Designs functional, safe, and aesthetically compelling buildings and structures.",
        "salary_min": 70000, "salary_max": 130000, "demand": "Moderate", "industry": "Engineering",
        "progression": ["Architectural Intern", "Architect", "Project Architect", "Principal Architect", "Partner"],
        "certifications": ["ARE (Architect Registration Exam)", "LEED AP BD+C", "AIA Membership"],
        "courses": ["https://www.ncarb.org", "https://www.coursera.org/learn/modern-architecture"]
    },
    {
        "job_title": "Petroleum Engineer",
        "skills": "reservoir simulation, petrel, eclipse, well logging, drilling engineering, production optimization, petrophysics, fluid mechanics, pressure transient analysis, field development planning",
        "education": "bachelor", "interests": "energy, geology, engineering, oil and gas, subsurface, petroleum, physics", "experience": "mid",
        "description": "Develops methods to extract oil and gas from reservoirs efficiently, safely, and economically.",
        "salary_min": 100000, "salary_max": 175000, "demand": "Moderate", "industry": "Engineering",
        "progression": ["Junior PE", "Petroleum Engineer", "Senior PE", "Reservoir Engineer", "Engineering Director"],
        "certifications": ["PE License (Petroleum)", "SPE Membership", "SPWLA"],
        "courses": ["https://www.spe.org/en/education", "https://www.coursera.org/learn/petroleum-engineering"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # MARKETING & SALES
    # ══════════════════════════════════════════════════════════════════════════
    {
        "job_title": "Marketing Specialist",
        "skills": "marketing campaigns, google analytics, email marketing, content creation, seo, social media, hubspot, crm, marketing automation, audience segmentation, copywriting",
        "education": "bachelor", "interests": "marketing, branding, communication, digital media, consumer behavior, campaigns", "experience": "mid",
        "description": "Plans and executes integrated marketing campaigns across digital and traditional channels.",
        "salary_min": 50000, "salary_max": 95000, "demand": "High", "industry": "Marketing",
        "progression": ["Marketing Coordinator", "Marketing Specialist", "Marketing Manager", "Marketing Director", "CMO"],
        "certifications": ["Google Analytics Certification", "HubSpot Marketing Hub", "Meta Blueprint"],
        "courses": ["https://academy.hubspot.com", "https://skillshop.google.com"]
    },
    {
        "job_title": "Digital Marketing Manager",
        "skills": "google ads, facebook ads, seo, sem, ppc, email marketing, marketing analytics, conversion rate optimization, landing pages, a/b testing, crm, marketing automation, content strategy",
        "education": "bachelor", "interests": "digital marketing, advertising, analytics, performance marketing, growth hacking, social media", "experience": "mid",
        "description": "Manages digital advertising, SEO, and performance marketing to drive online growth and conversions.",
        "salary_min": 65000, "salary_max": 120000, "demand": "High", "industry": "Marketing",
        "progression": ["Digital Marketing Specialist", "Digital Marketing Manager", "Senior Digital Manager", "Head of Digital", "CMO"],
        "certifications": ["Google Ads Certified", "Facebook Blueprint", "HubSpot Digital Marketing"],
        "courses": ["https://skillshop.google.com", "https://academy.hubspot.com"]
    },
    {
        "job_title": "SEO Specialist",
        "skills": "on-page seo, technical seo, link building, keyword research, google search console, google analytics, semrush, ahrefs, content strategy, core web vitals, schema markup",
        "education": "bachelor", "interests": "search engines, digital marketing, analytics, content, organic growth, data", "experience": "junior",
        "description": "Optimizes websites to rank higher in search engines and drive sustainable organic traffic.",
        "salary_min": 45000, "salary_max": 90000, "demand": "High", "industry": "Marketing",
        "progression": ["SEO Analyst", "SEO Specialist", "Senior SEO Specialist", "SEO Manager", "Head of SEO"],
        "certifications": ["Google Analytics Certification", "SEMrush SEO Toolkit Exam", "HubSpot SEO Certification"],
        "courses": ["https://ahrefs.com/academy", "https://www.coursera.org/learn/seo"]
    },
    {
        "job_title": "Brand Manager",
        "skills": "brand strategy, consumer research, market positioning, competitive analysis, campaign management, creative briefing, brand guidelines, analytics, social media, p&l management",
        "education": "bachelor", "interests": "branding, marketing, creative strategy, consumer psychology, business, advertising", "experience": "mid",
        "description": "Develops and protects brand identity, overseeing all communications to ensure consistent messaging.",
        "salary_min": 65000, "salary_max": 120000, "demand": "High", "industry": "Marketing",
        "progression": ["Brand Coordinator", "Brand Specialist", "Brand Manager", "Senior Brand Manager", "VP of Marketing"],
        "certifications": ["AMA PCM", "HubSpot Brand Strategy", "Google Analytics"],
        "courses": ["https://www.coursera.org/learn/brand-management", "https://academy.hubspot.com"]
    },
    {
        "job_title": "Public Relations Specialist",
        "skills": "media relations, press releases, crisis communication, pitching journalists, event management, social media, writing, editing, stakeholder communication, brand reputation",
        "education": "bachelor", "interests": "communication, media, public affairs, writing, relationships, branding, journalism", "experience": "junior",
        "description": "Manages an organization's public image and cultivates relationships with media and key stakeholders.",
        "salary_min": 45000, "salary_max": 90000, "demand": "Moderate", "industry": "Marketing",
        "progression": ["PR Assistant", "PR Specialist", "PR Manager", "Communications Director", "VP Communications"],
        "certifications": ["APR (Accredited in Public Relations)", "PRSA Membership"],
        "courses": ["https://www.prsa.org", "https://www.coursera.org/learn/public-relations"]
    },
    {
        "job_title": "Social Media Manager",
        "skills": "instagram, tiktok, twitter/x, linkedin, youtube, content calendar, community management, analytics, video editing, copywriting, paid social, influencer partnerships, social listening",
        "education": "bachelor", "interests": "social media, content creation, community, trends, branding, video, engagement", "experience": "entry",
        "description": "Manages a brand's social presence through content creation, community engagement, and analytics.",
        "salary_min": 40000, "salary_max": 80000, "demand": "High", "industry": "Marketing",
        "progression": ["Social Media Coordinator", "Social Media Manager", "Social Media Strategist", "Head of Social Media", "CMO"],
        "certifications": ["Meta Blueprint", "HubSpot Social Media Certification", "Hootsuite Social Marketing"],
        "courses": ["https://www.coursera.org/learn/social-media-marketing", "https://academy.hubspot.com/courses/social-media"]
    },
    {
        "job_title": "Content Writer",
        "skills": "long-form writing, seo writing, copywriting, editing, proofreading, research, wordpress, content strategy, storytelling, grammar, headline writing, content briefs",
        "education": "bachelor", "interests": "writing, storytelling, media, communication, creativity, language, journalism", "experience": "entry",
        "description": "Writes engaging, SEO-optimized content for blogs, websites, and digital marketing campaigns.",
        "salary_min": 38000, "salary_max": 75000, "demand": "Moderate", "industry": "Marketing",
        "progression": ["Junior Content Writer", "Content Writer", "Content Strategist", "Content Manager", "Head of Content"],
        "certifications": ["HubSpot Content Marketing", "Google Analytics", "Semrush Content Marketing"],
        "courses": ["https://academy.hubspot.com/courses/content-marketing", "https://www.udemy.com/topic/copywriting/"]
    },
    {
        "job_title": "Sales Representative",
        "skills": "prospecting, cold calling, sales presentations, crm (salesforce), objection handling, negotiation, pipeline management, closing techniques, b2b sales, relationship building",
        "education": "associate", "interests": "sales, communication, business, relationships, competition, persuasion", "experience": "entry",
        "description": "Identifies and develops new business by prospecting leads, pitching solutions, and closing deals.",
        "salary_min": 45000, "salary_max": 110000, "demand": "High", "industry": "Sales",
        "progression": ["SDR", "Sales Representative", "Account Executive", "Sales Manager", "VP of Sales"],
        "certifications": ["Salesforce Sales Cloud Certification", "HubSpot Sales Software", "Challenger Sale"],
        "courses": ["https://trailhead.salesforce.com", "https://academy.hubspot.com/courses/sales-training"]
    },
    {
        "job_title": "Account Manager",
        "skills": "client relationship management, account growth, upselling, cross-selling, salesforce, contract renewals, qbr presentations, customer success, conflict resolution, data analysis",
        "education": "bachelor", "interests": "business relationships, sales, communication, customer success, account growth", "experience": "mid",
        "description": "Manages and expands relationships with existing clients to drive retention and revenue growth.",
        "salary_min": 55000, "salary_max": 110000, "demand": "High", "industry": "Sales",
        "progression": ["Junior Account Manager", "Account Manager", "Senior Account Manager", "Account Director", "VP of Accounts"],
        "certifications": ["Salesforce CRM Certification", "HubSpot Sales", "CSAM"],
        "courses": ["https://trailhead.salesforce.com", "https://www.coursera.org/learn/account-management"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # EDUCATION
    # ══════════════════════════════════════════════════════════════════════════
    {
        "job_title": "Teacher / Educator",
        "skills": "lesson planning, curriculum development, classroom management, formative assessment, differentiated instruction, learning management systems, student engagement, parent communication, ib/ap curriculum",
        "education": "bachelor", "interests": "teaching, education, child development, mentoring, learning, subject mastery", "experience": "mid",
        "description": "Designs and delivers engaging instruction that supports student learning and personal growth.",
        "salary_min": 40000, "salary_max": 75000, "demand": "High", "industry": "Education",
        "progression": ["Student Teacher", "Teacher", "Lead Teacher", "Head of Department", "Principal"],
        "certifications": ["State Teaching License", "TEFL/TESOL", "Special Education Certification"],
        "courses": ["https://www.coursera.org/learn/teaching-learning", "https://www.edx.org/learn/education"]
    },
    {
        "job_title": "Professor / Academic",
        "skills": "research design, academic writing, grant writing, peer review, lecturing, curriculum design, student mentoring, publication, scientific methodology, conference presentations",
        "education": "phd", "interests": "research, teaching, academic knowledge, intellectual inquiry, writing, discovery", "experience": "senior",
        "description": "Conducts original research and teaches at university level, mentoring the next generation of scholars.",
        "salary_min": 65000, "salary_max": 160000, "demand": "Moderate", "industry": "Education",
        "progression": ["Teaching Assistant", "Postdoctoral Researcher", "Assistant Professor", "Associate Professor", "Full Professor"],
        "certifications": ["PhD Degree", "Postdoctoral Fellowship", "Research Grants (NSF, NIH)"],
        "courses": ["https://www.coursera.org/learn/scientific-writing", "https://www.edx.org/learn/teaching"]
    },
    {
        "job_title": "Corporate Trainer",
        "skills": "training needs analysis, instructional design, facilitation, adult learning principles, lms administration, e-learning tools, presentation, assessment, onboarding programs, leadership development",
        "education": "bachelor", "interests": "education, professional development, training, corporate learning, communication, coaching", "experience": "mid",
        "description": "Designs and delivers skill-building training programs for employees across organizations.",
        "salary_min": 55000, "salary_max": 100000, "demand": "High", "industry": "Education",
        "progression": ["Training Coordinator", "Corporate Trainer", "Senior Trainer", "L&D Manager", "Chief Learning Officer"],
        "certifications": ["ATD CPTD", "SHRM Learning", "CPLP"],
        "courses": ["https://www.td.org", "https://www.coursera.org/learn/corporate-training"]
    },
    {
        "job_title": "Instructional Designer",
        "skills": "articulate storyline, lectora, camtasia, lms (moodle, canvas), storyboarding, e-learning development, scorm, xapi, adult learning theory, graphic design for learning, assessment design",
        "education": "master", "interests": "e-learning, education technology, instructional design, curriculum, digital learning, UX", "experience": "mid",
        "description": "Creates engaging digital and in-person learning experiences using instructional design principles.",
        "salary_min": 58000, "salary_max": 100000, "demand": "High", "industry": "Education",
        "progression": ["Instructional Designer", "Senior ID", "Learning Experience Designer", "L&D Manager", "CLO"],
        "certifications": ["ATD CPTD", "Articulate Certification", "CPLP"],
        "courses": ["https://www.td.org", "https://www.coursera.org/learn/e-learning-instructional-design"]
    },
    {
        "job_title": "School Counselor",
        "skills": "individual counseling, group counseling, college advising, academic planning, crisis intervention, social-emotional learning, career assessment, dsmv, parent consultation",
        "education": "master", "interests": "counseling, youth development, education, psychology, college prep, student wellbeing", "experience": "mid",
        "description": "Supports K-12 students with academic, social-emotional, and college/career development.",
        "salary_min": 50000, "salary_max": 80000, "demand": "High", "industry": "Education",
        "progression": ["School Counselor", "Senior Counselor", "Head Counselor", "Director of Counseling", "Dean of Students"],
        "certifications": ["State School Counseling License", "NCC", "ASCA Membership"],
        "courses": ["https://www.schoolcounselor.org", "https://www.counseling.org"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # LEGAL & GOVERNMENT
    # ══════════════════════════════════════════════════════════════════════════
    {
        "job_title": "Lawyer / Attorney",
        "skills": "legal research, case analysis, contract drafting, negotiation, litigation, oral advocacy, statutory interpretation, client counseling, legal writing, westlaw, lexisnexis",
        "education": "phd", "interests": "law, justice, advocacy, research, critical thinking, writing, policy", "experience": "mid",
        "description": "Represents clients in legal matters, drafts documents, and provides expert legal advice.",
        "salary_min": 80000, "salary_max": 250000, "demand": "High", "industry": "Legal",
        "progression": ["Law Clerk", "Associate Attorney", "Senior Associate", "Partner", "Managing Partner"],
        "certifications": ["Juris Doctor (JD)", "State Bar Admission", "LLM (specialty)"],
        "courses": ["https://www.coursera.org/learn/constitutional-law", "https://www.edx.org/learn/law"]
    },
    {
        "job_title": "Judge",
        "skills": "judicial reasoning, legal precedent, constitutional law, evidence rules, case management, written opinions, impartiality, oral arguments, sentencing guidelines, procedural law",
        "education": "phd", "interests": "law, justice, public service, ethics, government, critical thinking, policy", "experience": "senior",
        "description": "Presides over court proceedings, interprets law, weighs evidence, and delivers impartial judgments.",
        "salary_min": 120000, "salary_max": 220000, "demand": "Moderate", "industry": "Legal",
        "progression": ["Attorney", "Magistrate", "Judge", "Senior Judge", "Chief Justice"],
        "certifications": ["JD Degree", "State Bar Admission", "National Judicial College Training"],
        "courses": ["https://www.nji.org", "https://www.courtstudy.org"]
    },
    {
        "job_title": "Paralegal",
        "skills": "legal research, westlaw, lexisnexis, document review, e-discovery, case file management, contract review, deposition preparation, legal drafting, court filing procedures",
        "education": "associate", "interests": "law, research, organization, legal procedures, writing, justice", "experience": "entry",
        "description": "Assists attorneys with research, document preparation, and case management.",
        "salary_min": 40000, "salary_max": 70000, "demand": "Moderate", "industry": "Legal",
        "progression": ["Legal Assistant", "Paralegal", "Senior Paralegal", "Paralegal Manager", "Legal Operations Director"],
        "certifications": ["NALA CLA", "NFPA PACE", "State Paralegal Certification"],
        "courses": ["https://www.coursera.org/learn/paralegal", "https://www.nala.org"]
    },
    {
        "job_title": "Civil Servant / Government Officer",
        "skills": "public administration, policy analysis, report writing, stakeholder engagement, regulatory compliance, budgeting, project coordination, public communication, governance frameworks",
        "education": "bachelor", "interests": "government, public service, policy, administration, community, governance, law", "experience": "junior",
        "description": "Implements government policy, manages public services, and serves communities through administrative roles.",
        "salary_min": 40000, "salary_max": 100000, "demand": "High", "industry": "Government",
        "progression": ["Government Trainee", "Officer", "Senior Officer", "Assistant Director", "Director General"],
        "certifications": ["Civil Service Exam", "PMP", "Public Administration Certificate"],
        "courses": ["https://www.opm.gov/training-and-development", "https://www.coursera.org/learn/public-policy"]
    },
    {
        "job_title": "Policy Analyst",
        "skills": "policy research, legislative analysis, cost-benefit analysis, stakeholder mapping, report writing, statistics, data analysis, economics, policy modeling, public consultation",
        "education": "master", "interests": "policy, government, economics, social issues, research, public affairs, advocacy", "experience": "mid",
        "description": "Researches and evaluates government policies to develop evidence-based recommendations.",
        "salary_min": 55000, "salary_max": 110000, "demand": "High", "industry": "Government",
        "progression": ["Policy Researcher", "Policy Analyst", "Senior Policy Analyst", "Policy Manager", "Policy Director"],
        "certifications": ["CAPP Certification", "PMP", "GovLoop Training"],
        "courses": ["https://www.coursera.org/learn/public-policy", "https://www.urban.org/policy-centers"]
    },
    {
        "job_title": "Social Worker",
        "skills": "case management, motivational interviewing, community resources, crisis assessment, documentation, advocacy, family systems therapy, child protection, dsmv, cultural competency",
        "education": "bachelor", "interests": "social justice, helping others, community, psychology, advocacy, human welfare", "experience": "junior",
        "description": "Supports vulnerable individuals and families in navigating social services, mental health, and crisis situations.",
        "salary_min": 40000, "salary_max": 75000, "demand": "High", "industry": "Social Services",
        "progression": ["Case Worker", "Social Worker", "Senior Social Worker", "Clinical Social Worker", "Social Work Director"],
        "certifications": ["LCSW", "LMSW", "LSW", "NASW Membership"],
        "courses": ["https://www.socialworkers.org", "https://www.coursera.org/learn/social-work"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SKILLED TRADES & OTHER
    # ══════════════════════════════════════════════════════════════════════════
    {
        "job_title": "Electrician",
        "skills": "electrical wiring, nec code compliance, circuit breaker installation, conduit bending, blueprint reading, troubleshooting, panel board installation, plc basics, safety protocols, testing equipment",
        "education": "associate", "interests": "electrical, construction, hands-on, engineering, problem solving, trades", "experience": "junior",
        "description": "Installs, maintains, and repairs electrical systems in residential, commercial, and industrial settings.",
        "salary_min": 45000, "salary_max": 95000, "demand": "High", "industry": "Skilled Trades",
        "progression": ["Apprentice Electrician", "Journeyman Electrician", "Master Electrician", "Electrical Supervisor", "Electrical Contractor"],
        "certifications": ["Journeyman Electrician License", "Master Electrician License", "OSHA 30-Hour", "NFPA 70E"],
        "courses": ["https://www.nccer.org", "https://www.ibew.org/Training"]
    },
    {
        "job_title": "Plumber",
        "skills": "pipe fitting, drainage systems, water supply, gas line installation, blueprint reading, soldering, hydrostatic testing, plumbing codes, fixture installation, troubleshooting",
        "education": "associate", "interests": "construction, hands-on, problem solving, plumbing, water systems, trades", "experience": "junior",
        "description": "Installs and repairs plumbing systems for water, gas, and drainage in residential and commercial buildings.",
        "salary_min": 42000, "salary_max": 90000, "demand": "High", "industry": "Skilled Trades",
        "progression": ["Plumbing Apprentice", "Journeyman Plumber", "Master Plumber", "Plumbing Supervisor", "Plumbing Contractor"],
        "certifications": ["Journeyman Plumber License", "Master Plumber License", "OSHA 10-Hour"],
        "courses": ["https://www.phcppros.com/education", "https://www.nccer.org"]
    },
    {
        "job_title": "Commercial Pilot",
        "skills": "instrument flight, navigation, crew resource management, weather analysis, aircraft systems, flight planning, emergency procedures, atc communication, weight and balance, multi-engine operations",
        "education": "bachelor", "interests": "aviation, flying, travel, technology, safety, transportation, adventure", "experience": "senior",
        "description": "Operates commercial aircraft to safely transport passengers or cargo across domestic and international routes.",
        "salary_min": 80000, "salary_max": 250000, "demand": "High", "industry": "Transportation",
        "progression": ["Flight Student", "Private Pilot", "Commercial Pilot", "First Officer", "Captain"],
        "certifications": ["FAA Commercial Pilot License", "ATP Certificate", "Instrument Rating", "Type Rating"],
        "courses": ["https://www.faa.gov/pilots", "https://www.cfinotebook.net"]
    },
    {
        "job_title": "Police Officer",
        "skills": "law enforcement procedures, criminal law, de-escalation, report writing, evidence collection, community policing, defensive tactics, investigation, traffic enforcement, first aid",
        "education": "associate", "interests": "law enforcement, justice, public safety, community service, investigation, government", "experience": "entry",
        "description": "Maintains public order, enforces laws, investigates crimes, and protects community members.",
        "salary_min": 45000, "salary_max": 90000, "demand": "High", "industry": "Public Safety",
        "progression": ["Patrol Officer", "Senior Officer", "Detective / Investigator", "Sergeant", "Lieutenant", "Captain"],
        "certifications": ["Police Academy Certificate", "POST Certification", "Crisis Intervention Training"],
        "courses": ["https://www.theiacp.org/resources", "https://www.nleomf.org"]
    },
    {
        "job_title": "Chef / Culinary Artist",
        "skills": "culinary techniques, menu development, recipe creation, food cost control, kitchen management, food safety (haccp), plating and presentation, inventory management, team leadership",
        "education": "associate", "interests": "food, cooking, creativity, culinary arts, hospitality, gastronomy, restaurant management", "experience": "mid",
        "description": "Creates and executes culinary concepts, managing kitchen operations and menu development.",
        "salary_min": 40000, "salary_max": 95000, "demand": "Moderate", "industry": "Hospitality",
        "progression": ["Commis Chef", "Line Cook", "Sous Chef", "Head Chef", "Executive Chef"],
        "certifications": ["ServSafe Manager Certification", "ACF Culinary Certification", "CIA Graduate"],
        "courses": ["https://www.ciachef.edu", "https://www.coursera.org/learn/cooking"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SCIENCE & RESEARCH
    # ══════════════════════════════════════════════════════════════════════════
    {
        "job_title": "Research Scientist",
        "skills": "experimental design, statistical analysis, python, r, laboratory techniques, scientific writing, grant writing, peer review, literature review, hypothesis testing, data visualization",
        "education": "phd", "interests": "research, science, discovery, data analysis, experimentation, biology, chemistry, physics", "experience": "senior",
        "description": "Conducts original research to generate new scientific knowledge and advance specialized fields.",
        "salary_min": 80000, "salary_max": 150000, "demand": "High", "industry": "Science",
        "progression": ["Research Assistant", "Research Associate", "Research Scientist", "Senior Scientist", "Principal Investigator"],
        "certifications": ["Postdoctoral Fellowship", "NIH Certification", "Lab Safety"],
        "courses": ["https://www.coursera.org/learn/scientific-research", "https://www.edx.org/learn/research-methods"]
    },
    {
        "job_title": "Environmental Scientist",
        "skills": "environmental monitoring, gis, air quality analysis, water quality sampling, epa regulations, impact assessments, field data collection, statistical analysis, report writing, ecological modeling",
        "education": "bachelor", "interests": "environment, ecology, sustainability, science, field research, conservation, climate", "experience": "mid",
        "description": "Studies environmental conditions and develops solutions to pollution, climate, and conservation problems.",
        "salary_min": 55000, "salary_max": 95000, "demand": "Moderate", "industry": "Science",
        "progression": ["Environmental Technician", "Environmental Scientist", "Senior Scientist", "Environmental Manager", "Chief Scientist"],
        "certifications": ["CHMM", "REM (Registered Environmental Manager)", "ArcGIS Certification"],
        "courses": ["https://www.coursera.org/learn/sustainability", "https://www.esri.com/training"]
    },
    {
        "job_title": "Bioinformatics Scientist",
        "skills": "python, r, biopython, genomics, rna-seq, genome assembly, variant calling, blast, multiple sequence alignment, statistical genetics, high-performance computing, linux",
        "education": "phd", "interests": "biology, genomics, data science, genetics, computing, medicine, bioinformatics", "experience": "mid",
        "description": "Applies computational methods to analyze biological data including genomes, proteomes, and clinical data.",
        "salary_min": 85000, "salary_max": 145000, "demand": "High", "industry": "Science",
        "progression": ["Bioinformatics Analyst", "Bioinformatics Scientist", "Senior Scientist", "Principal Scientist", "Research Director"],
        "certifications": ["ISCB Membership", "Galaxy Training Certification"],
        "courses": ["https://www.coursera.org/specializations/bioinformatics", "https://www.edx.org/learn/bioinformatics"]
    },
    {
        "job_title": "Geologist",
        "skills": "geological mapping, stratigraphy, mineralogy, petrography, gis, remote sensing, core logging, structural geology, geochemistry, petrel, well log analysis",
        "education": "bachelor", "interests": "geology, earth science, minerals, fieldwork, environment, energy, mining", "experience": "mid",
        "description": "Studies Earth's structure, rock formations, and geological processes for energy, mining, and environmental work.",
        "salary_min": 60000, "salary_max": 110000, "demand": "Moderate", "industry": "Science",
        "progression": ["Field Geologist", "Geologist", "Senior Geologist", "Chief Geologist", "Geoscience Director"],
        "certifications": ["PG License", "GSA Membership", "ArcGIS Certification"],
        "courses": ["https://www.coursera.org/learn/geology", "https://www.geosociety.org/education"]
    },
    {
        "job_title": "Agricultural Scientist",
        "skills": "agronomy, soil science, crop physiology, irrigation management, gis, precision agriculture, pest management, plant genetics, field trials, remote sensing, sustainability",
        "education": "bachelor", "interests": "agriculture, biology, food systems, environment, sustainability, farming, science", "experience": "mid",
        "description": "Researches and develops methods to improve crop productivity, soil health, and sustainable farming practices.",
        "salary_min": 55000, "salary_max": 95000, "demand": "Moderate", "industry": "Agriculture",
        "progression": ["Research Assistant", "Agricultural Scientist", "Senior Scientist", "Research Lead", "Agricultural Director"],
        "certifications": ["CCA (Certified Crop Adviser)", "CPAg", "SSSA Certification"],
        "courses": ["https://www.coursera.org/learn/agriculture", "https://www.asa-cssa-sssa.org"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # HOSPITALITY, TRAVEL & OTHERS
    # ══════════════════════════════════════════════════════════════════════════
    {
        "job_title": "Hotel Manager",
        "skills": "hotel operations, revenue management, pms software, guest relations, staff supervision, budgeting, food and beverage management, housekeeping oversight, otas management, service standards",
        "education": "bachelor", "interests": "hospitality, customer service, travel, management, tourism, guest experience", "experience": "senior",
        "description": "Oversees all hotel departments to ensure exceptional guest experience and profitable operations.",
        "salary_min": 55000, "salary_max": 110000, "demand": "Moderate", "industry": "Hospitality",
        "progression": ["Front Desk Agent", "Department Supervisor", "Assistant Hotel Manager", "Hotel Manager", "Regional Director"],
        "certifications": ["CHA (Certified Hotel Administrator)", "CRME", "AH&LA Certification"],
        "courses": ["https://www.ahlei.org", "https://www.coursera.org/learn/hospitality-management"]
    },
    {
        "job_title": "Travel Consultant",
        "skills": "amadeus gds, sabre gds, itinerary planning, destination knowledge, visa procedures, travel insurance, customer service, package tours, airline booking, hotel contracting",
        "education": "associate", "interests": "travel, tourism, geography, culture, customer service, adventure, destinations", "experience": "entry",
        "description": "Creates personalized travel experiences by booking flights, hotels, tours, and handling travel logistics.",
        "salary_min": 35000, "salary_max": 65000, "demand": "Moderate", "industry": "Hospitality",
        "progression": ["Travel Agent", "Travel Consultant", "Senior Consultant", "Travel Manager", "Agency Director"],
        "certifications": ["CTC (Certified Travel Counselor)", "CLIA Membership", "ASTA Member"],
        "courses": ["https://www.asta.org/education", "https://www.coursera.org/learn/tourism-management"]
    },
    {
        "job_title": "Personal Trainer / Fitness Coach",
        "skills": "fitness assessment, exercise programming, strength training, nutrition coaching, injury prevention, periodization, client motivation, anatomy, functional movement, vo2max testing",
        "education": "associate", "interests": "fitness, health, wellness, sports, anatomy, coaching, motivation, nutrition", "experience": "entry",
        "description": "Creates and delivers personalized fitness programs to help clients achieve health and performance goals.",
        "salary_min": 35000, "salary_max": 80000, "demand": "High", "industry": "Sports & Fitness",
        "progression": ["Fitness Instructor", "Personal Trainer", "Senior Trainer", "Head Coach", "Studio Owner"],
        "certifications": ["NASM CPT", "ACE CPT", "NSCA CSCS", "Precision Nutrition"],
        "courses": ["https://www.nasm.org", "https://www.acefitness.org"]
    },
    {
        "job_title": "Sports Analyst",
        "skills": "sports statistics, r, python, tableau, video analysis, data wrangling, performance metrics, scouting reports, predictive modeling, sql, sports technology tools",
        "education": "bachelor", "interests": "sports, data analysis, statistics, performance, strategy, analytics, competition", "experience": "junior",
        "description": "Analyzes athlete and team performance data to inform coaching decisions and organizational strategy.",
        "salary_min": 50000, "salary_max": 100000, "demand": "Moderate", "industry": "Sports & Fitness",
        "progression": ["Data Analyst", "Sports Analyst", "Senior Analyst", "Head of Analytics", "VP of Analytics"],
        "certifications": ["Coursera Sports Analytics", "MIT Sports Analytics Certificate"],
        "courses": ["https://www.coursera.org/learn/sports-analytics", "https://www.edx.org/learn/sports-analytics"]
    },
    {
        "job_title": "Journalist / Reporter",
        "skills": "investigative reporting, interviewing, news writing, fact checking, ap style, source development, multimedia storytelling, social media, data journalism, video production",
        "education": "bachelor", "interests": "writing, news, investigation, current events, media, communication, storytelling", "experience": "junior",
        "description": "Investigates, writes, and reports news and feature stories across print, digital, and broadcast media.",
        "salary_min": 38000, "salary_max": 85000, "demand": "Moderate", "industry": "Media",
        "progression": ["Reporter", "Senior Reporter", "Staff Writer", "Editor", "Editor-in-Chief"],
        "certifications": ["SPJ Membership", "NCTJ Diploma", "Poynter Journalism Certification"],
        "courses": ["https://www.poynter.org", "https://www.coursera.org/learn/journalism"]
    },
    {
        "job_title": "Broadcast Technician",
        "skills": "audio engineering, video switchers, broadcast encoding, live streaming, obs, satellite systems, rf transmission, signal routing, troubleshooting broadcast equipment, production workflows",
        "education": "associate", "interests": "media production, technology, audio, video, broadcasting, live events, television", "experience": "junior",
        "description": "Operates and maintains technical broadcasting equipment for live and recorded media production.",
        "salary_min": 40000, "salary_max": 80000, "demand": "Moderate", "industry": "Media",
        "progression": ["Tech Assistant", "Broadcast Technician", "Senior Technician", "Broadcast Engineer", "Technical Director"],
        "certifications": ["SBE (Society of Broadcast Engineers)", "Adobe Certified Professional"],
        "courses": ["https://www.sbe.org", "https://www.coursera.org/learn/digital-media"]
    },
    {
        "job_title": "Real Estate Agent",
        "skills": "property valuation, comparative market analysis, listing presentations, buyer representation, contract negotiation, mls, client prospecting, open houses, real estate law, closing process",
        "education": "associate", "interests": "real estate, property, sales, investment, community, communication, negotiation", "experience": "entry",
        "description": "Guides clients through buying, selling, or renting properties using market expertise.",
        "salary_min": 40000, "salary_max": 150000, "demand": "Moderate", "industry": "Real Estate",
        "progression": ["Real Estate Agent", "Senior Agent", "Team Lead", "Real Estate Broker", "Agency Owner"],
        "certifications": ["State Real Estate License", "NAR Membership", "CRS", "ABR"],
        "courses": ["https://www.nar.realtor/education", "https://www.coursera.org/learn/real-estate"]
    },
    {
        "job_title": "Logistics Coordinator",
        "skills": "freight management, shipping documentation, customs clearance, warehouse operations, inventory tracking, erp, vendor coordination, route planning, excel, purchase orders",
        "education": "associate", "interests": "logistics, supply chain, operations, transportation, organization, coordination", "experience": "entry",
        "description": "Coordinates inbound and outbound shipments, warehousing, and delivery to ensure smooth logistics operations.",
        "salary_min": 40000, "salary_max": 70000, "demand": "High", "industry": "Transportation",
        "progression": ["Logistics Assistant", "Logistics Coordinator", "Logistics Manager", "Director of Logistics", "VP Operations"],
        "certifications": ["APICS CLTD", "CPIM", "OSHA Forklift"],
        "courses": ["https://www.apics.org", "https://www.coursera.org/learn/supply-chain-logistics"]
    },
    {
        "job_title": "Air Traffic Controller",
        "skills": "radar interpretation, aircraft separation standards, atc phraseology, emergency procedures, weather analysis, flight strip management, radio communication, stress management, spatial reasoning",
        "education": "bachelor", "interests": "aviation, safety, aircraft, technology, communication, coordination, government", "experience": "mid",
        "description": "Directs aircraft movement to maintain safe separation and efficient traffic flow in controlled airspace.",
        "salary_min": 90000, "salary_max": 160000, "demand": "High", "industry": "Transportation",
        "progression": ["Trainee ATC", "Developmental Controller", "Certified Professional Controller", "Senior Controller", "Facility Manager"],
        "certifications": ["FAA ATC Certificate", "NATCA Membership"],
        "courses": ["https://www.faa.gov/jobs/career_fields/aviation_careers", "https://www.eurocontrol.int"]
    },
    {
        "job_title": "Video Game Developer",
        "skills": "unity, unreal engine, c#, c++, game physics, collision detection, ai pathfinding, level design, shader programming, multiplayer networking, performance profiling, version control",
        "education": "bachelor", "interests": "gaming, programming, creativity, simulation, art, design, interactive media", "experience": "junior",
        "description": "Designs and programs interactive video game mechanics, systems, and experiences across platforms.",
        "salary_min": 65000, "salary_max": 130000, "demand": "Moderate", "industry": "Creative",
        "progression": ["Junior Game Developer", "Game Developer", "Senior Game Developer", "Lead Developer", "Game Director"],
        "certifications": ["Unity Certified Professional", "Unreal Engine Certification"],
        "courses": ["https://learn.unity.com", "https://www.coursera.org/learn/game-design"]
    },
    {
        "job_title": "Esports Coach / Analyst",
        "skills": "game-specific mechanics, meta analysis, vod review, performance statistics, strategy development, team communication, player psychology, coaching frameworks, data tools, streaming",
        "education": "associate", "interests": "esports, gaming, strategy, competition, coaching, teamwork, performance analysis", "experience": "mid",
        "description": "Coaches competitive esports teams by analyzing gameplay, developing strategies, and improving player performance.",
        "salary_min": 40000, "salary_max": 100000, "demand": "Moderate", "industry": "Creative",
        "progression": ["Amateur Coach", "Esports Analyst", "Head Coach", "Director of Esports", "Team GM"],
        "certifications": ["NACE Coaching Certification", "Sports Coaching Certificate"],
        "courses": ["https://www.nace.gg", "https://www.coursera.org/learn/esports"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SUSTAINABILITY
    # ══════════════════════════════════════════════════════════════════════════
    {
        "job_title": "Sustainability Consultant",
        "skills": "sustainability strategy, esg reporting, carbon footprint analysis, life cycle assessment, gri standards, stakeholder engagement, environmental auditing, green supply chain, renewable energy planning",
        "education": "bachelor", "interests": "sustainability, environment, business, green energy, corporate responsibility, climate", "experience": "mid",
        "description": "Advises organizations on reducing environmental impact and building long-term sustainability strategies.",
        "salary_min": 65000, "salary_max": 115000, "demand": "High", "industry": "Sustainability",
        "progression": ["Sustainability Analyst", "Sustainability Consultant", "Senior Consultant", "Sustainability Director", "Chief Sustainability Officer"],
        "certifications": ["LEED AP", "ISSP-SA", "GRI Certified"],
        "courses": ["https://www.coursera.org/learn/sustainability-through-soccer", "https://www.usgbc.org/leed"]
    },
    {
        "job_title": "Climate Analyst",
        "skills": "climate modeling, python, r, gis, climate data analysis, ipcc reports, carbon accounting, scenario analysis, environmental economics, policy analysis, data visualization",
        "education": "master", "interests": "climate science, environment, data, policy, sustainability, research, earth science", "experience": "mid",
        "description": "Analyzes climate data and models future scenarios to inform business and policy decision-making.",
        "salary_min": 65000, "salary_max": 120000, "demand": "Very High", "industry": "Sustainability",
        "progression": ["Climate Research Assistant", "Climate Analyst", "Senior Climate Analyst", "Climate Strategy Lead", "Chief Climate Officer"],
        "certifications": ["LEED AP", "CDP Disclosure", "Climate Reality Leadership Corps"],
        "courses": ["https://www.coursera.org/learn/climate-change", "https://www.edx.org/learn/climate-change"]
    },
    {
        "job_title": "Renewable Energy Engineer",
        "skills": "solar pv design, wind turbine engineering, power systems, grid integration, energy storage, homer pro, pvwatts, autocad electrical, power electronics, environmental permitting",
        "education": "bachelor", "interests": "renewable energy, environment, engineering, sustainability, solar, wind, clean energy", "experience": "mid",
        "description": "Designs and optimizes renewable energy systems including solar, wind, and battery storage solutions.",
        "salary_min": 75000, "salary_max": 135000, "demand": "Very High", "industry": "Sustainability",
        "progression": ["Energy Analyst", "Renewable Energy Engineer", "Senior RE Engineer", "Energy Systems Architect", "Director of Renewable Energy"],
        "certifications": ["NABCEP PV Installation Professional", "PE License", "LEED AP Energy"],
        "courses": ["https://www.coursera.org/learn/solar-energy", "https://www.edx.org/learn/renewable-energy"]
    },
    {
        "job_title": "ESG Consultant",
        "skills": "esg strategy, gri standards, sasb framework, tcfd disclosure, carbon accounting, double materiality assessment, esg data collection, stakeholder reporting, regulatory compliance, financial analysis",
        "education": "bachelor", "interests": "sustainability, finance, corporate governance, ethics, environment, social impact, reporting", "experience": "mid",
        "description": "Helps organizations define, measure, and report on Environmental, Social, and Governance performance.",
        "salary_min": 80000, "salary_max": 145000, "demand": "Very High", "industry": "Sustainability",
        "progression": ["ESG Analyst", "ESG Consultant", "Senior ESG Consultant", "Head of ESG", "Chief Sustainability Officer"],
        "certifications": ["GRI Certification", "CFA ESG Certificate", "SASB FSA Credential"],
        "courses": ["https://www.gri.org/standards", "https://www.coursera.org/learn/esg-investing"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # FUTURE TECH ROLES
    # ══════════════════════════════════════════════════════════════════════════
    {
        "job_title": "Prompt Engineer",
        "skills": "prompt design, chain-of-thought prompting, few-shot learning, llm evaluation, python, api integration, system prompt engineering, rag systems, llm fine-tuning, ai output testing",
        "education": "bachelor", "interests": "ai, language models, nlp, creativity, technology, writing, automation, problem solving", "experience": "junior",
        "description": "Crafts and optimizes prompts to maximize the accuracy, safety, and usefulness of AI language model outputs.",
        "salary_min": 85000, "salary_max": 175000, "demand": "Very High", "industry": "Future Tech",
        "progression": ["Prompt Specialist", "Prompt Engineer", "Senior Prompt Engineer", "AI Systems Designer", "Head of AI Products"],
        "certifications": ["DeepLearning.AI Prompt Engineering", "Anthropic Courses", "OpenAI Developer Certification"],
        "courses": ["https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers", "https://learnprompting.org"]
    },
    {
        "job_title": "AI Product Manager",
        "skills": "ai product strategy, ml product lifecycle, data-driven roadmapping, llm evaluation, user research, stakeholder management, model performance metrics, responsible ai, agile, go-to-market for ai",
        "education": "bachelor", "interests": "ai, product management, technology, business, strategy, innovation, data", "experience": "mid",
        "description": "Leads the development of AI-powered products, bridging technical ML capabilities with customer needs.",
        "salary_min": 130000, "salary_max": 220000, "demand": "Very High", "industry": "Future Tech",
        "progression": ["Associate PM", "AI Product Manager", "Senior AI PM", "Group PM (AI/ML)", "CPO"],
        "certifications": ["Pragmatic Institute AI PM", "AI Product Management (Coursera)", "PMP"],
        "courses": ["https://www.coursera.org/learn/ai-product-management", "https://www.productschool.com/ai"]
    },
    {
        "job_title": "AI Ethics Specialist",
        "skills": "ai bias auditing, fairness metrics, explainable ai, regulatory frameworks, ai governance, ethical risk assessment, policy writing, stakeholder consultation, responsible ai frameworks, data privacy",
        "education": "master", "interests": "ai, ethics, policy, social impact, philosophy, fairness, governance, human rights", "experience": "mid",
        "description": "Ensures AI systems are fair, transparent, and responsibly deployed by developing ethical frameworks and auditing models.",
        "salary_min": 90000, "salary_max": 160000, "demand": "Very High", "industry": "Future Tech",
        "progression": ["AI Ethics Researcher", "AI Ethics Analyst", "AI Ethics Specialist", "Head of Responsible AI", "Chief Ethics Officer"],
        "certifications": ["IEEE AI Ethics Certification", "ISACA AI Audit", "Responsible AI (Microsoft)"],
        "courses": ["https://www.coursera.org/learn/ai-ethics", "https://www.edx.org/learn/artificial-intelligence"]
    },
    {
        "job_title": "Autonomous Systems Engineer",
        "skills": "ros2, python, c++, lidar, radar, sensor fusion, kalman filtering, path planning, slam, computer vision, simulation (gazebo, carla), safety-critical systems, can bus",
        "education": "master", "interests": "robotics, self-driving, drones, automation, ai, engineering, autonomous systems", "experience": "senior",
        "description": "Designs perception, planning, and control systems for autonomous vehicles, drones, and industrial robots.",
        "salary_min": 130000, "salary_max": 210000, "demand": "Very High", "industry": "Future Tech",
        "progression": ["Robotics Engineer", "Autonomous Systems Engineer", "Senior AV Engineer", "Principal Engineer", "Director of Autonomy"],
        "certifications": ["Udacity Self-Driving Car Nanodegree", "NVIDIA DRIVE Certification", "ROS Certification"],
        "courses": ["https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd0013", "https://www.coursera.org/specializations/self-driving-cars"]
    },
    {
        "job_title": "Digital Twin Engineer",
        "skills": "azure digital twins, iot hub, 3d modeling, python, mqtt, time series databases, simulation modeling, unity, asset modeling, real-time data streaming, digital thread",
        "education": "bachelor", "interests": "simulation, iot, engineering, smart manufacturing, digital transformation, technology", "experience": "mid",
        "description": "Creates virtual replicas of physical assets or systems to simulate behavior and optimize real-world performance.",
        "salary_min": 100000, "salary_max": 165000, "demand": "Very High", "industry": "Future Tech",
        "progression": ["Simulation Engineer", "Digital Twin Engineer", "Senior DT Engineer", "Digital Twin Architect", "Head of Digital Engineering"],
        "certifications": ["Azure Digital Twins Associate", "NVIDIA Omniverse", "Siemens Digital Twin Certification"],
        "courses": ["https://learn.microsoft.com/azure/digital-twins", "https://www.coursera.org/learn/digital-twins"]
    },
    {
        "job_title": "Data Storyteller",
        "skills": "data visualization, tableau, power bi, d3.js, python, narrative design, dashboard design, business intelligence, executive communication, infographic design, data journalism",
        "education": "bachelor", "interests": "data, communication, storytelling, visualization, journalism, design, analytics", "experience": "mid",
        "description": "Translates complex data into compelling visual narratives and dashboards that drive organizational decisions.",
        "salary_min": 75000, "salary_max": 130000, "demand": "High", "industry": "Future Tech",
        "progression": ["Data Analyst", "Data Storyteller", "Senior Data Storyteller", "Head of Data Communication", "Chief Data Officer"],
        "certifications": ["Tableau Desktop Specialist", "Power BI Certification", "Google Data Analytics"],
        "courses": ["https://www.coursera.org/learn/data-visualization", "https://www.storytellingwithdata.com"]
    },
    {
        "job_title": "Automation Engineer",
        "skills": "rpa, uipath, automation anywhere, python, selenium, api automation, workflow orchestration, process mining, ci/cd, scripting, low-code platforms, test automation",
        "education": "bachelor", "interests": "automation, efficiency, software, rpa, robotics, programming, process improvement", "experience": "mid",
        "description": "Designs and deploys software robots and automated workflows to eliminate manual, repetitive tasks.",
        "salary_min": 80000, "salary_max": 140000, "demand": "Very High", "industry": "Future Tech",
        "progression": ["Automation Analyst", "Automation Engineer", "Senior Automation Engineer", "RPA Architect", "Head of Automation"],
        "certifications": ["UiPath Certified Advanced RPA Developer", "Automation Anywhere Certified", "Blue Prism Developer"],
        "courses": ["https://academy.uipath.com", "https://university.automationanywhere.com"]
    },
    {
        "job_title": "Decision Intelligence Analyst",
        "skills": "decision analysis, python, sql, statistics, machine learning, behavioral economics, predictive modeling, power bi, scenario planning, business strategy, causal inference",
        "education": "master", "interests": "data, decision science, business strategy, ai, economics, analytics, organizational behavior", "experience": "mid",
        "description": "Combines data science and decision theory to improve strategic and operational decision-making.",
        "salary_min": 90000, "salary_max": 155000, "demand": "High", "industry": "Future Tech",
        "progression": ["Data Analyst", "Decision Analyst", "Decision Intelligence Analyst", "Head of Decision Science", "Chief Analytics Officer"],
        "certifications": ["Gartner Decision Intelligence", "CFA", "Coursera Decision Making"],
        "courses": ["https://www.coursera.org/learn/decision-making", "https://www.edx.org/learn/data-science"]
    },
    {
        "job_title": "AI-Augmented Doctor",
        "skills": "clinical ai tools, diagnostic imaging ai, clinical decision support, ehr integration, ai-assisted pathology, digital biomarkers, telemedicine, evidence-based medicine, medical informatics",
        "education": "phd", "interests": "medicine, ai in healthcare, digital health, patient care, science, innovation, diagnostics", "experience": "senior",
        "description": "Physicians who integrate AI-powered diagnostic and clinical decision tools to enhance patient care and outcomes.",
        "salary_min": 200000, "salary_max": 450000, "demand": "Very High", "industry": "Future Tech",
        "progression": ["Resident", "Attending Physician", "AI-Augmented Physician", "Clinical AI Director", "Chief Medical AI Officer"],
        "certifications": ["Medical License", "Board Certification", "Clinical Informatics (ABPM)", "AI in Medicine (Stanford)"],
        "courses": ["https://www.coursera.org/learn/ai-in-medicine", "https://stanfordonline.stanford.edu"]
    },
    {
        "job_title": "Human-AI Interaction Designer",
        "skills": "conversational ux, ai ux patterns, figma, user research, psychological safety in ai, ethical design, prototyping ai interactions, trust calibration, human factors, accessibility",
        "education": "bachelor", "interests": "design, ai, human behavior, ux, psychology, interaction design, technology, ethics", "experience": "mid",
        "description": "Designs human-centered experiences for AI products ensuring usability, trust, and ethical interaction.",
        "salary_min": 95000, "salary_max": 160000, "demand": "Very High", "industry": "Future Tech",
        "progression": ["UX Designer", "AI UX Designer", "Human-AI Interaction Designer", "Principal Designer", "Head of AI Design"],
        "certifications": ["Google UX Design", "Nielsen Norman AI UX", "Interaction Design Foundation"],
        "courses": ["https://www.coursera.org/professional-certificates/google-ux-design", "https://www.interaction-design.org/courses/ai-for-designers"]
    },
    {
        "job_title": "AI Career Coach",
        "skills": "career counseling, ai coaching tools, resume analysis, interview coaching, labor market analysis, skills gap assessment, career pathing, communication, empathy, goal setting",
        "education": "bachelor", "interests": "career development, ai, helping others, education, psychology, professional coaching, workforce", "experience": "mid",
        "description": "Combines human coaching expertise with AI tools to provide personalized, data-driven career guidance.",
        "salary_min": 55000, "salary_max": 110000, "demand": "High", "industry": "Future Tech",
        "progression": ["Career Advisor", "AI Career Coach", "Senior Career Coach", "Head of Career Services", "Founder"],
        "certifications": ["ICF PCC Coaching Credential", "GCDF", "LinkedIn Career Coach Certification"],
        "courses": ["https://coachingfederation.org", "https://www.coursera.org/learn/career-counseling"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # WEB3 & METAVERSE
    # ══════════════════════════════════════════════════════════════════════════
    {
        "job_title": "Metaverse Designer",
        "skills": "unity, unreal engine, blender, virtual world building, spatial ux, vr interaction design, avatar creation, openxr, procedural generation, 3d asset optimization, web3 integration",
        "education": "bachelor", "interests": "metaverse, 3d design, virtual reality, gaming, creativity, web3, spatial computing", "experience": "junior",
        "description": "Designs and builds immersive 3D virtual worlds and metaverse experiences across platforms.",
        "salary_min": 75000, "salary_max": 145000, "demand": "High", "industry": "Web3 & Metaverse",
        "progression": ["3D Artist", "Metaverse Designer", "Senior Metaverse Designer", "Metaverse Architect", "Head of Virtual Worlds"],
        "certifications": ["Unity Certified 3D Artist", "Meta Horizon Worlds Creator", "Epic MegaGrants"],
        "courses": ["https://learn.unity.com", "https://www.coursera.org/learn/virtual-reality"]
    },
    {
        "job_title": "Blockchain Architect",
        "skills": "solidity, rust, hyperledger fabric, consensus mechanism design, layer 2 scaling, smart contract security, evm, cross-chain bridges, tokenomics design, zero knowledge proofs, dao governance",
        "education": "master", "interests": "blockchain, decentralization, cryptography, architecture, defi, web3, distributed systems", "experience": "senior",
        "description": "Designs enterprise-grade blockchain protocols, smart contract systems, and decentralized application architectures.",
        "salary_min": 130000, "salary_max": 220000, "demand": "High", "industry": "Web3 & Metaverse",
        "progression": ["Blockchain Developer", "Senior Blockchain Developer", "Blockchain Architect", "Principal Blockchain Architect", "Head of Web3"],
        "certifications": ["Certified Blockchain Architect (CBA)", "ConsenSys Academy", "Hyperledger Certified Expert"],
        "courses": ["https://www.hyperledger.org/learn", "https://www.cyfrin.io"]
    },
    {
        "job_title": "NFT Strategist",
        "skills": "nft market analysis, tokenomics, smart contract basics, community building, opensea, discord management, roadmap planning, web3 marketing, brand storytelling, mint strategy, dao governance",
        "education": "bachelor", "interests": "nft, digital art, blockchain, crypto, community, marketing, web3, brand building", "experience": "junior",
        "description": "Develops NFT collection strategy including concept, tokenomics, community growth, and go-to-market launch.",
        "salary_min": 55000, "salary_max": 150000, "demand": "Moderate", "industry": "Web3 & Metaverse",
        "progression": ["NFT Community Manager", "NFT Strategist", "Head of Web3 Marketing", "Web3 Brand Director", "Founder"],
        "certifications": ["Certified NFT Expert", "Blockchain Council NFT Certification"],
        "courses": ["https://academy.binance.com/en/articles/what-are-non-fungible-tokens-nfts", "https://www.coursera.org/learn/web3-blockchain-fundamentals"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # PERFORMING ARTS, DANCE & ENTERTAINMENT
    # ══════════════════════════════════════════════════════════════════════════
    {
        "job_title": "Dancer / Choreographer",
        "skills": "dancing, choreography, performance, rhythm, body movement, dance styles, stage presence, rehearsal management, flexibility, classical dance, contemporary dance, hip hop, ballet, creative direction",
        "education": "associate", "interests": "dancing, performing arts, music, creativity, fitness, movement, entertainment, art", "experience": "mid",
        "description": "Creates and performs choreographed dance routines for stage, film, events, and digital media.",
        "salary_min": 30000, "salary_max": 90000, "demand": "Moderate", "industry": "Performing Arts",
        "progression": ["Dance Student", "Backup Dancer", "Lead Dancer", "Choreographer", "Artistic Director"],
        "certifications": ["Bharatanatyam Certification", "RAD Ballet Certification", "Zumba Instructor License", "Dance Academy Diploma"],
        "courses": ["https://www.coursera.org/learn/music-and-dance", "https://www.udemy.com/topic/dance"]
    },
    {
        "job_title": "Dance Instructor / Teacher",
        "skills": "dancing, teaching, choreography, music theory, rhythm, student assessment, curriculum design, classical dance, contemporary dance, communication, patience, fitness training",
        "education": "associate", "interests": "dancing, teaching, music, fitness, performing arts, mentoring, creativity", "experience": "junior",
        "description": "Teaches dance techniques, styles, and performance skills to students of all ages and skill levels.",
        "salary_min": 25000, "salary_max": 65000, "demand": "Moderate", "industry": "Education",
        "progression": ["Dance Assistant", "Dance Instructor", "Senior Instructor", "Studio Director", "Academy Owner"],
        "certifications": ["Certified Dance Instructor (CDI)", "Zumba Instructor", "RAD Teaching Certificate", "ISTD Diploma"],
        "courses": ["https://www.udemy.com/topic/dance", "https://www.skillshare.com/browse/dance"]
    },
    {
        "job_title": "Actor / Performer",
        "skills": "acting, improvisation, script reading, character development, voice modulation, stage presence, emotional expression, audition skills, physical performance, dialogue delivery",
        "education": "associate", "interests": "acting, theatre, film, performing arts, storytelling, creativity, entertainment", "experience": "junior",
        "description": "Performs roles in theatre, film, television, and digital media through acting and character embodiment.",
        "salary_min": 25000, "salary_max": 200000, "demand": "Moderate", "industry": "Performing Arts",
        "progression": ["Extra / Background Actor", "Supporting Actor", "Lead Actor", "Film Actor", "Celebrity / Star"],
        "certifications": ["Acting Diploma (FTII)", "NSD Certification", "Screen Actors Guild"],
        "courses": ["https://www.coursera.org/learn/acting", "https://www.masterclass.com/categories/film-tv"]
    },
    {
        "job_title": "Theatre Director",
        "skills": "directing, script analysis, choreography, production management, casting, creative vision, communication, stage design, rehearsal direction, team leadership, storytelling",
        "education": "bachelor", "interests": "theatre, directing, performing arts, storytelling, creativity, literature, production", "experience": "senior",
        "description": "Oversees the artistic vision and execution of theatrical productions from casting to final performance.",
        "salary_min": 35000, "salary_max": 120000, "demand": "Moderate", "industry": "Performing Arts",
        "progression": ["Assistant Director", "Stage Manager", "Director", "Senior Director", "Artistic Director"],
        "certifications": ["NSD Directing Diploma", "FTII Direction Course", "Theatre Arts Degree"],
        "courses": ["https://www.coursera.org/learn/theatre", "https://www.edx.org/learn/performing-arts"]
    },
    {
        "job_title": "Event Choreographer",
        "skills": "choreography, dancing, event management, client coordination, music selection, performance staging, team management, creativity, stage production, budgeting, dance styles",
        "education": "associate", "interests": "dancing, events, choreography, music, performing arts, creativity, entertainment", "experience": "mid",
        "description": "Designs and directs dance performances for corporate events, weddings, film productions, and entertainment shows.",
        "salary_min": 35000, "salary_max": 100000, "demand": "Moderate", "industry": "Events & Entertainment",
        "progression": ["Backup Dancer", "Event Dancer", "Event Choreographer", "Senior Choreographer", "Production Director"],
        "certifications": ["Event Management Certification", "Choreography Diploma", "Dance Academy Certificate"],
        "courses": ["https://www.udemy.com/topic/event-management", "https://www.skillshare.com/browse/dance"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # MUSIC & LIVE PERFORMANCE
    # ══════════════════════════════════════════════════════════════════════════
    {
        "job_title": "Singer / Vocalist",
        "skills": "singing, vocal training, music theory, performance, stage presence, pitch control, breath control, recording, microphone technique, music composition, language skills",
        "education": "associate", "interests": "singing, music, performing arts, entertainment, creativity, storytelling, concerts", "experience": "mid",
        "description": "Performs vocal music across genres including classical, pop, film, and folk for live audiences and recordings.",
        "salary_min": 25000, "salary_max": 300000, "demand": "Moderate", "industry": "Performing Arts",
        "progression": ["Chorus Singer", "Playback Singer", "Live Performer", "Recording Artist", "Music Celebrity"],
        "certifications": ["Classical Music Diploma", "Hindustani/Carnatic Music Certificate", "Berklee Online Music"],
        "courses": ["https://www.berklee.edu/online", "https://www.coursera.org/learn/music"]
    },
    {
        "job_title": "Live Event Manager",
        "skills": "event planning, stage management, vendor coordination, budgeting, logistics, sound and lighting, artist management, ticketing, marketing, crisis management, team leadership",
        "education": "bachelor", "interests": "events, music, concerts, entertainment, organizing, performing arts, management", "experience": "mid",
        "description": "Plans and executes live events including concerts, festivals, and corporate shows from concept to execution.",
        "salary_min": 40000, "salary_max": 120000, "demand": "High", "industry": "Events & Entertainment",
        "progression": ["Event Coordinator", "Event Manager", "Senior Event Manager", "Director of Events", "CEO Event Agency"],
        "certifications": ["CMP (Certified Meeting Professional)", "CSEP", "Event Management Diploma"],
        "courses": ["https://www.coursera.org/learn/event-management", "https://www.udemy.com/topic/event-management"]
    },
    {
        "job_title": "Music Teacher / Trainer",
        "skills": "music theory, instrument training, singing coaching, ear training, music composition, curriculum design, patience, communication, performance coaching, rhythm, notation",
        "education": "bachelor", "interests": "music, teaching, instruments, singing, performing arts, mentoring, creativity", "experience": "junior",
        "description": "Teaches music theory, instruments, and vocal skills to students in schools, academies, or private sessions.",
        "salary_min": 25000, "salary_max": 70000, "demand": "Moderate", "industry": "Education",
        "progression": ["Music Tutor", "Music Teacher", "Senior Music Teacher", "Head of Music", "Music Academy Director"],
        "certifications": ["Trinity Music Teaching Certificate", "ABRSM Teaching Diploma", "Berklee Music Education"],
        "courses": ["https://www.berklee.edu/online", "https://www.coursera.org/learn/music-teaching"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SPORTS (PROFESSIONAL & COACHING)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "job_title": "Professional Athlete",
        "skills": "sport-specific skills, physical fitness, discipline, teamwork, competitive mindset, strength training, strategy, injury recovery, mental toughness, game tactics",
        "education": "associate", "interests": "sports, fitness, competition, teamwork, athletics, health, discipline", "experience": "senior",
        "description": "Competes professionally in a sport at club or national level, training full-time to achieve peak performance.",
        "salary_min": 30000, "salary_max": 5000000, "demand": "Moderate", "industry": "Sports & Fitness",
        "progression": ["Amateur Athlete", "Semi-Pro", "Professional Athlete", "National Player", "International / Celebrity Athlete"],
        "certifications": ["National Sports Federation Certification", "NSCA CSCS", "Sports Governing Body License"],
        "courses": ["https://www.coursera.org/learn/sports-performance", "https://www.udemy.com/topic/sports"]
    },
    {
        "job_title": "Yoga Instructor",
        "skills": "yoga, asana practice, pranayama, meditation, anatomy, class planning, mindfulness, communication, flexibility, strength, wellness coaching, spiritual knowledge",
        "education": "associate", "interests": "yoga, wellness, mindfulness, fitness, health, teaching, meditation, spirituality", "experience": "junior",
        "description": "Guides individuals and groups through yoga practices promoting physical health, mindfulness, and wellbeing.",
        "salary_min": 25000, "salary_max": 70000, "demand": "High", "industry": "Sports & Fitness",
        "progression": ["Yoga Student", "Yoga Instructor", "Senior Yoga Teacher", "Yoga Studio Owner", "Wellness Director"],
        "certifications": ["RYT 200 (Yoga Alliance)", "RYT 500", "Yin Yoga Certification", "Prenatal Yoga Certification"],
        "courses": ["https://www.yogaalliance.org", "https://www.udemy.com/topic/yoga"]
    },
    {
        "job_title": "Sports Coach",
        "skills": "coaching methodology, sports tactics, performance analysis, fitness planning, motivation, team management, injury prevention, video analysis, communication, athlete development",
        "education": "bachelor", "interests": "sports, coaching, fitness, strategy, teamwork, leadership, athlete development", "experience": "mid",
        "description": "Trains and mentors athletes or teams to improve performance, tactics, and physical conditioning.",
        "salary_min": 30000, "salary_max": 150000, "demand": "High", "industry": "Sports & Fitness",
        "progression": ["Assistant Coach", "Sports Coach", "Head Coach", "Director of Sport", "National Team Coach"],
        "certifications": ["Level 1/2/3 Coaching Certificate", "NSCA-CSCS", "UEFA/BCCI/AIFF Coaching License"],
        "courses": ["https://www.coursera.org/learn/sports-coaching", "https://www.udemy.com/topic/coaching"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # FASHION, BEAUTY & LIFESTYLE
    # ══════════════════════════════════════════════════════════════════════════
    {
        "job_title": "Fashion Stylist",
        "skills": "styling, fashion trends, wardrobe planning, color coordination, client consultation, shopping, editorial styling, brand knowledge, photography coordination, social media",
        "education": "associate", "interests": "fashion, styling, creativity, art, beauty, trends, photography, media", "experience": "junior",
        "description": "Selects and coordinates clothing and accessories for clients, photo shoots, films, and editorial work.",
        "salary_min": 30000, "salary_max": 150000, "demand": "Moderate", "industry": "Creative",
        "progression": ["Styling Assistant", "Fashion Stylist", "Senior Stylist", "Creative Director of Styling", "Celebrity Stylist"],
        "certifications": ["Fashion Styling Certificate (NIFT)", "London College of Fashion", "Vogue Institute"],
        "courses": ["https://www.coursera.org/learn/fashion", "https://www.udemy.com/topic/fashion-design"]
    },
    {
        "job_title": "Make-up Artist",
        "skills": "makeup application, skincare, color theory, special effects makeup, bridal makeup, editorial makeup, client consultation, product knowledge, photography lighting, hygiene",
        "education": "associate", "interests": "makeup, beauty, art, fashion, creativity, film, photography, skincare", "experience": "entry",
        "description": "Applies makeup for clients in film, TV, weddings, fashion shoots, and personal beauty services.",
        "salary_min": 25000, "salary_max": 120000, "demand": "Moderate", "industry": "Creative",
        "progression": ["Makeup Trainee", "Makeup Artist", "Senior MUA", "Key Makeup Artist", "Celebrity MUA"],
        "certifications": ["CIDESCO Diploma", "VLCC Makeup Certification", "MAC Pro Membership", "NIMA Certification"],
        "courses": ["https://www.udemy.com/topic/makeup", "https://www.skillshare.com/browse/makeup"]
    },
    {
        "job_title": "Model",
        "skills": "posing, runway walking, body language, communication, portfolio development, fitness, fashion knowledge, stage presence, social media, networking, client management",
        "education": "highschool", "interests": "fashion, modeling, photography, fitness, beauty, social media, travel, performing arts", "experience": "entry",
        "description": "Represents brands, designers, and products through photographic, runway, and commercial modeling work.",
        "salary_min": 20000, "salary_max": 500000, "demand": "Moderate", "industry": "Creative",
        "progression": ["Aspiring Model", "Commercial Model", "Fashion Model", "Runway Model", "Supermodel / Brand Ambassador"],
        "certifications": ["Modeling Agency Contract", "Portfolio Development Course", "Runway Training"],
        "courses": ["https://www.udemy.com/topic/modeling", "https://www.skillshare.com/browse/fashion"]
    },
    {
        "job_title": "Fitness Influencer / Wellness Coach",
        "skills": "fitness, nutrition, content creation, social media, video editing, personal training, motivational coaching, instagram, youtube, brand partnerships, community building",
        "education": "associate", "interests": "fitness, wellness, social media, content creation, health, nutrition, dancing, yoga, motivation", "experience": "junior",
        "description": "Builds an online audience by sharing fitness routines, wellness tips, and lifestyle content across platforms.",
        "salary_min": 30000, "salary_max": 300000, "demand": "High", "industry": "Sports & Fitness",
        "progression": ["Fitness Blogger", "Micro Influencer", "Fitness Influencer", "Brand Ambassador", "Wellness Brand Owner"],
        "certifications": ["NASM CPT", "ACE Health Coach", "Precision Nutrition", "Social Media Marketing Certificate"],
        "courses": ["https://www.nasm.org", "https://academy.hubspot.com/courses/social-media"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # COOKING, FOOD & HOSPITALITY
    # ══════════════════════════════════════════════════════════════════════════
    {
        "job_title": "Food Blogger / Recipe Developer",
        "skills": "cooking, food photography, recipe writing, content creation, seo, social media, food styling, video editing, wordpress, brand partnerships, nutrition knowledge",
        "education": "associate", "interests": "cooking, food, blogging, photography, social media, creativity, nutrition, writing", "experience": "entry",
        "description": "Creates and shares original recipes, food photography, and culinary content across blogs and social platforms.",
        "salary_min": 20000, "salary_max": 150000, "demand": "Moderate", "industry": "Creative",
        "progression": ["Home Cook Blogger", "Food Blogger", "Recipe Developer", "Food Content Creator", "Food Brand Owner"],
        "certifications": ["Food Safety Certificate", "Culinary Arts Diploma", "Google Analytics"],
        "courses": ["https://www.udemy.com/topic/food-photography", "https://academy.hubspot.com/courses/content-marketing"]
    },
    {
        "job_title": "Nutritionist / Dietitian",
        "skills": "nutrition science, diet planning, clinical assessment, health coaching, food safety, patient counseling, meal planning, sports nutrition, weight management, research",
        "education": "bachelor", "interests": "nutrition, health, food, cooking, wellness, fitness, helping others, science", "experience": "mid",
        "description": "Assesses clients' dietary habits and designs personalized nutrition plans to improve health outcomes.",
        "salary_min": 35000, "salary_max": 90000, "demand": "High", "industry": "Healthcare",
        "progression": ["Dietetic Intern", "Nutritionist", "Clinical Dietitian", "Senior Dietitian", "Head of Nutrition"],
        "certifications": ["RD (Registered Dietitian)", "CDN", "Sports Nutrition Certification (ISSN)", "INFS Diploma"],
        "courses": ["https://www.coursera.org/learn/nutrition", "https://www.edx.org/learn/nutrition"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # TRAVEL, LANGUAGE & CULTURE
    # ══════════════════════════════════════════════════════════════════════════
    {
        "job_title": "Travel Blogger / Vlogger",
        "skills": "content creation, video editing, travel planning, photography, storytelling, social media, seo, drone photography, writing, brand partnerships, community management",
        "education": "associate", "interests": "travel, writing, photography, social media, culture, adventure, video, blogging", "experience": "entry",
        "description": "Documents travel experiences through blogs, vlogs, and social media content to inspire and inform audiences.",
        "salary_min": 20000, "salary_max": 200000, "demand": "Moderate", "industry": "Media",
        "progression": ["Amateur Travel Blogger", "Travel Content Creator", "Travel Influencer", "Brand Ambassador", "Media Company Owner"],
        "certifications": ["Google Analytics", "Digital Marketing Certificate", "Drone Pilot License"],
        "courses": ["https://creatoracademy.youtube.com", "https://academy.hubspot.com/courses/content-marketing"]
    },
    {
        "job_title": "Translator / Interpreter",
        "skills": "multilingual communication, translation, interpretation, cultural knowledge, technical writing, proofreading, localization, legal translation, medical translation, attention to detail",
        "education": "bachelor", "interests": "languages, culture, writing, communication, travel, international affairs, linguistics", "experience": "junior",
        "description": "Converts written or spoken content between languages while preserving meaning, tone, and cultural context.",
        "salary_min": 30000, "salary_max": 90000, "demand": "High", "industry": "Media",
        "progression": ["Junior Translator", "Translator", "Senior Translator", "Lead Interpreter", "Translation Manager"],
        "certifications": ["ATA Certification", "BCI Interpreter Certificate", "ISO 17100 Translator"],
        "courses": ["https://www.coursera.org/learn/translation", "https://www.udemy.com/topic/translation"]
    },
    {
        "job_title": "Tour Guide",
        "skills": "tourism knowledge, communication, local history, multiple languages, customer service, storytelling, geography, group management, cultural awareness, first aid",
        "education": "associate", "interests": "travel, history, culture, tourism, communication, geography, people, adventure", "experience": "entry",
        "description": "Leads tourists through destinations sharing historical, cultural, and geographical insights.",
        "salary_min": 20000, "salary_max": 60000, "demand": "Moderate", "industry": "Hospitality",
        "progression": ["Tour Assistant", "Tour Guide", "Senior Guide", "Tour Manager", "Tourism Director"],
        "certifications": ["IATA Tour Guide Certificate", "Tourism Board License", "First Aid Certification"],
        "courses": ["https://www.coursera.org/learn/tourism-management", "https://www.udemy.com/topic/tourism"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # PSYCHOLOGY, PHILOSOPHY & SOCIAL SCIENCES
    # ══════════════════════════════════════════════════════════════════════════
    {
        "job_title": "Psychologist",
        "skills": "psychological assessment, therapy, cognitive behavioral therapy, research, report writing, diagnosis, empathy, active listening, statistical analysis, patient management",
        "education": "master", "interests": "psychology, mental health, research, human behavior, helping others, counseling, science", "experience": "mid",
        "description": "Studies human behavior and mental processes to diagnose and treat emotional, behavioral, and mental disorders.",
        "salary_min": 50000, "salary_max": 130000, "demand": "Very High", "industry": "Healthcare",
        "progression": ["Psychology Intern", "Junior Psychologist", "Psychologist", "Senior Psychologist", "Clinical Director"],
        "certifications": ["RCI License", "BPS Membership", "PhD Psychology", "NIMHANS Diploma"],
        "courses": ["https://www.coursera.org/learn/introduction-psychology", "https://www.edx.org/learn/psychology"]
    },
    {
        "job_title": "Life Coach",
        "skills": "coaching, active listening, goal setting, motivational interviewing, communication, empathy, behavioral change, mindfulness, personal development, business coaching",
        "education": "bachelor", "interests": "helping others, psychology, motivation, personal development, communication, wellness, leadership", "experience": "mid",
        "description": "Helps clients achieve personal and professional goals through structured coaching and accountability.",
        "salary_min": 30000, "salary_max": 120000, "demand": "High", "industry": "Social Services",
        "progression": ["Coaching Intern", "Life Coach", "Senior Life Coach", "Executive Coach", "Coaching Business Owner"],
        "certifications": ["ICF ACC/PCC Certification", "Tony Robbins Coach", "CPCC", "NLP Practitioner"],
        "courses": ["https://coachingfederation.org", "https://www.udemy.com/topic/life-coaching"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # CRAFTS, DIY & TRADES
    # ══════════════════════════════════════════════════════════════════════════
    {
        "job_title": "Carpenter / Woodworker",
        "skills": "woodworking, carpentry, blueprint reading, hand tools, power tools, joinery, furniture making, measurements, finishing, safety protocols, material selection",
        "education": "highschool", "interests": "woodworking, crafts, building, design, hands-on, construction, creativity, diy", "experience": "junior",
        "description": "Constructs and repairs wooden structures, furniture, and fixtures using hand and power tools.",
        "salary_min": 25000, "salary_max": 70000, "demand": "Moderate", "industry": "Skilled Trades",
        "progression": ["Apprentice Carpenter", "Carpenter", "Senior Carpenter", "Master Carpenter", "Construction Contractor"],
        "certifications": ["NCCER Carpentry Certification", "City and Guilds Carpentry", "OSHA 10-Hour"],
        "courses": ["https://www.nccer.org", "https://www.udemy.com/topic/woodworking"]
    },
    {
        "job_title": "Jewellery Designer",
        "skills": "jewellery design, gemology, cad (rhino/matrix), sketching, metalworking, stone setting, brand development, trend awareness, client consultation, costing",
        "education": "associate", "interests": "jewellery, design, crafts, art, fashion, creativity, gemstones, aesthetics", "experience": "junior",
        "description": "Designs and creates jewellery pieces from concept sketches through production for retail or bespoke clients.",
        "salary_min": 25000, "salary_max": 100000, "demand": "Moderate", "industry": "Creative",
        "progression": ["Jewellery Trainee", "Jewellery Designer", "Senior Designer", "Creative Lead", "Brand Owner"],
        "certifications": ["GIA Graduate Gemologist", "JDA Diploma", "Rhino Jewellery CAD Certificate"],
        "courses": ["https://www.gia.edu", "https://www.udemy.com/topic/jewelry-design"]
    },
    {
        "job_title": "Tattoo Artist",
        "skills": "tattooing, illustration, drawing, color theory, skin knowledge, hygiene, client consultation, custom design, stenciling, shading, linework",
        "education": "highschool", "interests": "art, drawing, tattoos, creativity, fashion, design, culture, body art", "experience": "junior",
        "description": "Creates custom tattoo designs and applies them to clients using professional tattooing equipment.",
        "salary_min": 25000, "salary_max": 150000, "demand": "Moderate", "industry": "Creative",
        "progression": ["Tattoo Apprentice", "Tattoo Artist", "Senior Tattoo Artist", "Studio Owner", "Celebrity Tattoo Artist"],
        "certifications": ["Blood-Borne Pathogen Certification", "Tattoo License (state)", "Health Department Permit"],
        "courses": ["https://www.udemy.com/topic/tattooing", "https://www.skillshare.com/browse/illustration"]
    },
]