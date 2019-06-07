from table import *
t1=[]
li_no=[]
code=[]
start_macro_line_no=[]
end_macro_line_no=[]
start_main=[]
start_data=[]
mac_token=["%macro","%endmacro"]
def macro_name(fd):
	for line in fd:
		if "%macro" in line:
			l_list=line.split()
			mac_name.append(l_list[1])
			mac_para.append(l_list[2])
			go_end_mac(line,fd)

def go_end_mac(line,fd):
	t1=[]
	for line in fd:
		if "%endmacro" in line:
			mac_def.append(t1)
			break
		else:
			line=line.replace("\t","")
			line=line.replace("\n","")
			t1.append(line)

def macdef(a,b):
	for j in range(a,b):
		#print(code[j])
		pass


if __name__=='__main__':
	fd=open("for_mac.asm","r")
	fd1=open("for_mac.asm","r")
	wr=open(".macro.asm","w")
	macro_name(fd1)
	lines=fd.readlines()
	for i,line in enumerate(lines):
		li_no.append(i)
		code.append(lines[i])
	for i in range(len(li_no)):
		if "%macro" in code[i]:
			start_macro_line_no.append(i)
		elif "%endmacro" in code[i]:
			end_macro_line_no.append(i)
		elif "main:" in code[i]:
			start_main.append(i)
		elif ".data" in code[i]:
			start_data.append(i)
	for i in range(len(start_macro_line_no)):
		macdef(start_macro_line_no[i],end_macro_line_no[i])
	if len(start_macro_line_no)!=len(end_macro_line_no):
		print("Error")
	elif len(start_macro_line_no) & len(end_macro_line_no) ==0:
		for j in range(len(li_no)):
			wr.write(code[j])
	else:
		for h in range(start_data[0],start_main[0]):
			wr.write(code[h])

		for i in range(start_main[0],len(li_no)):
			if ',' in code[i]:
				#print(code[i])
				l1=code[i].replace(","," ")
				l1=l1.split()
				if len(l1)<4:
					for k in range(len(mac_name)):
						if mac_name[k]==l1[0]:
							for i in range(len(mac_def[k])):
								if "%1" in mac_def[k][i]:
									s=mac_def[k][i].replace("%1",l1[1])
									wr.write(s)
									wr.write("\n")
									wr.write("\t")
								elif "%2" in mac_def[k][i]:
									s=mac_def[k][i].replace("%2",l1[2])
									wr.write(s)
									wr.write("\n")
									wr.write("\t")
								else:
									wr.write(mac_def[k][i])
									wr.write("\n")
									wr.write("\t")
						elif l1[0] not in mac_name:
							wr.write(code[i])
							break

			else:
				wr.write(code[i])
