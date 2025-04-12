import wikipedia
import warnings

# Suppress BeautifulSoup warnings as instructed
warnings.filterwarnings("ignore", category=UserWarning, module="wikipedia")


def get_wikipedia_page():
    """Prompt user for a Wikipedia page title and display its details until blank input."""
    while True:
        # Get user input
        title = input("Enter page title: ").strip()

        # Exit if input is blank
        if not title:
            print("Thank you.")
            break

        try:
            # Fetch page with auto_suggest=False to prevent API suggestions
            page = wikipedia.page(title, auto_suggest=False)

            # Print page details
            print(page.title)
            print(wikipedia.summary(title, sentences=2))  # First two sentences of summary
            print(page.url)
            print()  # Blank line for readability

        except wikipedia.exceptions.PageError:
            # Handle non-existent page (e.g., "jcu")
            print(f'Page id "{title}" does not match any pages. Try another id!')
            print()

        except wikipedia.exceptions.DisambiguationError as e:
            # Handle ambiguous page (e.g., "python")
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options[:10])  # Show up to 10 suggestions to avoid overwhelming output
            print()


# Run the program
if __name__ == "__main__":
    get_wikipedia_page()