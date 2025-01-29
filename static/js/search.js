const searchInput = document.getElementById("searchInput");

searchInput.addEventListener("input", filterContacts);
searchInput.addEventListener("keypress", (e) => {
  if (e.key === "Enter") e.preventDefault(); // Prevents form submission
});

function filterContacts() {
  const searchText = searchInput.value.toLowerCase();
  document.querySelectorAll("tbody tr").forEach((row) => {
    row.style.display = row.textContent.toLowerCase().includes(searchText)
      ? ""
      : "none";
  });
}
