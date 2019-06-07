from sys import argv
import os
import re
import fnmatch
from table import *
from macro import *
def generate_sym(filename):

	with open(filename,'r') as file:
		li=0
		ad=0
		for line in file:
			li=li+1
			if ":" in line:
				lab4=line.split(":")
				lable.append(lab4[0].strip())
			if " dd " in line:
				count=0
				val=[]
				d1=line.replace('\t','')
				d1=d1.replace(' ',',')
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
					addr.append(ad)
					ad=ad+4
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
				addr.append(ad)
				ad=ad+len(b2[1])
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
					addr.append("-")

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
					addr.append("-")
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
					addr.append("-")
				else:
					sym_name.append(lable[i])
					sym_size.append("-")
					sym_value.append("-")
					sym_type.append("S")
					sym_DU.append("D")
					section.append("text")
					line_no.append("-")
					sym_type1.append("-")
					addr.append("-")
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
					addr.append("-")
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
					addr.append("-")
				else:
					sym_name.append(store_lable[i])
					sym_size.append("-")
					sym_value.append("-")
					sym_type.append("S")
					sym_DU.append("U")
					section.append("text")
					line_no.append(lab_line[i])
					sym_type1.append("-")
					addr.append("-")
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
					addr.append("-")
				else:
					sym_name.append(lable[i])
					sym_size.append("-")
					sym_value.append("-")
					sym_type.append("S")
					sym_DU.append("D")
					section.append("text")
					line_no.append("-")
					sym_type1.append("-")
					addr.append("-")
				if store_lable[i] not in lable:
					sym_name.append(store_lable[i])
					sym_size.append("-")
					sym_value.append("-")
					sym_type.append("S")
					sym_DU.append("U")
					section.append("text")
					line_no.append(lab_line[i])
					sym_type1.append("-")
					addr.append("-")

	for i in range(len(sym_DU)):
		if 'U'==sym_DU[i]:
			er_li.append(li)
			er_name.append("error: symbol undefined")
			er.append(i)
			er_speci.append(sym_name[i])

	file.close()
	#print(lable,store_lable)
def check_inst(filename):
	with open(filename,'r') as file:
		li=0
		for line in file:
			li=li+1
			if "main" in line:
				after_main(line,li,file)
				break

def after_main(line,li,file):
	for line in file:
		li=li+1
		s=line.replace(","," ")
		p1=s.split()
		li_len=len(p1)
		#print(li_len)
		if li_len==1:
			zero_byte_inst(p1,li)
		elif li_len==2:
			one_byte_inst(p1,li)
		elif li_len==3:
			two_byte_inst(p1,li)
		elif li_len==4:
			del(p1[0])
			two_byte_inst(p1,li)
		elif li_len==5:
			er_li.append(li)
			er_name.append("Error:Invalid instruction")
			er.append(104)
			er_speci.append(line)
			break
	file.close()

def zero_byte_inst(p1,li):

	l="".join(p1)
	if ':' not in l:
		er_li.append(li)
		er_name.append("Error:Near")
		er.append(105)
		er_speci.append(l)
def one_byte_inst(p1,li):
	if p1[0] not in inst1:
		er_li.append(li)
		er_name.append("Error:Near")
		er.append(106)
		er_speci.append(p1[0])
	if p1[1] not in lib_call:
		if p1[1] not in reg:
			if "dword" not in p1[1]:
				if p1[1] not in sym_name:
					try:
						k=int(p1[1])
						#lit_name.append("lit")
						hexint='%.2X' % k
						lit_hexval.append(hexint)
						lit_actualval.append(p1[1])
					except ValueError:
						er_li.append(li)
						er_name.append("Error:undefined")
						er.append(109)
						er_speci.append(p1[1])
def two_byte_inst(p1,li):
	if p1[0] not in extern:
		if p1[0] not in inst2 :
			er_li.append(li)
			er_name.append("Error:Syntax Error Near")
			er.append(107)
			er_speci.append(p1[0])
	elif p1[1] not in lib_call:
		if p1[1] not in reg:
			er_li.append(li)
			er_name.append("Error:undefined register")
			er.append(108)
			er_speci.append(p1[1])
	if p1[2] not in reg:
		if p1[2] not in lib_call:
			if "dword" not in p1[2]:
				if p1[2] not in sym_name:
					try:
						k=int(p1[2])
						#lit_name.append("lit")
						hexint='%.2X' % k
						lit_hexval.append(hexint)
						lit_actualval.append(p1[2])
					except ValueError:
						er_li.append(li)
						er_name.append("Error:undefined")
						er.append(109)
						er_speci.append(p1[2])




