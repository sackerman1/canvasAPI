from canvasapi import Canvas
from parse import *
from datetime import datetime

def main():
	token = '13171~dvg11q0NmH6ZsUUXWEwbqSVjqS5cr5zchyTz49ZiXtn8lKqbt1xRhQgQ2n45YyaL'
	url = 'https://ucsd.instructure.com/api/v1/users/self'
	canvas = Canvas(url, token)
	user = canvas.get_current_user()
	temp = []
	for course in canvas.get_courses():
		for assign in course.get_assignments():
			temp.append(getDueDate(assign))
			print(assign, 'due in', getDueDate(assign)-datetime.now())
			myTemp = assign.due_at
	#print(temp)	



	# print(getAssignments(canvas)[0]['id'])
# for gen in user.get_profile():
# 	print(gen)
# for course in canvas.get_courses():
# 	for feet in course.get_enabled_features():
# 		print(feet)	




def getClassMates(canvas):
	temp = []
	for course in canvas.get_courses():
		for user in course.get_users():
			temp.append(user)
	return temp

def getAssignments(canvas):
	temp = []
	for course in canvas.get_courses():
		for assign in course.get_assignments():
			temp.append(assign)
	return temp

def getDueDate(assignment):
	if assignment.due_at is not None:
		return datetime.strptime(assignment.due_at, "%Y-%m-%dT%H:%M:%SZ")
	else:
		return datetime.now()

main()


from twilio.rest import Client

account_sid = "AC6fd8ad98a091f7f743b8806561981df5"
auth_token = "9141a3145a01567f2a84df0a4ff07198"
client = Client(account_sid, auth_token)

call = client.messages.create(
    to="+19258764016",
    from_="19253930247",
    body='suck on deez nuts'
)

