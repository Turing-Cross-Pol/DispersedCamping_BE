# # test_models.py
# import unittest
# import os
# from app import create_app, db
# from app.models import Campsite, Amenity
#
#
# class ModelTestCase(unittest.TestCase):
#
#     def setUp(self):
#         self.app = create_app(config_name="testing")
#         self.client = self.app.test_client
#         self.campsite = {'name': '18 Road'}
#         # binds the app to the current context
#         with self.app.app_context():
#             # create all tables
#             db.create_all()
#
#
#     def test_campsite_creation(self):
#         import pdb; pdb.set_trace()
#         self.assertEqual(1, 1)
#
#
#     def tearDown(self):
#         """teardown all initialized variables."""
#         with self.app.app_context():
#             # drop all tables
#             db.session.remove()
#             db.drop_all()
#
# # Make the tests conveniently executable
# if __name__ == "__main__":
#     unittest.main()
