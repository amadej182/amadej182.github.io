from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    technologies = [
        'Python', 'JavaScript', 'html5', 'css3', 'C', 'cplusplus',
        'Arduino', 'Raspberry Pi', 'NumPy', 'Pandas',
        'TensorFlow', 'Keras', 'Plotly', 'Matplotlib', 'PyTorch', 'sqlite', 'git', 'unity',
        'amazonwebservices', 'Docker'
    ]
    return render(request, 'main.html', {'technologies': technologies})

def projects(request):
    projects = [
        {
            'title': 'Traffic Sign Recognition and Overspeed Warning System',
            'description': 'Developed a traffic sign recognition and overspeed warning system using computer vision techniques. Methodology included image processing, feature extraction, and machine learning using Raspberry Pi and Arduino Uno.',
            'technologies': ['Python', 'TensorFlow', 'Yolo'],
            'images': ['jpeg/traffic/res50.png', 'jpeg/traffic/Screenshot from 2024-02-06 15-19-56.png']
        },
        {
            'title': 'Quality Control System for Manufacturing',
            'description': 'Developed a machine learning model for quality control in manufacturing process. Software identifies defects in products using images captured by an industrial camera.',
            'technologies': ['Python', 'Pandas', 'TensorFlow', 'Keras', 'Industrial Camera', 'PLC Programming'],
            'images': ['jpeg/nssm/NSSM.png', 'jpeg/nssm/NSSM_2.png']
        },
        {
            'title': 'Software for Simulation of Dynamic Systems',
            'description': 'Developed a software tool for simulating dynamic systems using Python. Software was tested using ANSYS Software.',
            'technologies': ['Python', 'ANSYS'],
            'images': ['jpeg/dinamika/pomiki_konstrukcije_2.png', 'jpeg/dinamika/1.png', 'jpeg/dinamika/primerjava_lastnih_oblik_2.png']
        },
        {
            'title': 'NAS System',
            'description': '3D printed case for NAS System and Raspberry Pi. The case was designed using Onshape and 3D printed using PLA filament. The system is used for storing and sharing files over a network.',
            'technologies': ['Python', 'onshape', 'Raspberry Pi'],
            'images': ['jpeg/onshape.png']
        },
        {
            'title': 'Simulation Software for Biogas Plant',
            'description': 'Developed a simulation environment for biogas plant operations using Python.',
            'technologies': ['Python', 'NumPy', 'Matplotlib', 'SciPy'],
            'images': ['jpeg/mnz/realni_2.png', 'jpeg/mnz/realni_3.png']
        },
        {
            'title': 'Alarm System for Home Automation',
            'description': 'Designed and implemented an alarm system for home automation using Arduino and Python. The system was developed for Arduino Uno and communicates with other devices using 433 MHz RF modules.',
            'technologies': ['Arduino', 'C'],
            'images': ['jpeg/alarm/alarm.jpg', 'jpeg/alarm/MPKM_seminarska_SFC.png', 'jpeg/alarm/vezje_shema.png']
        },
        {
            'title': 'Peltrier Module Simulation and Optimization',
            'description': 'Analyzed and optimized thermodynamic cycles using Python and NumPy.',
            'technologies': ['Python', 'NumPy', 'Matplotlib', 'SciPy'],
            'images': ['jpeg/term/Q.png', 'jpeg/term/zahtevana_temp.png']
        },
        {
            'title': 'Heat Cycle Simulation',
            'description': 'Developed a simulation tool for simulating heat cycles of a Heat Pump and calculating effective COP.',
            'technologies': ['Python', 'NumPy', 'Plotly'],
            'images': ['jpeg/term/cikel.png', 'jpeg/term/COP_T_diff.png', 'jpeg/term/moc_komp.png']
        },

    ]


    return render(request, 'projects.html', {'projects': projects})

def education(request):
    schools = [
        {
            'school': 'Faculty of Mechanical Engineering, University of Ljubljana',
            'degree': 'Master of Science in Mechanical Engineering',
            'year': '2022 - 2025',
            'description': 'Focused on advanced mechanical systems, simulations, robotics, and machine learning.',
            'EQF_level': '7',
            'image': 'jpeg/fs.png'
        },
        {
            'school': 'Faculty of Mechanical Engineering, University of Ljubljana',
            'degree': 'Bachelor of Science in Mechanical Engineering',
            'year': '2018 - 2022',
            'description': 'Focused on fundamental principles of mechanical engineering, including thermodynamics and fluid mechanics.',
            'EQF_level': '6',
            'image': 'jpeg/fs.png'
        },
        {
            'school': 'Prva gimnazija Maribor',
            'degree': 'High School Diploma',
            'year': '2014 - 2018',
            'description': 'Participated in many extracurricular activities and competed in math, chemistry and logic competitions.',
            'EQF_level': '4',
            'image': 'jpeg/prva_gimn_MB.webp'
        }

    ]
    return render(request, 'education.html', {'educations': schools})