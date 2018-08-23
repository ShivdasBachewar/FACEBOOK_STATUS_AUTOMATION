#!python3 
# A program that login into facebook and update my status as i have stated in programe...
from selenium import webdriver as w;
import time,os,pyautogui as p;

def main():
	try:
		email = q.find_element_by_id('email');		# identifying element for email or mob no
	except Exception as e:
		print("\t Unable to find Element 'email'");
	
	try:
		passwd = q.find_element_by_id('pass');	# identifying element for password
	except Exception as e:
		print("\t Unable to find Element 'pass'");
	
	p.moveTo(email.location['x']+80,110+email.location['y'],1)
	p.click();
	p.typewrite("your_mobile_number",0.25);

	p.moveTo(passwd.location['x']+80,110+passwd.location['y'],1)
	p.click();
	p.typewrite("password",0.25);
	p.PAUSE=1;

	p.press('enter');
	p.press('enter');
	time.sleep(10);

	#--------------------------Getting Status------------ 
	youtube = w.Firefox();
	youtube.get('http://youtu.be');
	p.PAUSE =1;

	p.moveTo(400,125,2);
	p.typewrite("Tu Na Badli",0.25);
	p.moveTo(930,125,1);
	p.click();
	
	p.PAUSE =3;
	p.moveTo(430,330,1);
	p.doubleClick();
	p.PAUSE =1;
	p.moveTo(310,75,1);
	p.doubleClick();
	p.PAUSE =1;
	p.hotkey('ctrl','c');
	p.PAUSE =1;
	p.hotkey('alt','f4');

	#--------------------------------------------
	temp = q.find_element_by_xpath("//textarea");	# identifying textarea of status box
	p.moveTo(temp.location['x']+80,110+temp.location['y'],1);
	p.click();
	p.hotkey('ctrl','v');
	p.PAUSE = 5;
	p.PAUSE = 5;
	p.moveTo(760,550,1);
	p.click();


	p.PAUSE = 12;
	temp = q.find_element_by_id('userNavigationLabel'); 		# identifying logout nevigation key
	p.moveTo(temp.location['x']+75,105+temp.location['y'],1);
	p.PAUSE = 1;
	p.click();
	p.PAUSE = 1;

	p.moveTo(980,530,2);
	p.click();
	p.PAUSE = 10;
	return;

q = w.Firefox();
p.PAUSE = 3;

try:
	q.get('http://www.faceboo.com');
	main();
except Exception as e:
	print("Can't Connect to facebook.com");

p = input("Press ENTER to exit or CTRL-C");
q.close();
