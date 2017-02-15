# Tim K. Chan
# 15/02/17

import servo

class ServoController:

	

	# Amount of turn of each discard
	quarterTurn = 30
	bottomAngle = [13, 55, 95, 133]
	topAngle = [0, 12, 170]
	

	def __init__(self, top, bottom):
		self.top = top
		self.bottom = bottom
		self.top.write_angle(250)	# top initial position
		self.bottom.write_angle(10)
		self.state = 0				# State = 0, 1, 2, 3
		self.direction = 1			# 1 = counter clockwise, -1 = clocwise
		self.empty = False
		self.stock = 3
		self.topDirection = 1


	def next(self):

		if self.state == 0 and self.direction == -1:
			self.direction *= -1
			self.bottom.write_angle(ServoController.bottomAngle[self.state + self.direction])
			self.state += self.direction
			print(self.state)


		elif self.state == 1 or self.state == 2 or (self.state == 0 and not self.empty):
			self.bottom.write_angle(ServoController.bottomAngle[self.state + self.direction])
			self.state += self.direction
			print(self.state)

		elif self.state == 0 or self.state == 3:
			self.direction *= -1
			self.bottom.write_angle(ServoController.bottomAngle[self.state + self.direction])
			self.state += self.direction
			print(self.state)

		self.stock -= 1

		if self.stock == 0:
			self.top.write_angle(ServoController.topAngle[self.topDirection])
			print('angle: ', ServoController.topAngle[self.topDirection])
			self.topDirection *= -1
			self.stock = 3
			print('restocked')



