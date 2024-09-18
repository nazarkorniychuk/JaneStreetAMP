import tkinter as tk

def tangram_puzzle():
	large_triangle_1 = [
    	50, 50,
    	50, 450,
    	250, 250
	]
	canvas.create_polygon(large_triangle_1,  fill='blue', outline='black')

	large_triangle_2 = [
    	50, 50,
    	250, 250,
    	450, 50
	]
	canvas.create_polygon(large_triangle_2,  fill='green', outline='black')

	medium_triangle = [
    	250, 450,
    	450, 450,
    	450, 250
	]
	canvas.create_polygon(medium_triangle,  fill='orange', outline='black')

	parallelogram = [
    	50, 450,
    	250, 450,
    	350, 350,
    	150,350
	]
	canvas.create_polygon(parallelogram,  fill='red', outline='black')

	small_triangle_1 = [
    	250,250,
    	350, 350,
    	150,350
	]
	canvas.create_polygon(small_triangle_1,  fill='yellow', outline='black')

	square = [
    	250,250,
    	350, 350,
    	450, 250,
    	350, 150
	]
	canvas.create_polygon(square,  fill='grey', outline='black')

	small_triangle_2 = [
    	450, 50,
    	450, 250,
    	350, 150
	]
	canvas.create_polygon(small_triangle_2,  fill='pink', outline='black')

if __name__ == "__main__":
	appWidth = 500
	appHeight = 500

	app = tk.Tk()
	app.title("Tangram Puzzle")
	app.geometry(f"{appWidth}x{appHeight}")
	canvas = tk.Canvas(app, bg="#FFFFFF", width=appWidth, height=appHeight)
	canvas.pack()

	tangram_puzzle()

	app.mainloop()