def gen_lit(filename):
	for i in range(len(sym_type1)):
		if sym_type1[i]=="db":
			hexnum="".join(sym_value[i])
			lit_actualval.append(sym_value[i])
			temp=[]
			for i in range(len(hexnum)):
				mychr=ord(hexnum[i])
				hexstr='%.2X' % mychr
				temp.append(hexstr)
			g="".join(temp)
			lit_hexval.append(g)
		elif sym_type1[i]=="dd":
			lit_actualval.append(sym_value[i])
			t=sym_value[i].split(',')
			temp=[]
			for j in range(len(t)):
				lv=int(t[j])
				hexint='%.2X' % lv
				temp.append(hexint)
			o="".join(temp)
			lit_hexval.append(o)


def inter_code(filenmae):
	with open(filename,"r") as file:
		s=[]
		if fnmatch.fnmatch(filename, '*.asm'):
			inter_file=os.path.splitext(filename)[0]
			li=[inter_file,'i']
			inter_file=".".join(li)
			f=1
			with open(inter_file,"w") as fd:
				for line in file:
					#print(line)
					if " dd " in line:
						l1=line.split()
						#print(l1)
						for i in range(len(s_name)):
							if l1[2] in sym_value[i]:
								l1[2]=s_name[i]
								l2=str(" ".join(l1))
								fd.write("\t")
								fd.write(l2)
								fd.write('\n')

					elif " db " in line:
						l1=line.split('"')
						for i in range(len(s_name)):
							if l1[1] in sym_value[i]:
								l1[1]=s_name[i]
								fd.write(' '.join(l1))
								break
					elif "main" in line:
						fd.write(line)
						after_main1(line,file,fd)
						break

					else:
						fd.write(line)
			return inter_file

def after_main1(line,file,fd):
	for line in file:
		line1=line.replace("\t","")
		line2=line1.replace("\n","")
		l1=line2.replace(","," ")
		l2=l1.split(" ")
		#print(l2)
		len_l2=len(l2)
		temp=[]
		if len_l2==1:
			fd.write("".join(l2))
		elif len_l2==2:
			if l2[0] in inst1:
				temp.append(l2[0])
			if l2[1] in myreg.keys():
				k1=l2[1]
				temp.append(myreg[k1])
			if l2[1] in sym_name:
				for i in range(len(sym_name)):
					if l2[1]==sym_name[i]:
						temp.append(s_name[i])
			if l2[1] in lit_actualval:
				for i in range(len(lit_actualval)):
					if l2[1]==lit_actualval[i]:
						temp.append(lit_name[i])
			if "dword" in l2[1]:
				u=l2[1].split('[')
				t=u[1].split(']')
				for i in range(len(sym_name)):
					if sym_name[i]==t[0]:
						#st='dword['+s_name[i]+']'
						temp.append(s_name[i])
			if l2[1] in lib_call:
				k1=l2[1]
				temp.append(k1)
		elif len_l2==3:
			if l2[0] in inst2:
				temp.append(l2[0])
			if l2[0] in extern:
				temp.append(l2[0])
			if l2[1] in myreg.keys():
				k=l2[1]
				temp.append(myreg[k])
			if l2[1] in lib_call:
				k=l2[1]
				temp.append(k)

			if l2[2] in myreg.keys():
				k1=l2[2]
				temp.append(myreg[k1])
			if l2[2] in lib_call:
				k1=l2[2]
				temp.append(k1)
			if l2[2] in lit_actualval:
				for i in range(len(lit_actualval)):
					if l2[2]==lit_actualval[i]:
						temp.append(lit_name[i])
			if l2[2] in sym_name:
				for i in range(len(sym_name)):
					if l2[2]==sym_name[i]:
						u=l2[2].split('[')
						t=u[1].split(']')
				for i in range(len(sym_name)):
					if sym_name[i]==t[0]:
						st='dword['+s_name[i]+']'
						temp.append(st)

		elif len_l2==4:
			temp.append(l2[0])
			if l2[1] in inst2:
				temp.append(l2[1])
				if l2[2] in myreg.keys():
					k=l2[2]
					temp.append(myreg[k])
				if l2[3] in myreg.keys():
					k1=l2[3]
					temp.append(myreg[k1])
				if l2[3] in lit_actualval:
					for i in range(len(lit_actualval)):
						if l2[3]==lit_actualval[i]:
							temp.append(lit_name[i])
				if l2[3] in sym_name:
					for i in range(len(sym_name)):
						if l2[3]==sym_name[i]:
							temp.append(sym_name[i])



		fd.write('\t')
		fd.write(" ".join(temp))
		fd.write("\n")

		#print(l2)

