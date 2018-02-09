
class Scene(object):
    def __init__(self, title, urlname, description, needhelp):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.needhelp = needhelp
        self.paths = {}

    def go(self, direction):
        default_direction = None
        if '*' in self.paths.keys():
            default_direction = self.paths.get('*')
        return self.paths.get(direction, default_direction)

    def add_paths(self, paths):
        self.paths.update(paths)

    def options(self):
        if self.name == "Laser Weapon Armory" or self.name == "Escape Pod":
            return "Sorry dude, not clever."
        elif self.paths == {}:
            pass

        else:
            return self.paths.keys()
