# Refactoring


class Movie:
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDRENS = 2

    def __init__(self, title, movie_type):
        self.title = title
        self.movie_type = movie_type

    def charge(self, days_rented):
        result = 0

        if self.movie_type == "REGULAR":
            result += 2
            result += (days_rented - 2) * 1.5 if days_rented > 2 else 0
        elif self.movie_type == "NEW_RELEASE":
            result += days_rented * 3
        elif self.movie_type == "CHILDRENS":
            result += 1.5
            result += (days_rented - 3) * 1.5 if days_rented > 3 else 0

        return result

    def frequent_renter_points(self, days_rented):
        return 2 if ((Movie.NEW_RELEASE == self.movie_type) and (1 < days_rented)) else 1


class Rental:
    def __init__(self, movie, days_rented):
        self.movie = movie
        self.days_rented = days_rented

    def charge(self):
        return self.movie.charge(self.days_rented)

    def frequent_renter_points(self):
        return self.movie.frequent_renter_points(self.days_rented)


class Costumer:
    def __init__(self, name):
        self.name = name
        self.rentals = []

    def add_rental(self, arg):
        self.rentals.append(arg)

    def total_charge(self):
        return sum([element.charge() for element in self.rentals])

    def total_frequent_renter_points(self):
        return sum([element.frequent_renter_points() for element in self.rentals])

    def statement(self):
        result = "Rental Record for {}\n".format(self.name)

        for element in self.rentals:
            # show figures
            result += "\t" + element.movie.title + "\t" + str(element.charge()) + "\n"

        result += "Amount owed is {}\n".format(self.total_charge())
        result += "You earned {} frequent renter points".format(self.total_frequent_renter_points())

        print(result)

        return {"total_amount": self.total_charge(),
                "frequent_renter_points": self.total_frequent_renter_points()}


if __name__ == "__main__":
    movie_1 = Movie("Titanic", "REGULAR")
    movie_2 = Movie("Pulp Fiction", "NEW_RELEASE")
    movie_3 = Movie("Casa", "CHILDRENS")

    rental_1 = Rental(movie_1, 7)
    rental_2 = Rental(movie_2, 5)
    rental_3 = Rental(movie_3, 1)

    consumer = Costumer("Rodrigo")
    consumer.rentals = [rent for rent in [rental_1, rental_2, rental_3]]
    consumer.statement()
