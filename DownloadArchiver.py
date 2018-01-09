#! python3

import shutil
import os

def fileWalker(directory):
	#walk files to make list of all current files NOT FOLDERS inside dir
	#returns list of files

	#return os.listdir() #returns list of sub folders and files in current dir

	files = []
	for folderName, subFolders, fileNames in os.walk(directory):
	#	print("the current folder is "+ folderName)

		# for subFolder in subFolders:
		# 	print ("SUBFOLDER OF "+ folderName + ": "+ subFolder)


		files.extend(fileNames)

	return files

def folderCreator(directory, fileTypes):
	#create folders based on file types
	#if folder exists it will not make a new one

	for fileType in fileTypes.keys():

		#TODO: only create folders for existing file types

		newDirectory = directory + "\\" + fileType

		if not os.path.exists(newDirectory):
			os.mkdir(newDirectory)

	return

def fileMover(file, fileTypes, directory):
	#take as parameter a file and move it to respective folder
	#TODO move videos to downloads folder in users/video folder


	if "." in file:
		temp = file.split(".")
		fileFormat = temp[-1]
	else:
		return

	for fileType in fileTypes.keys():

		source = directory + "\\" + file

		if fileFormat in fileTypes[fileType]:
			destination = directory + "\\" + fileType + "\\" # + file
			shutil.move(source, destination)



	return

def main():

	#define as dictionary file types and their respective folders
	fileTypes = {}
	fileTypes["Images"] = ["jpg", "gif", "png", "jpeg", "bmp"]
	fileTypes["Audio"] = ["mp3", "wav", "aiff", "flac", "aac"]
	fileTypes["Video"] = ["m4v", "flv", "mpeg", "mov", "mpg", "mpe", "wmv", \
	                      "MOV", "mp4"]
	fileTypes["Documents"] = ["doc", "docx", "txt", "ppt", "pptx", "pdf", "rtf", "xlsx"]
	fileTypes["Exe"] = ["exe"]
	fileTypes["Compressed"] = ["zip", "tar", "7", "rar"]
	fileTypes["ISO"] = ["iso"]

	directory = "C:\\Users\\MoCkY1998\\Downloads" #for now


	files = fileWalker(directory)

	folderCreator(directory, fileTypes)

	#iterate through list of files to add them to file mover
	for file in files:
		fileMover(file, fileTypes, directory)

	print("DONE")

main()
