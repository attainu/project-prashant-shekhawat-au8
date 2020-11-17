class Vehicle:
	def __init__(self,Rc_no,color):
		self.Rc_no = Rc_no
		self.color =  color

class ParkingLot:
	def __init__(self):
		self.space = 0
		self.slotid = 0
		self.Slots_filled = 0
		self.slots=[]

	def create_Parking(self,space):
		self.slots = [-1] * space
		self.space = space
		return self.space

	def available_spots(self):
		for i in range(len(self.slots)):
			if self.slots[i] == -1:
				return i

	def park(self,Rc_no,color):
		if self.Slots_filled < self.space: 
			slotid = self.available_spots()
			self.slots[slotid] =Vehicle(Rc_no,color)
			self.slotid = self.slotid+1
			self.Slots_filled = self.Slots_filled + 1
			return slotid+1
		else:
			return -1

	def leave(self,slotid):
		if self.Slots_filled > 0 and self.slots[slotid-1] != -1:
			self.slots[slotid-1] = -1
			self.Slots_filled = self.Slots_filled - 1
			return True
		else:
			return False

	def status(self):
		print("Slot No.\tRegistration No.\tColour")
		for i in range(len(self.slots)):
			if self.slots[i] != -1:
				print(str(i+1) + "\t\t" +str(self.slots[i].Rc_no) + "\t\t\t" + str(self.slots[i].color))
			else:
				continue
    
	def reg_no_by_color(self,color_tobe):
		for i in self.slots:
			if i== -1:
				continue
			elif i.color==color_tobe:
				print(i.Rc_no,end=",")
		print()

	def slot_by_reg_no(self,Rc_no_tobe):
		for i in range(len(self.slots)):
			if self.slots[i]== -1:
				continue
			elif self.slots[i].Rc_no==Rc_no_tobe:
				print(i+1)
				break
		print()

	def slot_by_color(self,color_for_slot):
		for i in range(len(self.slots)):
			if self.slots[i]== -1:
				continue
			elif self.slots[i].color==color_for_slot:
				print(i+1,end=",")
		print()		
	
				
	def view(self,command):
		# create paking with space
		if command.split(' ')[0]=="1":
			n = int(command.split(' ')[1])
			res = self.create_Parking(n)
			print('Parking slot has been created by '+str(res)+' slots')
		# fet details rc and color
		elif command.split(' ')[0]=="2":
			Rc_no = command.split(' ')[1]
			color = command.split(' ')[2]
			res = self.park(Rc_no,color)
			if self.slots==[]:
				print("Create your Parking First")
			else:
				if res == -1:
					print("Sorry, parking is full")
				else:
					print('Allocated slot number: '+str(res))
		# for leaving vehicle
		elif command.split(' ')[0]=="3":
			leave_slotid = int(command.split(' ')[1])
			status = self.leave(leave_slotid)
			if status:
				print('Slot number '+str(leave_slotid)+' is available now')
			else:
				print("The space is already vacant")
		# for status
		elif command.split(' ')[0]=="4":
			if self.slots==[]:
				print("No one Parked yet")
			else:
				self.status()
		#for reg_no_by_color
		elif command.split(' ')[0]=="5":
			color_tobe=command.split(' ')[1]
			count1=0
			for i in range(len(self.slots)):
				if self.slots[i]== -1:
					continue
				elif self.slots[i].color== color_tobe:
					count1=1
					break

			if count1==1:
				self.reg_no_by_color(color_tobe)
			else:
				print("not found")
		#for slot by registration no
		elif command.split(' ')[0]=="6":
			Rc_no_tobe=command.split(' ')[1]
			count2=0
			for i in range(len(self.slots)):
				if self.slots[i]== -1:
					continue
				elif self.slots[i].Rc_no== Rc_no_tobe:
					count2=1
					break

			if count2==1:
				self.slot_by_reg_no(Rc_no_tobe)
			else:
				print("not found")	
		#slot by color
		elif command.split(' ')[0]=="7":
			color_for_slot=command.split(' ')[1]
			count3=0
			for i in range(len(self.slots)):
				if self.slots[i]== -1:
					continue
				elif self.slots[i].color== color_for_slot:
					count3=1
					break

			if count3==1:
				self.slot_by_color(color_for_slot)
			else:
				print("not found")	
		# for exit
		elif command.split(' ')[0]=="0":
			exit(0)
		else:
			print("Wrong command inserted")


def main():
	key=input("Enter i for Interactive command OR Enter any key  for Read pre-written Command from files : ")
	parkinglot = ParkingLot()
	if key=="i":
		print("This is the Begnning of Parking Lot")
		print("Instruction ")
		print("i)    Enter 1, to create Praking ex=(1 6).")
		print("ii)   Enter 2, to Park ex=(2 Rc_no color)")
		print("iii)  Enter 3, to leave ex=(3 slot_id)")
		print("iv)   Enter 4, for status")
		print("v)    Enter 5, for reg_no by color ex=(6 color)")
		print("vi)   Enter 6, for slot by reg_no ex=(5 reg no)")
		print("vii)  Enter 7, for slot by color ex=(7 color)")
		print("viii) Enter 0 ,to exit.")
		while True:
			command = input("$ ")
			parkinglot.view(command)
	else:
		with open("new.txt",'r') as f:
			for command in f:
				command = command.rstrip('\n')
				parkinglot.view(command)
		
main()
	