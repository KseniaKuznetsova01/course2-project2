class Carbase:
    def __init__(self,car_type, photo_le_name, brand, carrying):
        self.car_type = car_type
        self.photo_le_name = photo_le_name
        self.brand = brand
        self.carrying = carrying

    def get_photo_le_ext(self):
        t = self.photo_le_name.find('.')
        return self.photo_le_name[t:]

class Car(Carbase):
    def __init__(self,car_type, photo_le_name, brand, carrying, passenger_seats_count = None, size = None, extra = None):
        super().__init__(car_type, photo_le_name, brand, carrying)
        self.passenger_seats_count = passenger_seats_count

class Truck(Carbase):
    def __init__(self,car_type, photo_le_name, brand, carrying,passenger_seats_count = None, size = None, extra = None):
        super().__init__(car_type, photo_le_name, brand, carrying)
        self.size = size
        self.body_width = 0.0
        self.body_height = 0.0
        self.body_length = 0.0

    def get_body_volume(self):
        x = self.size.find('x')
        self.body_width = float(self.size[:x])
        self.size = self.size[x+1:]
        x = self.size.find('x')
        self.body_height = float(self.size[:x])
        self.body_length = float(self.size[x+1:])
        v = self.body_width * self.body_height * self.body_length
        return v


class Specmachine(Carbase):
    def __init__(self,car_type, photo_le_name, brand, carrying,passenger_seats_count = None, size = None, extra= None):
        super().__init__(car_type, photo_le_name, brand, carrying)
        self.extra = extra


def get_car_list(filename):
    car_list = []
    with open(filename) as f:
        for line in f:
            first = line.find(';')

            if line[:first] == 'car':
                car_list.append(Car(*line.split(';')))
            elif line[:first] == 'truck':
                car_list.append(Truck(*line.split(';')))
            elif line[:first] == 'spec_machine':
                car_list.append(Specmachine(*line.split(';')))
            else:
                continue

    return car_list


def main():
    get_car_list('solution.txt')

if __name__ == '__main__':
    main()