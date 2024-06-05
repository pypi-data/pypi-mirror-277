
class Texutre:
	def __init__(self,path):
		self.textur3e = glGenTextures(1)
		glBindTexture(GL_TEXTURE_2D,self.texture)
		glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S,GL_REPEAT)
		glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T,GL_REPEAT)
		glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST)
		glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
		image = pg.image.load(filepath).convert()
		image_width, image_height = image.get_rect().size
		image_data = pg.image.tostring(image,"RGBA")
		glTexImage2D(GL_TEXTURE_2D)
