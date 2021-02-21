from django.urls import include, path
from .views import (
    AddEvent,
    EventView,
    CalendarView,
    RegisterForEvent,
    UnsubscribeFromEvent,
    UserRegistrations,
)

app_name: str = "event"

urlpatterns = [
    path(r"", CalendarView.as_view(), name="event_calendar"),
    path("add_event", AddEvent.as_view(), name="add_event"),
    path(r"<int:pk>", EventView.as_view(), name="event_detail"),
    path("register_event", RegisterForEvent.as_view(), name="register_event"),
    path("unsubscribe_event", UnsubscribeFromEvent.as_view(), name="unsubscribe_event"),
    path("user_registrations", UserRegistrations.as_view(), name="user_registrations"),
]
