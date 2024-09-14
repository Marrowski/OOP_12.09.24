from PIL import Image, ImageDraw


class Shape:
    def __init__(self):
        self.back_color = (155, 213, 117, 100)
        self.im = Image.new('RGBA', (500, 500), self.back_color)
        self.draw1 = ImageDraw.Draw(self.im)

    def draw(self):
        pass

    def erase(self):
        self.im = Image.new('RGBA', (500, 500), self.back_color)
        self.draw1 = ImageDraw.Draw(self.im)

    def save(self):
        print("Background was created")
        return self.im.save('picture.png', quality=95)


class Circle(Shape):
    def draw(self):
        self.draw1.ellipse((75, 100, 175, 200), fill='yellow', outline=(255, 255, 255))

    def erase(self):
        self.draw1.ellipse((75, 100, 175, 200), fill=self.back_color)

    def save(self):
        print("Image with circle was created")
        return self.im.save('draw-circle.png', quality=95)


class Square(Shape):
    def draw(self):
        self.draw1.rectangle((200, 100, 300, 200), fill='blue', outline=(255, 255, 255))

    def erase(self):
        self.draw1.rectangle((200, 200, 300, 200), fill=self.back_color)

    def save(self):
        print("Image with square was created")
        return self.im.save('draw-square.png', quality=95)


class Triangle(Shape):
    def draw(self):
        self.draw1.polygon([(400, 100), (350, 200), (450, 200)], fill=(255, 255, 255))

    def erase(self):
        self.draw1.polygon([(400, 100), (350, 200), (450, 200)], fill=self.back_color)

    def save(self):
        print("Image with triangle was created")
        return self.im.save('draw-triangle.png', quality=95)


class Cone(Shape):
    def __init__(self):
        self.width = 400
        self.height = 400
        self.image = Image.new("RGB", (self.width, self.height), "white")
        self.draw1 = ImageDraw.Draw(self.image)

    def draw(self):
        center_x = self.width // 2
        center_y = self.height // 2 + 50
        radius = 150
        height_cone = 250

        for i in range(radius):
            color_intensity = int(255 * (1 - i / radius))
            color = (color_intensity, color_intensity, 0)
            x_offset = i // 2

            self.draw1.line([(center_x - x_offset, center_y),
                             (center_x, center_y - height_cone + i)],
                            fill=color, width=2)
            self.draw1.line([(center_x + x_offset, center_y),
                             (center_x, center_y - height_cone + i)],
                            fill=color, width=2)

        self.draw1.ellipse([center_x - radius // 2, center_y - 10,
                            center_x + radius // 2, center_y + 10],
                           outline="black", fill=(200, 200, 0))

    def save(self):
        print('Cone image saved successfully')
        return self.image.save('cone.png', quality=95)


class Paraboloid(Shape):
    def draw(self):
        center_x = 250
        center_y = 250
        max_radius = 100
        height_paraboloid = 150

        for i in range(0, height_paraboloid, 5):
            radius = max_radius * (1 - (i / height_paraboloid) ** 2)
            color_intensity = int(255 * (1 - i / height_paraboloid))
            color = (color_intensity, color_intensity, 255)

            self.draw1.ellipse([center_x - radius, center_y + i,
                                center_x + radius, center_y + i + 10],
                               outline=color, fill=None)

    def save(self):
        print('Paraboloid image saved successfully')
        self.im.save('paraboloid.png', quality=95)


def work_with_obj(obj):
    obj.draw()
    obj.save()


def update_obj(obj):
    obj.erase()
    obj.save()


def menu():
    while True:
        value = int(input('\nМЕНЮ:\n\t1. Cтворити тло\n\t2. Cтворити коло\n\t3. Cтворити квадрат\n\t4. Cтворити трикутник'
                          '\n\t5. Зафарбувати коло\n\t6. Зафарбувати квадрат\n\t7. Зафарбувати трикутник\n\t'
                          '8. Створити конус\n\t9. Створити параболоїд\n\t10. Вихід з програми\nОберіть відповідний пункт меню: '))
        match value:
            case 1:
                s = Shape()
                s.save()
            case 2:
                c = Circle()
                work_with_obj(c)
            case 3:
                sq = Square()
                work_with_obj(sq)
            case 4:
                t = Triangle()
                work_with_obj(t)
            case 5:
                c = Circle()
                update_obj(c)
            case 6:
                sq = Square()
                update_obj(sq)
            case 7:
                t = Triangle()
                update_obj(t)
            case 8:
                co = Cone()
                work_with_obj(co)
            case 9:
                p = Paraboloid()
                work_with_obj(p)
            case 10:
                break
            case _:
                print('Оберіть пункт меню корректно!!!')


if __name__ == '__main__':
    menu()
