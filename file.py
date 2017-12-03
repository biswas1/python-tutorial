# this program is for opening , writing , reading a file 

file = open("test_data.txt","w")
# w means write mode 
file.write("python tutorial for opening and writing text in .txt file!")
file.close()
file=open("test_data.txt","r")
print file.read()
#r = reading mode