def obj_code(i_file):
	with open(i_file,"r") as ifile:
		o_file=os.path.splitext(filename)[0]
		o_file=o_file+'.o'
		ofile=open(o_file,"w")
		for line in ifile:
			if "main:" in line:
				for_ofile_after_main(line,ofile,ifile)
				break
	return o_file

def for_ofile_after_main(line,ofile,ifile):
	for line in ifile:
		splited_line=line.split()
		li_len=len(splited_line)
		if li_len==1:
			go_1(splited_line,ofile)
		elif li_len==2:
			go_2(splited_line,ofile)
		elif li_len==3:
			go_3(splited_line,ofile)
		elif li_len==4:
			go_3(splited_line,ofile)
def go_1(s_li,ofile):
	pass
def go_2(s_li,ofile):
	temp=[]
	if s_li[0] in inst1:
		temp.append(s_li[0])
	if s_li[1] in ob_reg.keys():
		temp.append("r32")
	elif s_li[1] in s_name:
		temp.append("imm32")
	elif s_li[1] in lit_actualval:
		temp.append("imm8")
	elif "dword" in s_li[1]:
		temp.append("rm32")
	elif s_li[1] in lib_call:
		temp.append("rel32")			#7:34 13/10/18 how to identify and set the opcode
	gen_obj(temp,s_li,ofile)
def go_3(s_li,ofile):
	temp=[]
	if s_li[0] in inst2:
		temp.append(s_li[0])
	if s_li[1] in list(ob_reg.keys())[0]:
		temp.append("r32")
		if "dword" in s_li[2]:
			temp.remove("r32")
			temp.append("eax")
			temp.append("moffs32")
	elif s_li[1] in list(ob_reg.keys())[1:]:
		temp.append("r32")
		if "dword" in s_li[2]:
			temp.append("rm32")
	if s_li[2] in ob_reg.keys():
		temp.append("r32")
	elif s_li[2] in lit_name:
		temp.append("imm8")
	#print(temp,s_li)
	gen_obj(temp,s_li,ofile)

