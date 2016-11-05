# Zipfiles Server

Zipping will be handled through a service, the
construction of which is placed in your able hands.

## Requirements
The service should be designed as an HTTP API, with endpoints for the following:
* Uploading a file
  - Should take a file together with username and filename, and return some
    type of file ID.
  - Should trigger a background job that zips the file.
* Retrieving a file
  - Should take a file ID and return the zipped file, or an error if the file
    hasn't been zipped yet.
* Listing files
  - Should produce a list of the uploaded files, with username, date and size.

## Guidelines
You may use Python or Java and tools you like to develop a solution.

Please design your solution to be as robust and realistic as possible, and use
what you consider to be best practices for API and code design, data storage,
et cetera.

We want to get an idea how you approach real-world problems, so try to commit
often and be prepared to discuss your design choices.

The assignment shouldn't take more than a few hours, so don't fret if you don't
have the time to create a production-ready solution.

On the other hand, you are also free to add any additional features if you feel
like it. A few ideas:
- An endpoint for unzipping files
- A web UI
- User management/auth
- Support for different compression formats

When you are done, submit a pull request to this repository.
Include a README with instructions on how to run your code.
