import os
import shutil

BASE_DIR = os.getcwd()
str_project_dir = r"microfinance_api\__pycache__"
str_api_dir = r"api\__pycache__"
ui_dir = r"static"

def cleanUp(str_dir):
	project_dir = os.path.join(BASE_DIR, str_dir)
	for x  in os.listdir(project_dir):
		old_file_path = os.path.join(project_dir, x)
		y = x.replace('.cpython-39', "")
		new_file_path = os.path.join(project_dir, y)
		os.rename(old_file_path, new_file_path)
	copyFiles(str_dir)


def copyFiles(str_dir):
	current_dir = os.path.join(BASE_DIR, str_dir)
	target_dir = os.path.join(BASE_DIR, str_dir.split("\\")[0])
	for x  in os.listdir(current_dir):
		original = os.path.join(str_dir, x)
		target = os.path.join(target_dir, x)
		shutil.copyfile(original, target)
	removePy(str_dir)


def removePy(str_dir):
	current_dir = os.path.join(BASE_DIR, str_dir.split("\\")[0])
	print(current_dir)
	for x  in os.listdir(current_dir):
		if x.endswith('.py'):
			os.remove(os.path.join(current_dir, x))
	removePycache(str_dir)

def removePycache(str_dir):
	for x  in os.listdir(str_dir):
		os.remove(os.path.join(str_dir, x))
	os.rmdir(os.path.join(BASE_DIR, str_dir))


def cleanAppCSS(str_dir):
	x_path = os.path.join(str_dir, "app.css")
	app_css = open(x_path,"rt")
	data = app_css.read()

	data = data.replace('/public/static/bja.jpg', 'bja.jpg')
	data = data.replace('../img/bja.jpg', 'bja.jpg')
	app_css.close()
	app_css = open(x_path, 'wt')
	app_css.write(data)
	app_css.close()

def moveStatic(str_dir):
	for x in os.listdir(os.path.join(str_dir, "static")):
		shutil.copyfile(os.path.join(os.path.join(str_dir, "static"), x), os.path.join(str_dir, x))
		os.remove(os.path.join(os.path.join(str_dir, "static"),x))
	os.rmdir(os.path.join(str_dir, "static"))



x = int(input("""1.Compile Py files only\n2.Compile static files only\n3.Compile all files\n : """))

if x == 1:
	try:
		cleanUp(str_project_dir)
		cleanUp(str_api_dir)
	except FileNotFoundError:
		print("No new files found!, compile first and run again")
elif x == 2:
	try:
		cleanAppCSS(ui_dir)
		moveStatic(ui_dir)
	except FileNotFoundError:
		print("No new files found!, build and add new static files")
elif x == 3:
	cleanUp(str_project_dir)
	cleanUp(str_api_dir)
	cleanAppCSS(ui_dir)
	moveStatic(ui_dir)
else:
	print("Invalid choice")

