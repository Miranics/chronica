document.getElementById("search-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    
    const date = document.getElementById("date").value;
    if (!date) return;

    const response = await fetch(`/search?date=${date}`);
    const data = await response.json();

    const eventsList = document.getElementById("events-list");
    eventsList.innerHTML = ""; // Clear previous results

    if (data.events && data.events.length > 0) {
        data.events.forEach(event => {
            const li = document.createElement("li");
            li.innerHTML = `
                <strong>${event.year}</strong>: ${event.description}
                ${event.link ? `<a href="${event.link}" target="_blank">[Learn More]</a>` : ""}
            `;
            eventsList.appendChild(li);
        });
    } else {
        eventsList.innerHTML = "<li>No events found for this date.</li>";
    }
});
