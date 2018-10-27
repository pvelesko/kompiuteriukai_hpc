from vpython import *
r = 0.1
dt = 0.1
m = 1
t = 0
mycolors = [color.red, color.blue, color.green]

def change_size_from_txt():
    try:
        f = open("size.txt", "r")
        lines = f.readlines()
        if len(lines) > 0:
            ball.radius = float(lines[0])
        f.close()
    except e:
        pass




class Scene:

    def __init__(self):
        self.actors = []
        self.base = box(pos=vector(0, -0.2, 0), size=vector(10, 0.1, 10), color=color.white)

    def get_vec_field(self, loc):
        x = t % 1
        y = cos(loc.x)
        z = 0
        return vector(x, y, z)

    def add_actor(self, id):
        c = mycolors[id]
        actor = sphere(pos=vector(1, 0, 0), radius=r, color=c)
        actor.id = id
        actor.count = 1
        self.actors.append(actor)
        
    def update_pos(self):
        for i in range(len(self.actors)):
            #loc = self.actors[i].pos + self.get_vec_field(self.actors[i].pos)/m*dt
            #self.actors[i].pos = vector(loc)
            x = self.actors[i].pos.x
            y = self.actors[i].pos.y
            z = self.actors[i].pos.z
            loc = vector(cos(t)+random()%0.1, 1+t/100+random()%0.1, sin(t)+random()%0.1)
            self.actors[i].pos = loc
    def run(self):
        while():
            self.update_pos()
            rate(100)


if __name__ == "__main__":
    scene = Scene()
    scene.add_actor(1)
    while(True):
        scene.update_pos()
        t = t + dt
        rate(100)
    #scene.run()
