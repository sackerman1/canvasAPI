from canvasapi import Canvas, course, assignment
import canvasapi
from parse import *
from datetime import datetime
from twilio.rest import Client



def main():
	token = '13171~dvg11q0NmH6ZsUUXWEwbqSVjqS5cr5zchyTz49ZiXtn8lKqbt1xRhQgQ2n45YyaL'
	url = 'https://ucsd.instructure.com/api/v1/users/self'
	canvas = Canvas(url, token)
	user = canvas.get_current_user()
	print(user.id)

	assignmentList = []
	for assign in getAssignments(canvas):
		if(not isPast(getDueDate(assign))):
			assignmentList.append(assign)

	for assign in assignmentList:
		print(assign, 'due in', getDueDate(assign)-datetime.now())

	assignmentList = sortListByDate(assignmentList)
	print('-'*150)

	for assign in assignmentList:
		print(assign, 'due in', getDueDate(assign)-datetime.now())

	# Useful commands:
	# canvas.get_courses(); Gets list of all courses for the user
	# course.get_assignments(); Gets a list of all get_assignment
	# assignment.due_at; Gets due date of assignment



def courseHasEnded(crse):
	return course.end_at_date.replace(tzinfo=None) < datetime.now(None)


def getClassMates(canvas: Canvas):
	temp = []
	for course in canvas.get_courses():
		for user in course.get_users():
			temp.append(user)
	return temp

def getAssignments(canvas: Canvas):
	temp = []
	for course in canvas.get_courses():
		for assign in course.get_assignments():
			temp.append(assign)
	return temp

def getDueDate(assignment):
	if assignment.due_at is not None:
		return datetime.strptime(assignment.due_at, "%Y-%m-%dT%H:%M:%SZ")
	else:
		return datetime(1,1,1)

def getDate(dateStr):
	if dateStr:
		return datetime.strptime(dateStr, "%Y-%m-%dT%H:%M:%SZ")

def isPast(datetimeObj):
	if(datetimeObj<datetime.now()):
		return True
	return False

def sortListByDate(assList):
	assList.sort(key=lambda date: datetime.strptime(date.due_at, "%Y-%m-%dT%H:%M:%SZ"))
	return assList

main()




# account_sid = "AC6fd8ad98a091f7f743b8806561981df5"
# auth_token = "9141a3145a01567f2a84df0a4ff07198"
# client = Client(account_sid, auth_token)

# call = client.messages.create(
#     to="+19258764016",
#     from_="19253930247",
#     body='suck on deez nuts'
# )

