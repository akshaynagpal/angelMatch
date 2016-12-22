import csv
from random import randint
first_names = ['rahul','abhijeet','akshay','sid','abhishek','chad','adam','dave','mark','nishant','himani','tiffany','mia','lisa','priya','kendra','ashima','simar','rohit','varun']
last_names = ['gandhi','mehrotra','nagpal','bhatnagar','wartney','dangelo','parker','ann','arora','roy','walia','singh','sherawat','rai','kapoor']

skills=['Python' , 'JavaScript' , 'Jquery' , 'html' , 'html5' , 'java' , 'sql' , 'matlab' , 'cloud' , 'leadership' , 'public speaking' , 'Teamwork' , 'Problem Solving' , 'Construction' , 'Creative' , 'Editing' , 'Entertainment' , 'Financial Report Auditing' , 'Fundraising' , 'Innovation' , 'Investigation' , 'Logical Thinking' , 'Management' , 'Microsoft Office' , 'Motivation' , 'Multitasking' , 'Negotiation' , 'Networking' , 'Numerical Analysis' , 'Overseeing Operation' , 'Personal Interaction' , 'Plan Development' , 'Planning' , 'Prediction' , 'Preparing Written Documents' , 'Principal Concept Knowledge' , 'Prioritizing' , 'Promotions' , 'Proposals' , 'Proposal Writing' , 'Publications' , 'Public Relations' , 'Public Speaking' , 'Questioning Others' , 'Reading Volumes' , 'Reasoning' , 'Recommendations' , 'Regulating Rules' , 'Rehabilitating Others' , 'Remembering Facts' , 'Reporting' , 'Report Writing' , 'Responsibility' , 'Service' , 'Scheduling' , 'Screening Calls' , 'Sketching' , 'Supervision' , 'Technical Support' , 'Team Building' , 'Teamwork' , 'Technical' , 'Technology' , 'Time Management' , 'Toleration' , 'Training' , 'Transferable' , 'Updating Files' , 'Account Analysis' , 'Account Reconciliation' , 'Accounting Information Systems' , 'Accounting Software' , 'Accounts Payable' , 'Accounting Processes' , 'Accounting Principles' , 'Accounts Receivable' , 'Accuracy' , 'ADP' , 'Aging Reports' , 'Analytical' , 'Analysis' , 'Annual Reports' , 'Asset Management' , 'Attention to Detail' , 'Audits' , 'Audit Schedules' , 'Balance Sheets' , 'Banking' , 'Bank Deposits' , 'Bank Reconciliations' , 'Bill Payment' , 'Bookkeeping' , 'Budgets' , 'Business Awareness' , 'Cash Receipts' , 'Certified Public Accountant (CPA)' , 'Chart of Accounts' , 'Check Runs' , 'Collections' , 'Commitment' , 'Communication' , 'Corporate Reports' , 'Corporate Tax' , 'Cost Accounting' , 'Credit Management' , 'Credits' , 'Crystal Reports' , 'Debt Management' , 'Depreciation' , 'Detail Orientation' , 'Federal Tax Law' , 'Finance' , 'Financial Analysis' , 'Financial Reporting' , 'Financial Software' , 'Financial Statements' , 'Financial Statement Analysis' , 'Fixed Assets' , 'Forecasts' , 'Forecasting' , 'Income Tax' , 'Interest Calculations' , 'Interpersonal Skills' , 'Invoices' , 'IT Knowledge' , 'Job Cost Reports' , 'Journal Entry Preparation/Posting' , 'Mathematical' , 'Microsoft Office' , 'Monthly Closes' , 'Motivation' , 'Multitasking' , 'MS Access' , 'MS Excel' , 'MS Word' , 'Numerical Competence' , 'Oracle' , 'Organization' , 'Paychex' , 'Payroll' , 'Payroll Liabilities' , 'Payroll Taxes' , 'Peachtree' , 'Personal Tax' , 'Tax Analysis' , 'Tax Compliance' , 'Tax Filing' , 'Tax Law' , 'Tax Liabilities' , 'Tax Reporting' , 'Tax Returns' , 'Tax Software' , 'Technology' , 'Critical Thinking' , 'Accuracy' , 'Answer Client Questions' , 'Attention to Detail' , 'Balance Allocation' , 'Banking Software' , 'Bilingual' , 'Cash Drawer Maintenance' , 'Checking Account Deposit' , 'Checking Account Withdrawal' , 'Computer Programs' , 'Communications' , 'Cross Sales of Service' , 'Customer Relations' , 'Customer Service' , 'Dedication' , 'Deposits' , 'Detail Oriented' , 'Directing Customers' , 'Establishing Procedures' , 'Excel' , 'Exercising Discretion' , 'Financial Service Recognition' , 'Transaction Inquiries' , 'Trial Balancing' , 'Verbal Communication' , 'Verifications' , 'Verifying Transactions' , 'Withdrawals' , 'Written Communication' , 'Auto Body Repair' , 'Brake Repair' , 'Brake Resurfacing' , 'Car Tune-Up' , 'Change and Repair Tires' , 'Conduct tests and inspections' , 'Customer Relations' , 'Customer Service' , 'Diagnostic Abilities' , 'Diesel Engine Repair' , 'Direction' , 'Engine Repair' , 'General Auto Repair' , 'Networking' , 'Oil Change' , 'Perform routine and schedule maintenance' , 'Pumping Gas' , 'Rebuild Parts' , 'Recordkeeping' , 'Sales' , 'Service Advising' , 'Service Writing' , 'Stocking' , 'Supervising' , 'Teaching' , 'Towing' , 'Troubleshooting Abilities' , 'Truck Driving' , 'Appointment Scheduling' , 'Attending Classes' , 'Communication' , 'Conditioning Hair' , 'Cosmetics Consulting' , 'Creativity' , 'Hair Coloring' , 'Hair Cutting' , 'Hair Design' , 'Hair Highlighting' , 'Hair Lightening' , 'Hair Styling' , 'Ordering Supplies' , 'Pedicures' , 'Recordkeeping' , 'Sales' , 'Scalp Treatment' , 'Scheduling' , 'Service' , 'Shampooing Hair' , 'Skin Care' , 'Styling' , 'Active Listening' , 'Assertiveness' , 'Empathy' , 'Flexibility' , 'Administrative Tasks' , 'Attention to Detail' , 'Baking' , 'Baking Techniques' , 'Banquet' , 'Budgeting' , 'Business Acumen' , 'Business Sense' , 'Catering' , 'Cleanliness' , 'Commitment to Quality' , 'Communication' , 'Computer' , 'Concepts' , 'Consistency' , 'Cooking' , 'Control Labor Costs' , 'Cost Control' , 'First Aid' , 'Flexibility' , 'Food Preparation' , 'Food Pricing' , 'Food Safety' , 'Food Regulations' , 'Food Science' , 'Heat Control' , 'Health and Safety' , 'Hiring' , 'Hotel Kitchen' , 'Hygiene' , 'Ingredient Selection' , 'Initiative' , 'Interpersonal' , 'Inventory Management' , 'Inventory Rotation' , 'Kitchen Management' , 'Menus' , 'Menu Planning' , 'Ordering' , 'Operations' , 'Organization' , 'Organizing' , 'Passion' , 'Pastry' , 'Planning' , 'Team Building' , 'Team Player' , 'Teamwork' , 'Techniques' , 'Temperature Control' , 'Time Efficient' , 'Training' , 'Map Reading' , 'Mathematics' , 'Physics' , 'Prepare Designs and Estimates' , 'Technical Writing' , 'Test Building Materials' , 'Agile Development' , 'Agile Project Methodology' , 'Amazon Web Services (AWS)' , 'Analytical' , 'Analytics' , 'APIs' , 'Application and Server Monitoring Tools' , 'Azure' , 'Automated Deployment' , 'Best Practices' , 'Big Data' , 'Cloud Applications' , 'Cloud Based Development' , 'Cloud Based Visualizations' , 'Big Data' , 'Build, Manage and Monitor Cloud Environments' , 'Cloud Applications' , 'Cloud Based Visualizations' , 'Cloud Hosting Services' , 'Cloud Maintenance Tasks' , 'Cloud Systems Administration' , 'Code Management and Promotion Tools' , 'Coding' , 'Data Imports' , 'Data Modeling' , 'Data Visualization Tools' , 'Decision Making' , 'Deploying Applications in a Cloud Environment' , 'Deployment Automation Tools' , 'Deployment of Cloud Services' , 'Design' , 'DevOps' , 'Documentation' , 'Flexibility' , 'Google Cloud' , 'Hadoop' , 'Hosting Virtualization Platforms' , 'HP' , 'Integrating Security Protocols with Cloud Design' , 'Interpersonal' , 'iOS' , 'Java' , 'J2EE' , 'Linux' , 'Managing Full Application Stacks' , 'Metrics' , 'Attentiveness' , 'Benchmarking' , 'Caring' , 'Confidence' , 'Communication' , 'Complaints' , 'Computer' , 'Conflict Resolution' , 'Courtesy' , 'Customer Care' , 'Depersonalization' , 'Detail Oriented' , 'Diplomacy' , 'Efficiency' , 'Negotiation' , 'Organizational' , 'Oral Communication' , 'Patience' , 'People Oriented' , 'Persuasion' , 'Positivity' , 'Problem Analysis' , 'Problem Solving' , 'Product Knowledge' , 'Poise' , 'Positive Attitude' , 'Public Speaking' , 'Information Architecture' , 'Information Design' , 'Interaction Design' , 'Interaction Flows' , 'Mobile' , 'Microsoft Office' , 'Mock Ups' , 'Multitasking' , 'Adaptability' , 'Algorithms' , 'Algorithmic' , 'Analytical' , 'AWS' , 'Big Data' , 'C++' , 'Collaboration' , 'Communication' , 'Data Science Tools' , 'Data Tools' , 'Data Mining' , 'D3.js' , 'Decision Making' , 'Decision Trees' , 'Development' , 'Documenting' , 'Drawing Consensus' , 'ECL' , 'Analysis' , 'Reporting' , 'Report Writing' , 'Online searches' , 'Identifying Audience' , 'Content Review' , 'Content Management' , 'Copy Editing' , 'Copy writing' , 'Digital Media' , 'Drafting' , 'Editing' , 'Establishing Tone' , 'Formatting' , 'Grammar' , 'Identifying Theme' , 'Establishing purpose' , 'Journalist Ethics' , 'Language' , 'Media' , 'Microsoft Office' , 'Electrical Installations' , 'Electrical Schematics' , 'Evaluating Options and Ordering Equipment and Tools' , 'Evaluating Processes' , 'Explaining Scope of Work to Stakeholders' , 'Following Directions' , 'Industrial Control Systems' , 'Manual Dexterity' , 'Business Storytelling' , 'Collaboration' , 'Communication' , 'Content Management' , 'Content Management Systems (CMS)' , 'Content Programming' , 'Content Promotion' , 'Content Strategy' , 'Creating Interactive Charts, Graphs, and Maps' , 'Critical Thinking' , 'CSS' , 'Decision Making' , 'Digital Marketing' , 'Editing ' , 'Email Marketing' , 'Engagement' , 'Evaluating Emerging Digital Technology Tools' , 'Generating Content for Social Media Outlets' , 'Google Analytics' , 'Handling Criticism Calmly' , 'HTML' , 'Image Management' , 'Optimization' , 'Organizational' , 'Photography' , 'Photoshop' , 'Pitching Story Possibilities to Editors' , 'Planning Strategy for Websites and Social Media' , 'Problem Solving' , 'Proofreading' , 'PowerPoint' , 'Presenting Proposals to Colleagues' , 'Prioritizing' , 'Problem Solving' , 'Programmim ng Web Pages' , 'Project Management' , 'Proofreading' , 'Usability' , 'Web Metrics' , 'WordPress' , 'Counseling' , 'Creating Educational Materials' , 'Critical Thinking' , 'Customer Service' , 'Data Entry' , 'Decision Making' , 'Associate Designer' , 'Bedding Designer' , 'Boutique Assistant' , 'Brand Ambassador' , 'Brand Strategist' , 'Buyer' , 'Client Services Manager' , 'Creative Director' , 'Curated Merchant' , 'Customer Service Representative' , 'Events Manager' , 'Event Planner' , 'Factory Manager' , 'Fashion Buyer' , 'General Manager' , 'Graphic Artist' , 'Personal Shopper' , 'Planner' , 'Planning Assistant' , 'Product Developer' , 'Product Development Manager' , 'Product Planner' , 'Production Assistant' , 'Production Coordinator' , 'Production Sourcing Director' , 'Receptionist' , 'Research and Development Manager' , 'Retail Buyer' , 'Retail Fashion Recruiter' , 'Retail Footwear Buyer']

with open('new_persondata.csv','wb') as csvfile:
    filewriter = csv.writer(csvfile)
    for i in range(1001):
    	skillset=[]
    	for i in range(randint(3,20)):
    		skillset.append(skills[randint(0,len(skills)-1)])
    	skillstring = ', '.join(skillset)
    	endorsement = []
    	for s in skillset:
    		endorsement.append(str(randint(1,50)))
    	estring = ', '.join(endorsement)
    	filewriter.writerow([ str(id), first_names[randint(0,len(first_names)-1)], last_names[randint(0,len(last_names)-1)], skillstring,estring,str(randint(1,10)),str(randint(10,500)),'location', 'cause1,cause2','industry','summary'])