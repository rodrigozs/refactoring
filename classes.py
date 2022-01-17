# Refactoring


class Movie:
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDRENS = 2

    def __init__(self, title, movie_type):
        self.title = title
        self.movie_type = movie_type


class Rental:
    def __init__(self, movie, days_rented):
        self.movie = movie
        self.days_rented = days_rented

    def amount_for(self):
        result = 0

        if self.movie.movie_type == "REGULAR":
            result += 2
            result += (self.days_rented - 2) * 1.5 if self.days_rented > 2 else 0
        elif self.movie.movie_type == "NEW_RELEASE":
            result += self.days_rented * 3
        elif self.movie.movie_type == "CHILDRENS":
            result += 1.5
            result += (self.days_rented - 3) * 1.5 if self.days_rented > 3 else 0

        return result


class Costumer:
    def __init__(self, name):
        self.name = name
        self.rentals = []

    def add_rental(self, arg):
        self.rentals.append(arg)

    def statement(self):
        total_amount, frequent_renter_points = 0, 0
        result = "Rental Record for {}\n".format(self.name)

        for element in self.rentals:
            this_amount = element.amount_for()

            # add frequent renter points
            frequent_renter_points += 1
            # add bonus
            if (element.movie.movie_type == Movie.NEW_RELEASE) and (element.days_rented > 1):
                frequent_renter_points += 1

            # show figures
            result += "\t" + element.movie.title + "\t" + str(this_amount) + "\n"
            total_amount += this_amount

        result += "Amount owed is {}\n".format(total_amount)
        result += "You earned {} frequent renter points".format(frequent_renter_points)

        print(result)

        return {"total_amount": total_amount,
                "frequent_renter_points": frequent_renter_points}


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
