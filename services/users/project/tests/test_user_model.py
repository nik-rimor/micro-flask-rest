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
        user = add_user('justatest', 'test@test.com', 'greaterthaneight')
        self.assertTrue(user.id)
        self.assertEqual(user.username, 'justatest')
        self.assertEqual(user.email, 'test@test.com')
        self.assertTrue(user.active)
        self.assertTrue(user.password)

    def test_add_user_duplicate_username(self):
        """Ensure error is thrown when added useer has duplicate uername."""
        add_user('justatest', 'test@test.com', 'greaterthaneight')
        dupplicate_user = User(
            username='justatest',
            email='test@test2.com',
            password='greaterthaneight',
        )
        db.session.add(dupplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)

    def test_add_user_duplicate_email(self):
        """Ensure error is thrown when added useer has duplicate email."""
        add_user('justatest', 'test@test.com', 'greaterthaneight')
        dupplicate_user = User(
            username='justanothertest',
            email='test@test.com',
            password='greaterthaneight',
        )
        db.session.add(dupplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)

    def test_to_json(self):
        """Ensure user object translates to JSON dict properly."""
        user = add_user('justatest', 'test@test.com', 'greaterthaneight')
        self.assertTrue(isinstance(user.to_json(), dict))

    def test_passwords_are_random(self):
        """Ensure password are randomly generated."""
        user_one = add_user('justatest', 'test@test.com', 'greaterthaneight')
        user_two = add_user('justatest2', 'test@test2.com', 'greaterthaneight')
        self.assertNotEqual(user_one.password, user_two.password)


if __name__ == '__main__':
    unittest.main()
