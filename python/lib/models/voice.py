import pygame
pygame.mixer.init()

class Voice(object):
	def __init__(self, volume):
		self.setVolume(volume)

	def play(self, soundFile):
		if (pygame.mixer.music.get_busy() == True):
			return

		pygame.mixer.music.load(soundFile)
		pygame.mixer.music.play()

	def say(self, phrase):
		if (phrase == 'walle_1'):
			self.setVolume(0.12)
			path = "/var/walle/python/lib/sounds/walle_1.mp3"
			self.play(path)

		if (phrase == 'walle_2'):
			self.setVolume(0.18)
			path = "/var/walle/python/lib/sounds/walle_2.mp3"
			self.play(path)

		if (phrase == 'walle_3'):
			self.setVolume(0.21)
			path = "/var/walle/python/lib/sounds/walle_3.mp3"
			self.play(path)

		elif (phrase == 'eva_1'):
			self.setVolume(0.15)
			path = "/var/walle/python/lib/sounds/eva_1.mp3"
			self.play(path)
		
		elif (phrase == 'eva_2'):
			self.setVolume(0.19)
			path = "/var/walle/python/lib/sounds/eva_2.mp3"
			self.play(path)
		
		elif (phrase == 'eva_3'):
			self.setVolume(0.12)
			path = "/var/walle/python/lib/sounds/eva_3.mp3"
			self.play(path)
		
		elif (phrase == 'tada'):
			self.setVolume(0.06)
			path = "/var/walle/python/lib/sounds/tada_2.mp3"
			self.play(path)
		
		elif (phrase == 'whoa'):
			self.setVolume(0.1)
			path = "/var/walle/python/lib/sounds/whoa.mp3"
			self.play(path)
		
		elif (phrase == 'grunting'):
			self.setVolume(0.15)
			path = "/var/walle/python/lib/sounds/grunting.mp3"
			self.play(path)
		
		elif (phrase == 'buynlarge'):
			self.setVolume(0.1)
			path = "/var/walle/python/lib/sounds/buynlarge.mp3"
			self.play(path)

	def sing(self, song):
		if (song == 'la vie en rose'):
			self.setVolume(0.08)
			path = "/var/walle/python/lib/sounds/la_vie_en_rose.mp3"
			self.play(path)

		elif (song == 'background_music'):
			self.setVolume(0.1)
			path = "/var/walle/python/lib/sounds/background_music.mp3"
			self.play(path)

	def getVolume(self):
		return pygame.mixer.music.get_volume()

	def setVolume(self, newVolume):
		pygame.mixer.music.set_volume(newVolume)