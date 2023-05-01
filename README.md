
# Firebase Link Saver

This is a simple Python program that allows you to save links to Firebase and view them from the Python terminal.

## Setup

1. Clone this repository to your local machine.
2. Install the required dependencies by running the following command:

   ```sh
   pip install firebase-admin
   ```
   
   This program uses the `firebase-admin` library to interact with Firebase from Python.
   
3. Follow the instructions in the [Firebase documentation](https://firebase.google.com/docs/admin/setup) to set up a Firebase project and download a service account key file. Save the key file in the root directory of this project.

## Usage

To save a link to Firebase, run the following command:

```sh
python save_link.py <link> <description>
```

Replace `<link>` with the URL of the link you want to save, and `<description>` with a brief description of the link. This will add a new document to the `links` collection in your Firebase database.

To view your saved links from the terminal, run the following command:

```sh
python view_links.py
```

This will retrieve all the documents in the `links` collection and print them to the terminal.

## Contributing

Pull requests are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork this repository.
2. Create a new branch for your feature or bug fix.
3. Implement your changes and write tests if possible.
4. Commit your changes and push them to your fork.
5. Submit a pull request to this repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
