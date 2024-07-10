# DocuSearch

Docusearch is a simple localized search engine - similar to that of `File Explorer` on windows. This project is meant to help understand how search engines work at a smaller scale using your own machine as the reference base. 

## How to run DocuSearch

The first step in using DocuSearch is to fork the repository on Github and then to clone the repository to your local machine. After that is complete the rest is quite simple, make sure that the root of the project is the DocuSearch direcotry and then run the following command:

`python -m src.main`

The above command will open up a simple UI in which the user will be greeted with 2 buttones:

- Index Files
- Search Files

Before trying to query strings in your files you have to index the directories you want to query. Clicking the `Index Files` buttons will quide you through that process.

Once you have completed the Indexing of the files, you can proceed to search for query strings in the UI using the `Search Files` button.