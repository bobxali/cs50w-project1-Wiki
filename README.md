# cs50w-project1-Wiki
# cs50w-project1-Wiki
# cs50w-project1-Wiki

**Design and implement a Wikipedia-like online encyclopedia using Django and Markdown.**

### Background
Wikipedia is a free online encyclopedia that contains entries on various topics. Each entry can be viewed by visiting its page, and the content is typically written in a markup language called Wikitext. However, for this project, we'll store encyclopedia entries using Markdown, a lighter-weight and human-friendly markup language.

### Getting Started
Make sure you have Django installed. If not, you can install it using pip install Django.
Run the development server using python manage.py runserver in the main project directory.
### Features
* **Entry Page**: Visiting /wiki/TITLE displays the contents of an encyclopedia entry.
* **Index Page**: Click on any entry name to be taken directly to that entry page.
* **Search**: Allows users to search for encyclopedia entries and redirects to the page if it exists.
* **New Page**: Allows users to create new encyclopedia entries using a title and Markdown content.
* **Edit Page**: Users can edit existing encyclopedia entries using a textarea pre-populated with the existing Markdown content.
* **Random Page**: Takes users to a random encyclopedia entry.
* **Markdown to HTML Conversion**: Converts Markdown content into HTML for display.
### How to Use
1. Access the application by running the development server and navigating to the local host in your web browser.
1. Use the search bar in the sidebar to look for specific encyclopedia entries.
1. Click on an entry name to view its content.
1. Create a new entry by clicking "Create New Page" in the sidebar.
1. Edit an entry by clicking the "Edit" link on the entry page.
1. Use the "Random Page" link to visit a random encyclopedia entry.
### Implementation Details
* The project uses Django to handle URL routing, templates, and views.
* The util.py file contains functions for interacting with encyclopedia entries.
* Entries are saved as Markdown files in the entries/ directory.
