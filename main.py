import web
web.config.debug = False
from replit import db
import requests
import json
from asteval import Interpreter

urls = (
	'/', 'index',
	'/login', 'login',
	'/signup', 'signup',
	'/save', 'save',
	'/delete', 'delete'
)

app = web.application(urls, locals())
render = web.template.render("templates/")
session = web.session.Session(app, web.session.DiskStore('sessions'))

class index:
	def GET(self):
		user = session.get("user")
		saved = []
		for key in db:
			if db[key]['user'] == user:
				saved.append([int(key), db[key]])
		eq, answer = "", ""
		return render.index(eq, saved, user, answer)
	def POST(self):
		i = web.input()
		user = session.get("user")
		saved = []
		for key in db:
			if db[key]['user'] == user:
				saved.append([int(key), db[key]])
		eq = i.eq.strip().replace(" ", "").replace("÷", "/").replace("^", "**").replace("√", "sqrt").replace("π", "pi")
		aeval = Interpreter()
		answer = aeval(f"""
def factorial(x):
	fact = 1
	for i in range(1,x+1): 
		fact = fact * i
	return fact 
{eq}
""")
		if len(aeval.error)>0:
			answer = ""
			for err in aeval.error:
				answer += err.get_error()[0]
		return render.index(i.eq, saved, user, answer)

class save:
	def POST(self):
		i = web.input()
		ids = []
		for key in db:
			ids.append(int(key))
		if ids == []:
			id = 1
		else:
			id = ids[-1] + 1
		db[id] = {
			"eq":i.eq,
			"ans": i.answer,
			"user": session.get("user")
		}
		raise web.seeother('/')

class delete:
	def POST(self):
		i = web.input()
		del db[i.key]
		raise web.seeother('/')

class login:
	def GET(self):
		##os.system("clear")	
		i = web.input(code=0)
		msg = ""
		if i.code == "1":
			msg = "An error occurred while logging you in. Please try again or contact a deveoper."
		return render.login(msg)
		##os.system("clear")	
		 
	def POST(self):
		##os.system("clear")	
		i = web.input()
		r = requests.post("https://sjauth.coolcodersj.repl.co/apil", data={"user":i.user, "passw":i.passw, "cn":"Calcy"})
		if r.text == "True":
			web.setcookie("logged_in", True)
			session.user = i.user
			raise web.seeother("/")
		else:
			raise web.seeother("/login?code=1")
		##os.system("clear")

class signup:
	def GET(self):
		##os.system("clear")
		i = web.input(code=0)
		msg = ""
		if i.code == "1":
			msg = "An error occurred while signing you up. Please try again or contact a deveoper."	
		return render.signup(msg)
		##os.system("clear")	
		 
	def POST(self):
		##os.system("clear")	
		i = web.input()
		r = requests.post("https://sjauth.coolcodersj.repl.co/apisi", data={"user":i.user, "passw":i.passw, "cn":"Calcy"})
		if r.text == "True":
			web.setcookie("logged_in", True)
			session.user = i.user
			raise web.seeother("/")
		else:
			raise web.seeother("/signup?code=1")
		##os.system("clear")	

if __name__ == "__main__":
	app.run()