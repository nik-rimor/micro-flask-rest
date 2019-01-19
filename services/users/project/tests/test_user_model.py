# services/users/project/tests/test_user_model.py


import unittest

from project import db
from project.api.models import User
from project.tests.base import BaseTestCase
from project.tests.utils import add_user

from sqlalchemy.exc import IntegrityError


class TestUserModel(BaseTestCase):

    def test_add_user(self):
        """Ensure user is added to database properly."""
        user = add_user('justatest', 'test@test.com')
        self.assertTrue(user.id)
        self.assertEqual(user.username, 'justatest')
        self.assertEqual(user.email, 'test@test.com')
        self.assertTrue(user.active)

    def test_add_user_duplicate_username(self):
        """Ensure error is thrown when added useer has duplicate uername."""
        add_user('justatest', 'test@test.com')
        dupplicate_user = User(
            username='justatest',
            email='test@test2.com',
        )
        db.session.add(dupplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)

    def test_add_user_duplicate_email(self):
        """Ensure error is thrown when added useer has duplicate email."""
        add_user('justatest', 'test@test.com')
        dupplicate_user = User(
            username='justanothertest',
            email='test@test.com',
        )
        db.session.add(dupplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)

    def test_to_json(self):
        """Ensure user object translates to JSON dict properly."""
        user = add_user('justatest', 'test@test.com')
        self.assertTrue(isinstance(user.to_json(), dict))


if __name__ == '__main__':
    unittest.main()
