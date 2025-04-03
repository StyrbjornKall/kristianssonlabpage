# README
This is a website based on the helios template, see below.

## How it works
To edit this webpage and push it to GitHub, follow these steps:

1. **Clone the Repository**:
	- Open a terminal or command prompt.
	- Clone the GitHub repository to your local machine using the command:
	  ```
	  git clone <repository-url>
	  ```
	  Replace `<repository-url>` with the URL of the GitHub repository hosting this webpage.

2. **Pull the Latest Changes**:
	- Before making any edits, ensure you have the latest changes from the repository:
	  - Open a terminal or command prompt in the cloned repository folder.
	  - Run the following command:
		```
		git pull origin main
		```
		Replace `main` with the branch name if your repository uses a different default branch.

3. **Make Edits**:
	- Navigate to the cloned repository folder on your local machine.
	- Open the HTML, CSS, or JavaScript files in a text editor or IDE of your choice (e.g., Visual Studio Code, Sublime Text).
	- Make the necessary changes to the code.

4. **Preview Changes Locally**:
	- To preview the webpage locally with JavaScript functionality, you need to host it using a simple HTTP server. You can use Python or PHP for this:
	  - **Using Python**:
		- Open a terminal or command prompt in the folder containing your HTML file.
		- Run the following command:
		  ```
		  python -m http.server
		  ```
		- Open a web browser and navigate to `http://localhost:8000` to view the webpage.
	  - **Using PHP**:
		- Ensure PHP is installed on your system.
		- Open a terminal or command prompt in the folder containing your HTML file.
		- Run the following command:
		  ```
		  php -S localhost:8000
		  ```
		- Open a web browser and navigate to `http://localhost:8000` to view the webpage.

5. **Commit Changes**:
	- After making edits, save the files.
	- Open the terminal or command prompt, navigate to the repository folder, and run the following commands:
	  ```
	  git add .
	  git commit -m "Describe your changes here"
	  ```

6. **Push Changes to GitHub**:
	- Push your changes to the GitHub repository using:
	  ```
	  git push origin main
	  ```
	  Replace `main` with the branch name if your repository uses a different default branch.
	  
	Note: Ensure you have the necessary permissions to push changes to the repository.

7. **View the Updated Webpage**:
	- The repository is configured for GitHub Pages, the changes will automatically reflect on the hosted webpage.
	- Visit the GitHub Pages URL (usually `https://<username>.github.io/<repository-name>/`) to see the updated webpage.

# HTML Template
Helios by HTML5 UP
html5up.net | @ajlkn
Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)


This is Helios, a brand new site template for HTML5 UP. It's clean, modern, and designed
to take advantage of larger (well, wider) displays while still being capable of gracefully
scaling down to fit all manner of smaller ones.

Demo images* courtesy of Michael Domaradzki, an awesome photographer I met over at
deviantART. Check out his portfolio here:

http://md.photomerchant.net/

(* = Not included! Only meant for use with my own on-site demo, so please do NOT download
and/or use any of Michaels's work without his explicit permission!)

AJ
aj@lkn.io | @ajlkn


Credits:

	Demo Images:
		Michael Domaradzki (md.photomerchant.net)

	Icons:
		Font Awesome (fontawesome.io)

	Other:
		jQuery (jquery.com)
		Scrollex (github.com/ajlkn/jquery.scrollex)
		Responsive Tools (github.com/ajlkn/responsive-tools)