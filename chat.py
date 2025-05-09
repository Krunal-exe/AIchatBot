import base64
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

def generate(input_text):
    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY"),
    )

    model = "gemini-2.0-pro-exp-02-05"

    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""hello"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Hello! I'm here to help you with any questions you have about institute transfers within Gujarat Technological University (GTU) affiliated Self-Financed Institutes (SFIs). I have the guidelines here, so feel free to ask me anything! I will provide you with clear, simple, and pinpointed answers.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""which semester i can change my collage in?
"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Here's the breakdown of when you can change your college within GTU:

*   **General Rule:** You can apply for an institute transfer from the **3rd semester onwards** of your program.

*   **Last Semester Restriction:** You *cannot* apply for a transfer if you are in the **last semester** of your program.

*   **Special Case (1st Semester):** You can apply for a transfer in the **1st semester, after the admission process is over,** *only* if one of your parents (father or mother) has passed away.

**In simple words:** Normally, you start applying from your 3rd semester. You can't change in your very last semester. There's a special exception for 1st-semester transfers if a parent has passed away.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=f"""{input_text}"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=0.2,
        top_p=0.95,
        top_k=64,
        max_output_tokens=8192,
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""You are a help assistant for the students in Gujarat Technological University(GTU), which provides the students assistance and help regarding the student college transfer the rules as follows :

The following guidelines are applicable for seeking transfer within GTU affiliated Self
Financed institutes (SFI).

Guidelines of Institute Transfer: 
1) Students can apply for institute (SFI) transfer from 3rd semester onwards of respective 
program. Student Studying in last semester of a program will not be allowed to apply for 
the transfer. 
 
2) Students may apply for the institute (SFI) transfer, in the 1 st semester, after the admission 
process is over, only in the case of demise of his/her parent (father/ mother). 
 
3) Students who have taken admission on Tuition Fees Waiver (TFW) seats or are detained 
and/or penalized under UFM Rules (excluding the applicant‟s Detained or UFM status of 
current semester) should not apply for institute (SFI) transfer, since such applications will 
not be considered for transfer and no intimation will be sent to such applicants. 
 
4) A student can apply for Institute (SFI) transfer when the Online Portal is opened for 
accepting applications for institute transfer (http://www.gtu.ac.in/InstituteTransfer.aspx). 
The Online Portal shall be kept open for certain time duration. The online portal will 
remain open from 25/04/2018 to 31/05/2018. 
 
5) The Institute (SFI) transfer shall be granted to those eligible students who have applied 
through the Online Portal only.  Any application submitted without applying through the 
Online Portal, will be summarily rejected. 
 
6)  Student will not be transferred from shift 1 to shift 2 or vice versa in the same institute.  
 
7) As soon as the student is declared as “transferred” by means of a transfer order; the parent 
institute shall officially transfer the attendance and all academic records of respective 
semester(s) (including the current semester) to the receiving institute. 
 
8) The academic record-keeping of the transferred student shall be the responsibility of the 
receiving institute. 
 
9) The transfer of any student from any Institute (SFI) will be as per the norms of the 
respective statutory councils such as Pharmacy Council of India (PCI), Council of 
Architecture (COA), etc. Hence, the transfer process will strictly follow the respective Statutory Council‟s Norms prevailing from time to time. For example, the Students, 
studying in the Institute having no approval of PCI, will not be eligible to get transfer in 
the other Institution and vice versa. 

10) Transfer will not be given to those students who have already taken transfer before. 
 
11)  The receiving Institute shall issue the „No objection Certificate‟ to the student only if the 
seats are vacant in the respective branch/course. Institute has to issue N.O.C on original 
letter head with the signature and stamp of Principal/Director/head of institute .The Name 
of the signatory has to be printed below the signature. The Format is given in Annexure I. 
 
12) List of documents to be submitted by the receiving institute to the university is as below. 
(After the transfer order is issued on GTU Website) 
a) The detailed table stating status of available vacant seat branch-wise and semester 
wise at the Institute   
b) Original Joining Report of every individual transferred student in his/her own 
handwriting.  
c) New Enrollment Form of every individual transferred student  
d)  Copy of Bank Challan of the Enrollment Fees of all transferred student  
e) Letter of undertaking regarding strict adherence to the institute/college transfer rules 
and the sanctioned intake. The format is given in Annexure  II 
13) The Principal/Director/head of institute shall give the declaration of number of    N.O.Cs 
issued for the purpose of student transferred from/ to his/her institute. The format of 
declaration is to be given on a stamp paper of Rs.100 is given in Annexure III.
                                 
here is the list of diploma collages which are affiliated by GTU or come under GTU : 
    # GTU Diploma Engineering Institute Data (2024-25)

# Data Format Description:

# Each institute is represented by a block of data.
# Key-value pairs are used, with the key followed by a colon and the space, then the value.
#  - 'Institute Code' is a unique numerical identifier.
#  - 'Zone' is a numerical grouping.
#  - 'Institute Name' is the full name of the institute.
#  - 'Address' is the physical address.
#  - 'District' is the district in Gujarat.
#  - 'Institute Type' is either 'Govt.' (Government), 'Private-SFI' (Private Self-Financed), or 'PPP'(Public-Private Partnership).
#  - 'Contact No' is the phone number.
#  - 'Mail Id' is the email address.
#  - 'Courses' is a list of courses offered, each with:
#     - 'Course Name'
#     - 'AICTE Intake 2024-25'
#     - 'GTU Intake 2024-25'

# Data:
Institute Code: 609
Zone: 1
Institute Name: C.U.Shah Polytechnic
Address: Near Boda Talav, G.I.D.C area, Wadhwan City, Surendranagar-363035
District: Surendranagar
Institute Type: Govt.
Contact No: 9099063209
Mail Id: dec609owner@gtu.edu.in
Courses:
  - Course Name: Automobile Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
  - Course Name: Computer Engineering, AICTE Intake 2024-25: 120, GTU Intake 2024-25: 120
  - Course Name: Civil Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
  - Course Name: Mechanical Engineering, AICTE Intake 2024-25: 90, GTU Intake 2024-25: 90
  - Course Name: Electrical Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
  - Course Name: Computer Aided Costume Design and Dress Making, AICTE Intake 2024-25: 30, GTU Intake 2024-25: 30
  - Course Name: Mechanical Engineering (CAD/CAM), AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60

Institute Code: 614
Zone: 1
Institute Name: Government Polytechnic for Girls
Address: Opp. Physical Research Laboratory, Nr.Atira, Navrangpura, Ahmedabad -380015.
District: Ahmedabad
Institute Type: Govt.
Contact No: 9099063214
Mail Id: dec614owner@gtu.edu.in
Courses:
  - Course Name: Biomedical Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
  - Course Name: Computer Engineering, AICTE Intake 2024-25: 120, GTU Intake 2024-25: 120
  - Course Name: Electronics and Communications Engineering, AICTE Intake 2024-25: 30, GTU Intake 2024-25: 30
  - Course Name: Computer Aided Costume Design and Dress Making, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
  - Course Name: Information Technology, AICTE Intake 2024-25: 120, GTU Intake 2024-25: 120
  - Course Name: Civil Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
  - Course Name: Information and communication Technology, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60

Institute Code: 617
Zone: 1
Institute Name: Government Polytechnic, Ahmedabad
Address: Nr. Panjrapol Char Rasta, Ambawadi, Ahmedabad-380015
District: Ahmedabad
Institute Type: Govt.
Contact No: 9099063217
Mail Id: dec617owner@gtu.edu.in
Courses:
    - Course Name: Information Technology, AICTE Intake 2024-25: 122, GTU Intake 2024-25: 122
    - Course Name: Information and communication Technology, AICTE Intake 2024-25: 30, GTU Intake 2024-25: 30
    - Course Name: Instrumentation and Control Engineering, AICTE Intake 2024-25: 123, GTU Intake 2024-25: 123
    - Course Name: Mechanical Engineering, AICTE Intake 2024-25: 123, GTU Intake 2024-25: 123
    - Course Name: Biomedical Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
    - Course Name: Computer Engineering, AICTE Intake 2024-25: 183, GTU Intake 2024-25: 183
    - Course Name: Electronics & Communication Engg, AICTE Intake 2024-25: 152, GTU Intake 2024-25: 152
    - Course Name: Plastic Engineering(Sandwich Pattern), AICTE Intake 2024-25: 63, GTU Intake 2024-25: 63
    - Course Name: Electrical Engineering, AICTE Intake 2024-25: 123, GTU Intake 2024-25: 123
    - Course Name: Automobile Engineering, AICTE Intake 2024-25: 183, GTU Intake 2024-25: 183
    - Course Name: Civil Engineering, AICTE Intake 2024-25: 123, GTU Intake 2024-25: 123
    - Course Name: Mechanical Engineering (CAD/CAM), AICTE Intake 2024-25: 120, GTU Intake 2024-25: 120
    - Course Name: Automation and robotics, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60

Institute Code: 632
Zone: 1
Institute Name: SWAMI KRISHNAJIVANDASJI INSTITUTE OF TECHNOLOGY
Address: Hansalpur- Sokli Road, Nr Narmada Canal, Hansalpur, Ta: Viramgam, Dist: Ahmedbad-382150
District: Ahmedabad
Institute Type: Private-SFI
Contact No: 9099063232
Mail Id: dec632owner@gtu.edu.in
Courses:
  - Course Name: Automobile Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
  - Course Name: Computer Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
  - Course Name: Civil Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
  - Course Name: Mechanical Engineering, AICTE Intake 2024-25: 90, GTU Intake 2024-25: 90

Institute Code: 640
Zone: 1
Institute Name: R. C. TECHNICAL INSTITUTE
Address: Opp. Gujarat High Court, S.G. Highway, Sola, Ahmedabad-380060
District: Ahmedabad
Institute Type: Govt.
Contact No: 9099063240
Mail Id: dec640owner@gtu.edu.in
Courses:
 - Course Name: Civil Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
 - Course Name: Textile Processing Technology, AICTE Intake 2024-25: 30, GTU Intake 2024-25: 30
 - Course Name: Information Technology, AICTE Intake 2024-25: 180, GTU Intake 2024-25: 180
 - Course Name: Textile Manufacturing and Technology, AICTE Intake 2024-25: 30, GTU Intake 2024-25: 30
 - Course Name: Mechanical Engineering, AICTE Intake 2024-25: 240, GTU Intake 2024-25: 240
 - Course Name: Electrical Engineering, AICTE Intake 2024-25: 240, GTU Intake 2024-25: 240
 - Course Name: Computer Engineering, AICTE Intake 2024-25: 240, GTU Intake 2024-25: 240
 - Course Name: Printing Technology, AICTE Intake 2024-25: 30, GTU Intake 2024-25: 30
 - Course Name: Information & Communication Technology, AICTE Intake 2024-25: 30, GTU Intake 2024-25: 30
 - Course Name: Automobile Engineering, AICTE Intake 2024-25: 92, GTU Intake 2024-25: 92
 - Course Name: Electronics and Communications Engg, AICTE Intake 2024-25: 30, GTU Intake 2024-25: 30

Institute Code: 649
Zone: 1
Institute Name: SIR BHAVSINHJI POLYTECHNIC INSTITUTE
Address: Opp. Valiya Arts College, Vidhyanagar, Bhavnagar-364002
District: Bhavnagar
Institute Type: Govt.
Contact No: 9099063249
Mail Id: dec649owner@gtu.edu.in
Courses:
- Course Name: Civil Engineering, AICTE Intake 2024-25: 182, GTU Intake 2024-25: 182
- Course Name: Electrical Engineering, AICTE Intake 2024-25: 152, GTU Intake 2024-25: 152
- Course Name: Chemical Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
- Course Name: Information Technology, AICTE Intake 2024-25: 184, GTU Intake 2024-25: 184
- Course Name: Mechanical Engineering, AICTE Intake 2024-25: 182, GTU Intake 2024-25: 182
- Course Name: Textile Manufacturing Technology, AICTE Intake 2024-25: 30, GTU Intake 2024-25: 30
- Course Name: Fabrication Technology, AICTE Intake 2024-25: 30, GTU Intake 2024-25: 30
- Course Name: Computer Aided Costume Design and Dress Making, AICTE Intake 2024-25: 30, GTU Intake 2024-25: 30
- Course Name: Mechanical Engineering (CAD/CAM), AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60

Institute Code: 664
Zone: 1
Institute Name: Atul Polytechnic
Address: At& Post-Khadat Mahudi Road, Near Psl Factory, Ta-Mansa, Dist-Gandhinagar-382855.
District: Gandhinagar
Institute Type: Private-SFI
Contact No: 9099063264
Mail Id: dec664owner@gtu.edu.in
Courses:
- Course Name: Civil Engineering, AICTE Intake 2024-25: 120, GTU Intake 2024-25: 120
- Course Name: Mechanical Engineering, AICTE Intake 2024-25: 120, GTU Intake 2024-25: 120
- Course Name: Electrical Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
- Course Name: Automobile Engineering, AICTE Intake 2024-25: 120, GTU Intake 2024-25: 120
- Course Name: Computer Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
- Course Name: Electronics & Communication Engg, AICTE Intake 2024-25: 30, GTU Intake 2024-25: 0

Institute Code: 698
Zone: 1
Institute Name: Shri J M Sabva Inst Of Engg & Tech
Address: ARADHANA EDUCATIONAL CAMPUS, BHAVNAGAR ROAD, BOTAD-364710
District: BOTAD
Institute Type: SFI
Contact No: 9099063446
Mail Id: dec698owner@gtu.edu.in
Courses:
- Course Name: No Admission Zone for A.Y. 2024-25

Institute Code: 985
Zone: 1
Institute Name: Bhavnagar Polytechnic Institute
Address: Behind Dhammapaali Vipassana Center, Near Palitana, Todi Village, Taluka Sihor, District Bhavnagar
District: Bhavnagar
Institute Type: Private-SFI
Contact No: 7574843599
Mail Id: dec985owner@gtu.edu.in
Courses:
- Course Name: Civil Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
- Course Name: Electrical Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
- Course Name: Mechanical Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
- Course Name: Computer Engineering, AICTE Intake 2024-25: 120, GTU Intake 2024-25: 120

Institute Code: 451
Zone: 1
Institute Name: Sal Institute of Diploma Studies
Address: Opp. Science City, Sola Road, Ahmedabad-380060
District: Ahmedabad
Institute Type: Private-SFI
Contact No: 9825094982
Mail Id: dec451owner@gtu.edu.in
Courses:
- Course Name: Computer Engineering, AICTE Intake 2024-25: 180, GTU Intake 2024-25: 180
- Course Name: Information Technology, AICTE Intake 2024-25: 120, GTU Intake 2024-25: 120
- Course Name: Computer Science and Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60

Institute Code: 455
Zone: 1
Institute Name: APOLLO INSTITUTE OF ENGGINEERING &
Address: C/O Snme Campus, At: Anasan, Near S. P. Ring Road Circle, Naroda-
District: Ahmedabad
Institute Type: Private-SFI
Contact No: 02718240233
Mail Id: dec455owner@gtu.edu.in
Courses:
- Course Name: Computer Engineering, AICTE Intake 2024-25: 150, GTU Intake 2024-25: 150
- Course Name: Mechanical Engineering, AICTE Intake 2024-25: 30, GTU Intake 2024-25: 30
- Course Name: Automobile Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 0
- Course Name: Civil Engineering, AICTE Intake 2024-25: 120, GTU Intake 2024-25: 60

Institute Code: 613
Zone: 2
Institute Name: EXCEL INSTITUTE OF DIPLOMA STUDIES
Address: Block No.:224, Nr. Amrit Hotel, At:Ola.Po:Ishand. Ta: Kalol, Dist Gandhinagar-382721
District: Gandhinagar
Institute Type: Private-SFI
Contact No: 9099063213
Mail Id: dec613owner@gtu.edu.in
Courses:
- Course Name: Computer Engineering, AICTE Intake 2024-25: 120, GTU Intake 2024-25: 120
- Course Name: Electrical Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
- Course Name: Electronics and Communications Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 0
- Course Name: Mechanical Engineering, AICTE Intake 2024-25: 180, GTU Intake 2024-25: 120

Institute Code: 623
Zone: 2
Institute Name: Government Polytechnic, Gandhinagar
Address: Sector-26, GIDC Electronics Estate, K-6 Circle, Gandhinagar - 382044.
District: Gandhinagar
Institute Type: Govt.
Contact No: 9099063223
Mail Id: dec623owner@gtu.edu.in
Courses:
- Course Name: Information Technology, AICTE Intake 2024-25: 180, GTU Intake 2024-25: 180
- Course Name: Biomedical Engineering, AICTE Intake 2024-25: 120, GTU Intake 2024-25: 120
- Course Name: Chemical Engineering, AICTE Intake 2024-25: 180, GTU Intake 2024-25: 180
- Course Name: Computer Engineering, AICTE Intake 2024-25: 180, GTU Intake 2024-25: 180
- Course Name: Electrical Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
- Course Name: Electronics and Communications Engineering, AICTE Intake 2024-25: 30, GTU Intake 2024-25: 30
- Course Name: Instrumentation and Control Engineering, AICTE Intake 2024-25: 30, GTU Intake 2024-25: 30
- Course Name: Automation and Robotics, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
- Course Name: Civil Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
- Course Name: Information & communication Technology, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
- Course Name: Mechanical Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
- Course Name: Metallurgy, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60

Institute Code: 624
Zone: 2
Institute Name: Government Polytechnic, Himatnagar
Address: Gadhoda Road, Motipura, Himatnagar, Sabarkantha-383001
District: Himatnagar
Institute Type: Govt.
Contact No: 9099063224
Mail Id: dec624owner@gtu.edu.in
Courses:
- Course Name: Automobile Engineering, AICTE Intake 2024-25: 30, GTU Intake 2024-25: 30
- Course Name: Civil Engineering, AICTE Intake 2024-25: 90, GTU Intake 2024-25: 90
- Course Name: Computer Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
- Course Name: Electrical Engineering, AICTE Intake 2024-25: 90, GTU Intake 2024-25: 90
- Course Name: Information Technology, AICTE Intake 2024-25: 150, GTU Intake 2024-25: 150
- Course Name: Mechanical Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
- Course Name: Computer Aided Costume Design and Dress Making, AICTE Intake 2024-25: 30, GTU Intake 2024-25: 30
- Course Name: Renewable Energy, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60

Institute Code: 626
Zone: 2
Institute Name: Government Polytechnic Palanpur
Address: Government Polytechnic Palanpur, Outside Malan Gate, Ambaji Road, Palanpur, Banaskantha-385001
District: Palanpur
Institute Type: Govt.
Contact No: 9099063226
Mail Id: dec626owner@gtu.edu.in
Courses:
- Course Name: Civil Engineering, AICTE Intake 2024-25: 90, GTU Intake 2024-25: 90
- Course Name: Information Technology, AICTE Intake 2024-25: 30, GTU Intake 2024-25: 30
- Course Name: Electrical Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
- Course Name: Electronics & Communication Engg, AICTE Intake 2024-25: 30, GTU Intake 2024-25: 30
- Course Name: Mechanical Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
- Course Name: Information & communication Technology, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60

Institute Code: 628
Zone: 2
Institute Name: GOVERMENT POLYTECHNIC
Address: B/H S.T.Workshop, Vadnagar, Dist. Mehsana-384355
District: Mehsana
Institute Type: Govt.
Contact No: 9099063228
Mail Id: dec628owner@gtu.edu.in
Courses:
- Course Name: Computer Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
- Course Name: Mechanical Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
- Course Name: Information & communication Technology, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
- Course Name: Civil Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60

Institute Code: 631
Zone: 2
Institute Name: Kilachand Devchand Polytechnic
Address: Near Hemchandracharya North Gujarat University, Opp. T.B.Hospital, University Road, Patan-384265
District: Patan
Institute Type: Govt.
Contact No: 9099063231
Mail Id: dec631owner@gtu.edu.in
Courses:
- Course Name: Civil Engineering, AICTE Intake 2024-25: 120, GTU Intake 2024-25: 120
- Course Name: Mechanical Engineering, AICTE Intake 2024-25: 120, GTU Intake 2024-25: 120
- Course Name: Electrical Engineering, AICTE Intake 2024-25: 90, GTU Intake 2024-25: 90
- Course Name: Computer Engineering, AICTE Intake 2024-25: 180, GTU Intake 2024-25: 180

Institute Code: 635
Zone: 2
Institute Name: M.L.INSTITUTE OF DIPLOMA STUDIES, BHANDU
Address: Lalji Park, Unjha-Mehsana Highway, Bhandu, Ta-Visnagar, District-Mehsana,384120
District: Mehsana
Institute Type: Private-SFI
Contact No: 9099063235
Mail Id: dec635owner@gtu.edu.in
Courses:
- Course Name: Automobile Engineering, AICTE Intake 2024-25: 120, GTU Intake 2024-25: 120
- Course Name: Civil Engineering, AICTE Intake 2024-25: 120, GTU Intake 2024-25: 120
- Course Name: Computer Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
- Course Name: Electrical Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
- Course Name: Electronics & Communication Engg, AICTE Intake 2024-25: 30, GTU Intake 2024-25: 30
- Course Name: Mechanical Engineering, AICTE Intake 2024-25: 120, GTU Intake 2024-25: 120

Institute Code: 654
Zone: 2
Institute Name: VPMP POLYTECHNIC
Address: LDRP-ITR CAMPUS, Nr.ITI,KH-5, SECTOR-15,GANDHINAGAR. PIN NO:382015
District: Gandhinagar
Institute Type: Private-SFI
Contact No: 9998890610
Mail Id: dec654owner@gtu.edu.in
Courses:
- Course Name: Civil Engineering, AICTE Intake 2024-25: 120, GTU Intake 2024-25: 120
- Course Name: Computer Engineering, AICTE Intake 2024-25: 180, GTU Intake 2024-25: 180
- Course Name: Electrical Engineering, AICTE Intake 2024-25: 90, GTU Intake 2024-25: 90
- Course Name: Electronics & Communication Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
- Course Name: Mechanical Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60

Institute Code: 661
Zone: 2
Institute Name: Vedvyas Polytechnic
Address: Samarth Campus Opp:Sabar Dairy, Nh-8, Haji, Samarth Campus Opp:Sabar Dairy, Nh-8, Hajipur, Himatnagar Sabarkantha-383001
District: Sabarkantha
Institute Type: Private-SFI
Contact No: 9099063261
Mail Id: dec661owner@gtu.edu.in
Courses:
- Course Name: Progressive Clouser AY 2024-25

Institute Code: 668
Zone: 2
Institute Name: MERCHANT ENGINEERING COLLEGE
Address: At. Piludara, Ta. Mehsana, Dist. Mehsana - 384380
District: Mehsana
Institute Type: Private-SFI
Contact No: 9099063268
Mail Id: dec668owner@gtu.edu.in
Courses:
- Course Name: Civil Engineering, AICTE Intake 2024-25: 120, GTU Intake 2024-25: 120
- Course Name: Computer Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
- Course Name: Electrical Engineering, AICTE Intake 2024-25: 120, GTU Intake 2024-25: 120
- Course Name: Electronic & Communication Engg, AICTE Intake 2024-25: 30, GTU Intake 2024-25: 30
- Course Name: Mechanical Engineering, AICTE Intake 2024-25: 150, GTU Intake 2024-25: 150

Institute Code: 675
Zone: 2
Institute Name: F.D.(MUBIN) INSTITUTE OF ENGINEERING & TECHNOLOGY
Address: Bahiyal, Survey No.582/587, At & Post: Tal: Dehgam, Dist. Gandhinagar-382308
District: Gandhinagar
Institute Type: Private-SFI
Contact No: 9099063413
Mail Id: dec675owner@gtu.edu.in
Courses:
- Course Name: Civil Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
- Course Name: Computer Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
- Course Name: Electrical Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
- Course Name: Electronics & Communication Engg, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
- Course Name: Mechanical Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60

Institute Code: 677
Zone: 2
Institute Name: Shree Hari Polytechnic Institute
Address: Gurukul Campus, Nani Kadi, Taluka Kadi District Mehsana, Nani Kadi, Mehsana-382715
District: Mehsana
Institute Type: Private-SFI
Contact No: 9099063400
Mail Id: dec677owner@gtu.edu.in
Courses:
- Course Name: Mechanical Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
- Course Name: Civil Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
- Course Name: Electrical Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60
- Course Name: Computer Engineering, AICTE Intake 2024-25: 60, GTU Intake 2024-25: 60

Institute Code: 681
Zone: 2
Institute Name: SMT. R.S PATEL INSTITUTE OF DIPLOMA ENGINEERING
Address: Shelavi Station,P.o. Palasar Tal.Chansma,
District: Patan
Institute Type: Private-SFI
Contact No: 9099063414
Mail Id: dec681owner@gt

                                 Gujarat Technological University (GTU) has specific guidelines and procedures for students seeking to transfer from one affiliated college to another. Below is a general overview of the GTU college transfer process. However, please note that policies may change, and it is always best to refer to the latest official GTU circulars or contact the university directly for the most accurate and updated information.

---

### **Key Points About GTU College Transfer:**

1. **Eligibility for Transfer:**
   - Students must have valid reasons for transferring, such as relocation, medical issues, or other genuine circumstances.
   - The transfer is subject to the availability of seats in the desired college and program.
   - Students must have no outstanding dues or disciplinary issues in their current college.

2. **When to Apply:**
   - Transfers are typically allowed at the beginning of the academic year or semester.
   - Mid-semester transfers are generally not permitted unless under exceptional circumstances.

3. **Required Documents:**
   - Application form for college transfer (available on the GTU website or college office).
   - No Objection Certificate (NOC) from the current college.
   - Admission approval letter from the new college.
   - Mark sheets of previous semesters.
   - Valid reason for transfer (e.g., medical certificate, relocation proof, etc.).
   - Fee receipts and proof of no dues from the current college.
   - Migration certificate (if applicable).

4. **Approval Process:**
   - The application must be approved by both the current and the new college.
   - The transfer request is then forwarded to GTU for final approval.
   - GTU will issue a transfer order if the request is approved.

5. **Fees:**
   - A transfer fee may be applicable, as per GTU norms.
   - Students must also ensure that all fees at the current college are cleared before applying for a transfer.

6. **Rules for Lateral Entry Students:**
   - Students admitted through lateral entry (e.g., diploma to degree) may have additional restrictions or requirements for transfer.

7. **Important Considerations:**
   - Transfers are not guaranteed and are subject to GTU's discretion.
   - The new college must be affiliated with GTU and offer the same program.
   - Transfers may not be allowed during the final year of the program.

---

### **Steps to Apply for College Transfer:**

1. Obtain the transfer application form from GTU's official website or your current college.
2. Submit the completed form along with the required documents to your current college.
3. Obtain a No Objection Certificate (NOC) from your current college.
4. Apply for admission to the new college and get an approval letter.
5. Submit the NOC, approval letter, and other documents to GTU for final approval.
6. Wait for GTU's transfer order and complete the admission process at the new college.

---

### **Important Links:**
- GTU Official Website: [https://www.gtu.ac.in](https://www.gtu.ac.in)
- GTU Student Portal: [https://www.gtustudent.org](https://www.gtustudent.org)

---

### **Contact Information:**
For further clarification or assistance, you can contact GTU's student support services or visit the nearest GTU regional office.

---

**Note:** Always verify the latest guidelines from GTU, as policies may change. If you are unsure about any step, consult your current college's administration or GTU's helpdesk.


(you should give answers with very understandable and detailed pinpointed, easy to read and no hard words)

"""),
        ],
    )
    
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    running = True
    while running:
        inputText = str(input("\nyou: "))
        generate(input_text=inputText)
        