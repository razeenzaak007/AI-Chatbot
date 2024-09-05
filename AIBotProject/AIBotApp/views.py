from django.shortcuts import render
from django.http import HttpResponse

from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer , ChatterBotCorpusTrainer
# Create your views here.


bot3 = ChatBot('chatbot',read_only=False,
                logic_adapters=[
                    {
                        
                        'import_path': 'chatterbot.logic.BestMatch',
                        'default_response': 'Sorry, I dont know what that means!',
                        'maximum_similarity_threshold': 0.90
                    
                    
                    
                    }])

list_to_train= [
    "hi", 
    "hi there how are you", 
    "Whats your name",
    "I am DocAI",
    "What is your fav food?",
    "I like cheese",
    "Whats your favorite sports?",
    "Football",
    "what is covid 19",
    "COVID-19, caused by the SARS-CoV-2 virus, emerged in late 2019 and led to a global pandemic declared by the World Health Organization (WHO) in March 2020. Here's a summary of key information about COVID-19:",
    "What is computer?",
    "Computer is an electronic device",
    "What are the symptoms of the flu?",
    "Common symptoms of the flu include fever, chills, muscle aches, cough, congestion, runny nose, headaches, and fatigue.",
    "How can I prevent a cold?",
    "To prevent a cold, wash your hands frequently, avoid close contact with sick people, and maintain a healthy immune system by eating well, exercising, and getting enough sleep.",
    "What should I do if I have a fever?",
    "If you have a fever, rest, stay hydrated, and take over-the-counter medications like acetaminophen or ibuprofen. If your fever is very high or persists for more than three days, seek medical attention.",
    "What are the symptoms of COVID-19?",
    "Common symptoms of COVID-19 include fever, cough, and difficulty breathing. Some people may also experience fatigue, body aches, loss of taste or smell, sore throat, and congestion.",
    "How does the COVID-19 vaccine work?",
    "The COVID-19 vaccine helps your body develop immunity to the virus that causes COVID-19 without you having to get the illness. Different types of vaccines work in different ways to offer protection.",
    "What is hypertension?",
    "Hypertension, or high blood pressure, is a condition in which the force of the blood against your artery walls is too high, which can lead to heart disease and other health problems.",
    "What are the symptoms of diabetes?",
    "Symptoms of diabetes can include increased thirst, frequent urination, extreme fatigue, blurred vision, and slow healing of wounds.",
    "What is a balanced diet?",
    "A balanced diet includes a variety of foods in the right proportions, including plenty of fruits and vegetables, lean proteins, whole grains, and limited amounts of fats, sugar, and salt.",
    "How much water should I drink daily?",
    "It's generally recommended to drink about 8 glasses, or 2 liters, of water a day, though individual needs may vary based on activity level, climate, and overall health.",
    "What are the benefits of regular exercise?",
    "Regular exercise can help improve cardiovascular health, strengthen muscles and bones, boost mental health, aid in weight management, and reduce the risk of chronic diseases.",
    "What is asthma?",
    "Asthma is a chronic condition that affects the airways in your lungs, causing them to become inflamed and narrow, which makes it difficult to breathe.",
    "What are the symptoms of asthma?",
    "Common symptoms of asthma include wheezing, shortness of breath, chest tightness, and coughing, especially at night or early in the morning.",
    "How can I manage my asthma?",
    "To manage asthma, follow your doctor's advice, take prescribed medications, avoid asthma triggers, and monitor your symptoms to keep them under control.",
    "What is a migraine?",
    "A migraine is a type of headache characterized by severe pain, usually on one side of the head, and is often accompanied by nausea, vomiting, and sensitivity to light and sound.",
    "How can I prevent migraines?",
    "To prevent migraines, identify and avoid triggers, maintain a regular sleep schedule, stay hydrated, manage stress, and consider medications or treatments prescribed by a healthcare provider.",
    "What is anemia?",
    "Anemia is a condition in which you lack enough healthy red blood cells to carry adequate oxygen to your body's tissues, leading to fatigue and weakness.",
    "What are the symptoms of anemia?",
    "Symptoms of anemia include fatigue, weakness, pale or yellowish skin, irregular heartbeats, shortness of breath, dizziness, and cold hands and feet.",
    "What is osteoporosis?",
    "Osteoporosis is a condition that weakens bones, making them fragile and more likely to break.",
    "How can I prevent osteoporosis?",
    "To prevent osteoporosis, ensure adequate intake of calcium and vitamin D, engage in regular weight-bearing exercises, avoid smoking, and limit alcohol consumption.",
    "What are the symptoms of depression?",
    "Symptoms of depression can include persistent sadness, loss of interest in activities once enjoyed, changes in appetite or weight, difficulty sleeping, and thoughts of death or suicide.",
    "How can I manage depression?",
    "Managing depression may involve therapy, medications, lifestyle changes like regular exercise, healthy eating, adequate sleep, and support from loved ones.",
    "What is anxiety?",
    "Anxiety is a feeling of worry, nervousness, or unease about something with an uncertain outcome, often accompanied by physical symptoms like increased heart rate, sweating, and trembling.",
    "What are the symptoms of anxiety?",
    "Symptoms of anxiety include excessive worry, restlessness, fatigue, difficulty concentrating, irritability, muscle tension, and sleep disturbances.",
    "How can I manage anxiety?",
    "To manage anxiety, consider therapy, medications, mindfulness practices, regular physical activity, and avoiding caffeine and alcohol.",
    "What is the common cold?",
    "The common cold is a viral infection of your nose and throat (upper respiratory tract), usually harmless and caused by many different types of viruses.",
    "What are the symptoms of the common cold?",
    "Symptoms of the common cold include a runny or stuffy nose, sore throat, cough, congestion, slight body aches, sneezing, and low-grade fever.",
    "How can I treat a common cold?",
    "Treatment for a common cold includes resting, staying hydrated, using over-the-counter medications to relieve symptoms, and using saline nasal drops or sprays."
    "What is bronchitis?",
    "Bronchitis is an inflammation of the lining of your bronchial tubes, which carry air to and from your lungs.",
    "What are the symptoms of bronchitis?",
    "Symptoms of bronchitis include coughing up mucus, wheezing, shortness of breath, chest discomfort, and fatigue.",
    "How can I treat bronchitis?",
    "Treatment for bronchitis involves rest, fluids, avoiding smoke and fumes, and using a humidifier. For chronic bronchitis, medication and pulmonary rehabilitation may be necessary.",
    "What is pneumonia?",
    "Pneumonia is an infection that inflames the air sacs in one or both lungs, which may fill with fluid or pus.",
    "What are the symptoms of pneumonia?",
    "Symptoms of pneumonia include chest pain when you breathe or cough, confusion or changes in mental awareness, cough, fatigue, fever, sweating and shaking chills, nausea, vomiting, and diarrhea.",
    "How is pneumonia treated?",
    "Treatment for pneumonia may include antibiotics, antiviral or antifungal medications, rest, fluids, and over-the-counter medications to manage pain and fever.",
    "What is arthritis?",
    "Arthritis is inflammation of one or more of your joints, causing pain and stiffness that can worsen with age.",
    "What are the symptoms of arthritis?",
    "Symptoms of arthritis include joint pain, stiffness, swelling, redness, and decreased range of motion.",
    "How can I manage arthritis?",
    "Managing arthritis may involve medications, physical therapy, lifestyle changes like regular exercise and weight management, and sometimes surgery."
    "What is Alzheimer's disease?",
    "Alzheimer's disease is a progressive disorder that causes brain cells to degenerate and die, leading to a continuous decline in thinking, behavioral and social skills that disrupts a person's ability to function independently.",
    "What are the symptoms of Alzheimer's disease?",
    "Symptoms of Alzheimer's disease include memory loss, difficulty planning and solving problems, confusion with time or place, difficulty completing familiar tasks, and changes in mood and personality.",
    "How is Alzheimer's disease treated?",
    "There is no cure for Alzheimer's disease, but treatments can help manage symptoms. These include medications, cognitive therapies, and lifestyle changes to support brain health.",
    "What is heart disease?",
    "Heart disease refers to various types of conditions that affect the heart, including coronary artery disease, arrhythmias, and heart defects present at birth.",
    "What are the symptoms of heart disease?",
    "Symptoms of heart disease can include chest pain, shortness of breath, pain, numbness, weakness or coldness in your legs or arms, and pain in the neck, jaw, throat, upper abdomen or back.",
    "How can I prevent heart disease?",
    "To prevent heart disease, maintain a healthy diet, exercise regularly, avoid smoking, limit alcohol, manage stress, and keep conditions like high blood pressure, high cholesterol, and diabetes under control.",
    "What is stroke?",
    "A stroke occurs when the blood supply to part of your brain is interrupted or reduced, preventing brain tissue from getting oxygen and nutrients.",
    "What are the symptoms of a stroke?",
    "Symptoms of a stroke include trouble speaking",
    "What should I do if I have a fever?",
    "If you have a fever, it's important to rest, stay hydrated, and take over-the-counter fever reducers like acetaminophen or ibuprofen if needed. If the fever is very high or persistent, seek medical attention.",
    "I have a sore throat and runny nose. What could it be?",
    "These symptoms could indicate the common cold. To prevent spreading it, wash your hands frequently, avoid close contact with others, and rest to help your body recover.",
    "I have a headache, fever, and body aches. What might be the cause?",
    "These symptoms could be indicative of the flu. It's important to rest, stay hydrated, and take over-the-counter medications to relieve symptoms. If symptoms worsen or you have trouble breathing, seek medical attention.",
    "I have a rash and itching. What could it be?",
    "A rash and itching could be signs of an allergic reaction or a skin condition like eczema. Avoid scratching, keep the area clean, and consider using antihistamines or topical creams. If the rash persists or worsens, consult a healthcare provider.",
    "I have chest pain and shortness of breath. What should I do?",
    "Chest pain and shortness of breath could be signs of a serious condition like a heart attack or pulmonary embolism. Seek emergency medical attention immediately.",
    "I have nausea and vomiting. What could be causing it?",
    "Nausea and vomiting could be caused by a variety of issues, such as a stomach virus (gastroenteritis), food poisoning, or even stress. Stay hydrated, rest, and avoid solid foods until you feel better. If symptoms persist, seek medical advice.",
    "I have joint pain and swelling. What could it be?",
    "Joint pain and swelling could be symptoms of arthritis or another inflammatory condition. Rest the affected joint, apply ice, and take over-the-counter pain relievers. If symptoms persist, see a healthcare provider.",
    "I have persistent cough and weight loss. What should I do?",
    "A persistent cough and unexplained weight loss could be signs of a serious condition like tuberculosis or lung cancer. It's important to seek medical evaluation as soon as possible.",
    "I have a high fever, chills, and night sweats. What could it be?",
    "These symptoms could indicate malaria, especially if you've recently traveled to a region where malaria is common. Seek medical attention immediately.",
    "I have frequent urination, excessive thirst, and fatigue. What might be the cause?",
    "These symptoms could be indicative of diabetes. It's important to consult a healthcare provider for proper diagnosis and treatment.",
    "I have sudden severe headache, stiff neck, and sensitivity to light. What should I do?",
    "These symptoms could be signs of meningitis. Seek emergency medical attention immediately.",
    "I have a persistent dry cough, shortness of breath, and fatigue. What could it be?",
    "These symptoms could indicate a condition like chronic obstructive pulmonary disease (COPD) or asthma. Consult a healthcare provider for evaluation and treatment.",
    "I have severe abdominal pain, nausea, and vomiting. What might be the issue?",
    "These symptoms could be indicative of appendicitis or a gastrointestinal obstruction. Seek emergency medical attention.",
    "I have difficulty swallowing and chest pain. What could it be?",
    "These symptoms could be signs of gastroesophageal reflux disease (GERD) or a more serious condition like esophageal cancer. Consult a healthcare provider for evaluation.",
    "I have swollen lymph nodes, fever, and unexplained weight loss. What should I do?",
    "These symptoms could indicate lymphoma or another type of cancer. It's important to seek medical evaluation as soon as possible.",
    "I have frequent headaches, blurred vision, and dizziness. What might be the cause?",
    "These symptoms could be indicative of a migraine or a more serious condition like a brain tumor. Consult a healthcare provider for evaluation.",
    "I have chest pain that radiates to my arm and jaw. What could it be?",
    "These symptoms could be signs of a heart attack. Seek emergency medical attention immediately.",
    "I have a sore that doesn't heal and changes in skin color. What might it be?",
    "These symptoms could indicate skin cancer. It's important to consult a dermatologist for evaluation.",
    "I have fatigue, yellowing of the skin and eyes, and dark urine. What could it be?",
    "These symptoms could be signs of hepatitis or another liver condition. Consult a healthcare provider for proper diagnosis and treatment.",
    "I have persistent itching and redness in my eyes. What might be the issue?",
    "These symptoms could indicate conjunctivitis (pink eye) or allergies. Keep the area clean and avoid touching your eyes. Consult a healthcare provider if symptoms persist.",
    "I have numbness and tingling in my hands and feet. What could it be?",
    "These symptoms could be signs of peripheral neuropathy, which can be caused by diabetes or other conditions. Consult a healthcare provider for evaluation.",
    "I have difficulty breathing, wheezing, and chest tightness. What should I do?",
    "These symptoms could indicate asthma or an allergic reaction. Use an inhaler if prescribed and seek medical attention if symptoms worsen.",
    "I have a sudden loss of vision in one eye. What could it be?",
    "This symptom could be a sign of a retinal detachment or stroke. Seek emergency medical attention immediately.",
    "I have high fever, chills, and night sweats. What could it be?",
    "These symptoms could indicate malaria, especially if you've recently traveled to a region where malaria is common. Seek medical attention immediately.",
    "I have frequent urination, excessive thirst, and fatigue. What might be the cause?",
    "These symptoms could be indicative of diabetes. It's important to consult a healthcare provider for proper diagnosis and treatment.",
    "I have sudden severe headache, stiff neck, and sensitivity to light. What should I do?",
    "These symptoms could be signs of meningitis. Seek emergency medical attention immediately.",
    "I have a persistent dry cough, shortness of breath, and fatigue. What could it be?",
    "These symptoms could indicate a condition like chronic obstructive pulmonary disease (COPD) or asthma. Consult a healthcare provider for evaluation and treatment.",
    "I have severe abdominal pain, nausea, and vomiting. What might be the issue?",
    "These symptoms could be indicative of appendicitis or a gastrointestinal obstruction. Seek emergency medical attention.",
    "I have difficulty swallowing and chest pain. What could it be?",
    "These symptoms could be signs of gastroesophageal reflux disease (GERD) or a more serious condition like esophageal cancer. Consult a healthcare provider for evaluation.",
    "I have swollen lymph nodes, fever, and unexplained weight loss. What should I do?",
    "These symptoms could indicate lymphoma or another type of cancer. It's important to seek medical evaluation as soon as possible.",
    "I have frequent headaches, blurred vision, and dizziness. What might be the cause?",
    "These symptoms could be indicative of a migraine or a more serious condition like a brain tumor. Consult a healthcare provider for evaluation.",
    "I have chest pain that radiates to my arm and jaw. What could it be?",
    "These symptoms could be signs of a heart attack. Seek emergency medical attention immediately.",
    "I have a sore that doesn't heal and changes in skin color. What might it be?",
    "These symptoms could indicate skin cancer. It's important to consult a dermatologist for evaluation.",
    "I have fatigue, yellowing of the skin and eyes, and dark urine. What could it be?",
    "These symptoms could be signs of hepatitis or another liver condition. Consult a healthcare provider for proper diagnosis and treatment.",
    "I have persistent itching and redness in my eyes. What might be the issue?",
    "These symptoms could indicate conjunctivitis (pink eye) or allergies. Keep the area clean and avoid touching your eyes. Consult a healthcare provider if symptoms persist.",
    "I have numbness and tingling in my hands and feet. What could it be?",
    "These symptoms could be signs of peripheral neuropathy, which can be caused by diabetes or other conditions. Consult a healthcare provider for evaluation.",
    "I have difficulty breathing, wheezing, and chest tightness. What should I do?",
    "These symptoms could indicate asthma or an allergic reaction. Use an inhaler if prescribed and seek medical attention if symptoms worsen.",
    "I have a sudden loss of vision in one eye. What could it be?",
    "This symptom could be a sign of a retinal detachment or stroke. Seek emergency medical attention immediately.",
    "I have a persistent cough with blood. What might be the cause?",
    "Coughing up blood could be a sign of a serious condition like tuberculosis or lung cancer. Seek medical evaluation as soon as possible.",
    "I have swelling and pain in one leg. What could it be?",
    "These symptoms could indicate deep vein thrombosis (DVT). It's important to seek medical attention immediately to prevent complications.",
    "I have unexplained weight gain and fatigue. What might be the cause?",
    "These symptoms could be indicative of hypothyroidism. Consult a healthcare provider for proper diagnosis and treatment.",
    "I have a high fever, severe headache, and a rash. What could it be?",
    "These symptoms could indicate dengue fever or another serious infection. Seek medical attention immediately.",
    "I have joint stiffness and pain, especially in the morning. What could it be?",
    "These symptoms could be indicative of rheumatoid arthritis. Consult a healthcare provider for evaluation and management.",
    "I have abdominal pain, bloating, and changes in bowel habits. What might be the cause?",
    "These symptoms could indicate irritable bowel syndrome (IBS) or another gastrointestinal condition. Consult a healthcare provider for evaluation.",
    "I have a persistent sore throat and hoarseness. What could it be?",
    "These symptoms could be signs of laryngitis or throat cancer. Consult a healthcare provider for proper diagnosis.",
    "I have severe back pain and difficulty walking. What should I do?",
    "These symptoms could indicate a herniated disc or spinal stenosis. Consult a healthcare provider for evaluation and treatment.",
    "I have a rapid heartbeat, sweating, and trembling. What could it be?",
    "These symptoms could be signs of a panic attack or hyperthyroidism. Seek medical attention for proper diagnosis and management.",
    "I have persistent fatigue and muscle weakness. What might be the cause?",
    "These symptoms could be indicative of chronic fatigue syndrome or an autoimmune disorder like multiple sclerosis. Consult a healthcare provider for evaluation.",
    "I have a severe headache and vision problems. What could it be?",
    "These symptoms could be signs of a migraine or a more serious condition like a brain aneurysm. Seek medical attention immediately.",
    "I have a sore and painful joint. What might be the cause?",
    "These symptoms could indicate gout or an infection in the joint (septic arthritis). Consult a healthcare provider for evaluation and treatment.",
    "I have excessive sweating and unexplained weight loss. What could it be?",
    "These symptoms could be indicative of hyperthyroidism or another metabolic condition. Consult a healthcare provider for proper diagnosis and treatment.",
    "I have difficulty speaking and weakness on one side of my body. What should I do?",
    "These symptoms could be signs of a stroke. Seek emergency medical attention immediately.",
    "I have a severe sore throat and difficulty swallowing. What might be the cause?",
    "These symptoms could indicate tonsillitis or strep throat. Consult a healthcare provider for proper diagnosis and treatment.",
    "I have persistent vomiting and severe abdominal pain. What could it be?",
    "These symptoms could be signs of pancreatitis or another serious gastrointestinal condition. Seek medical attention immediately.",
    "I have a persistent cough and weight loss. What should I do?",
    "A persistent cough and unexplained weight loss could be signs of tuberculosis or lung cancer. It's important to seek medical evaluation as soon as possible.",
    "What are the precautions for diabetes?",
    "To manage diabetes, follow a healthy diet low in sugar and refined carbs, exercise regularly, monitor your blood sugar levels, take prescribed medications, and attend regular check-ups with your healthcare provider.",
    "What are the precautions for hypertension?",
    "To manage hypertension, maintain a low-sodium diet, exercise regularly, manage stress, avoid excessive alcohol, quit smoking, and follow your doctor's recommendations for medication and lifestyle changes.",
    "What are the treatments for migraine?",
    "Migraine treatments include prescription medications, over-the-counter pain relievers, lifestyle changes like regular sleep and avoiding triggers, and preventive medications for frequent migraines. Consult a healthcare provider for personalized treatment.",
    "What are the precautions for asthma?",
    "To manage asthma, avoid known triggers, use prescribed inhalers as directed, monitor your symptoms, maintain a clean environment, and get regular check-ups with your healthcare provider.",
    "What are the treatments for seasonal allergies?",
    "Treatments for seasonal allergies include avoiding allergens, using antihistamines, nasal corticosteroids, decongestants, and maintaining a clean home environment. Consult a healthcare provider for personalized allergy management.",
    "What are the treatments for eczema?",
    "Eczema treatments include using topical corticosteroids, moisturizing regularly, avoiding irritants, and managing stress. Consult a dermatologist for a treatment plan tailored to your needs.",
    "What are the precautions for influenza?",
    "To prevent influenza, get an annual flu vaccine, practice good hygiene like frequent handwashing, avoid close contact with sick individuals, and maintain a healthy lifestyle.",
    "What are the treatments for cold sores?",
    "Cold sore treatments include antiviral medications, topical creams, and keeping the area clean. Avoid close contact with others and manage stress to reduce outbreaks.",
    "What are the precautions for tuberculosis?",
    "To prevent tuberculosis, follow the treatment regimen as prescribed, cover your mouth when coughing, get regular check-ups, and avoid close contact with others until you're no longer contagious.",
    "What are the treatments for gout?",
    "Gout treatments include medications to reduce uric acid levels, anti-inflammatory drugs, lifestyle changes like reducing alcohol intake and purine-rich foods, and staying hydrated.",
    "What are the precautions for a urinary tract infection (UTI)?",
    "To prevent UTIs, drink plenty of water, practice good personal hygiene, urinate frequently, and avoid holding in urine for long periods. Consult a healthcare provider for appropriate treatment if you have symptoms.",
    "What are the treatments for high cholesterol?",
    "Treatments for high cholesterol include lifestyle changes such as a heart-healthy diet, regular exercise, and possibly medications like statins as prescribed by your doctor.",
    "What are the precautions for a heart attack?",
    "To prevent a heart attack, maintain a healthy diet, exercise regularly, manage stress, avoid smoking, and follow your doctor’s advice for managing conditions like hypertension and high cholesterol.",
    "What are the treatments for hypothyroidism?",
    "Hypothyroidism is commonly treated with synthetic thyroid hormones. Regular blood tests to monitor thyroid levels and dose adjustments may be needed. Consult your healthcare provider for a treatment plan.",
    "What are the precautions for osteoporosis?",
    "To manage osteoporosis, ensure adequate intake of calcium and vitamin D, engage in weight-bearing exercises, avoid smoking and excessive alcohol, and follow your doctor's recommendations for bone health.",
    "What are the treatments for pancreatitis?",
    "Pancreatitis treatments include hospitalization for severe cases, a diet low in fat, pain management, and treating underlying causes. Follow your healthcare provider’s instructions for managing this condition.",
    "What are the precautions for shingles?",
    "To prevent shingles, get the shingles vaccine, maintain a healthy immune system, and avoid close contact with individuals who have active shingles. Consult your healthcare provider for vaccination and treatment options.",
    "What are the treatments for sleep apnea?",
    "Sleep apnea treatments include using a CPAP machine, lifestyle changes like weight loss and sleeping on your side, and sometimes surgical options. Consult a healthcare provider for a personalized treatment plan.",
    "What are the precautions for a common cold?",
    "To prevent a common cold, practice good hygiene like frequent handwashing, avoid close contact with sick individuals, and maintain a healthy immune system through a balanced diet and regular exercise.",
    "What are the treatments for depression?",
    "Depression treatments include therapy (such as cognitive-behavioral therapy), antidepressant medications, regular exercise, and support from friends and family. Consult a mental health professional for an individualized treatment plan.",
    "What are the precautions for a stomach ulcer?",
    "To manage a stomach ulcer, avoid NSAIDs and alcohol, reduce stress, eat a balanced diet, and take prescribed medications to reduce stomach acid. Consult your healthcare provider for a tailored treatment plan.",
    "What are the treatments for chronic obstructive pulmonary disease (COPD)?",
    "COPD treatments include quitting smoking, using bronchodilators and corticosteroids, pulmonary rehabilitation, and managing symptoms. Consult a healthcare provider for a comprehensive management plan.",
    "What are the precautions for fibromyalgia?",
    "To manage fibromyalgia, engage in regular gentle exercise, maintain a healthy diet, manage stress, and follow your healthcare provider's recommendations for medication and therapies.",
    "What are the treatments for tonsillitis?",
    "Tonsillitis treatments may include antibiotics for bacterial infections, pain relievers, and in severe cases, surgery to remove the tonsils. Consult a healthcare provider for a treatment plan.",
    "What are the precautions for vertigo?",
    "To manage vertigo, avoid sudden head movements, stay hydrated, and follow your doctor’s advice on medications and exercises to reduce symptoms. Consult a healthcare provider for personalized management.",
    "What are the treatments for high blood pressure?",
    "High blood pressure treatments include lifestyle changes like a low-sodium diet and regular exercise, as well as medications like ACE inhibitors or beta-blockers. Consult your healthcare provider for a treatment plan.",
    "What are the precautions for celiac disease?",
    "To manage celiac disease, follow a strict gluten-free diet, avoid foods and products containing gluten, and consult a dietitian for a balanced and safe meal plan.",
    "What are the treatments for a sinus infection?",
    "Sinus infection treatments may include nasal decongestants, saline nasal sprays, and antibiotics for bacterial infections. Consult a healthcare provider for the appropriate treatment based on the cause of the infection.",
    "What are the precautions for rheumatoid arthritis?",
    "To manage rheumatoid arthritis, take prescribed medications, engage in regular low-impact exercise, manage stress, and maintain a balanced diet. Consult a healthcare provider for a comprehensive treatment plan.",
    "What are the treatments for IBS (Irritable Bowel Syndrome)?",
    "IBS treatments include dietary changes (like a low FODMAP diet), medications for symptom relief, and stress management techniques. Consult a healthcare provider for a tailored treatment plan.",
    "What are the precautions for shingles?",
    "To prevent shingles, get the shingles vaccine, manage stress, and maintain a healthy immune system. Consult a healthcare provider for advice on vaccination and lifestyle changes.",
    "What are the treatments for an allergy?",
    "Allergy treatments include avoiding allergens, taking antihistamines, using nasal sprays, and considering allergy shots. Consult an allergist for a comprehensive management plan.",
    "What are the precautions for hypothyroidism?",
    "To manage hypothyroidism, take prescribed thyroid hormone replacement, have regular blood tests to monitor thyroid levels, and follow your healthcare provider’s recommendations for diet and exercise.",
    "What are the treatments for gastritis?",
    "Gastritis treatments include avoiding irritants (like NSAIDs and alcohol), taking antacids or acid-reducing medications, and making dietary changes. Consult a healthcare provider for a treatment plan.",
    "What are the precautions for Lyme disease?",
    "To prevent Lyme disease, use insect repellent, wear protective clothing in tick-prone areas, and perform tick checks after outdoor activities. If bitten by a tick, seek medical attention if symptoms arise.",
    "What are the treatments for bronchitis?",
    "Bronchitis treatments include rest, staying hydrated, using a humidifier, and taking prescribed medications like cough suppressants or bronchodilators. Consult a healthcare provider for appropriate treatment.",
    "What are the precautions for hepatitis C?",
    "To manage hepatitis C, follow your treatment regimen, avoid alcohol, practice safe sex, and get regular medical check-ups. Consult a healthcare provider for a comprehensive management plan.",
    "What are the treatments for cellulitis?",
    "Cellulitis treatments include antibiotics to fight the infection, keeping the affected area elevated, and applying warm compresses. Consult a healthcare provider for appropriate treatment.",
    "What are the precautions for a herniated disc?",
    "To manage a herniated disc, follow a treatment plan including physical therapy, pain management, and avoiding activities that exacerbate the pain. Consult a healthcare provider for personalized advice.",
    "What are the treatments for a urinary tract infection (UTI)?",
    "UTI treatments include antibiotics, staying hydrated, and practicing good personal hygiene. Consult a healthcare provider for the appropriate antibiotic and management plan.",
    "What are the precautions for a stroke?",
    "To reduce the risk of a stroke, manage risk factors like high blood pressure and diabetes, avoid smoking, eat a healthy diet, exercise regularly, and follow your doctor’s recommendations.",
    "What are the treatments for chronic kidney disease?",
    "Chronic kidney disease treatments include managing underlying conditions (like diabetes and hypertension), making dietary changes, and potentially undergoing dialysis or kidney transplantation. Consult a healthcare provider for a comprehensive treatment plan.",
    "What are the precautions for shingles?",
    "To manage shingles, take antiviral medications as prescribed, keep the rash clean and covered, avoid close contact with pregnant women and those who haven’t had chickenpox, and consult your healthcare provider for ongoing care.",
    "What are the treatments for a fungal infection?",
    "Fungal infection treatments include antifungal medications, keeping the affected area dry and clean, and avoiding sharing personal items. Consult a healthcare provider for the appropriate antifungal treatment.",
    "What are the precautions for a cold sore?",
    "To manage cold sores, use antiviral medications, avoid touching the sore, wash your hands frequently, and avoid close contact with others until the sore has healed.",
    "What are the treatments for a common cold?",
    "Common cold treatments include rest, staying hydrated, using over-the-counter decongestants and pain relievers, and practicing good hygiene. Consult a healthcare provider if symptoms persist or worsen."
]


#chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)


list_trainer = ListTrainer(bot3)
list_trainer.train(list_to_train)

#chatterbotCorpusTrainer.train('chatterbot.corpus.english')


def getResponse(request):
   userMessage = request.GET.get('userMessage')
   chatResponse = str(bot3.get_response(userMessage))
   return HttpResponse(chatResponse)



def index(request):
    return render(request,'myapp2/index.html')

def about(request):
    return render(request,'myapp2/about.html')

def doctors(request):
    return render(request,'myapp2/hospitals.html')

def contact(request):
    return render(request,'myapp2/contact.html')

def home(request):
    return render(request,'myapp2/index.html')

def chat(request):
    return render(request,'myapp2/service.html')

def appointment(request):
    return render(request,'myapp2/appointment.html')