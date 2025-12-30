from functools import reduce
from math import inf, ceil, floor
from itertools import chain, pairwise
from PIL import Image

def visualize(
		data, # all the input data points (in the same order): [(x0, y0), (x1, y1), ...]
		pts_pair, # two points defining the maximum-area rectangle: ((xA, yA), (xB, yB))
		img_at_least_dim=500, # make image at least this large in the "max dimension" direction (ignoring margins)
		img_max_dim=5_000, # make image no larger than this in the "max dimension" direction (ignoring margins)
		img_margin=10, # margin around data in pixels (a bit of visual padding in the image)
		polyline_color=(255, 120, 120), # Reddish color for the main data's "polyline" boundary
		background_color=(0, 0, 0),     # Black color for the image's background
		max_rect_color=(0, 80, 0),	    # Dark Green color for the valid rectangle with maximum area
		two_pts_color=(50, 150, 0),     # Yellowish Green color for the two corner points defining the maximum rectangle
		savefile_name="visualization.png"
	):

	def get_corners(A, B):
		A, B = (min(A[0], B[0]), max(A[1], B[1])), (max(A[0], B[0]), min(A[1], B[1]))
		return [A, (A[0], B[1]), B, (B[0], A[1]), A]

	class Matrix(list):
		def __matmul__(self, other):
			result = Matrix([[0]*len(other[0]) for _ in range(len(self))])
			for i in range(len(self)):
				for j in range(len(other[0])):
					result[i][j] = sum(self[i][k]*other[k][j] for k in range(len(other)))
			return result

	def xf(M, pt):
		return tuple(map(round, chain(*(M@Matrix([*[[c] for c in pt], [1]]))[:-1])))

	xy_minmax = [] # [[min_x, min_y], [max_x, max_y]]
	for fnc, init in [(min, [inf, inf]), (max, [-inf, -inf])]:
		xy_minmax.append( reduce(lambda acc, pt: [fnc(z) for z in zip(acc, pt)], data, init) )

	WH = [mx - mn + 1 for mn, mx in zip(xy_minmax[0], xy_minmax[1])]
	s = max(img_at_least_dim, min(max(WH), img_max_dim)) / max(WH) # rescaled data max_dim
	minus = 0 if s < 2 else int(ceil(s/2))
	plus = 0 if s < 2 else int(floor(s/2))
	pt_radius = 6 if s < 2 else min(minus, plus) # "radius" of points marking corners of the big rectangle
	img_margin += 2*pt_radius
	T = Matrix([[1, 0, -xy_minmax[0][0]], # translation matrix
							[0, 1, -xy_minmax[0][1]],
							[0, 0, 1]])
	S = Matrix([[s, 0, 0],                # scaling matrix
							[0, s, 0],
							[0, 0, 1]])
	P = Matrix([[1, 0, img_margin],       # final translation matrix
							[0, 1, img_margin],
							[0, 0, 1]])
	PST = P @ S @ T
	xf_mx = xf(PST, xy_minmax[1])
	img_data = [xf(PST, pt) for pt in data]
	big_rect = [xf(PST, pt) for pt in get_corners(*pts_pair)]
	AB = [xf(PST, pt) for pt in pts_pair]
	img = Image.new('RGB', (xf_mx[0]+img_margin, xf_mx[1]+img_margin), color = background_color)
	# max rectangle
	for y in range(big_rect[1][1] - minus, big_rect[0][1] + plus+1):
		for x in range(big_rect[0][0] - minus, big_rect[2][0] + plus+1):
			img.putpixel((x, y), max_rect_color)
	# polyline
	for (ax, ay), (bx, by) in pairwise(chain(img_data, [img_data[0]])):
		if ax == bx: # vertical line
			for y in range(min(ay, by) - minus, max(ay, by) + plus+1):
				for x in range(ax - minus, ax + plus+1):
					img.putpixel((x, y), polyline_color)
		else: # horizontal line
			for x in range(min(ax, bx) - minus, max(ax, bx) + plus+1):
				for y in range(ay - minus, ay + plus+1):
					img.putpixel((x, y), polyline_color)
	# two corner points
	for px, py in AB:
		for y in range(py-pt_radius, py+pt_radius+1):
			for x in range(px-pt_radius, px+pt_radius+1):
				img.putpixel((x, y), two_pts_color)
	img.save(savefile_name)
