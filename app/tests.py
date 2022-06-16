from django.test import TestCase
from .models import Neighborhood, Business, User

# Create your tests here.


class NeighborhoodTestClass(TestCase):
    """
    Testing Neighborhood model functions
    """

    def setUp(self):
        """Set up method"""
        self.chescourt = Neighborhood(
            name='Chester Court', location='Nairobi', occupants_count=10)

    def test_instance(self):
        """Test instance"""
        self.admin = User(username='admin',
                          email='admin@test.com', password='admin')
        self.assertTrue(isinstance(self.chescourt, Neighborhood))

    def test_create_neighborhood(self):
        """Test create_neighborhood"""
        self.chescourt.create_neighborhood()
        neighborhood = Neighborhood.objects.all()
        self.assertTrue(len(neighborhood) > 0)

    def test_delete_neighborhood(self):
        """Test delete_neighborhood"""
        self.chescourt.create_neighborhood()
        self.chescourt.delete_neighborhood()
        neighborhood = Neighborhood.objects.all()
        self.assertTrue(len(neighborhood) == 0)

    def test_find_neighborhood(self):
        """Test find_neighborhood"""
        self.chescourt.create_neighborhood()
        neighborhood = Neighborhood.objects.get(name='Chester Court')
        self.assertTrue(neighborhood.name == 'Chester Court')

    def test_update_neighborhood(self):
        """Test update_neighborhood"""
        self.chescourt.create_neighborhood()
        self.chescourt.update_neighborhood('Chester Court', 'Nairobi', 10)
        neighborhood = Neighborhood.objects.get(name='Chester Court')
        self.assertTrue(neighborhood.name == 'Chester Court')
        self.assertTrue(neighborhood.location == 'Nairobi')
        self.assertTrue(neighborhood.occupants_count == 10)

    def test_get_occupants_count(self):
        """Test get_occupants_count"""
        self.chescourt.create_neighborhood()
        neighborhood = Neighborhood.objects.get(name='Chester Court')
        self.assertTrue(neighborhood.get_occupants_count() == 10)

    def tearDown(self):
        """Tear down method"""
        Neighborhood.objects.all().delete()
        User.objects.all().delete()


class BusinessTestClass(TestCase):
    """  Testing Business model functions   """

    def setUp(self):
        """_summary_: set up method
        """
        self.business = Business(name='Meaty Palace', email='meaty@palace.com')

    def test_instance(self):
        """Test instance"""
        self.assertTrue(isinstance(self.business, Business))

     # delete, update, find business

    def test_create_business(self):
        """Test create_business"""
        self.business.create_business()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)

    def test_delete_business(self):
        """_summary_: test delete_business
        """
        self.business.create_business()
        self.business.delete_business()
        business = Business.objects.all()
        self.assertTrue(len(business) == 0)

    def tearDown(self):
        """tear down to delete saved instances"""
        Business.objects.all().delete()

    def test_update_neighborhood(self):
        """_summary_: test update_business
        """
        self.business.create_business()
        self.business.update_business('Meaty Palace', 'meaty@palace.com')
        business = Business.objects.get(name='Meaty Palace')
        self.assertTrue(business.name == 'Pretty Meaty Palace')
        self.assertTrue(business.email == 'prettymeaty@gmail.com')

    def test_find_business(self):
        """Test find_neighborhood"""
        self.business.create_business()
        business = Business.objects.get(name='Meaty Palace')
        self.assertTrue(business.name == 'Meaty Palace')
