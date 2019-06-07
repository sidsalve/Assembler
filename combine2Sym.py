from table import *
from sys import argv	
def generate_sym(filename):
	
	with open(filename,'r') as file:
		li=0
		for line in file:
			li=li+1
			if ":" in line:
				lab4=line.split(":")
				lable.append(lab4[0].strip())			
			if " dd " in line:
				count=0
				val=[]
				d1=line.replace(' ',',')
				d2=d1.split(',')
				if d2[0] not in sym_name:
					sym_name.append(d2[0])
					for i in range(2,len(d2)):
						count=count+1
						val.append(d2[i])
					s=",".join(val)
					sym_size.append((4*count))
					sym_value.append(s)
					sym_type.append("S")
					sym_DU.append("D")
					section.append("data")
					line_no.append(li)
					sym_type1.append("dd")
				else:
					er_li.append(li)
					er_name.append("Error:already defined")
					er.append(110)
					er_speci.append(d2[0])
				
			elif " db " in line:
				b1=line.replace(' ',',')
				b2=b1.split('"')
				#print(b2)
				sym_value.append(b2[1].replace(',',' '))
				#print(sym_value)
				sym_size.append(len(b2[1]))
				b3=b2[0].replace(',',' ')
				b4=b3.split()
				sym_name.append(b4[0])	
				sym_type.append("S")
				sym_DU.append("D")
				section.append("data")
				line_no.append(li)
				sym_type1.append("db")
			elif " resb " in line:
				rb1=line.split()
				if rb1[0] in sym_name:
					er_li.append(li)
					er_name.append("Error:already defined")
					er.append(101)
					er_speci.append(rb[0])
					
				else:
					
					sym_name.append(rb1[0])
					sym_size.append(1*int(rb1[2]))
					sym_value.append(rb1[2])
					sym_type.append("L")
					sym_DU.append("D")
					section.append("bss")
					line_no.append(li)
					sym_type1.append("resb")
				
			elif " resd " in line:
				rd1=line.split()
				if rd1[0] in sym_name:
					er_li.append(li)
					er_name.append("Error:already defined")
					er.append(102)
					er_speci.append(rd1[0])
				else:
					
					sym_name.append(rd1[0])
					sym_size.append(4*int(rd1[2]))
					sym_value.append(rd1[2])
					sym_type.append("L")
					sym_DU.append("D")
					section.append("bss")
					line_no.append(li)
					sym_type1.append("resd")
			elif "global" in line:
				lab=line.split()
				#print(len(lab))
				if len(lab)>1:
					store_lable.append(lab[1])
					lab_line.append(li)
				else:
					er_li.append(li)
					er_name.append("Error:main function not defined")
					er.append(103)
					er_speci.append("-")
					
				
					
					
			elif "jmp" in line:
				lab1=line.split()
				if len(lab1)>1:
					store_lable.append(lab1[1])
					lab_line.append(li)
					
			elif "jz" in line:
				lab2=line.split()
				if len(lab2)>1:
					store_lable.append(lab2[1])
					lab_line.append(li)					
					
		if len(lable)>len(store_lable):
			for i in range(len(lable)):
				if lable[i] in store_lable:
					sym_name.append(lable[i])
					sym_size.append("-")
					sym_value.append("-")
					sym_type.append("S")
					sym_DU.append("D")
					section.append("text")
					line_no.append("-")
					sym_type1.append("-")		
				else:
					sym_name.append(lable[i])
					sym_size.append("-")
					sym_value.append("-")
					sym_type.append("S")
					sym_DU.append("D")
					section.append("text")
					line_no.append("-")
					sym_type1.append("-")		
			for i in range(len(store_lable)):
				if store_lable[i] not in lable:
					sym_name.append(store_lable[i])
					sym_size.append("-")
					sym_value.append("-")
					sym_type.append("S")
					sym_DU.append("U")
					section.append("text")
					line_no.append(lab_line[i])
					sym_type1.append("-")		
		elif len(lable)<len(store_lable):
			for i in range(len(store_lable)):
				if store_lable[i] in lable:
					sym_name.append(store_lable[i])
					sym_size.append("-")
					sym_value.append("-")
					sym_type.append("S")
					sym_DU.append("D")
					section.append("text")
					line_no.append("-")
					sym_type1.append("-")				
				else:
					sym_name.append(store_lable[i])
					sym_size.append("-")
					sym_value.append("-")
					sym_type.append("S")
					sym_DU.append("U")
					section.append("text")
					line_no.append(lab_line[i])
					sym_type1.append("-")		
		elif len(lable)==len(store_lable):
			for i in range(len(store_lable)):
				if lable[i] not in store_lable:
					sym_name.append(lable[i])
					sym_size.append("-")
					sym_value.append("-")
					sym_type.append("S")
					sym_DU.append("D")
					section.append("text")
					line_no.append("-")
					sym_type1.append("-")		
				else:
					sym_name.append(lable[i])
					sym_size.append("-")
					sym_value.append("-")
					sym_type.append("S")
					sym_DU.append("D")
					section.append("text")
					line_no.append("-")
					sym_type1.append("-")				
				if store_lable[i] not in lable:
					sym_name.append(store_lable[i])
					sym_size.append("-")
					sym_value.append("-")
					sym_type.append("S")
					sym_DU.append("U")
					section.append("text")
					line_no.append(lab_line[i])
					sym_type1.append("-")		
		
	for i in range(len(sym_DU)):
		if 'U'==sym_DU[i]:
			er_li.append(li)
			er_name.append("error: symbol undefined")
			er.append(i)
			er_speci.append(sym_name[i])					
	
	file.close()
if __name__=='__main__':
	file1=argv[1]
	file2=argv[2]
	for i in range(len(argv)):
		if i==1:
			generate_sym(file1)
		elif i==2:
			generate_sym(file2)
		
	for i in range(len(sym_name)):
		sname=['sym']
		sname.append(str(i))
		sname="".join(sname)
		s_name.append(sname)	
	for i in range(len(sym_name)):
		print(s_name[i],'\t',sym_name[i],'\t',sym_size[i],'\t',sym_DU[i],'\t',sym_type[i],'\t',line_no[i],'\t',section[i],'\t',sym_type1[i],'\t',sym_value[i])
	#print(len(s_name),'\t',len(sym_name),'\t',len(sym_size),'\t',len(sym_DU),'\t',len(sym_type),'\t',len(line_no),'\t',len(section),'\t',len(sym_type1),'\t',len(sym_value))


	print(sym_name)	

