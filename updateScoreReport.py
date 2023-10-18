import time

def UpdateScoreReport():
	file = open('/home/tstark/Desktop/ScoreReport.html', 'r')
	lines = file.readlines()
	
	linesToWrite = []
	for line in lines:
		if "MISS" not in line:
			linesToWrite.append(line)
	file.close()
	
	file = open('/home/tstark/Desktop/ReadScoreReport.html', 'w')
	file.writelines(linesToWrite)
	file.close()
			
starttime = time.monotonic()

while True:
	UpdateScoreReport()
	time.sleep(30.0 - ((time.monotonic() - starttime) %30))
