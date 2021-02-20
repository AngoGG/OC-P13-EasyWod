from django.urls import include, path
from .views import AddEvent, AddEventMember, EventView, CalendarView

app_name: str = "event"

urlpatterns = [
    path(r"", CalendarView.as_view(), name="event_calendar"),
    path("add_event", AddEvent.as_view(), name="add_event"),
    path(r"<int:pk>", EventView.as_view(), name="event_detail"),
    path("add_eventmember", AddEventMember.as_view(), name="add_eventmember"),
]