def gen_obj(t,s_li,ofile):
	#print(t,s_li)
	op_file=open("opcode_tab.txt","r")
	for line in op_file:
		line=line.replace("\n","")
		p1=line.split("\t")
		#print(p1)
		p2=p1[1].split("|")
		#print(p1[0],p2,t,s_li)
		if t==p2:
			if p1[0]=="A1":
				for i in range(len(s_name)):
					if s_name[i] in s_li[2]:
						for j in range(len(lit_name)):
							if lit_actualval[i]==sym_value[i]:
								ob_line=p1[0]+lit_hexval[i]
								ofile.write(ob_line)
								ofile.write("\n")
								break
			elif p1[0]=="8B/r":
				for i in range(len(s_name)):
					if s_name[i] in s_li[2]:
						for j in range(len(lit_name)):
							if lit_actualval[i]==sym_value[i]:
								q=lit_hexval[i]
								break
				ls=p1[0].replace('/r','')
				for k in ob_reg.keys():
					if k==s_li[1]:
						code='00'+ob_reg[k]+'101'
				ob_line=ls+str(int(code[:4],2))+str(int(code[4:],2))+q
				ofile.write(ob_line)
				ofile.write("\n")
			elif p1[0]=="89/r":
				ls=p1[0].replace('/r','')
				for k in ob_reg.keys():
					if k==s_li[1]:
						p1=ob_reg[k]
					if k==s_li[2]:
						p2=ob_reg[k]
				code='11'+p2+p1
				a=int(code[4:],2)
				b=int(code[:4],2)
				a='%2X'%a
				b='%2X'%b
				ob_line=ls+b.replace(" ",'')+a.replace(" ",'')
				ofile.write(ob_line)
				ofile.write("\n")
			elif p1[0]=='01/r':
				ls=p1[0].replace('/r','')
				for k in ob_reg.keys():
					if k==s_li[1]:
						p1=ob_reg[k]
					if k==s_li[2]:
						p2=ob_reg[k]
				code='11'+p2+p1
				a=int(code[4:],2)
				b=int(code[:4],2)
				a='%2X'%a
				b='%2X'%b
				ob_line=ls+b.replace(" ",'')+a.replace(" ",'')
				ofile.write(ob_line)
				ofile.write("\n")
				#print(p1)
			elif p1[0]=='50+rd':
				ls=p1[0].replace('+rd','')
				for k in ob_reg.keys():
					if k==s_li[1]:
						ob_line=50+int(ob_reg[k],2)
						ofile.write(str(ob_line))
						ofile.write("\n")
			elif p1[0]=='68/id':
				ls=p1[0].replace('/id','')
				for i in range(len(sym_name)):
					if s_name[i]==s_li[1]:
						ob_line='68'+'[0'+str(addr[i])+'000000]'
						ofile.write(ob_line)
						ofile.write("\n")
			elif p1[0]=='E8/cd':
				ls=p1[0].replace('/cd','')
				ob_line=ls+'(00000000)'
				ofile.write(ob_line)
				ofile.write("\n")
			elif p1[0]=='83/0,ib':
				ls=p1[0].replace('/0,ib','')
				for k in ob_reg.keys():
					if k==s_li[1]:
						p=int(ob_reg[k],2)
						a='%2X'% p
						a=a.replace(' ','')
						for i in range(len(lit_name)):
							if s_li[2]==lit_name[i]:
								h=lit_hexval[i]
						ob_line=ls+'C'+a+h
						ofile.write(ob_line)
						ofile.write("\n")
	return
				#print(p1)
	#ofile.close()
		#ifile.close()

def smaco(o_file):
	n=2
	with open(o_file,"r") as f1:
		for line in f1:
			if(bool(re.match(r'[a-zA-Z0-9]*$',line))):
				print(line)
			else:
				print(line)

if __name__=='__main__':
	if len(argv)<2:
		print("Error:Specify file name")
	else:
		filename=argv[1]
		if fnmatch.fnmatch(filename, '*.asm'):
			generate_sym(filename)
			gen_lit(filename)
			check_inst(filename)
			if len(er)==0:
				for i in range(len(sym_name)):
					sname=['sym']
					sname.append(str(i))
					sname="".join(sname)
					s_name.append(sname)
				#print("\n\n\t\t-----------******Symbol Table******--------------\n\n")
			#	print("sname","sym_name","sym_size","sym_DU","sym_type","line_no","section","sym_value")
				#print(len(s_name),'\t',len(sym_name),'\t',len(sym_size),'\t',len(sym_DU),'\t',len(sym_type),'\t',len(line_no),'\t',len(section),'\t',len(sym_type1),'\t',len(sym_value))
				#for i in range(len(sym_name)):
				#	print(s_name[i],'\t',sym_name[i],'\t',sym_size[i],'\t',sym_DU[i],'\t',sym_type[i],'\t',line_no[i],'\t',section[i],'\t',sym_type1[i],'\t',sym_value[i],'\t',addr[i])

				temp=[]
			#	print("\n\n\t\t-----------******Literal Table******--------------\n\n")
				for i in range(len(lit_name)):
					temp.append(lit_name[i])
					temp.append('{}'.format(i))
					d="".join(temp)
					lit_name[i]=d
					temp=[]
				for i in range(len(lit_hexval)):
					lname=['lit']
					lname.append(str(i))
					lname="".join(lname)
					lit_name.append(lname)
				#	print(lit_name[i],'\t',lit_actualval[i],'\t',lit_hexval[i])
				i_file=inter_code(filename)
				#print(i_file)
				o_file=obj_code(i_file)
				smaco(o_file)
			else:
				for i in range(len(er)):
					print(er[i],filename,':',er_li[i],':',er_name[i],'"',er_speci[i],'"')
		else:
			print("Warrning:Please Specify only .asm file")
