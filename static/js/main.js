// Get the search form and page links
let searchForm = document.getElementById('searchForm');
let pageLinks = document.getElementsByClassName('page-link');

// Ensure the search form exists
if(searchForm) {
    for(let i=0; pageLinks.length > i; i++) {
        // Add the search query to the page links
        pageLinks[i].addEventListener('click', function() {
            // Get the page number
            let page_number = this.dataset.page;

            // Add the search input to the form
            searchForm.innerHTML += `<input type="hidden" name="page" value="${page_number}" />`;
            // Submit the form
            searchForm.submit();
        });
    }
}