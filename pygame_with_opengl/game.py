import pygame as pg 
import numpy as np 
from OpenGL.GL import *
# Импортируем функции, упрощающие работу с шейдерами
from OpenGL.GL.shaders import compileShader, compileProgram


# Исходный код вершинного шейдера
vertex_src = """
#version 440

layout(location=0) in vec3 vertex_position; 	// координаты вершин
layout(location=1) in vec3 in_color; 			// цвета вершин
out vec3 out_color;

void main()
{
	/* Передаем координаты на следующие
	 * этапы графического конвейера
	 * без матричных преобразований.
	 */
	 gl_Position = vec4(vertex_position, 1);

	 // Передаем цвета во фрагментный шейдер.
	 out_color = in_color;
}
"""

# Исходный код фрагментного шейдера
fragment_src = """
#version 440

//принимаем цвета из вершинного шейдера
in vec3 out_color;

out vec4 fragment_color;

void main()
{
	fragment_color = vec4(out_color, 1);
}
"""


class Game():
	"""
	Класс, содержащий все данные и методы игры.

	Атрибуты
	----------
	caption : str
		Заголовок окна игры.
	screen_width : int
		Ширина окна игры в пикселях.
	screen_height : int
		Высота окна игры в пикселях.

	"""
	def __init__(self):
		self.caption = "Pygame with OpenGL"
		self.screen_width = 800
		self.screen_height = 600

	def run(self):
		"""
		Метод, который инициализирует Pygame и игровые объекты и запускает  игру.
		"""
		pg.init()
		
		# Указываем параметры pg.DOUBLEBUF и pg.OPENGL, чтобы использовать 
		# функции OpenGL для рисования. При этом функции рисования из Pygame перестанут работать!
		screen = pg.display.set_mode((self.screen_width, self.screen_height), pg.DOUBLEBUF | pg.OPENGL)
		
		pg.display.set_caption(self.caption)

		# Задаем фоновый цвет. Исходный цвет серый: (200, 200, 200), здесь
		# каждый цветовой канал (красный, зеленый, синий) выражен 8-битным числом,
		# т.е. числом от 0 до 255. Но в OpenGL цветовые каналы принимают значение от 0 до 1,
		# поэтому делим число в каждом цветовом канале на 255.
		glClearColor(200/255, 200/255, 200/255, 1)

		# Задаем массив с координатами и цветами вершин треугольника.
		triangle = [ 
					# x     y    z     r        g        b
					 0.0,  0.5, 0.0, 52/255, 178/255, 152/255,
					-0.5, -0.5, 0.0, 57/255, 151/255, 211/255,
					 0.5, -0.5, 0.0, 81/255, 179/255, 110/255
					]
		# Из-за того, что в Python динамическая типизация, мы не можем
		# передать данные из питоновского списка в буфер напрямую.
		# Необходимо преобразовать его в numpy-массив и указать тип данных.
		triangle = np.array(triangle, dtype=np.float32)


		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ РАБОТА С БУФЕРАМИ ~~~~~~~~~~~~~~~~~~~~~~~~~~~
		# 1. Cоздаем буфер.
		triangle_buffer = glGenBuffers(1)

		# 2. "Привязываем" буфер, чтобы затем загрузить в него данные.
		glBindBuffer(GL_ARRAY_BUFFER, triangle_buffer)

		# 3. Передаем в буфер данные из массива.
		glBufferData(GL_ARRAY_BUFFER, triangle.nbytes, triangle, GL_STATIC_DRAW)

		# Считываем данные из буфера (из любопытства).
		buffer_data = glGetBufferSubData(GL_ARRAY_BUFFER, 0, triangle.nbytes)
		# Выводим данные в консоль.
		print(buffer_data.view(dtype=np.float32))



		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ РАБОТА С ШЕЙДЕРАМИ ~~~~~~~~~~~~~~~~~~~~~~~~~~~
		# 1. Написать исходный код шейдеров. См. vertex_src и fragment_src в начале этого файла.
		
		# 2.1. Компилируем вершинный шейдер.
		vertex_shader = compileShader(vertex_src, GL_VERTEX_SHADER)

		# 2.2. Компилируем фрагментный шейдер.
		fragment_shader = compileShader(fragment_src, GL_FRAGMENT_SHADER)

		# 3. Объединяем ("линкуем") шейдеры в шейдерную программу
		shader_program = compileProgram(vertex_shader, fragment_shader)

		# 4. Делаем нашу шейдерную программу активной
		glUseProgram(shader_program)



		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ ПЕРЕДАЕМ ДАННЫЕ В ВЕРШИННЫЙ ШЕЙДЕР ~~~~~~~~~~~~~~~~~~~~~~~~~~~
		# Передаем координаты вершин в вершинный шейдер
		glEnableVertexAttribArray(0)
		glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, triangle.itemsize*6, ctypes.c_void_p(0))

		#Передаем цвета вершин в вершинный шейдер
		glEnableVertexAttribArray(1)
		glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, triangle.itemsize*6, ctypes.c_void_p(triangle.itemsize*3))
		# Зададим сиреневый цвет для проверки работы glEnableVertexAttribArray
		glVertexAttrib3fv(1, np.array([142/255, 68/255, 173/255], dtype=np.float32))

		# Попробуйте закомментировать строку: glEnableVertexAttribArray(1).
		# Тогда следующая за ней строка glVertexAttribPointer(....) станет бесполезной,
		# т.к. мы не указали, что нужно использовать данные из буфера.
		# В то же время строка glVertexAttrib3fv(....) перестанет быть бесполнезной ...
		
		while True:
			for event in pg.event.get():
				if event.type == pg.QUIT:
					quit()
				if event.type == pg.KEYDOWN:
					if event.key == pg.K_ESCAPE:
						quit()

			# Применяем фоновую заливку окна.
			# Стираем старый кадр из Color Buffer перед рисованием следующего кадра.
			glClear(GL_COLOR_BUFFER_BIT)

			# Выводим треугольник на экран.
			glDrawArrays(GL_TRIANGLES, 0, 3)
			
			pg.display.flip()


if __name__ == "__main__":
	new_game = Game()
	new_game.run()
