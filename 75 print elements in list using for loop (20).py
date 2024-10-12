#in python file can be used to perform operations (ie read and write operation)
"""
1. Text Files
Plain Text Files: These files contain unformatted text (e.g., .txt).
CSV Files: Comma-separated values files, often used for storing tabular data (e.g., .csv).
JSON Files: JavaScript Object Notation files used for structured data interchange (e.g., .json).
XML Files: Extensible Markup Language files for structured data (e.g., .xml).
2. Binary Files
Executable Files: Compiled programs that can be executed (e.g., .exe).
Image Files: Files containing image data, like PNG, JPEG (e.g., .png, .jpg).
Audio Files: Files that contain audio data (e.g., .mp3, .wav).
Video Files: Files containing video data (e.g., .mp4, .avi).
Pickle Files: Used for serializing Python objects (e.g., .pkl, .pickle).

3. Special File Types
Log Files: Files used for logging information (e.g., .log).
Configuration Files: Files used for application configurations (e.g., .ini, .conf).
HTML Files: Files that contain HTML markup (e.g., .html)."""

#OPEN < READ AND CLOSE FILE
# f = open("file.txt", mode) can be read nad write
#data=f.write()
#data=f.read()
#f.close()

f=open("demo.text","r")
data=f.read()
print(data)
f.close()
