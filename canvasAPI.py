from canvasapi import Canvas

def main():
	token = '13171~dvg11q0NmH6ZsUUXWEwbqSVjqS5cr5zchyTz49ZiXtn8lKqbt1xRhQgQ2n45YyaL'
	url = 'https://ucsd.instructure.com/api/v1/users/self'
	canvas = Canvas(url, token)
	user = canvas.get_current_user()
	for course in canvas.get_courses():
		for assign in course.get_assignments():
			print(assign.muted)
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

main()