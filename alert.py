import smtplib
#from translate import Translator
from email.message import EmailMessage

#Phone ext URL: https://www.youtube.com/watch?v=B1IsCbXp0uE&ab_channel=ClarityCoders


def translateAssignment():
    translator = Translator(to_lang="Spanish")
    translation = translator.translate("Assignment")
    print (translation)
    return translation

def email_alert(subject, body, to):
	#Library EmailMessage
	msg = EmailMessage()
	msg.set_content(body)
	msg['subject'] = subject

	#userReceiving
	msg['to'] = to

	user = "rafaelalvaradojr.jw@gmail.com"
	msg['from'] = user
	password = "vlssqldczskqtvdd"

	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(user, password)
	server.send_message(msg)

	server.quit()

#if __name__ == '__main__':
#11/7/22 Convert English to Spanish accents
#subject = translateAssignment()
#body = translate("This is a reminder you have part the week of 7 of November to 13 of November please confirm if you received this message. ")
#verizon alerts
#email_alert("Hubby", "I Love you", "6692631514@vtext.com")
email_alert("Friend", "ChatGpt", "5107178766@vtext.com")
