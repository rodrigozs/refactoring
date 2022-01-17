import unittest
import classes as cl


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.movie_1 = cl.Movie("Titanic", "REGULAR")
        self.movie_2 = cl.Movie("Pulp Fiction", "NEW_RELEASE")
        self.movie_3 = cl.Movie("Casa", "CHILDRENS")

        self.rental_1 = cl.Rental(self.movie_1, 7)
        self.rental_2 = cl.Rental(self.movie_2, 5)
        self.rental_3 = cl.Rental(self.movie_3, 1)

        self.consumer = cl.Costumer("Rodrigo")
        self.consumer.rentals = [rent for rent in [self.rental_1, self.rental_2, self.rental_3]]

    def test_total_amount(self):
        self.assertEqual(self.consumer.statement()["total_amount"], 26.0)  # add assertion here
        self.assertEqual(self.consumer.statement()["frequent_renter_points"], 3)


if __name__ == '__main__':
    unittest.main()
