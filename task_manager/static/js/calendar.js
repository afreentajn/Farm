// Example JavaScript for basic calendar setup using a library (like FullCalendar or custom)
document.addEventListener('DOMContentLoaded', function () {
    const calendarEl = document.getElementById('calendar');
    const calendar = new FullCalendar.Calendar(calendarEl, {
        events: '/tasks/', // Fetch tasks dynamically
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,dayGridWeek,dayGridDay'
        }
    });
    calendar.render();
});
