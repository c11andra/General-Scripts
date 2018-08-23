import os
import win32clipboard

win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()
desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
path = desktop+'\\test.xml'
file = open(path, 'w')
encodedData = data.encode('string_escape')
strippeddata = encodedData.rstrip('\\x00\n\r')
decodedData = strippeddata.decode('string_escape')
file.write(decodedData)
file.close()
print "Data has been written to "+path
