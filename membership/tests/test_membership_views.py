from datetime import datetime
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.test import Client, TestCase
from user.models import User
from membership.models import Membership, UserMembership, Subscription


class TestMembershipView(TestCase):
    def test_access_page(self) -> None:
        """Test if a connected user can access the MemberShip Page
        """
        Membership.objects.create(membership_type="TRIAL")
        free_membership = Membership.objects.get(membership_type='TRIAL')

        User.objects.create_user(
            email="matt-fraser@gmail.com",
            password="password8chars",
            first_name="Matt",
            last_name="Fraser",
            date_of_birth="1997-4-10",
        )

        # Only Employee can access the membership page, so we need to set the correct user type
        users = User.objects.filter(email="matt-fraser@gmail.com")
        for user in users:
            user.type = "EMPLOYEE"
            user.save()

        # Creating a new UserMembership
        user_membership = UserMembership.objects.create(
            user=user, membership=free_membership
        )
        user_membership.save()

        # Creating a new UserSubscription
        user_subscription = Subscription()
        user_subscription.user_membership = user_membership
        user_subscription.save()

        client: Client = Client()
        client.login(username="matt-fraser@gmail.com", password="password8chars")

        response: HttpResponse = client.get("/membership/")
        self.assertTemplateUsed(response, "membership/list.html")

    def test_changing_membership(self) -> None:
        """Test if a user can change his membership
        """
        Membership.objects.create(membership_type="TRIAL")
        Membership.objects.create(membership_type="PREMIUM")
        free_membership = Membership.objects.get(membership_type='TRIAL')

        User.objects.create_user(
            email="matt-fraser@gmail.com",
            password="password8chars",
            first_name="Matt",
            last_name="Fraser",
            date_of_birth="1997-4-10",
        )

        # Only Employee can access the membership page, so we need to set the correct user type
        users = User.objects.filter(email="matt-fraser@gmail.com")
        for user in users:
            user.type = "EMPLOYEE"
            user.save()

        # Creating a new UserMembership
        user_membership = UserMembership.objects.create(
            user=user, membership=free_membership
        )
        user_membership.save()

        # Creating a new UserSubscription
        user_subscription = Subscription()
        user_subscription.user_membership = user_membership
        user_subscription.save()

        client: Client = Client()
        client.login(username="matt-fraser@gmail.com", password="password8chars")

        client.post("/membership/", {'membership_type': ['PREMIUM']})

        user_modified: QuerySet = User.objects.first()  # type: ignore
        # Check if the User has a correct TRIAL membership
        self.assertEqual(
            "PREMIUM", user_modified.user_membership.membership.membership_type
        )

