from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__, static_folder=None)

# ============================================================
# BASIS PENGETAHUAN — Knowledge Base Sistem Pakar Karir IT
# Metode: Forward Chaining dengan Certainty Factor
# ============================================================
careers = [
    {
        "name": "Software Engineer",
        "icon": "fa-laptop-code",
        "description": "Kalau kamu sering iseng bikin program kecil-kecilan atau suka debugging sampe larut malem, kemungkinan besar kamu bakal betah jadi Software Engineer. Kerjaannya sehari-hari ya nulis kode, diskusi sama tim soal fitur baru, dan benerin bug yang datang tiba-tiba. Nggak glamor, tapi worth it.",
        "rules": { "programming": 1.0, "logic": 1.0, "troubleshooting": 0.8 },
        "traits": ["Problem Solver", "Detail-oriented", "Logical"],
        "roadmap": {
            "skills": ["Algoritma & Struktur Data", "OOP & Design Patterns", "REST API", "Testing & Debugging"],
            "tools":  ["Git & GitHub", "Docker", "VS Code / IntelliJ", "Postman"],
            "certs":  ["AWS Certified Developer", "Google Associate Cloud Engineer", "Oracle Java SE Certified"]
        }
    },
    {
        "name": "UI/UX Designer",
        "icon": "fa-pen-nib",
        "description": "Kamu tipe yang kalau pakai aplikasi langsung nyadar 'tombolnya nggak enak nih posisinya' atau 'warnanya nggak cocok'. Itu tanda kamu punya insting desain yang bagus. UI/UX Designer itu orangnya yang mastiin pengguna nggak bingung dan nggak frustrasi waktu pakai produk. Figma jadi senjata utamamu.",
        "rules": { "design": 1.0, "aesthetics": 1.0, "empathy": 0.8 },
        "traits": ["Kreatif", "Empatetik", "Visual Thinker"],
        "roadmap": {
            "skills": ["UX Research", "Wireframing", "Desain Visual & Tipografi", "Usability Testing"],
            "tools":  ["Figma", "Adobe XD", "Maze", "Zeplin"],
            "certs":  ["Google UX Design Certificate", "Interaction Design Foundation", "NN/g UX Certification"]
        }
    },
    {
        "name": "Data Scientist",
        "icon": "fa-chart-line",
        "description": "Kamu tipe yang lebih senang tanya 'kenapa bisa gitu ya?' daripada langsung nerima fakta. Data Scientist kerjanya gali-gali data, nyari pola yang nggak keliatan kasatmata, terus jelasin hasilnya ke tim bisnis supaya mereka bisa bikin keputusan yang lebih tepat. Python dan statistik jadi teman setia kamu.",
        "rules": { "data": 1.0, "programming": 0.8, "ai": 0.6 },
        "traits": ["Analitis", "Teliti", "Senang Eksplorasi"],
        "roadmap": {
            "skills": ["Statistika & Probabilitas", "Machine Learning Dasar", "SQL", "Data Visualization"],
            "tools":  ["Python (Pandas, NumPy)", "Jupyter Notebook", "Tableau / Power BI", "Scikit-learn"],
            "certs":  ["IBM Data Science Professional", "Google Data Analytics", "Coursera ML Specialization"]
        }
    },
    {
        "name": "Cybersecurity Analyst",
        "icon": "fa-user-secret",
        "description": "Kamu tipe yang penasaran banget sama cara kerja di balik layar dan seneng mikir dua langkah lebih depan. Cybersecurity Analyst itu kayak detektif di dunia digital — kamu yang nyari lubang di sistem sebelum orang jahat sempat masuk. Skill ini langka, dan banyak perusahaan mau bayar mahal buat orang yang beneran paham.",
        "rules": { "security": 1.0, "infrastructure": 0.7, "programming": 0.4 },
        "traits": ["Waspada", "Investigatif", "Sistematis"],
        "roadmap": {
            "skills": ["Network Security", "Ethical Hacking", "Kriptografi", "Incident Response"],
            "tools":  ["Kali Linux", "Wireshark", "Metasploit", "Nmap"],
            "certs":  ["CompTIA Security+", "CEH (Certified Ethical Hacker)", "CISSP"]
        }
    },
    {
        "name": "DevOps Engineer",
        "icon": "fa-infinity",
        "description": "Kamu orangnya nggak sabaran kalau ngeliat proses yang harusnya bisa diotomasi tapi masih dikerjain manual. DevOps Engineer itu yang mastiin kode dari developer bisa sampe ke server dengan mulus, cepat, dan aman — tanpa drama. Makin banyak startup dan perusahaan gede yang butuh orang kayak gini.",
        "rules": { "infrastructure": 1.0, "programming": 0.7, "security": 0.4 },
        "traits": ["Suka Otomasi", "Efisien", "Systems Thinker"],
        "roadmap": {
            "skills": ["CI/CD Pipeline", "Containerization", "Infrastructure as Code", "Cloud Fundamentals"],
            "tools":  ["Docker & Kubernetes", "Jenkins / GitHub Actions", "Terraform", "Ansible"],
            "certs":  ["AWS DevOps Professional", "Certified Kubernetes Administrator", "HashiCorp Terraform Associate"]
        }
    },
    {
        "name": "Product Manager",
        "icon": "fa-sitemap",
        "description": "Kamu yang paling sering tanya 'ini dibuat buat siapa sih?' waktu ngeliat produk baru. Product Manager itu yang ngejagain supaya tim dev, desainer, dan bisnis jalan ke arah yang sama. Kamu nggak harus bisa coding, tapi harus ngerti cukup buat ngobrol sama semua pihak tanpa salah paham.",
        "rules": { "management": 1.0, "communication": 1.0, "design": 0.4, "data": 0.4 },
        "traits": ["Leader", "Strategis", "Komunikatif"],
        "roadmap": {
            "skills": ["Product Strategy", "Agile & Scrum", "Data-driven Decision", "Stakeholder Management"],
            "tools":  ["Jira / Linear", "Notion", "Mixpanel", "Miro"],
            "certs":  ["Certified Scrum Product Owner", "Google PM Certificate", "PMI-ACP"]
        }
    },
    {
        "name": "AI / ML Engineer",
        "icon": "fa-robot",
        "description": "Kamu penasaran sama cara ChatGPT bisa jawab pertanyaan atau kenapa TikTok bisa tau video apa yang kamu mau tonton. AI/ML Engineer itu yang bikin 'otak'-nya. Kamu bakal banyak ngutak-atik data, coba-coba model, dan seneng kalau akurasi prediksinya naik walau cuma 0.5 persen.",
        "rules": { "ai": 1.0, "programming": 0.9, "data": 0.7 },
        "traits": ["Inovatif", "Research-driven", "Algoritmik"],
        "roadmap": {
            "skills": ["Deep Learning", "NLP & Computer Vision", "MLOps", "Linear Algebra & Kalkulus"],
            "tools":  ["PyTorch / TensorFlow", "Hugging Face", "MLflow", "Google Colab"],
            "certs":  ["TensorFlow Developer Certificate", "DeepLearning.AI Specialization", "AWS ML Specialty"]
        }
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/consult', methods=['POST'])
def consult():
    user_facts = request.get_json()
    if not user_facts or not isinstance(user_facts, dict):
        return jsonify({'error': 'Data tidak valid'}), 400
    results = []
    for career in careers:
        score = 0.0
        max_possible = sum(career['rules'].values())
        for trait, weight in career['rules'].items():
            fact_value = user_facts.get(trait, 0.0)
            try:
                score += float(fact_value) * weight
            except (ValueError, TypeError):
                score += 0.0
        match_pct = round((score / max_possible) * 100, 1) if max_possible > 0 else 0.0
        results.append({
            "name": career["name"],
            "icon": career["icon"],
            "description": career["description"],
            "traits": career["traits"],
            "roadmap": career["roadmap"],
            "score": match_pct
        })
    results.sort(key=lambda x: x['score'], reverse=True)
    return jsonify(results)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
