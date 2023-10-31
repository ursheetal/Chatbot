from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import spacy
spacy.load('en_core_web_sm')
# from spacy.lang.en import English
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot('<b>VDC BOT</b>')

# nlp = spacy.load("en_core_web_sm")

chatbot = ChatBot(
    'ChatBot for College Enquiry',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': "Hi there, Welcome to VDC BOT! 👋 If you need any assistance, I'm always here.Go ahead and write the number of any query. 😃✨<b><br><br>  Which of the following user groups do you belong to? <br><br>1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br><br>",
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'   
) 
trainer = ListTrainer(chatbot)

# python app.py
# Training with Personal Ques & Ans 
conversation = [
"<b><br><br><br>I am sorry! may be i can help u here<br> Which of the following user groups do you belong to? <br><br>1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br><br>",
"Hi there",   
"Hi",
"Helloo!",
"Hey",

"How are you?",
"I'm good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"Great",
"Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"good",
"Go ahead and write the number of any query. 😃✨ <br> 2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"fine",
"Go ahead and write the number of any query. 😃✨ <br> 2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"Thank You",
"Your Welcome 😄",

"Thanks",
"Your Welcome 😄",

"Bye",
"Thank You for visiting!..",

"What do you do?",
"I am made to give Information about  VDC  college.",

"What else can you do?",
"I can help you know more about VDC ",

"What is your name?",
"My name is VDC Bot",

"What does VDC mean?",
"VDC stands for Vivekananda Degree College",

"what is the full form of VDC?",
"VDC stands for Vivekananda Degree College",

"who is the Principal of VDC?",
"Prof.Vishnu Ganapathi Bhat M.Sc, M.Phil",

"principle's name",
"Prof.Vishnu Ganapathi Bhat",

"principal contact number",
"+91 8251 233 635 (Principal’s Office)",

"office number",
"+91 8251 233 0455 (Admn. Office)",

"vdc",
"Vivekananda Degree College",

"VDC",
"Vivekananda Degree College",

"Syllabus",
"<b>Syllabus<br>The link to Events👉  <a href=" 'https://sites.google.com/view/vdcsyllabus/home' ">Click Here</a> </b>",

"Admissions",
"<b>Admissions <br>The link to Events👉 <a href=" 'https://sites.google.com/view/fees-payment/home' ">Click Here</a></b>",

"Teachers contact information",
"<b>Teachers contact info<br>The link to Teachers Information👉<a href=" 'https://sites.google.com/view/teacherscontactinformation/home' ">Click Here</a> </b>",

"Notices",
"<b>Notice <br>Notice for students👉 <a href=" 'https://sites.google.com/view/studentnotice/home' ">Click Here</a> </b>",

"Available Question papers",
"<b>Available Question papers <br>Question Papers👉 <a href=" 'https://www.csvcputtur.in/p/bca-question-papers_6.html?m=1' ">Click Here</a> </b>",

"Notice for Faculty",
"<b> Notice for Faculty<br>The link to notices👉<a href=" 'https://sites.google.com/view/faculty-notice/stuff-notices' ">Click Here</a> </b>",

"About us",
"<b > About VBC<br>The link to About VDC👉 <a href=" 'https://vcputtur.ac.in/about-us/' ">Click Here</a> </b>",
"<b > Management Address <br>The link to Management Address👉<a href=" 'https://vcputtur.ac.in/management/' ">Click Here</a> </b>",
"<b > Principal's Desk <br>The link to Principal's Desk👉 <a href=" 'https://vcputtur.ac.in/principals-desk/' ">Click Here</a> </b>",

"Fees payment",
"<b > Fees payment <br> The link to Payment Details 👉 <a href=" 'https://sites.google.com/view/fees-payment/home' ">Click Here</a> </b>",

"location",
"<b > College Location<br>These are the top results:<br> <br>4.4.1 Location </b>",

" college location",
"<b > College Location<br>These are the top results:<br> <br>4.4.1 Location </b>",

"college detailes",
"<b > About VBC<br>The link to About VDC👉 <a href=" 'https://vcputtur.ac.in/about-us/' ">Click Here</a> </b>",
"<b > Management Address <br>The link to Management Address👉<a href=" 'https://vcputtur.ac.in/management/' ">Click Here</a> </b>",
"<b > Principal's Desk <br>The link to Principal's Desk👉 <a href=" 'https://vcputtur.ac.in/principals-desk/' ">Click Here</a> </b>",
"<b > PROGRAMS WE OFFER <br>These are the top results:<br> <br>4.2.1 Under-Graduate <br> 4.2.2 Post-Graduate<br> 4.2.3 Certificate/Diploma </b>",
"<b > Under-Graduate<br>The link to Under-Graduate👉 <a href=" 'https://vcputtur.ac.in/ug-courses' ">Click Here</a> </b>",
"<b > Post-Graduate <br>The link to Post-Graduate👉<a href=" 'https://vcputtur.ac.in/pg-courses/' ">Click Here</a> </b>",
"<b > Certificate/Diploma<br>The link to Certificate/Diploma👉 <a href=" 'https://vcputtur.ac.in/certificate-diploma/' ">Click Here</a> </b>",
"<b > Academic Facilities<br>The link to Academic Facilities👉 <a href=" 'https://vcputtur.ac.in/facility/#academic-facility' ">Click Here</a> </b>",
"<b > Other Facilites<br>The link to facilities👉<a href=" 'https://vcputtur.ac.in/facilities/other-facilities/' ">Click Here</a> </b>",

"Do u know me?",
"I am sorry!!I am not trained to know users personally",


"1",

    "<b>STUDENT <br>The following are frequently searched terms related to student . Please select one from the options below : <br> <br> 1.1 Syllabus<br>1.2  Admissions<br>1.3  Teachers contact information<br>1.4  Notices<br>1.5  Available Question Papers</b>",
    
    "1.1",
    "<b>Syllabus<br>The link to Events👉  <a href=" 'https://sites.google.com/view/vdcsyllabus/home' ">Click Here</a> </b>",
    "1.2",
    "<b>Admissions <br>The link to Events👉 <a href=" 'https://sites.google.com/view/fees-payment/home' ">Click Here</a></b>",
    "1.3",
    "<b>Teachers contact info<br>The link to Teachers Information👉<a href=" 'https://sites.google.com/view/teacherscontactinformation/home' ">Click Here</a> </b>",
    "1.4",
    "<b>Notice <br>Notice for students👉 <a href=" 'https://sites.google.com/view/studentnotice/home' ">Click Here</a> </b>",
    "1.5",
    "<b>Available Question papers <br>Question Papers👉 <a href=" 'https://www.csvcputtur.in/p/bca-question-papers_6.html?m=1' ">Click Here</a> </b>",

    "2",
    "<b >FACULTY<br>The following are frequently searched terms related to faculty. Please select one from the options below :</br></br>2.1 Notice for Faculty<br>2.2  PERSONAL DETAILES<br>2.3  Question papers </b>",
    
    "2.1",
    "<b> Notice for Faculty<br>The link to notices👉<a href=" 'https://sites.google.com/view/faculty-notice/stuff-notices' ">Click Here</a> </b>",
    "2.2",
    "<b> Contact details<br>Faculty Contact details👉<a href=" 'https://sites.google.com/view/teacherscontactinformation/home' ">Click Here</a> </b>",
    "2.3",
    "<b> Available Question papers <br>The link to papers 👉<a href=" 'https://www.csvcputtur.in/p/bca-question-papers_6.html?m=1' ">Click Here</a> </b>",
    
    "3",
    "<b> PARENTS <br>The following are frequently searched terms related to Parents. Please select one from the options below : <br> <br> 3.1 About Us <br>3.2 Notices <br>3.3 Fee Payment <br>3.4 Placements <br>3.5 Teachers contact information</b>",

    "3.1",
    "<b > ABOUT US<br>These are the top results:<br> <br> 3.1.1 About VDC<br> 3.1.2 Management Address <br> 3.1.3 Principal's Desk</b>",
    "3.1.1",
    "<b > 3.1.1 About VBC<br>The link to About VDC👉 <a href=" 'https://vcputtur.ac.in/about-us/' ">Click Here</a> </b>",
    "3.1.2",
    "<b > 3.1.2 Management Address <br>The link to Management Address👉<a href=" 'https://vcputtur.ac.in/management/' ">Click Here</a> </b>",
    "3.1.3",
    "<b > 3.1.3 Principal's Desk <br>The link to Principal's Desk👉 <a href=" 'https://vcputtur.ac.in/principals-desk/' ">Click Here</a> </b>",

    "3.2",
    "<b > News and Events<br>These are the top results:<br> <br> 3.2.1 News and Events </b>",
    "3.2.1",
    "<b > 3.2.1 All News and Events<br>The link to All News and Events👉 <a href=" 'https://vcputtur.ac.in/news-and-events/%e0%b2%a8%e0%b2%be%e0%b2%9f%e0%b2%95-%e0%b2%ae%e0%b2%a4%e0%b3%8d%e0%b2%a4%e0%b3%81-%e0%b2%b0%e0%b2%82%e0%b2%97%e0%b2%ad%e0%b3%82%e0%b2%ae%e0%b2%bf-%e0%b2%92%e0%b2%82%e0%b2%a6%e0%b3%81-%e0%b2%aa/' ">Click Here</a> </b>",

    "3.3", 
    "<b > Fees payment <br> The link to Payment Details 👉 <a href=" 'https://sites.google.com/view/fees-payment/home' ">Click Here</a> </b>",
     
    "3.4",
    "<b > PLACEMENTS <br>The link to Placements and Training Cell👉 <a href=" 'https://vcputtur.ac.in/placements-new-2020/' ">Click Here</a> </b>",

    "3.5",
    "<b>Teachers contact info <br>The link to Teachers Information👉<a href=" 'https://sites.google.com/view/teacherscontactinformation/home' ">Click Here</a> </b>",


    
    "4",
    "<b VISITORS <br>The following are frequently searched terms related to visitors. Please select one from the options below : <br> <br> 4.1 About Us<br>4.2 Programs We Offer <br>4.3 Student Bodies <br>4.4 Extra-Curricular </b>",
    
    "4.1",
    "<b > ABOUT US<br>These are the top results:<br> <br>4.1.1 About VDC<br> 4.1.2 Management Address <br> 4.1.3 Principal's Desk </b>",
    "4.1.1",
    "<b > 4.1.1 About VDC<br>The link to About VDC👉 <a href=" 'https://vcputtur.ac.in/about-us/' ">Click Here</a> </b>",
    "4.1.2",
    "<b > 4.1.2 Management Address <br>The link to Management Address👉<a href=" 'https://vcputtur.ac.in/management/' ">Click Here</a> </b>",
    "4.1.3",
    "<b > 4.1.3 Principal's Desk <br>The link to Principal's Desk👉 <a href=" 'https://vcputtur.ac.in/principals-desk/' ">Click Here</a> </b>",

    "4.2",
    "<b > PROGRAMS WE OFFER <br>These are the top results:<br> <br>4.2.1 Under-Graduate <br> 4.2.2 Post-Graduate<br> 4.2.3 Certificate/Diploma </b>",
    "4.2.1",
    "<b > 4.2.1 Under-Graduate<br>The link to Under-Graduate👉 <a href=" 'https://vcputtur.ac.in/ug-courses' ">Click Here</a> </b>",
    "4.2.2",
    "<b > 4.2.2 Post-Graduate <br>The link to Post-Graduate👉<a href=" 'https://vcputtur.ac.in/pg-courses/' ">Click Here</a> </b>",
    "4.2.3",
    "<b > 4.2.3 Certificate/Diploma<br>The link to Certificate/Diploma👉 <a href=" 'https://vcputtur.ac.in/certificate-diploma/' ">Click Here</a> </b>",

    "4.3",
    "<b > Facilities<br>These are the top results:<br> 4.3.1 Acadamic Facilities<br> 4.3.2 Other facilites <br>",
    "4.3.1",
    "<b > 4.3.1 Academic Facilities<br>The link to Academic Facilities👉 <a href=" 'https://vcputtur.ac.in/facility/#academic-facility' ">Click Here</a> </b>",
    "4.3.2",
    "<b > 4.3.2 Other Facilites<br>The link to facilities👉<a href=" 'https://vcputtur.ac.in/facilities/other-facilities/' ">Click Here</a> </b>",

    "4.4",
    "<b > College Location<br>These are the top results:<br> <br>4.4.1 Location </b>",
    "4.4.1",
    "<b > 4.4.1 location<br>The link to location   👉 <a href=" 'https://www.google.com/maps/dir/12.6892881,75.1113/vivekananda+degree+college+puttur/@12.737908,75.1094318,13z/data=!3m1!4b1!4m9!4m8!1m1!4e1!1m5!1m1!1s0x3ba4bd11a6a9050f:0xd866a7b41d8c42fc!2m2!1d75.1869907!2d12.7805033' ">Click Here</a> </b>",
    
    "4.5",
    "<b > Contact<br>These are the top results:<br> 4.5.1 Contact Us<br>",
    "4.5.1",
    "<b > 4.5.1 Contact Us<br>The link to Contact Us👉 <a href=" 'https://vcputtur.ac.in/contact/' ">Click Here</a> </b>",
    "4.3.2",

]

trainer.train(conversation)
