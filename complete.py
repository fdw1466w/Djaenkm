from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.keys import Keys
import getpass
import time

def login(driver):
	driver.get("https://learn.zybooks.com/signin")
	email_input = driver.find_element_by_xpath("//*[@id='ember912']")
	password_input = driver.find_element_by_xpath("//*[@id='ember918']")
	signin_button = driver.find_element_by_xpath("//*[@id='ember920']")
	
	while(True):
		email = input("Please enter your zyBooks email: ")
		email_input.send_keys(email)
		password = getpass.getpass("Enter your zyBooks password: ")
		password_input.send_keys(password)
		signin_button.click()
		time.sleep(3)
		if(driver.find_elements_by_xpath("//button[@disabled='']") or driver.find_elements_by_xpath("//div[contains(text(), 'Invalid email or password')]")):
			print("--Invalid email or password--\n")
			email_input.clear()
			password_input.clear()
		else:
			print("\nLogin Successful\n")
			break

def selectzyBook(driver):
	while(True):
		try:
			course_identifier = input("Enter your course ID or the name of your course: ")
			course_identifier = course_identifier.replace(" ", "")
			zybook_selection = driver.find_element_by_xpath("//a[contains(@href, '" + course_identifier + "')]")
			zybook_selection.click()
			break
		except:
			print("Invalid course")
		else:
			print("Course selected\n")

def chapterSelection(driver):
	while(True):
		chapter = input("Enter the chapter number you want completed: ")
		try:
			chapter_selection = driver.find_element_by_xpath("//*[@class='chapter-title' and contains(text(), '" + chapter + ".')]")
			chapter_selection.click()
			return chapter
		except:
			print("Invalid chapter")
	
def sectionSelection(driver, chapter):
	while(True):
		section = input("\nEnter the section number you want completed. Enter \"all\" if you would like the entire chapter completed. To exit the script, enter \"quit\": ")
		if(section.isnumeric()):
			section_button = driver.find_element_by_xpath("//span[@class='section-title' and contains(text(), '" + chapter + "." + section + "')]")
			section_button.click()
			completeParticipationActivities(driver)
			return_to_zybook = driver.find_element_by_xpath("//a[@href='/zybook/SMUCSE1342EvansSpring2019']")
			return_to_zybook.click()
			break
		elif(section == "all"):
			sections = driver.find_elements_by_xpath("//span[@class='section-title' and contains(text(), '" + chapter + ".')]")
			for index, section in enumerate(sections, 1):
				section = str(index)
				section_link = driver.find_element_by_xpath("//span[@class='section-title' and contains(text(), '" + chapter + "." + section + "')]")
				section_link.click()
				completeParticipationActivities(driver)
				return_to_zybook = driver.find_element_by_xpath("//a[@href='/zybook/SMUCSE1342EvansSpring2019']")
				return_to_zybook.click()
			break
		else:
			print("Please make a valid section selection.")

def completeParticipationActivities(driver):
	time.sleep(5)
	playAnimations(driver)
	time.sleep(1)
	completeMultipleChoice(driver)
	time.sleep(1)
	completeShortAnswer(driver)
	time.sleep(1)
	completeSelectionProblems(driver)
		
def playAnimations(driver):
	animation_players = driver.find_elements_by_xpath("/html/body/div[3]/div/section/div/article/div/div[@class='interactive-activity-container animation-player-content-resource participation medium ember-view']")
	animation_players += driver.find_elements_by_xpath("/html/body/div[3]/div/section/div/article/div/div[@class='interactive-activity-container animation-player-content-resource participation large ember-view']")
	animation_players += driver.find_elements_by_xpath("/html/body/div[3]/div/section/div/article/div/div[@class='interactive-activity-container animation-player-content-resource participation small ember-view']")
	for animation in animation_players:
		double_speed = animation.find_element_by_xpath(".//div[@class='speed-control ']")
		double_speed.click()
		start_button = animation.find_element_by_xpath(".//div[@class='start-button start-graphic']")
		start_button.click()
		time.sleep(1)
		while(True):
			if(animation.find_elements_by_xpath(".//div[@class='pause-button']")):
				time.sleep(.1)
				continue
			try:
				play_button = animation.find_element_by_xpath(".//div[@class='play-button  bounce']")
				play_button.click()
			except:
				pass
			if(animation.find_elements_by_xpath(".//div[@class='play-button rotate-180 ']")):
				break
		print("Completed animation activity")

def completeMultipleChoice(driver):
	multiple_choice_sets = driver.find_elements_by_xpath("//div[@class='interactive-activity-container multiple-choice-content-resource participation large ember-view']")
	multiple_choice_sets += driver.find_elements_by_xpath("//div[@class='interactive-activity-container multiple-choice-content-resource participation medium ember-view']")
	multiple_choice_sets += driver.find_elements_by_xpath("//div[@class='interactive-activity-container multiple-choice-content-resource participation small ember-view']")
	for question_set in multiple_choice_sets:
		questions = question_set.find_elements_by_xpath(".//div[@class='question-set-question multiple-choice-question ember-view']")
		for question in questions:
			choices = question.find_elements_by_xpath(".//label[@aria-hidden='true']")
			for choice in choices:
				choice.click()
				if(question.find_elements_by_xpath(".//div[@class='explanation has-explanation correct']")):
					break
		print("Completed multiple choice set")
			
def completeShortAnswer(driver):
	short_answer_sets = driver.find_elements_by_xpath("//div[@class='interactive-activity-container short-answer-content-resource participation large ember-view']")
	short_answer_sets += driver.find_elements_by_xpath("//div[@class='interactive-activity-container short-answer-content-resource participation medium ember-view']")
	short_answer_sets += driver.find_elements_by_xpath("//div[@class='interactive-activity-container short-answer-content-resource participation small ember-view']")
	for question_set in short_answer_sets:
		questions = question_set.find_elements_by_xpath(".//div[@class='question-set-question short-answer-question ember-view']")
		for question in questions:
			show_answer_button = question.find_element_by_xpath(".//button[@class='show-answer-button zb-button secondary ember-view']")
			show_answer_button.click()
			show_answer_button.click()
			answer = question.find_element_by_xpath(".//span[@class='forfeit-answer']").text
			text_area = question.find_element_by_xpath(".//textarea[@class='zb-text-area hide-scrollbar ember-text-area ember-view']")
			text_area.send_keys(answer)
			check_button = question.find_element_by_xpath(".//button[@class='check-button zb-button primary raised ember-view']")
			check_button.click()
		print("Completed short answer set")

def completeSelectionProblems(driver):
	selection_problem_sets = driver.find_elements_by_xpath("//div[@class='interactive-activity-container detect-answer-content-resource participation large ember-view']")
	selection_problem_sets += driver.find_elements_by_xpath("//div[@class='interactive-activity-container detect-answer-content-resource participation medium ember-view']")
	selection_problem_sets += driver.find_elements_by_xpath("//div[@class='interactive-activity-container detect-answer-content-resource participation small ember-view']")
	for question_set in selection_problem_sets:
		questions = question_set.find_elements_by_xpath(".//div[@class='question-set-question detect-answer-question ember-view']")
		for question in questions:
			choices = question.find_elements_by_xpath(".//div[@class='explanation has-explanation correct']")
			for choice in choices:
				choice.click()
				if(question.find_elements_by_xpath(".//div[@class='explanation has-explanation correct']")):
					break
		print("Completed selection problem set")

driver = webdriver.Firefox()
login(driver)
selectzyBook(driver)
time.sleep(.5)
chapter = chapterSelection(driver)
sectionSelection(driver, chapter)
#driver.quit()