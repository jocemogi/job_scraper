# -*- coding: utf-8 -*-
print("This is the job scraper program")
jobs = [
	{
		"title" : "Business Operations Analyst",
		"description" : "About Flowspace: In less than three years, Flowspace has created one of the largest on-demand modern omnichannel fulfillment networks in the country, powered by cloud and mobile technology. We enable hundreds of brands and retailers to dynamically store, fulfill and ship products seamlessly to consumers nationwide from 120+ locations. Join us in our mission to transform a $100 billion warehouse and logistics industry. Flowspace is backed by Canvas Ventures, Moment Ventures, Y Combinator, and other prominent angels. Flowspace is looking for a Financial Analyst to help optimize our operations and finance departments. The ideal candidate must be passionate about solving problems using data and be comfortable refining existing processes and creating new ones. This position will collaborate with all teams at Flowspace and will be a highly visible role that will report to the Manager of Finance and Strategy. This is a great opportunity for a self starter who wants to make an impact and be on the ground floor of a fast growing start up. What you'll do: Create cost analysis process by establishing and enforcing policies and procedures; providing trends and forecasts; explaining processes and techniques; recommending actions. Analyze shipping contracts and recommend appropriate actions to senior management Engage in ongoing forecasting for marketing spend, revenue tracking, headcount, and strategic planning Work with all departments and collaborate to create plans for increased productivity Who we're looking for: Bachelor’s Degree in Finance, Accounting or a related field 1-2 years of relevant experience in analytical role (strategic planning, management consulting, investment banking, etc.), logistics/software/ technology industry experience a plus Proficient in Excel (pivot tables, Vlookups, etc) Ability to multitask and meet constant deadlines Exceptional communication skills Highly organized and detail oriented Benefits: Meaningful equity in a venture backed start-up Competitive Salary Medical, vision, dental benefits 401K Matching A clear success path within the company. We want you to grow and lead with us. Catered lunches once a week, drinks and snacks all the time. Office happy hours Monthly Gym Credits"
	}
]

def contains_target_phrase(description, phrases):
	for phrase in phrases:
		if phrase in description:
			return True
	return False

target_phrases = [
  '1-2 relevant work experience',
  '0-2 years experience'
]

for job in jobs:
	if contains_target_phrase(job['description'], target_phrases):
		print(job["title"])
