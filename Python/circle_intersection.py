import math
import random
from matplotlib import pyplot as plt
round_up = 3

# ----------- circle class -----------------

class Circle:
    x, y, r = None, None, None

    def __init__(self, x=None, y=None, r=None, xrange=[-100, 100], yrange=[-100, 100], rrange=[10, 30]):
        self.x = x if x!=None else random.randint(*xrange)
        self.y = y if y!=None else random.randint(*yrange)
        self.r = r if r!=None else random.randint(*rrange)
        
    def __eq__(self, other):
        return round(self.x-other.x, round_up)==0 and round(self.y-other.y, round_up)==0 and round(self.r-other.r, round_up)==0
    
    def __hash__(self):
        return hash(self.params())

    def params(self): return self.x, self.y, self.r

# -------------- function to create random circles --------------------

# only needs rrange if intersection point (ip) is fixed
def random_circle(xrange=[-100, 100], yrange=[-100, 100], rrange=[10, 30], ip=None):
    if ip==None: return Circle(None, None, None, xrange, yrange, rrange)

    a = random.randint(0, 360)
    r = random.randint(*rrange)
    x = ip[0] + r*math.cos(math.radians(a))
    y = ip[1] + r*math.sin(math.radians(a))
    return Circle(x, y, r)

# ------------- helper functions ----------------

def distance(p1, p2): return round(math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2), round_up)

# ------------ function to find the intersection points -----------------

def intersection_points(circles):

    circles = list(set(circles))
    n = len(circles)

    if n<=1: return set()

    # intersection of two cirlces
    # source: http://paulbourke.net/geometry/circlesphere/#:~:text=Intersection%20of%20two%20circles
    if n==2:
        x0, y0, r0 = circles[0].params()
        x1, y1, r1 = circles[1].params()
        
        d = distance((x0, y0), (x1, y1))
        if d==0 or d<abs(round(r0-r1, round_up)) or d>abs(round(r0+r1, round_up)): return set()
        
        a = (r0**2 - r1**2 + d**2)/(2*d)
        h = math.sqrt(r0**2 - a**2)
        
        x2 = x0 + a*(x1-x0)/d
        y2 = y0 + a*(y1-y0)/d
        
        return set((
            (round(x2 + h*(y1-y0)/d), round(y2 - h*(x1-x0)/d)),
            (round(x2 - h*(y1-y0)/d), round(y2 + h*(x1-x0)/d))
        ))

    # intersection of all circles
    ips = intersection_points([circles[0], circles[1]])

    for i in range(1, n-1):
        new_ips = intersection_points([circles[i], circles[i+1]])
        ips = ips.intersection(new_ips)
        if len(ips)==0: break
    
    return ips


# ------------ function to see the circles ---------------------

def draw_circles(circles, xrange, yrange, ips=None, save=False):
    figure, axes = plt.subplots()
    axes.set_aspect(1)
    plt.xlim(*xrange)
    plt.ylim(*yrange)
    plt.title('Intersection of Circles')

    for circle in circles: axes.add_artist(plt.Circle((circle.x, circle.y), circle.r, fill=False, color='blue'))
    
    if ips==None: ips = list(intersections(circles))
    for ip in ips: axes.add_artist(plt.Circle((ip[0], ip[1]), 1, fill=True, color='red'))

    if save: plt.savefig('output.png')
    return plt.show()


'''
Sample Input & Output:

number of circles: 10
range of x-coord values (For e.g, -100 100): -1000 1000
range of y-coord values (For e.g, -100 100): -1000 1000
range of radius values (For e.g, 10 50): 100 400
do you want to set an intersection point? (Y/N): N
picked a random intersection point:  (-96, 414)    
do you want to save the result as an image? (Y/N): Y
generating random cirlces...done
calculating intersection points...
Found:  (-96, 414)
saving results... (close the pyplot window)
----- finished -----

'''

if __name__=="__main__":

    n = int(input("number of circles: "))
    xrange = list(map(int, input("range of x-coord values (For e.g, -100 100): ").split()))
    yrange = list(map(int, input("range of y-coord values (For e.g, -100 100): ").split()))
    rrange = list(map(int, input("range of radius values (For e.g, 10 50): ").split()))
    
    if input("do you want to set an intersection point? (Y/N): ").lower()[0]=='y':
        ip = list(map(int, input("enter a coord within xrange and yrange (For e.g, 60 20): ")))
    else: 
        ip = random.randint(xrange[0]/2, xrange[1]/2), random.randint(yrange[0]/2, yrange[1]/2)
        print("picked a random intersection point: ", ip)

    output = input("do you want to save the result as an image? (Y/N): ").lower()[0]=='y'
    
    print("generating random cirlces...", end="")
    circles = [random_circle(rrange=rrange, ip=ip) for _ in range(n)]
    print("done")
    print("calculating intersection points...")
    for point in intersection_points(circles): print("Found: ", point)

    if output:
        print("saving results... (close the pyplot window)")
        draw_circles(circles, xrange, yrange, ips=[ip], save=output)

    print("----- finished -----\n")
